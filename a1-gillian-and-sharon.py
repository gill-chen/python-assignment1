#
# inf1340, section L102
# assignment 1 - due 2018-10-17
# Chen, Gillian Siyuan
# Lam, Sharon
#
# POS program for MinMax
# v 1.1 - 2018-10-13
# compatible with Python version 3.6.5
# source file: a1-gillian-and-sharon.py
#

PRICE_SINGLE = 1.00
PRICE_SMALL = 5.00
PRICE_LARGE = 19.00
UPC_SINGLE = 111111
UPC_SMALL = 666666
UPC_LARGE = 242424
HST_RATE = 0.13

# display a welcome message
def display_welcome():
    """(NoneType) -> str
    Print string welcoming the customer and prompting the cashier to begin scanning barcodes.
    >>> display_welcome()
    Welcome to MinMax! The cashier will scan the items you wish to purchase.
    """

    print("Welcome to MinMax! The cashier will scan the items you wish to purchase.")

# prompt cashier to scan barcodes
def get_barcode():
    """(NoneType) -> list
    Returns a list of barcodes entered from input. Calls calculate_subtotal and calculate_total_bill
    to print the running subtotal and tax of the scanned items with tax and nickel rounding until input of 0 is
    received, then prints a completion message. Prints an error message if scan code is not recognised.
    >>> get_barcode()
    Please scan an item: 111111
    Total amount due: $1.15
    Please scan an item: 666666
    Total amount due: $6.80
    Please scan an item: 242424
    Total amount due: $28.25
    Please scan an item: 123456
    Please enter a valid scan code.
    Please scan an item: 0
    Scanning complete.
    """

    scanning = True
    UPC = []

    while scanning == True:
        cashier_input = input("Please scan an item: ")
        cashier_input = int(cashier_input)

        if cashier_input == 0:
            print("Scanning complete.")
            scanning = False
            break
        elif cashier_input == UPC_SINGLE:
            UPC.append(UPC_SINGLE)
        elif cashier_input == UPC_SMALL:
            UPC.append(UPC_SMALL)
        elif cashier_input == UPC_LARGE:
            UPC.append(UPC_LARGE)
        else:
            print("Please enter a valid scan code.")
            continue

        subtotal_before_tax = calculate_subtotal(UPC)
        totals = calculate_total_bill(subtotal_before_tax)
        print("Total amount due: $" + "{:.2f}".format(totals[3]))

    return UPC

# calculate and return the subtotal before tax
def calculate_subtotal(UPC):
    """ (list) -> float
    Returns the subtotal_before_tax by multiplying the corresponding price with the count of
    each UPC code in the list UPC, then adding all three.
    >>> calculate_subtotal((1 * 1.0) + (1 * 5.0) + (1 * 19.0))
    25.0
    """

    subtotal_before_tax = ((UPC.count(UPC_SINGLE) * PRICE_SINGLE) + (UPC.count(UPC_SMALL) * PRICE_SMALL)
     + (UPC.count(UPC_LARGE) * PRICE_LARGE))

    return subtotal_before_tax

# calculate and return the total bill, then call display_total_bill
def calculate_total_bill(subtotal_before_tax):
    """ (float) -> list
    Returns list totals containing subtotal_before_tax, tax_amount, total_before_rounding, and total_bill
    rounded to the nearest 5 cents.
    >>> calculate_total_bill(25.0)
    [25.0, 3.25, 28.25, 28.25]
    >>> calculate_total_bill(2.0)
    [2.0, 0.26, 2.26, 2.25]
    """

    tax_amount = HST_RATE * subtotal_before_tax
    total_before_rounding = subtotal_before_tax + tax_amount
    total_bill = round((round(total_before_rounding / 0.05) * 0.05), 2)

    totals = [subtotal_before_tax, tax_amount, total_before_rounding, total_bill]

    return totals

# print the subtotal before tax, tax amount, total before rounding, and rounded total
def display_total_bill(totals):
    """ (list) -> NoneType
    Prints strings with the subtotal_before_tax, tax_amount, total_before_rounding, and total_bill
    from four items in list totals.
    >>> display_total_bill([25.0, 3.25, 28.25, 28.25])
    Subtotal before taxes: $25.00
    Tax amount: $3.25
    Total: $28.25
    Total amount due: $28.25
    >>> display_total_bill([2.0, 0.26, 2.26, 2.25])
    Subtotal before taxes: $2.00
    Tax amount: $0.26
    Total: $2.26
    Total amount due: $2.25
    """

    print("Subtotal before taxes: $" + str("{:.2f}".format(totals[0])))
    print("Tax amount: $" + str("{:.2f}".format(totals[1])))
    print("Total: $" + str("{:.2f}".format(totals[2])))
    print("Total amount due: $" + str("{:.2f}".format(totals[3])))

# prompt cashier to enter the amount tendered by the customer and allow transaction to be cancelled
def get_amount_tendered(total_bill):
    """ (list) -> float 
    Return the amount_tendered after checking it against total_bill. If input of 0 is received, a
    cancellation message is printed. If the amount_tendered is less than total_bill, an error
    message will be displayed.
    >>> get_amount_tendered(2.25)
    To cancel the transaction, enter 0.
    Please enter the amount tendered: 2
    The amount tendered is $0.25 short of the total. Please pay the full amount.
    Please enter the amount tendered: 0
    Transaction cancelled.
    >>> get_amount_tendered(2.25)
    To cancel the transaction, enter 0.
    Please enter the amount tendered: 3
    3
    """

    print("To cancel the transaction, enter 0.")
    paying = True
    while paying == True:
        amount_tendered = float(input("Please enter the amount tendered: "))
        if amount_tendered >= total_bill:
            paying = False
        elif amount_tendered == 0:
            print("Transaction cancelled.")
            return 0.00 
        elif amount_tendered < total_bill:
                print("The amount tendered is $" + str("{:.2f}".format(total_bill - amount_tendered))
                + " short of the total. Please pay the full amount.")

    return amount_tendered

# calculate and print the amount of change to be given to the customer with a goodbye message
def display_change(amount_tendered, total_bill):
    """ (float, list) -> NoneType
    Prints the amount_of_change calculated from amount_tendered and total_bill if amount_tendered
    is greater than 0. Prints a goodbye message.
    >>> display_change(3, [2.0, 0.26, 2.26, 2.25])
    Your change is: $0.75
    Thank you for shopping at MinMax. Please come again!
    >>> display_change(2.25, [2.0, 0.26, 2.26, 2.25])
    Your change is: $0.00
    Thank you for shopping at MinMax. Please come again!
    """

    amount_of_change = amount_tendered - total_bill
    amount_of_change = round((round(amount_of_change / 0.05) * 0.05), 2)
    if amount_tendered > 0:
        print("Your change is: $" + str("{:.2f}".format(amount_of_change)))
    print("Thank you for shopping at MinMax. Please come again!")


if __name__  ==  "__main__":
    """The cashier is prompted to start scanning items.
    """
    display_welcome()
    UPC = get_barcode()
    subtotal_before_tax = calculate_subtotal(UPC)
    totals = calculate_total_bill(subtotal_before_tax)
    display_total_bill(totals)
    total_bill = totals[3]
    amount_tendered = get_amount_tendered(total_bill)
    display_change(amount_tendered, total_bill)