import tkinter as tk
# from tkinter import ttk

# Create variables that indicate the inventory of each item
VANILLA = 000.0
CHOCOLATE = 000.0
SPRINKLES = 0.0
WHIP_CREAM = 0.0
HOT_F = 0.0

# Create variables for financial data
SALES = 0.00
EXPENSES = 0.00
PROFIT = 0.00
order_revenue = 0.00

# variable with user feedback
FEEDBACK = "Please add inventory or place an order"


# Function to update displays
def update_displays():
    lbl_vanilla["text"] = VANILLA
    lbl_chocolate["text"] = CHOCOLATE
    lbl_sprinkles["text"] = SPRINKLES
    lbl_cream["text"] = WHIP_CREAM
    lbl_fudge["text"] = HOT_F
    lbl_sales_output["text"] = SALES
    lbl_expenses_output["text"] = EXPENSES
    lbl_profit_output["text"] = PROFIT
    lbl_feedback["text"] = FEEDBACK


def add_inventory():
    global EXPENSES, SALES, PROFIT, VANILLA, CHOCOLATE, SPRINKLES, WHIP_CREAM, HOT_F
    # pass
    #   get values from checked boxes of what to update
    # chocolate_get_inv = chk_chocolate_var.get()
    # vanilla_get_inv = chk_vanilla_var.get()
    # sprinkles_get_inv = chk_sprinkles_add_var.get()
    # cream_get_inv = chk_cream_add_var.get()
    # fudge_get_inv = chk_fudge_add_var.get()

    # Ensure checkboxes are pulling properly
    # print("*** DEBUGGING *** Chocolate Checked:", chocolate_get_inv)
    # print("*** DEBUGGING *** Vanilla Checked:", vanilla_get_inv)
    # print("*** DEBUGGING *** Sprinkles Checked:", sprinkles_get_inv)
    # print("*** DEBUGGING *** Whipped Cream checked:", cream_get_inv)
    # print("*** DEBUGGING *** Hot Fudge checked:", fudge_get_inv)

    #   update global variables with integer values
    #   see write up for amounts
    #   Calculating the expense of adding inventory | DONE - Julian
    amount_spent = 0
    if chk_vanilla_var.get() == 1:
        amount_spent += 15.00  # Cost of adding vanilla
        VANILLA += 256.0
    if chk_chocolate_var.get() == 1:
        amount_spent += 15.00  # Cost of adding chocolate
        CHOCOLATE += 256.0
    if chk_sprinkles_add_var.get() == 1:
        amount_spent += 40.00  # Cost of adding Sprinkles
        SPRINKLES += 64.0
    if chk_cream_add_var.get() == 1:
        amount_spent += 12.00  # Cost of adding Whipped Cream
        WHIP_CREAM += 64.0
    if chk_fudge_add_var.get() == 1:
        amount_spent += 10.00  # Cost of adding Hot Fudge
        HOT_F += 64.0

    #   Updating financial data | DONE - Julian
    update_finances(expense_change=amount_spent)
    # update displays
    # print("***DEBUGGING*** amount_spent is:", amount_spent)
    update_displays()


def place_order():
    global EXPENSES, SALES, PROFIT, FEEDBACK, CHOCOLATE, VANILLA, HOT_F, SPRINKLES, WHIP_CREAM
    scoop_count = ent_scoops.get()

    if scoop_count.isnumeric() is False:
        FEEDBACK = "ERROR - type in an integer for scoops"
    elif int(scoop_count) < 1:
        FEEDBACK = "ERROR - must have at least one scoop"
    else:
        scoop_count = int(scoop_count)

        #  Get flavor from radio buttons
        # flavor_choice_get = flavor_choice.get()
        # print("*** DEBUGGING *** Flavor Choice is: ", flavor_choice_get)

        # Ensuring checkboxes are pulling properly
        # print("*** DEBUGGING *** Sprinkles checked:", sprinkles_get)
        # print("*** DEBUGGING *** Whipped Cream checked:", cream_get)
        # print("*** DEBUGGING *** Hot Fudge checked:", fudge_get)

        #   check inventory that the items are in stock; display error message if not
        # Grab number of scoops needed
        # run boolean flavor choice function for if guard
        boo_chocolate = 0
        boo_vanilla = 0
        if flavor_choice.get() == "Chocolate":
            boo_chocolate = 1
        if flavor_choice.get() == "Vanilla":
            boo_vanilla = 1

        print("***DEBUGGING*** boo_chocolate is: ", boo_chocolate)
        print("***DEBUGGING*** boo_vanilla is: ", boo_vanilla)
        # variables to store amount needed for each type - using boolean math and having everything rerun every time

        chocolate_needed = scoop_count * 4 * boo_chocolate
        vanilla_needed = scoop_count * 4 * boo_vanilla
        sprinkles_needed = float(chk_sprinkles_var.get()) * .25
        cream_needed = chk_cream_var.get() * 1
        fudge_needed = float(chk_fudge_var.get()) * .5

        # Ensuring process only runs if there is adequate inventory
        if boo_vanilla == 0 and boo_chocolate == 0:
            FEEDBACK = "ERROR - must select either chocolate or vanilla"
        elif (
                CHOCOLATE >= chocolate_needed
                and VANILLA >= vanilla_needed
                and SPRINKLES >= sprinkles_needed
                and WHIP_CREAM >= cream_needed
                and HOT_F >= fudge_needed
        ):
            # Simple math to calculate updates and update storage variables
            CHOCOLATE -= chocolate_needed
            VANILLA -= vanilla_needed
            SPRINKLES -= sprinkles_needed
            WHIP_CREAM -= cream_needed
            HOT_F -= fudge_needed
            FEEDBACK = "Order successfully placed"
            # print("***DEBUGGING*** Scoop_count is: ", scoop_count)

            # Math to calculate price
            scoop_price = 3
            if scoop_count > 1:
                scoop_price += (scoop_count - 1)
            update_finances(sales_change=scoop_price)  # DONE by JULIAN
        else:
            FEEDBACK = "ERROR - insufficient inventory for order"

    update_displays()


def update_finances(expense_change=0, sales_change=0):  # | DONE - JULIAN
    global EXPENSES, SALES, PROFIT
    # DONE - Julian
    #   Each time the user adds to inventory, expenses will be increased.
    EXPENSES += expense_change
    #   Each time an order is made, sales will be increased.
    SALES += sales_change

    #   the profit is calculated by subtracting the expenses from the sales.
    PROFIT = SALES - EXPENSES

    #  Updating the GUI - commenting out as update_displays function replaces this plb3509
    # expenses_label.config(text=f"\t${EXPENSES:.2f}")
    # sales_label.config(text=f"\t${SALES:.2f}")
    # profit_label.config(text=f"\t${PROFIT:.2f}")


# def user_feedback(message):      #  |    DONE - JULIAN
#   FEEDBACK.set(message)


# Creating window
root_window = tk.Tk()
root_window.title("Ice Cream Shop")
root_window.geometry("1000x400")

# INVENTORY (done)
tk.Label(root_window, text="INVENTORY").grid(row=0, column=0, sticky=tk.W)
tk.Label(root_window, text="Vanilla:").grid(row=1, column=0, sticky=tk.W)
tk.Label(root_window, text="Chocolate:").grid(row=2, column=0, sticky=tk.W)
tk.Label(root_window, text="Sprinkles:").grid(row=3, column=0, sticky=tk.W)
tk.Label(root_window, text="Whipped cream:").grid(row=4, column=0, sticky=tk.W)
tk.Label(root_window, text="Hot fudge:").grid(row=5, column=0, sticky=tk.W)

lbl_vanilla = tk.Label(root_window, text=VANILLA)
lbl_vanilla.grid(row=1, column=1, sticky=tk.W)
lbl_chocolate = tk.Label(root_window, text=CHOCOLATE)
lbl_chocolate.grid(row=2, column=1, sticky=tk.W)
lbl_sprinkles = tk.Label(root_window, text=SPRINKLES)
lbl_sprinkles.grid(row=3, column=1, sticky=tk.W)
lbl_cream = tk.Label(root_window, text=WHIP_CREAM)
lbl_cream.grid(row=4, column=1, sticky=tk.W)
lbl_fudge = tk.Label(root_window, text=HOT_F)
lbl_fudge.grid(row=5, column=1, sticky=tk.W)

## Defining GUI labels - labels already exist, commenting out plb3509
# expenses_label=tk.Label(root_window, text=f"\t${EXPENSES:.2f}")
# expenses_label.grid(row = 2, column = 8, sticky=tk.W)

# sales_label = tk.Label(root_window, text=f"\t${SALES:.2f}")
# sales_label.grid(row=1, column=8, sticky=tk.W)

# profit_label = tk.Label(root_window, text=f"\t${PROFIT:.2f}")
# profit_label.grid(row=3, column=8, sticky=tk.W)


# FEEDBACK GUI   | DONE - JULIAN


# ADD TO INVENTORY
tk.Label(root_window, text="\tADD TO INVENTORY").grid(row=0, column=3)
# check boxes here for all the options (see the write up for particulars) - DONE plb3509
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

#  button to "Add To Inventory" - DONE plb3509
tk.Button(root_window, text="Add To Inventory", command=add_inventory).grid(row=6, column=3, sticky=tk.W)
#  code so that pushing the button calls the proper functions - DONE plb3509
# Done via add_inventory command in button code

# ORDER FORM
tk.Label(root_window, text="\tORDER FORM").grid(row=0, column=4)
tk.Label(root_window, text="\tScoops:").grid(row=1, column=4)
ent_scoops = tk.Entry(root_window, width=5)
ent_scoops.grid(row=1, column=5, sticky=tk.W)
#  add radio buttons for Vanilla/Chocolate row 2 - DONE plb3509
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

lbl_sales_output = tk.Label(root_window, text="0")
lbl_sales_output.grid(row=1, column=8, sticky=tk.W)
lbl_expenses_output = tk.Label(root_window, text="0")
lbl_expenses_output.grid(row=2, column=8, sticky=tk.W)
lbl_profit_output = tk.Label(root_window, text="0")
lbl_profit_output.grid(row=3, column=8, sticky=tk.W)

# USER FEEDBACK (done)
tk.Label(root_window, text="USER FEEDBACK:").grid(row=10, column=0)
lbl_feedback = tk.Label(root_window, text=FEEDBACK)
lbl_feedback.grid(row=11, column=0)

root_window.mainloop()


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


