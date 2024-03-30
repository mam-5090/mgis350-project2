import tkinter as tk
from tkinter import ttk

# Create variables that indicate the inventory of each item
VANILLA = 0
CHOCOLATE = 0
SPRINKLES = 0
WHIP_CREAM = 0
HOT_F = 0

# Create variables for financial data
SALES = 0.00
EXPENSES = 0.00
PROFIT = 0.00

# variable with user feedback
FEEDBACK = " "



def add_inventory():
    # pass
    chocolate_get_inv = chk_chocolate_var.get()
    vanilla_get_inv = chk_vanilla_var.get()
    sprinkles_get_inv = chk_sprinkles_add_var.get()
    cream_get_inv = chk_cream_add_var.get()
    fudge_get_inv = chk_fudge_add_var.get()

    # Ensure checkboxes are pulling properly
    print("*** DEBUGGING *** Chocolate Checked:", chocolate_get_inv)
    print("*** DEBUGGING *** Vanilla Checked:", vanilla_get_inv)
    print("*** DEBUGGING *** Sprinkles Checked:", sprinkles_get_inv)
    print("*** DEBUGGING *** Whipped Cream checked:", cream_get_inv)
    print("*** DEBUGGING *** Hot Fudge checked:", fudge_get_inv)

# TODO
#   update global variables with integer values
#   see write up for amounts
#   update expenses with the cost
#   update profit by subtracting expenses from sales


def place_order():

    #  Get flavor from radio buttons
    flavor_choice_get = 0
    flavor_choice_get = flavor_choice.get()
    print("*** DEBUGGING *** Flavor Choice is: ", flavor_choice_get)
#   get values from checked boxes for toppings - Done plb3509
    sprinkles_get = chk_sprinkles_var.get()
    cream_get = chk_cream_var.get()
    fudge_get = chk_fudge_var.get()

    # Ensuring checkboxes are pulling properly
    print("*** DEBUGGING *** Sprinkles checked:", sprinkles_get)
    print("*** DEBUGGING *** Whipped Cream checked:", cream_get)
    print("*** DEBUGGING *** Hot Fudge checked:", fudge_get)

#   TODO
#       check inventory that the items are in stock; display error message if not
#       place order and call financial data function
#       The first scoop is $3.00. Each scoop extra is $1.00; calculate cost
#       update the inventory
#       update financial data

    # scoops = int(ent_scoops.get())
    # cost = 0.00
    # ADD AN IF GUARD HERE FOR AMT OF SCOOPS TO UPDATE COST


def update_finances():
    pass
# TODO
#   Each time the user adds to inventory, expenses will be increased.
#   Each time an order is made, sales will be increased.
#   the profit is calculated by subtracting the expenses from the sales.


def user_feedback():
    pass
# TODO
#   update textbox with necessary error


# Creating window
root_window = tk.Tk()
root_window.title("Ice Cream Shop")
root_window.geometry("800x400")

# INVENTORY (done)
tk.Label(root_window, text="INVENTORY").grid(row=0, column=0, sticky=tk.W)
tk.Label(root_window, text="Vanilla:").grid(row=1, column=0, sticky=tk.W)
tk.Label(root_window, text="Chocolate:").grid(row=2, column=0, sticky=tk.W)
tk.Label(root_window, text="Sprinkles:").grid(row=3, column=0, sticky=tk.W)
tk.Label(root_window, text="Whipped cream:").grid(row=4, column=0, sticky=tk.W)
tk.Label(root_window, text="Hot fudge:").grid(row=5, column=0, sticky=tk.W)

tk.Label(root_window, text=VANILLA).grid(row=1, column=1, sticky=tk.W)
tk.Label(root_window, text=CHOCOLATE).grid(row=2, column=1, sticky=tk.W)
tk.Label(root_window, text=SPRINKLES).grid(row=3, column=1, sticky=tk.W)
tk.Label(root_window, text=WHIP_CREAM).grid(row=4, column=1, sticky=tk.W)
tk.Label(root_window, text=HOT_F).grid(row=5, column=1, sticky=tk.W)

# ADD TO INVENTORY
tk.Label(root_window, text="\tADD TO INVENTORY").grid(row=0, column=3)


# Variables to store checkbox selections
chk_vanilla_var = tk.IntVar()
chk_chocolate_var = tk.IntVar()
chk_sprinkles_add_var = tk.IntVar()
chk_cream_add_var = tk.IntVar()
chk_fudge_add_var = tk.IntVar()

# Creating vanilla checkbox
chk_vanilla = tk.Checkbutton(root_window, text="Add 256.0 oz of Vanilla", variable=chk_vanilla_var)
chk_vanilla.grid(row=1, column=3, sticky=tk.W)

# Creating Chocolate checkbox
chk_chocolate = tk.Checkbutton(root_window, text="Add 256.0 oz of Chocolate", variable=chk_chocolate_var)
chk_chocolate.grid(row=2, column=3, sticky=tk.W)

# Creating Sprinkles checkbox
chk_sprinkles_add = tk.Checkbutton(root_window, text="Add 64.0 oz of Sprinkles", variable=chk_sprinkles_add_var)
chk_sprinkles_add.grid(row=3, column=3, sticky=tk.W)

# Creating Whipped Cream checkbox
chk_cream_add = tk.Checkbutton(root_window, text="Add 64.0 oz of Whipped Cream", variable=chk_cream_add_var)
chk_cream_add.grid(row=4, column=3, sticky=tk.W)

# Creating Hot Fudge checkbox
chk_fudge_add = tk.Checkbutton(root_window, text="Add 64.0 oz of Hot Fudge", variable=chk_fudge_add_var)
chk_fudge_add.grid(row=5, column=3, sticky=tk.W)

tk.Button(root_window, text="Add To Inventory", command=add_inventory).grid(row=6, column=3, sticky=tk.W)
#  code so that pushing the button calls the proper functions - DONE plb3509
# Done via add_inventory command in button code

# ORDER FORM
tk.Label(root_window, text="\tORDER FORM").grid(row=0, column=4)
tk.Label(root_window, text="\tScoops:").grid(row=1, column=4)
ent_scoops = tk.Entry(root_window, width=5)
ent_scoops.grid(row=1, column=5, sticky=tk.W)

# TODO add radio buttons for Vanilla/Chocolate row 2 - DONE plb3509
# Variable to store flavor choice
flavor_choice = tk.StringVar()
# Chocolate RadioButton
rdo_chocolate = tk.Radiobutton(root_window, text="Chocolate", variable=flavor_choice, value="Chocolate")
rdo_chocolate.grid(row=2, column=5, sticky=tk.W)
# Vanilla RadioButton
rdo_vanilla = tk.Radiobutton(root_window, text="Vanilla", variable=flavor_choice, value="Vanilla")
rdo_vanilla.grid(row=2, column=6, sticky=tk.W)


# Variable to store checkbox states
chk_sprinkles_var = tk.IntVar()
chk_cream_var = tk.IntVar()
chk_fudge_var = tk.IntVar()
#  add check boxes for Sprinkles, row 3 - DONE plb3509
# Sprinkles checkbox (order form)
chk_sprinkles = tk.Checkbutton(root_window, text="Sprinkles", variable=chk_sprinkles_var)
chk_sprinkles.grid(row=3, column=5, sticky=tk.W)
#  Whipped Cream, row4 - Done plb3509
# Whipped Cream checkbox (order form)
chk_cream = tk.Checkbutton(root_window, text="Whipped Cream", variable=chk_cream_var)
chk_cream.grid(row=4, column=5, sticky=tk.W)
#  and Hot Fudge row5 - Done plb3509
# Hot Fudge checkbox (order form)
chk_fudge = tk.Checkbutton(root_window, text="Hot Fudge", variable=chk_fudge_var)
chk_fudge.grid(row=5, column=5, sticky=tk.W)
# Place Order button
tk.Button(root_window, text="Place Order", command=place_order).grid(row=6, column=5, sticky=tk.W)


# FINANCIAL DATA (done)
tk.Label(root_window, text="\tFINANCIAL DATA").grid(row=0, column=7)
tk.Label(root_window, text="\tSales:").grid(row=1, column=7, sticky=tk.W)
tk.Label(root_window, text="\tExpenses:").grid(row=2, column=7, sticky=tk.W)
tk.Label(root_window, text="\tProfit:").grid(row=3, column=7, sticky=tk.W)

tk.Label(root_window, text=f"\t${SALES:.2f}").grid(row=1, column=8, sticky=tk.W)
tk.Label(root_window, text=f"\t${EXPENSES:.2f}").grid(row=2, column=8, sticky=tk.W)
tk.Label(root_window, text=f"\t${PROFIT:.2f}").grid(row=3, column=8, sticky=tk.W)


# USER FEEDBACK (done)
tk.Label(root_window, text="USER FEEDBACK:").grid(row=10, column=0)
tk.Label(root_window, text=FEEDBACK).grid(row=11, column=0)


# code below is copy pasted from class

# transaction_type = tk.IntVar()
# rdo_deposit = tk.Radiobutton(root_window, text="Deposit", variable=transaction_type, value=1)
# rdo_deposit.grid(row=2, column=0, sticky=tk.W)
# rdo_deposit.select()
# rdo_withdrawal = tk.Radiobutton(root_window, text="Withdrawal", variable=transaction_type, value=-1)
# rdo_withdrawal.grid(row=3, column=0, sticky=tk.W)
#
# # Setting up Combobox
# cbo_accounts = ttk.Combobox(root_window, values=["Checking", "Savings"])
# cbo_accounts.grid(row=1, column=1, sticky=tk.W)
# cbo_accounts.bind("<<ComboboxSelected>>", fn_update_outputs)
#
# # Setting up balance controls
# tk.Label(root_window, text="Balance:").grid(row=4, column=0, sticky=tk.W)
# lbl_balance = tk.Label(root_window, text="$0.00")
# lbl_balance.grid(row=4, column=1, sticky=tk.W)
#
# # Setting up remove controls
# tk.Button(root_window, text="Remove", command=cmd_remove).grid(row=3, column=2, sticky=tk.W)
#
# # Setting up display of transaction controls
# tk.Label(root_window, text="Transactions:").grid(row=0, column=3, sticky=tk.W)
# frm_transactions = tk.Frame(root_window)
# frm_transactions.grid(row=1, rowspan=4, column=3, sticky=tk.W)
# lst_transactions = tk.Listbox(frm_transactions, height=5, selectmode=tk.SINGLE)
# lst_transactions.grid(row=0, column=0)
# scr_transactions = tk.Scrollbar(frm_transactions, command=lst_transactions.yview)
# scr_transactions.grid(row=0,column=1,sticky=tk.N+tk.S+tk.W)
# lst_transactions['yscrollcommand'] = scr_transactions.set

root_window.mainloop()
