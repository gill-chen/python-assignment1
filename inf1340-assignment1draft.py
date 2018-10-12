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
UPC_SINGLE = 111111
UPC_SMALL = 666666
UPC_LARGE = 242424
HST_RATE = 0.13


import math 

# displays welcome message 
def display_welcome():
	print("Welcome to Minmax! Your cashier will assist you with your items") 

# gets barcode from items, calculates running total, and returns total bill 
def get_barcode(): 
	''' -> NoneType
	
	'''
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
			break
		elif (cashier_input == UPC_SINGLE):
			subtotal_before_tax += PRICE_SINGLE
		elif (cashier_input == UPC_SMALL):
			subtotal_before_tax += PRICE_SMALL
		elif (cashier_input == UPC_LARGE):
			subtotal_before_tax += PRICE_LARGE
		else: 
			print("Please enter valid scan code")
			continue 

		# subtotal_before_tax = "%0.2f" % subtotal_before_tax
		print ("Subtotal: " + str("{:.2f}".format(subtotal_before_tax))) 

		tax = round(HST_RATE * subtotal_before_tax, 2) 
		print ("HST: " + str(tax)) 

		total_before_rounding = calculate_subtotal(HST_RATE, subtotal_before_tax) 
		total_bill = calculate_total_bill(total_before_rounding)

		print ("Total: " + str(total_bill))
	
	display_total_bill(subtotal_before_tax, tax, total_before_rounding, total_bill)
	return total_bill 

#calculates total cost with tax (no rounding yet)
def calculate_subtotal(HST_RATE, subtotal_before_tax):
	''' (float, int) -> float 
	
	Returns the subtotal_before_tax with tax by calculating the tax 
	from the HST_RATE

	>>> calculate_subtotal(0.13, 25)
	39.55 
	>>> calculate_subtotal(0.13, 24)
	27.12 
	'''
	tax = HST_RATE * subtotal_before_tax
	total_before_rounding = subtotal_before_tax + tax 
	# print (total_before_rounding)
	return total_before_rounding

#takes the total cost + tax, and rounds out the result 
def calculate_total_bill(total_before_rounding):
	''' (float) -> float 
	
	Returns total_bill after rounding the total_before_rounding to the nearest 5 cents. 

	>>> calculate_total_bill(39.55)
	39.55 
	>>> calculate_total_bill(27.12)
	27.10
	>>> calculate_total_bill(18.08)
	18.10 
	'''
	total_bill = round(0.05 * round(float(total_before_rounding)/0.05),2)
	return total_bill

#displays "receipt" 
def display_total_bill(subtotal_before_tax, tax, total_before_rounding, total_bill):
	''' (int, float, float, float) -> NoneType 
	
	Prints the subtotal_before_tax, tax, total_before_rounding, and total_bill. 

	>>> display_total_bill(1, 0.13, 1.13, 1.15)
	Here's your subtotal before tax: 1.00, tax amount: 0.13, total before rounding: 1.13, total bill: 1.15
	'''
	
	print("Here's your subtotal before tax: %s, tax amount: %s, total before rounding: %s, total bill: %s" % 
		(str("{:.2f}".format(subtotal_before_tax)), str("{:.2f}".format(tax)), 
		str("{:.2f}".format(total_before_rounding)), str("{:.2f}".format(total_bill))))
	

#gets cash amount from customer 
def get_amount_tendered(total_bill):
	''' (float) -> NoneType
	
	Takes input for amount_tendered, if amount_tendered is 0, it prints "Transaction Cancelled". 
	If amount_tendered is less than total_bill, it continues to prompt until amount_tendered is 
	greater than or equal to total_bill.  

	>>> amount_tendered
	40 
	'''
	cash_not_received = True 
	while (cash_not_received):
		amount_tendered = input("Please enter amount tendered: ")
		amount_tendered = int(amount_tendered)
		if amount_tendered == 0:
			print("Transaction cancelled.")
			return 0
		elif amount_tendered >= total_bill:
			return amount_tendered
		elif amount_tendered < total_bill:
			print("Please pay the full amount.")
			continue 

# calculates the change owed to customer 
def display_change(total_bill, amount_tendered):
	''' (float, int) -> NoneType 
	
	Calculates the difference between amount_tendered and total_bill, and prints 
	the difference as amount_of_change. 

	>>> display_change(2.25, 40)
	Here's your change: 37.75
	Thank you for shopping with MinMax! 
	'''
	amount_of_change = round(amount_tendered - total_bill, 2) 
	if amount_of_change >= 0:
		print ("Here's your change: %s" % str("{:.2f}".format(amount_of_change)))
	print ("Thank you for shopping with MinMax!")



if __name__ == "__main__":
	display_welcome()
	total_bill = get_barcode()
	amount_tendered = get_amount_tendered(total_bill)
	display_change(total_bill, amount_tendered)
	
	



