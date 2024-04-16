import tkinter as tk
from tkinter import ttk
import sqlite3
import pathlib
from tkinter import messagebox

db_file = pathlib.Path("Project 3 Database - Template.sqlite3")

# Test to see if the database exists
if db_file.exists():
    print("Database found")
    # Open the database and set up the cursor
    conn = sqlite3.connect(db_file)
    cur = conn.cursor()
else:
    messagebox.showerror("DATABASE ERROR", "Database not found!")
    # Force quit the program
    quit()

# create tables if not exist
fin_tbl = "CREATE TABLE IF NOT EXISTS finances( id INT primary key, sales REAL, expenses REAL);"
inv_tbl = ("CREATE TABLE IF NOT EXISTS inventory( id INT primary key, vanilla REAL, chocolate REAL, sprinkles REAL, "
       "whipcream REAL, hotfudge REAL);")
ord_tbl = "CREATE TABLE IF NOT EXISTS orders( id INT primary key, orderNumber INT, lineItemText TEXT);"

cur.execute(fin_tbl)
cur.execute(inv_tbl)
cur.execute(ord_tbl)

# Create variables that indicate the inventory of each item and grab current values
cur.execute("SELECT vanilla, chocolate,sprinkles,whipcream,hotfudge FROM inventory WHERE id = (SELECT MAX(id) FROM inventory);")
row = cur.fetchone()
VANILLA = row[0]
CHOCOLATE = row[1]
SPRINKLES = row[2]
WHIP_CREAM = row[3]
HOT_F = row[4]

# create list of line orders
line_orders = list()

# Create variables for financial data
cur.execute("SELECT sales, expenses FROM finances WHERE id = (SELECT MAX(id) FROM finances);")
row = cur.fetchone()
SALES = row[0]
EXPENSES = row[1]
PROFIT = SALES-EXPENSES
order_revenue = 0.00


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
    lbl_feedback["text"] = "UPDATE" # TODO update this to change PAST ORDERS
    # TODO update line items
    # TODO update PAST ORDER DETAILS


def add_inventory():
    global VANILLA, CHOCOLATE, SPRINKLES, WHIP_CREAM, HOT_F

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
        HOT_F += 48.0

    #   Updating financial data
    update_finances(expense_change=amount_spent)

    # TODO write sql statement to update inventory

    # print("***DEBUGGING*** amount_spent is:", amount_spent)
    update_displays()


def add_order():
    # TODO update line item box
    scoop_count = ent_scoops.get()

    if scoop_count.isnumeric() is False:
        messagebox.showerror("ERROR - type in an integer for scoops")
    elif int(scoop_count) < 1:
        messagebox.showerror("ERROR - must have at least one scoop")
    else:
        scoop_count = int(scoop_count)

    flv = flavor_choice.get()
    sp = ""
    wc = ""
    fudge = ""
    if chk_sprinkles_var.get():
        sp = " Sprinkles"
    if chk_cream_var.get():
        wc = " Whip Cream"
    if chk_fudge_var.get():
        fudge = " Hot Fudge"

    order = f"{scoop_count} Scoops {flv}{sp}{wc}{fudge}"
    # TODO add order to line_orders list



def cancel_order():
    pass
# TODO clear line item box and temp lst


def place_order():
    global CHOCOLATE, VANILLA, HOT_F, SPRINKLES, WHIP_CREAM
    scoop_count = ent_scoops.get()

    if scoop_count.isnumeric() is False:
        messagebox.showerror("ERROR - type in an integer for scoops")
    elif int(scoop_count) < 1:
        messagebox.showerror("ERROR - must have at least one scoop")
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
            # TODO display this in Line Items
        if flavor_choice.get() == "Vanilla":
            boo_vanilla = 1
            # TODO display this in Line Items

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
            messagebox.showerror("ERROR - must select either chocolate or vanilla")
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
            # print("***DEBUGGING*** Scoop_count is: ", scoop_count)

            # Math to calculate price
            scoop_price = 3
            if scoop_count > 1:
                scoop_price += (scoop_count - 1)
            update_finances(sales_change=scoop_price)
        else:
            messagebox.showerror("ERROR - insufficient inventory for order")

    update_displays()


def update_finances(expense_change=0, sales_change=0):
    global EXPENSES, SALES, PROFIT
    #   Each time the user adds to inventory, expenses will be increased.
    EXPENSES += expense_change
    #   Each time an order is made, sales will be increased.
    SALES += sales_change

    #   the profit is calculated by subtracting the expenses from the sales.
    PROFIT = SALES - EXPENSES

    # TODO write SQL statement to reflect the changes in the above, don't forget to increase ID of lineorder


# Creating window
root_window = tk.Tk()
root_window.title("Ice Cream Shop; Project 3")
root_window.geometry("1000x400")

# INVENTORY
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


# ORDER FORM
tk.Label(root_window, text="\tORDER FORM").grid(row=0, column=4)
tk.Label(root_window, text="\tScoops:").grid(row=1, column=4)
ent_scoops = tk.Entry(root_window, width=5)
ent_scoops.grid(row=1, column=5, sticky=tk.W)
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

# Sprinkles checkbox (order form)
chk_sprinkles = tk.Checkbutton(root_window, text="Sprinkles", variable=chk_sprinkles_var)
chk_sprinkles.grid(row=3, column=5, sticky=tk.W)
# Whipped Cream checkbox (order form)
chk_cream = tk.Checkbutton(root_window, text="Whipped Cream", variable=chk_cream_var)
chk_cream.grid(row=4, column=5, sticky=tk.W)
# Hot Fudge checkbox (order form)
chk_fudge = tk.Checkbutton(root_window, text="Hot Fudge", variable=chk_fudge_var)
chk_fudge.grid(row=5, column=5, sticky=tk.W)
# add to order button
tk.Button(root_window, text="Add To Order", command=add_order).grid(row=6, column=5, sticky=tk.W)
#cancel order button
tk.Button(root_window, text="Cancel Order", command=cancel_order).grid(row=6, column=5, sticky=tk.W)
# Place Order button
tk.Button(root_window, text="Place Order", command=place_order).grid(row=6, column=5, sticky=tk.W)


# FINANCIAL DATA
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

# TODO change this to be Past Orders. also add a show order details button
# USER FEEDBACK
tk.Label(root_window, text="USER FEEDBACK:").grid(row=10, column=0)
lbl_feedback = tk.Label(root_window, text="change")
lbl_feedback.grid(row=11, column=0)

# TODO add LINE ITEMS
#  Place Order button
#  Cancel Order button

# TODO add PAST ORDER DETAILS


root_window.mainloop()

# Close the cursor and connection
cur.close()
conn.close()

