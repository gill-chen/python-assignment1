# INF1340, section 
# Assignment 1 - due 2018-10-17
# Chen, Gillian Siyuan
# Lam, Sharon

# POS program for MinMax
# compatible with Python versions 3.4 - 3.7
# source file: a1-Gillian-and-Sharon.py

  
PRICE_SINGLE = 1 
PRICE_SMALL = 5 
PRICE_LARGE = 19
HST_RATE = 0.13



import math 

# displays welcome message 
def display_welcome():
	print("Welcome to Minmax! Your cashier will assist you with your items") 

# gets barcode from items, calculates running total, and returns total bill 
def get_barcode(): 
	scan_not_complete = True
	subtotal_before_tax = 0
	total_before_rounding = 0 
	total_bill = 0

	while (scan_not_complete):
		cashier_input = input("Please scan item code: ")
		cashier_input = int(cashier_input)
		
		if (cashier_input == 0):
			print("scanning complete - no more items to scan")
			scan_not_complete = False 
		elif (cashier_input == 111111):
			subtotal_before_tax += PRICE_SINGLE
		elif (cashier_input == 666666):
			subtotal_before_tax += PRICE_SMALL
		elif (cashier_input == 242424):
			subtotal_before_tax += PRICE_LARGE
		else: 
			print("Please enter valid scan code")
			continue 

		total_before_rounding = calculate_subtotal(HST_RATE, subtotal_before_tax) 
		total_bill = calculate_total_bill(total_before_rounding)
	
	display_total_bill(subtotal_before_tax, total_before_rounding, total_bill)
	return total_bill 

#calculates total cost with tax (no rounding yet)
def calculate_subtotal(HST_RATE, subtotal_before_tax):
	tax = HST_RATE * subtotal_before_tax
	total_before_rounding = subtotal_before_tax + tax 
	print (total_before_rounding)
	return total_before_rounding

#takes the total cost + tax, and rounds out the result 
def calculate_total_bill(total_before_rounding):
	total_bill = round(0.05 * round(float(total_before_rounding)/0.05),2)
	return total_bill

#displays "receipt" 
def display_total_bill(subtotal_before_tax, total_before_rounding, total_bill):
	tax = round(total_before_rounding - subtotal_before_tax, 2) 
	print("Here's your subtotal before tax: %s, tax amount: %s, total before rounding: %s, total bill: %s" % (subtotal_before_tax, tax, 
		total_before_rounding, total_bill))
	print(total_before_rounding)

#gets cash amount from customer 
def get_amount_tendered(total_bill):
	cash_not_received = True 
	while (cash_not_received):
		amount_tendered = input("Please enter amount tendered: ")
		amount_tendered = int(amount_tendered)
		if amount_tendered == 0:
			print("Transaction cancelled")
			return 0
		elif amount_tendered >= total_bill:
			return amount_tendered
		elif amount_tendered < total_bill:
			continue 

# calculates the change owed to customer 
def display_change(total_bill, amount_tendered):
	amount_of_change = round(amount_tendered - total_bill, 2) 
	if amount_of_change >= 0:
		print ("Here's your change: %s" % amount_of_change)
	print ("Thank you for shopping with MinMax!")



if __name__ == "__main__":
	display_welcome()
	total_bill = get_barcode()
	amount_tendered = get_amount_tendered(total_bill)
	display_change(total_bill, amount_tendered)
	
	



