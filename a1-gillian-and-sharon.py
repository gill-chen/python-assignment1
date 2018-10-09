#
# inf1340, section L102
# assignment 1 - due 2018-10-17
# Chen, Gillian Siyuan
# Lam, Sharon
#
# POS program for MinMax
# v 1.0 - 2018-10-09
# compatible with Python version 3.6.5
# source file: a1-gillian-and-sharon.py)
#

""" Test cases:

"""

PRICE_SINGLE = 1.00
PRICE_SMALL = 5.00
PRICE_LARGE = 19.00
UPC_SINGLE = 111111
UPC_SMALL = 666666
UPC_LARGE = 242424
HST_RATE = 0.13

# display a welcome message
def display_welcome():
    print("Welcome to MinMax! The cashier will scan the items you wish to purchase.")

# prompt cashier to scan for each item, show the running total, and show the total bill
def get_barcode():
    scanning = True
    running_total = 0
    number_of_singles = 0
    number_of_smalls = 0
    number_of_larges = 0

    while (scanning):
        cashier_input = input("Please scan an item: ")
        cashier_input = int(cashier_input)

        if cashier_input == 0:
            print("Scanning complete.")
            scanning = False
        elif cashier_input == UPC_SINGLE:
            cost = PRICE_SINGLE + (PRICE_SINGLE * HST_RATE)
            cost_rounded = round((round(cost / 0.05) * 0.05), 2)
            running_total = running_total + cost_rounded
            number_of_singles = number_of_singles + 1
            print(running_total)
        elif cashier_input == UPC_SMALL:
            cost = PRICE_SMALL + (PRICE_SMALL * HST_RATE)
            cost_rounded = round((round(cost / 0.05) * 0.05), 2)
            running_total = running_total + cost_rounded
            number_of_smalls = number_of_smalls + 1
            print(running_total)
        elif cashier_input == UPC_LARGE:
            cost = PRICE_LARGE + (PRICE_LARGE * HST_RATE)
            cost_rounded = round((round(cost / 0.05) * 0.05), 2)
            running_total = running_total + cost_rounded
            number_of_larges = number_of_larges + 1
            print(running_total)
        else:
            print("Please enter a valid scan code.")
            continue

    subtotal_before_tax = calculate_subtotal(number_of_singles, number_of_smalls, number_of_larges)
    tax_amount = HST_RATE * subtotal_before_tax
    total_before_rounding = subtotal_before_tax + tax_amount
    total_bill = calculate_total_bill(subtotal_before_tax, tax_amount, total_before_rounding)
    display_total_bill(subtotal_before_tax, tax_amount, total_before_rounding, total_bill)

    return total_bill

# calculate the subtotal before tax
def calculate_subtotal(number_of_singles, number_of_smalls, number_of_larges):
    subtotal_before_tax = (number_of_singles * PRICE_SINGLE) + (number_of_smalls * PRICE_SMALL) + (number_of_larges * PRICE_LARGE)
    return subtotal_before_tax

# calculate the total bill
def calculate_total_bill(subtotal_before_tax, tax_amount, total_before_rounding):
    total_bill = round((round(total_before_rounding / 0.05) * 0.05), 2)
    return total_bill

# display the subtotal before tax, tax amount, total before rounding, and rounded total
def display_total_bill(subtotal_before_tax, tax_amount, total_before_rounding, total_bill):
    print("Your subtotal before taxes is: " + str(subtotal_before_tax))
    print("Tax amount: " + str(tax_amount))
    print("Total: " + str(total_before_rounding))
    print("Total amount due: " + str(total_bill))

# prompt cashier to enter the amount tendered by the customer and allow transaction to be cancelled
def get_amount_tendered(total_bill):
    print("To cancel the transaction, enter 0.")
    paying = True
    while paying == True:
        amount_tendered = float(input("Please enter the amount tendered: "))
        if amount_tendered >= total_bill:
            paying = False
        elif amount_tendered == 0:
            print("Transaction cancelled.")
            return 0
        elif amount_tendered < total_bill:
                print("The amount tendered is " + str(round((total_bill - amount_tendered), 2)) + " short of the total. Please pay the full amount." )

    return amount_tendered

# calculate and display the amount of change to be given to the customer with a goodbye message
def display_change(amount_tendered, total_bill):
    amount_of_change = amount_tendered - total_bill
    amount_of_change = round((round(amount_of_change / 0.05) * 0.05), 2)
    if amount_tendered > 0:
        print("Your change is: " + str(amount_of_change))
    print("Thank you for shopping at MinMax. Please come again!")


if __name__  ==  "__main__":
    """The cashier is prompted to start scanning items.
    """
    display_welcome()
    total_bill = get_barcode()
    amount_tendered = get_amount_tendered(total_bill)
    display_change(amount_tendered, total_bill)
