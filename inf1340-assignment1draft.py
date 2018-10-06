 # to "scan" items 10 marks
 # to calculate subtotal 15 marks
 # to calculate total bill, including rounding 15 marks
 # to enter and consider the amount tendered 15 marks
 # to display the amount of change

scan_not_complete = True  
PRICE_SINGLE = 1 
PRICE_SMALL = 5 
PRICE_LARGE = 19
HST_RATE = 0.13; 

import math 


def display_welcome():
	print("Welcome to Minimax! Your cashier will assist you with your items") 

def get_barcode(scan_not_complete): 
	subtotal_before_tax = 0 

# keeps prompting cashier for input until he hits "0" = done 
	while (scan_not_complete):
		cashier_input = input("Please scan item code")
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
	return subtotal_before_tax

# print("Here's your subtotal before tax: %d" % subtotal_before_tax)

#calculates total cost with tax 
def calculate_subtotal(HST_RATE, subtotal_before_tax):
	total_before_rounding = (1 + HST_RATE) * subtotal_before_tax
	print (total_before_rounding)
	return total_before_rounding

#takes the total cost + tax, and rounds it out 
def calculate_total_bill(total_before_rounding):
	total_bill = round(0.05 * round(float(total_before_rounding)/0.05),2)
	print (total_bill)
	return total_bill

if __name__ == "__main__":
	display_welcome()
	subtotal_before_tax = get_barcode(scan_not_complete)
	total_before_rounding = calculate_subtotal(HST_RATE, subtotal_before_tax)
	total_bill = calculate_total_bill(total_before_rounding)
	print (total_bill)

