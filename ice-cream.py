import tkinter as tk
from tkinter import ttk

# Create an empty list for the transactions of all accounts
transactions = list()

# Create variables that indicate the inventory of each item
VANILLA = 0
CHOCOLATE = 0
SPRINKLES = 0
WHIP_CREAM = 0
HOT_F = 0

# def place_order():
#     # Read in amount
#     scoops = float(ent_scoops.get())
#     flavor =
#     sp =
#     whip =
#     hotf =
#     fn_update_outputs()


def cmd_remove():
    fn_update_outputs()


def fn_update_outputs(event=None):
    #pass
    balance = 0
    lst_transactions.delete(0, tk.END)
    # Loop through all the transactions and filter out those that match the combobox
    for transaction in transactions:
        # Test to see if the current transaction matches the combobox
        if transaction["account"] == cbo_accounts.get():
            # Add the value to the balance
            balance = balance + transaction["amount"]
            # Add the value to the listbox
            lst_transactions.insert(tk.END, transaction["amount"])

    # Output the balance
    lbl_balance["text"] = balance



# Creating window
root_window = tk.Tk()
root_window.title("Ice Cream Shop")
root_window.geometry("600x300")

# Setting up input controls
tk.Label(root_window, text="INVENTORY:").grid(row=0, column=0, sticky=tk.W)
tk.Label(root_window, text="Vanilla:").grid(row=1, column=0, sticky=tk.W)
tk.Label(root_window, text="Chocolate:").grid(row=2, column=0, sticky=tk.W)
tk.Label(root_window, text="Sprinkles:").grid(row=3, column=0, sticky=tk.W)
tk.Label(root_window, text="Whipped cream:").grid(row=4, column=0, sticky=tk.W)
tk.Label(root_window, text="Hot fudge:").grid(row=5, column=0, sticky=tk.W)

tk.Label(root_window, text=VANILLA).grid(row=1, column=5, sticky=tk.W)
tk.Label(root_window, text=CHOCOLATE).grid(row=2, column=5, sticky=tk.W)
tk.Label(root_window, text=SPRINKLES).grid(row=3, column=5, sticky=tk.W)
tk.Label(root_window, text=WHIP_CREAM).grid(row=4, column=5, sticky=tk.W)
tk.Label(root_window, text=HOT_F).grid(row=5, column=5, sticky=tk.W)

#ADD TO INVENTORY



#ORDER FORM
# ent_scoops = tk.Entry(root_window, width=5)
# ent_scoops.grid(row=0, column=50, sticky=tk.W)
# tk.Button(root_window, text="Place Order", command=place_order).grid(row=2, column=2, sticky=tk.W)
# tk.Label(root_window, text="Account:").grid(row=1, column=0, sticky=tk.W)
#


# FINANCIAL DATA





# USER FEEDBACK



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