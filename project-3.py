"""
MGIS-350-02 Spring 2024
Group 3
Project 3 due 4/29/24 11:59
@author Madeline Mariano mam5090
@author Poonam S psgpt
@author Parker Barnaby plb359
@author Kyeni Musembi km7138
@author

(please add your name as you work on the project)

"""
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
conn.commit()

# Create variables that indicate the inventory of each item and grab current values
cur.execute("SELECT vanilla, chocolate,sprinkles,whipcream,hotfudge FROM inventory WHERE id = 1;")
row = cur.fetchone()
VANILLA = 0
CHOCOLATE = 0
SPRINKLES = 0
WHIP_CREAM = 0
HOT_F = 0
print(row)
if row:
    VANILLA = row[0]
    CHOCOLATE = row[1]
    SPRINKLES = row[2]
    WHIP_CREAM = row[3]
    HOT_F = row[4]
else:
    cur.execute("INSERT INTO inventory(id, vanilla, chocolate, sprinkles, whipcream, hotfudge) VALUES"
                "(1,0,0,0,0,0);")
    conn.commit()

# create list of line orders
print(VANILLA)
line_orders = list()
order_details = list()
# scoops choc van sprinkles whippedcream hotfudge

# Create variables for financial data
cur.execute("SELECT sales, expenses FROM finances WHERE id = 1;")
row = cur.fetchone()
print(row)

if row:
    SALES = float(row[0])
    EXPENSES = float(row[1])
else:
    cur.execute("INSERT INTO finances (id, sales, expenses) VALUES (1, 0.0, 0.0);")
    conn.commit()
    SALES = 0.00
    EXPENSES = 0.00

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
    past_orders()
    # TODO change PAST ORDER DETAILS-- psgpt
    # TODO update line items -- psgpt


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

    # cur.execute("SELECT vanilla, chocolate,sprinkles,whipcream,hotfudge FROM inventory WHERE id = 1;")
    # print(cur.fetchone())
    cur.execute("""
         UPDATE inventory
         SET vanilla = ?, chocolate = ?, sprinkles = ?, whipcream = ?, hotfudge = ?
         WHERE id = 1; """, (VANILLA, CHOCOLATE, SPRINKLES, WHIP_CREAM, HOT_F))
    conn.commit()
    cur.execute("SELECT vanilla, chocolate,sprinkles,whipcream,hotfudge FROM inventory WHERE id = 1;")
    print(cur.fetchone())

    update_displays()


def add_order():
    global order_details, line_orders
    scoop_count = ent_scoops.get()

    if scoop_count.isnumeric() is False:
        messagebox.showerror("ERROR", "Type in an integer for scoops")
    elif int(scoop_count) < 1:
        messagebox.showerror("ERROR", "Must have at least one scoop")
    else:
        scoop_count = int(scoop_count)

    order_det = f"{scoop_count}"
    flv = flavor_choice.get()
    if flv == "Chocolate":
        order_det += "10"
        flv = " Chocolate"
    if flv == "Vanilla":
        order_det += "01"
        flv = " Vanilla"
    sp = ""
    wc = ""
    fudge = ""
    if chk_sprinkles_var.get():
        sp = " Sprinkles"
        order_det += "1"
    else:
        order_det += "0"
    if chk_cream_var.get():
        wc = " Whip Cream"
        order_det += "1"
    else:
        order_det += "0"
    if chk_fudge_var.get():
        fudge = " Hot Fudge"
        order_det += "1"
    else:
        order_det += "0"

    order = f"{scoop_count} Scoops{flv}{sp}{wc}{fudge}"
    line_orders.append(order)
    order_details.append(order_det)
    #  TODO update line items display box


def cancel_order():
    global order_details, line_orders
    line_orders.clear()
    order_details.clear()
    update_line_items()

# done clear order_details lst (global)
# done clear line_orders lst (global)


def place_order():
    global CHOCOLATE, VANILLA, SPRINKLES, WHIP_CREAM, HOT_F, order_details, line_orders

    # DONE set values of needed variables below to the index in the string of order_details.
    # DONE will need to be a for loop since order_details is a list of strings of numbers. don't forget to cast the value as an int

    # ORDER OF VALUES IN ELEMENTS OF ORDER_DETAILS scoops choc van sprinkles whippedcream hotfudge
    # the elements in order_details for example could be 310001 and that would be 3 scoops of chocolate with hot fudge
    # first number is num of scoops, 0 indicates not in order, 1 indicates yes in order

    cur.execute("SELECT MAX(id) FROM orders;")
    result = cur.fetchone()
    if result[0] is not None:  # this ensures that if there are no orders placed we begin indexing at 1, else set new_id to max
        new_id = int(result[0])
    else:
        new_id = 0

    print(new_id) #testing
    idx = 0
    for order in order_details:
        new_id += 1
        scoop_count = int(order[0])

        chocolate_needed = scoop_count * 4 * int(order[1])
        vanilla_needed = scoop_count * 4 * int(order[2])
        sprinkles_needed = float(order[3]) * .25
        cream_needed = int(order[4]) * 1
        fudge_needed = float(order[5]) * .5

        # DEBUGGING:
        print(CHOCOLATE >= chocolate_needed,
                VANILLA >= vanilla_needed,
                 SPRINKLES >= sprinkles_needed,
                 WHIP_CREAM >= cream_needed,
                 HOT_F >= fudge_needed)

        # Ensuring process only runs if there is adequate inventory
        if (
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
            cur.execute("""
                    UPDATE inventory
                    SET vanilla = ?, chocolate = ?, sprinkles = ?, whipcream = ?, hotfudge = ?
                    WHERE id = 1;
                """, (VANILLA, CHOCOLATE, SPRINKLES, WHIP_CREAM, HOT_F))

            # Math to calculate price
            scoop_price = 3
            if scoop_count > 1:
                scoop_price += (scoop_count - 1)
            update_finances(sales_change=scoop_price)
            cur.execute("""INSERT INTO orders(id, orderNumber, lineItemText) VALUES (?, ?, ?);""",
                        (new_id, new_id, line_orders[idx]))
            conn.commit()
        else:
            messagebox.showerror("ERROR", "Insufficient inventory for order")
        idx += 1

    # done for each line_item in line_orders, create an SQL statement to add it to "orders" table
    # done clear global line_orders and order_details

    cancel_order() # note this isn't actually canceling the order, it is just clearing the screen
    update_displays()


def update_finances(expense_change=0, sales_change=0):
    global EXPENSES, SALES, PROFIT
    #   Each time the user adds to inventory, expenses will be increased.
    EXPENSES += expense_change
    #   Each time an order is made, sales will be increased.
    SALES += sales_change

    #   the profit is calculated by subtracting the expenses from the sales.
    PROFIT = SALES - EXPENSES

    # done write SQL statement to reflect the changes in the above
    cur.execute("""
            UPDATE finances
            SET sales = ?, expenses = ? 
            WHERE id = 1;
        """, (SALES, EXPENSES))
    conn.commit()
    update_displays()


def update_line_items():
    global line_orders
    if len(line_orders) == 0:
        pass
        # TODO CLEAR THE BOX

    for order in line_orders:
        pass
        # TODO display this order in the line orders text box. see write up - km7138


def past_orders():
    pass
    # TODO populate the ID numbers of past orders into the textbox(?). see write up - km7138
    #  note THIS WILL REQUIRE SQL CALLS


def show_details():
    pass
    # TODO show order details of selected order in the PASTORDERS box. see write up - km7138
    #  note THIS WILL REQUIRE SQL CALLS


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
chk_fudge_add = tk.Checkbutton(root_window, text="Add 48.0 oz of Hot Fudge", variable=chk_fudge_add_var)
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



# FINANCIAL DATA
tk.Label(root_window, text="\tFINANCIAL DATA").grid(row=0, column=7)
tk.Label(root_window, text="\tSales:").grid(row=1, column=7, sticky=tk.W)
tk.Label(root_window, text="\tExpenses:").grid(row=2, column=7, sticky=tk.W)
tk.Label(root_window, text="\tProfit:").grid(row=3, column=7, sticky=tk.W)

lbl_sales_output = tk.Label(root_window, text=SALES)
lbl_sales_output.grid(row=1, column=8, sticky=tk.W)
lbl_expenses_output = tk.Label(root_window, text=EXPENSES)
lbl_expenses_output.grid(row=2, column=8, sticky=tk.W)
lbl_profit_output = tk.Label(root_window, text=PROFIT)
lbl_profit_output.grid(row=3, column=8, sticky=tk.W)

# ADD Past Orders. also add a show order details button note that the line the user selects will be notes - DONE plb3059
frm_pastorder = tk.Frame(root_window)
frm_pastorder.grid(row=7, column=3, sticky=tk.E)
tk.Label(frm_pastorder, text="\tPast Orders").grid(column=0, row=0, sticky=tk.W)
lst_pastorder = tk.Listbox(frm_pastorder, height=5, width=25, selectmode=tk.SINGLE)
lst_pastorder.grid(column=0, row=1, sticky=tk.E)
scr_pastorder = tk.Scrollbar(frm_pastorder, command=lst_pastorder.yview)
scr_pastorder.grid(row=1, column=1)
# Create button
tk.Button(root_window, text="Show Order Details", command=show_details).grid(row=8, column=3, sticky=tk.W)
#  when the button is pressed. the button should call show_details
#   NOTE the row/column values will need to be changed to reflect new lay out
# add to order button
tk.Button(root_window, text="Add To Order", command=add_order).grid(row=6, column=5, sticky=tk.W)
# cancel order button
tk.Button(root_window, text="Cancel Order", command=cancel_order).grid(row=9, column=5, sticky=tk.W)
# Place Order button
tk.Button(root_window, text="Place Order", command=place_order).grid(row=8, column=5, sticky=tk.W)

#  add LINE ITEMS DONE plb3509
frm_line_items = tk.Frame(root_window)
frm_line_items.grid(row=7, column=5, sticky=tk.E)
tk.Label(frm_line_items, text="\tLine Items").grid(column=0, row=0, sticky=tk.W)
lst_line_items = tk.Listbox(frm_line_items, height=5, width=25, selectmode=tk.SINGLE)
lst_line_items.grid(column=0, row=1, sticky=tk.E)
scr_line_items = tk.Scrollbar(frm_line_items, command=lst_line_items.yview)
scr_line_items.grid(row=1, column=1, sticky=tk.E)
lst_line_items['yscrollcommand'] = scr_line_items
#  add PAST ORDER DETAILS DONE plb3509
frm_pastorder_det = tk.Frame(root_window)
frm_pastorder_det.grid(row=7, column=7, sticky=tk.E)
tk.Label(frm_pastorder_det, text="\tPast Order Details").grid(column=0, row=0, sticky=tk.W)
lst_pastorder_det = tk.Listbox(frm_pastorder_det, height=5, width=25, selectmode=tk.SINGLE)
lst_pastorder_det.grid(column=0, row=1, sticky=tk.E)
scr_pastorder_det = tk.Scrollbar(frm_pastorder_det, command=lst_pastorder_det.yview)
scr_pastorder_det.grid(row=1, column=1)

root_window.mainloop()

# Close the cursor and connection
cur.close()
conn.close()

