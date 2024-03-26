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
    pass
# TODO
#   get values from checked boxes of what to update
#   update global variables with integer values
#   see write up for amounts
#   update expenses with the cost
#   update profit by subtracting expenses from sales


def place_order():
    pass
# TODO
#   get flavor from radio buttons
#   get values from checked boxes for toppings
#   check inventory that the items are in stock; display error message if not
#   place order and call financial data function
#   The first scoop is $3.00. Each scoop extra is $1.00; calculate cost
#   update the inventory
#   update financial data

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
# TODO check boxes here for all the options (see the write up for particulars)
# TODO button to "Add To Inventory"
# TODO code so that pushing the button calls the proper functions


# ORDER FORM
tk.Label(root_window, text="\tORDER FORM").grid(row=0, column=4)
tk.Label(root_window, text="\tScoops:").grid(row=1, column=4)
ent_scoops = tk.Entry(root_window, width=5)
ent_scoops.grid(row=1, column=5, sticky=tk.W)
# TODO add radio buttons for Vanilla/Chocolate row 2
# TODO add check boxes for Sprinkles, row 3
# TODO Whipped Cream, row4
# TODO and Hot Fudge row5
tk.Button(root_window, text="Place Order", command=place_order).grid(row=6, column=5, sticky=tk.W)


# FINANCIAL DATA (done)
tk.Label(root_window, text="\tFINANCIAL DATA").grid(row=0, column=6)
tk.Label(root_window, text="\tSales:").grid(row=1, column=6, sticky=tk.W)
tk.Label(root_window, text="\tExpenses:").grid(row=2, column=6, sticky=tk.W)
tk.Label(root_window, text="\tProfit:").grid(row=3, column=6, sticky=tk.W)

tk.Label(root_window, text=f"\t${SALES:.2f}").grid(row=1, column=7, sticky=tk.W)
tk.Label(root_window, text=f"\t${EXPENSES:.2f}").grid(row=2, column=7, sticky=tk.W)
tk.Label(root_window, text=f"\t${PROFIT:.2f}").grid(row=3, column=7, sticky=tk.W)


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
