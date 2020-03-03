import menu
import display
from tabulate import tabulate
import time

# A list that holds the items that the customer orders.
customer_order = []
# Customer total is the price of all the items in the customer_order.
customer_total = 0.0
def total(customer_total):
    """Get's the customer's total."""
    customer_total = 0.0
    for food_item in customer_order:
            customer_total += menu.menu_items[food_item]
            print('\n')
            print(*customer_order, sep='\n')
            print('\n')
            print("$" + str(round(customer_total, 2)).ljust(4,'0'))
    
    customer_payment = float(input('Your total is ' + str('${:,.2f}'.format(round(customer_total, 2))) + ', please enter your card into the terminal. \n'))        
    while  customer_payment >= customer_total:
        customer_change = customer_payment - customer_total
        print('\n'+"Your change is " + str('${:,.2f}'.format(round(customer_change,2))) + " Thank you for choosing McDonald's and have a great day! :D \n")
        break
    else:
            print('Your total is $' + str(round(customer_total, 2)).ljust(4,'0') + '\n')
            customer_payment = ('Sorry, your payment could not be accepted, please try again.\n')
            print(customer_payment)
    return(customer_total)



def ordering(order = 'Do you still want to order?'):
    """Take the customer's order."""
    while True:
        order = input("What would you like to order? Please enter 'Help' to see the options available to you.\n").title()
        if order in menu.menu_items:
            customer_order.append(order)
            print('Your current order is ' + str(customer_order))
        elif order == 'Done' and len(customer_order) == 0:
            cancel_order = input("Your order is empty, if you would like to cancel please type 'Cancel' \n")
            print('\n')
            if cancel_order == 'Cancel':
                print('Please come again soon! \n')
            break
        elif order == 'Done':
            print(customer_order)
            total(customer_total)
            customer_order.clear()
        
        elif order == 'Menu':
            print(display.display)
        elif order == 'Order':
            print(str(customer_order))
        elif order == 'Help':
            print('\n')
            help_cmd = """ Here are all the help commands
            If you want to see the menu again, type 'Menu'
            If you want to remove something from your order, type 'Remove'
            If you are done with your order type 'Done'
            If you want to view your order type 'Order' 
            If you would like to exit the terminal, please enter 'Exit' twice. """
            print(help_cmd)
        elif order == 'Remove':
            remove = input('Here is your current order ' + str(customer_order) + ' what would you like to remove? \n').title()
            if remove in customer_order:
                customer_order.remove(remove)
                print(str(customer_order) + '\n')
            else:
                print("Sorry this item is not in your current order:" + str(customer_order) + '\n' )
        elif order not in menu.menu_items:
            print('This item is not on our menu, please select something from the menu.\n')
        return(order)