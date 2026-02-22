from tkinter import *
import os
import time
import datetime
from tkinter import messagebox

# ---------- MODERN THEME ----------
BG_MAIN = "#F4F6F8"      # app background (light grey)
BG_PANEL = "#FFFFFF"     # frames (white)
BG_HEADER = "#2C3E50"    # title bar (dark blue)
BTN_COLOR = "#3498DB"    # buttons (blue)
BTN_EXIT = "#E74C3C"     # exit button red
TEXT_COLOR = "#2C3E50"


FONT_MAIN = ("Segoe UI", 11)
FONT_BOLD = ("Segoe UI", 11, "bold")
FONT_TITLE = ("Segoe UI", 26, "bold")



root =Tk()
root.geometry("1350x750+0+0")
root.title("Food Billing System")
root.configure(bg=BG_MAIN)

Tops = Frame(root,bg=BG_HEADER,pady=10)
Tops.pack(side=TOP, fill=X)

lblTitle=Label(
    Tops,
    text='Food Billing System',
    font=FONT_TITLE,
    bg=BG_HEADER,
    fg="white"
)
lblTitle.pack()

# ===== MAIN CONTENT AREA =====
ContentFrame = Frame(root, bg=BG_MAIN)
ContentFrame.pack(fill=BOTH, expand=True, padx=20, pady=20)

ReceiptCal_F = Frame(ContentFrame, bg=BG_PANEL, bd=2, relief=RIDGE, width=420)
ReceiptCal_F.pack(side=RIGHT, fill=Y, padx=10)

ReceiptCal_F.pack_propagate(False)

# Receipt should be TOP
Receipt_F=Frame(ReceiptCal_F,bg=BG_PANEL,bd=6,relief=FLAT)
Receipt_F.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)

# Buttons at bottom
Buttons_F=Frame(ReceiptCal_F,bg=BG_PANEL,bd=6,relief=FLAT)
Buttons_F.pack(side=BOTTOM, fill=X, padx=5, pady=5)


MenuFrame = Frame(ContentFrame, bg=BG_PANEL, bd=2, relief=RIDGE)
MenuFrame.pack(side=LEFT, fill=BOTH, expand=True, padx=20, pady=10)


Label(MenuFrame, text="Menu", font=FONT_BOLD, bg=BG_PANEL, fg=TEXT_COLOR)\
    .pack(anchor="w", padx=10, pady=(5,0))

MenuContent = Frame(MenuFrame, bg=BG_PANEL)
MenuContent.pack(fill=BOTH, expand=True, pady=10)


Drinks_F=Frame(MenuContent,bg=BG_PANEL,bd=4,relief=FLAT)
Drinks_F.grid(row=0, column=0, padx=40, pady=10, sticky="n")

Food_F=Frame(MenuContent,bg=BG_PANEL,bd=4,relief=FLAT)
Food_F.grid(row=0, column=1, padx=40, pady=10, sticky="n")

MenuContent.grid_columnconfigure(0, weight=1)
MenuContent.grid_columnconfigure(1, weight=1)

Cost_F = Frame(MenuFrame, bg=BG_PANEL, bd=2, relief=RIDGE)
Cost_F.pack(fill=X, padx=20, pady=(0,20))   # small tweak

Label(
    Cost_F,
    text="Billing Summary",
    font=FONT_BOLD,
    bg=BG_PANEL,
    fg=TEXT_COLOR
).grid(row=0, column=0, columnspan=4, sticky="w", pady=(0,8))

###################################################variables################################################


DateofOrder = StringVar()
Receipt_Ref = StringVar()
PaidTax = StringVar()
SubTotal = StringVar()
TotalCost = StringVar()
CostofFood = StringVar()
CostofDrinks = StringVar()
ServiceCharge = StringVar()
GST_Percent = StringVar(value="5")
Discount_Percent = StringVar(value="0")
DiscountAmount = StringVar()



E_Sprite = StringVar()
E_Pepsi = StringVar()
E_DietCoke = StringVar()
E_Mojito = StringVar()
E_Cappuccino = StringVar()
E_Fanta = StringVar()
E_CocaCola = StringVar()
E_ColdCoffee = StringVar()

E_HotDog = StringVar()
E_VegBurger = StringVar()
E_Pasta = StringVar()
E_RicePlate = StringVar()
E_Sandwich = StringVar()
E_Fires = StringVar()
E_Spagetti = StringVar()
E_Fazitas = StringVar()

E_Sprite.set("0")
E_Pepsi.set("0")
E_DietCoke.set("0")
E_Mojito.set("0")
E_Cappuccino.set("0")
E_Fanta.set("0")
E_CocaCola.set("0")
E_ColdCoffee.set("0")

E_HotDog.set("0")
E_VegBurger.set("0")
E_Pasta.set("0")
E_RicePlate.set("0")
E_Sandwich.set("0")
E_Fires.set("0")
E_Spagetti.set("0")
E_Fazitas.set("0")

DateofOrder.set(datetime.datetime.now().strftime("%d/%m/%Y  %I:%M %p"))

PRICES = {
    "Sprite": 65,
    "Pepsi": 75,
    "DietCoke": 99,
    "Mojito": 130,
    "Cappuccino": 180,
    "Fanta": 75,
    "CocaCola": 75,
    "ColdCoffee": 89,
    "HotDog": 260,
    "VegBurger": 175,
    "Pasta": 255,
    "RicePlate": 480,
    "Sandwich": 240,
    "Fries": 110,
    "Spaghetti": 340,
    "Fajitas": 213
}

MENU_VARS = {
    "Sprite": E_Sprite,
    "Pepsi": E_Pepsi,
    "DietCoke": E_DietCoke,
    "Mojito": E_Mojito,
    "Cappuccino": E_Cappuccino,
    "Fanta": E_Fanta,
    "CocaCola": E_CocaCola,
    "ColdCoffee": E_ColdCoffee,

    "HotDog": E_HotDog,
    "VegBurger": E_VegBurger,
    "Pasta": E_Pasta,
    "RicePlate": E_RicePlate,
    "Sandwich": E_Sandwich,
    "Fries": E_Fires,
    "Spaghetti": E_Spagetti,
    "Fajitas": E_Fazitas
}

SERVICE_PERCENT = 5
is_total_calculated = False
##########################################Function Declaration####################################################


def change_qty(textvar, delta):
    try:
        value = int(textvar.get())
    except:
        value = 0

    value += delta
    if value < 0:
        value = 0

    textvar.set(str(value))

    global is_total_calculated
    is_total_calculated = False

def iExit():
    iExit = messagebox.askyesno("Exit Restaurant System","Confirm if you want to exit")
    if iExit > 0:
        root.destroy()
        return

def Reset():

    PaidTax.set("Rs 0.00")
    SubTotal.set("Rs 0.00")
    TotalCost.set("Rs 0.00")
    CostofFood.set("Rs 0.00")
    CostofDrinks.set("Rs 0.00")
    ServiceCharge.set("Rs 0.00")
    txtReceipt.delete("1.0",END)
    Discount_Percent.set("0")
    DiscountAmount.set("Rs 0.00")


    E_Sprite.set("0")
    E_Pepsi.set("0")
    E_DietCoke.set("0")
    E_Mojito.set("0")
    E_Cappuccino.set("0")
    E_Fanta.set("0")
    E_CocaCola.set("0")
    E_ColdCoffee.set("0")

    E_HotDog.set("0")
    E_VegBurger.set("0")
    E_Pasta.set("0")
    E_RicePlate.set("0")
    E_Sandwich.set("0")
    E_Fires.set("0")
    E_Spagetti.set("0")
    E_Fazitas.set("0")



    
    btnReceipt.config(state=DISABLED)

    global is_total_calculated
    is_total_calculated = False

def get_valid_number(value, item_name):
    try:
        # Empty input = treat as 0
        if value.strip() == "":
            return 0.0
        return float(value)
    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            f"Please enter a valid number for {item_name}"
        )
        raise


def CostofItem():
    quantities = {}

    # ---- Read all quantities safely ----
    try:
        for item, var in MENU_VARS.items():
            quantities[item] = get_valid_number(var.get(), item)
    except:
        return

    # ---- Calculate Drinks & Food totals ----
    PriceofDrinks = 0
    PriceofFood = 0

    drink_items = ["Sprite","Pepsi","DietCoke","Mojito","Cappuccino","Fanta","CocaCola","ColdCoffee"]

    for item, qty in quantities.items():
        if item in drink_items:
            PriceofDrinks += qty * PRICES[item]
        else:
            PriceofFood += qty * PRICES[item]

    CostofDrinks.set(f"Rs {PriceofDrinks:.2f}")
    CostofFood.set(f"Rs {PriceofFood:.2f}")

    items_total = PriceofDrinks + PriceofFood

    # ---- Discount ----
    try:
        discount_input = float(Discount_Percent.get())
    except:
        messagebox.showerror("Invalid Discount","Enter valid discount number")
        return

    if discount_input < 0 or discount_input > 90:
        messagebox.showwarning("Invalid Discount","Discount must be between 0% and 90%")
        return

    discount_percent = discount_input / 100

    discount_amount = items_total * discount_percent
    DiscountAmount.set(f"Rs {discount_amount:.2f}")

    # ---- Service charge BEFORE discount ----
    service_amount = items_total * SERVICE_PERCENT / 100
    ServiceCharge.set(f"Rs {service_amount:.2f}")

    subtotal_before_discount = items_total + service_amount

    # ---- Apply discount ----
    discount_amount = subtotal_before_discount * discount_percent
    DiscountAmount.set(f"Rs {discount_amount:.2f}")

    SubTotalValue = subtotal_before_discount - discount_amount
    SubTotal.set(f"Rs {SubTotalValue:.2f}")

       # ---- GST ----
    try:
        gst_input = GST_Percent.get().strip()
        gst = float(gst_input if gst_input else 0) / 100
    except:
        messagebox.showerror("Invalid GST","Enter valid GST number")
        return

    TaxAmount = SubTotalValue * gst
    PaidTax.set(f"Rs {TaxAmount:.2f}")

    # ---- Final total ----
    TotalCost.set(f"Rs {SubTotalValue + TaxAmount:.2f}")

    btnReceipt.config(state=NORMAL)

    global is_total_calculated
    is_total_calculated = True


def auto_save_receipt():
    data = txtReceipt.get("1.0", END)

    if data.strip() == "":
        messagebox.showwarning("Empty","No receipt to save")
        return

    folder_path = os.path.join(os.getcwd(), "Manual_Backups")

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    filename = f"ManualBackup_{int(time.time())}.txt"
    full_path = os.path.join(folder_path, filename)

    with open(full_path, "w", encoding="utf-8") as f:
        f.write(data)


    messagebox.showinfo("Saved", f"Backup saved in:\n{full_path}")

def auto_save_receipt_background():
    data = txtReceipt.get("1.0", END)
    if data.strip() == "":
        return

    folder_path = os.path.join(os.getcwd(), "Receipts")

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    filename = f"{Receipt_Ref.get()}_{int(time.time())}.txt"
    full_path = os.path.join(folder_path, filename)

    with open(full_path, "w", encoding="utf-8") as f:
        f.write(data)

def Receipt():
    if not is_total_calculated:
        messagebox.showwarning(
            "Calculate First",
            "Please click TOTAL before generating receipt"
        )
        return
    DateofOrder.set(datetime.datetime.now().strftime("%d/%m/%Y  %I:%M %p"))
    txtReceipt.delete("1.0",END)

    Receipt_Ref.set("Bill" + str(int(time.time())))

    # Header
    txtReceipt.insert(END,      "        Adil's Restaurant\n")
    txtReceipt.insert(END,  "=============================================\n")
    txtReceipt.insert(END,  f"Receipt No : {Receipt_Ref.get()}\n")
    txtReceipt.insert(END,  f"Date       : {DateofOrder.get()}\n")
    txtReceipt.insert(END,  "=============================================\n")
    txtReceipt.insert(END,  "Item            Qty    Price    Total\n")
    txtReceipt.insert(END,  "---------------------------------------------\n")

    items = [(item, var.get()) for item, var in MENU_VARS.items()]

    total_qty = 0

    for item, qty in items:
        qty = float(qty or 0)
        if qty > 0:
            price = PRICES[item]
            total = qty * price
            total_qty += qty

            # PERFECT COLUMN ALIGNMENT
            txtReceipt.insert(
                END,
                f"{item:<18}{int(qty):<6}{price:<8}Rs {total:>8.2f}\n"
            )

    txtReceipt.insert(END,"---------------------------------------------\n")

    # Totals section
    txtReceipt.insert(END,f"{'Cost of Drinks:':<25}{CostofDrinks.get()}\n")
    txtReceipt.insert(END,f"{'Cost of Food:':<25}{CostofFood.get()}\n")
    txtReceipt.insert(END,f"{'Service Charge:':<25}{ServiceCharge.get()}\n")
    txtReceipt.insert(END,f"{'Discount:':<25}{DiscountAmount.get() or 'Rs 0.00'}\n")
    txtReceipt.insert(END,f"{'Sub Total:':<25}{SubTotal.get()}\n")
    txtReceipt.insert(END,f"{'GST Paid:':<25}{PaidTax.get()}\n")

    txtReceipt.insert(END,"=============================================\n")
    txtReceipt.insert(END,f"{'TOTAL AMOUNT:':<25}{TotalCost.get()}\n")
    txtReceipt.insert(END,f"{'Total Items:':<25}{int(total_qty)}\n")
    txtReceipt.insert(END,"=============================================\n")

    # Footer
    txtReceipt.insert(END,"\n        Thank You Visit Again 🙏\n")
    auto_save_receipt_background()
   

    


# ================= DRINKS =================

Label(Drinks_F, text="DRINKS", font=("Segoe UI", 13, "bold"),
      bg=BG_PANEL, fg=BTN_COLOR).grid(row=0, column=0, columnspan=4, pady=(0,10))

# Sprite
Label(Drinks_F,text="Sprite (Rs 65)",font=FONT_MAIN,bg=BG_PANEL).grid(row=2,column=0,sticky=W,pady=6)
Button(Drinks_F,text="➖",width=2,command=lambda: change_qty(E_Sprite,-1)).grid(row=2,column=1)
Entry(Drinks_F,textvariable=E_Sprite,width=5,justify=CENTER,font=FONT_MAIN).grid(row=2,column=2)
Button(Drinks_F,text="➕",width=2,command=lambda: change_qty(E_Sprite,1)).grid(row=2,column=3)

# Pepsi
Label(Drinks_F,text="Pepsi (Rs 75)",font=FONT_MAIN,bg=BG_PANEL).grid(row=3,column=0,sticky=W,pady=6)
Button(Drinks_F,text="➖",width=2,command=lambda: change_qty(E_Pepsi,-1)).grid(row=3,column=1)
Entry(Drinks_F,textvariable=E_Pepsi,width=5,justify=CENTER,font=FONT_MAIN).grid(row=3,column=2)
Button(Drinks_F,text="➕",width=2,command=lambda: change_qty(E_Pepsi,1)).grid(row=3,column=3)

# Diet Coke
Label(Drinks_F,text="Diet Coke (Rs 99)",font=FONT_MAIN,bg=BG_PANEL).grid(row=4,column=0,sticky=W,pady=6)
Button(Drinks_F,text="➖",width=2,command=lambda: change_qty(E_DietCoke,-1)).grid(row=4,column=1)
Entry(Drinks_F,textvariable=E_DietCoke,width=5,justify=CENTER,font=FONT_MAIN).grid(row=4,column=2)
Button(Drinks_F,text="➕",width=2,command=lambda: change_qty(E_DietCoke,1)).grid(row=4,column=3)

# Mojito
Label(Drinks_F,text="Mojito (Rs 130)",font=FONT_MAIN,bg=BG_PANEL).grid(row=5,column=0,sticky=W,pady=6)
Button(Drinks_F,text="➖",width=2,command=lambda: change_qty(E_Mojito,-1)).grid(row=5,column=1)
Entry(Drinks_F,textvariable=E_Mojito,width=5,justify=CENTER,font=FONT_MAIN).grid(row=5,column=2)
Button(Drinks_F,text="➕",width=2,command=lambda: change_qty(E_Mojito,1)).grid(row=5,column=3)

# Cappuccino
Label(Drinks_F,text="Cappuccino (Rs 180)",font=FONT_MAIN,bg=BG_PANEL).grid(row=6,column=0,sticky=W,pady=6)
Button(Drinks_F,text="➖",width=2,command=lambda: change_qty(E_Cappuccino,-1)).grid(row=6,column=1)
Entry(Drinks_F,textvariable=E_Cappuccino,width=5,justify=CENTER,font=FONT_MAIN).grid(row=6,column=2)
Button(Drinks_F,text="➕",width=2,command=lambda: change_qty(E_Cappuccino,1)).grid(row=6,column=3)

# Fanta
Label(Drinks_F,text="Fanta (Rs 75)",font=FONT_MAIN,bg=BG_PANEL).grid(row=7,column=0,sticky=W,pady=6)
Button(Drinks_F,text="➖",width=2,command=lambda: change_qty(E_Fanta,-1)).grid(row=7,column=1)
Entry(Drinks_F,textvariable=E_Fanta,width=5,justify=CENTER,font=FONT_MAIN).grid(row=7,column=2)
Button(Drinks_F,text="➕",width=2,command=lambda: change_qty(E_Fanta,1)).grid(row=7,column=3)

# CocaCola
Label(Drinks_F,text="Coca Cola (Rs 75)",font=FONT_MAIN,bg=BG_PANEL).grid(row=8,column=0,sticky=W,pady=6)
Button(Drinks_F,text="➖",width=2,command=lambda: change_qty(E_CocaCola,-1)).grid(row=8,column=1)
Entry(Drinks_F,textvariable=E_CocaCola,width=5,justify=CENTER,font=FONT_MAIN).grid(row=8,column=2)
Button(Drinks_F,text="➕",width=2,command=lambda: change_qty(E_CocaCola,1)).grid(row=8,column=3)

# Cold Coffee
Label(Drinks_F,text="Cold Coffee (Rs 89)",font=FONT_MAIN,bg=BG_PANEL).grid(row=9,column=0,sticky=W,pady=6)
Button(Drinks_F,text="➖",width=2,command=lambda: change_qty(E_ColdCoffee,-1)).grid(row=9,column=1)
Entry(Drinks_F,textvariable=E_ColdCoffee,width=5,justify=CENTER,font=FONT_MAIN).grid(row=9,column=2)
Button(Drinks_F,text="➕",width=2,command=lambda: change_qty(E_ColdCoffee,1)).grid(row=9,column=3)


# ================= FOOD =================

Label(Food_F, text="FOOD", font=("Segoe UI", 13, "bold"),
      bg=BG_PANEL, fg=BTN_COLOR).grid(row=0, column=0, columnspan=4, pady=(0,10))

# Hot Dog
Label(Food_F,text="Hot Dog (Rs 260)",font=FONT_MAIN,bg=BG_PANEL).grid(row=2,column=0,sticky=W,pady=6)
Button(Food_F,text="➖",width=2,command=lambda: change_qty(E_HotDog,-1)).grid(row=2,column=1)
Entry(Food_F,textvariable=E_HotDog,width=5,justify=CENTER,font=FONT_MAIN).grid(row=2,column=2)
Button(Food_F,text="➕",width=2,command=lambda: change_qty(E_HotDog,1)).grid(row=2,column=3)

# Veg Burger
Label(Food_F,text="Veg Burger (Rs 175)",font=FONT_MAIN,bg=BG_PANEL).grid(row=3,column=0,sticky=W,pady=6)
Button(Food_F,text="➖",width=2,command=lambda: change_qty(E_VegBurger,-1)).grid(row=3,column=1)
Entry(Food_F,textvariable=E_VegBurger,width=5,justify=CENTER,font=FONT_MAIN).grid(row=3,column=2)
Button(Food_F,text="➕",width=2,command=lambda: change_qty(E_VegBurger,1)).grid(row=3,column=3)

# Pasta
Label(Food_F,text="Pasta (Rs 255)",font=FONT_MAIN,bg=BG_PANEL).grid(row=4,column=0,sticky=W,pady=6)
Button(Food_F,text="➖",width=2,command=lambda: change_qty(E_Pasta,-1)).grid(row=4,column=1)
Entry(Food_F,textvariable=E_Pasta,width=5,justify=CENTER,font=FONT_MAIN).grid(row=4,column=2)
Button(Food_F,text="➕",width=2,command=lambda: change_qty(E_Pasta,1)).grid(row=4,column=3)

# Rice Plate
Label(Food_F,text="Rice Plate (Rs 480)",font=FONT_MAIN,bg=BG_PANEL).grid(row=5,column=0,sticky=W,pady=6)
Button(Food_F,text="➖",width=2,command=lambda: change_qty(E_RicePlate,-1)).grid(row=5,column=1)
Entry(Food_F,textvariable=E_RicePlate,width=5,justify=CENTER,font=FONT_MAIN).grid(row=5,column=2)
Button(Food_F,text="➕",width=2,command=lambda: change_qty(E_RicePlate,1)).grid(row=5,column=3)

# Sandwich
Label(Food_F,text="Sandwich (Rs 240)",font=FONT_MAIN,bg=BG_PANEL).grid(row=6,column=0,sticky=W,pady=6)
Button(Food_F,text="➖",width=2,command=lambda: change_qty(E_Sandwich,-1)).grid(row=6,column=1)
Entry(Food_F,textvariable=E_Sandwich,width=5,justify=CENTER,font=FONT_MAIN).grid(row=6,column=2)
Button(Food_F,text="➕",width=2,command=lambda: change_qty(E_Sandwich,1)).grid(row=6,column=3)

# Fries
Label(Food_F,text="Fries (Rs 110)",font=FONT_MAIN,bg=BG_PANEL).grid(row=7,column=0,sticky=W,pady=6)
Button(Food_F,text="➖",width=2,command=lambda: change_qty(E_Fires,-1)).grid(row=7,column=1)
Entry(Food_F,textvariable=E_Fires,width=5,justify=CENTER,font=FONT_MAIN).grid(row=7,column=2)
Button(Food_F,text="➕",width=2,command=lambda: change_qty(E_Fires,1)).grid(row=7,column=3)

# Spaghetti
Label(Food_F,text="Spaghetti (Rs 340)",font=FONT_MAIN,bg=BG_PANEL).grid(row=8,column=0,sticky=W,pady=6)
Button(Food_F,text="➖",width=2,command=lambda: change_qty(E_Spagetti,-1)).grid(row=8,column=1)
Entry(Food_F,textvariable=E_Spagetti,width=5,justify=CENTER,font=FONT_MAIN).grid(row=8,column=2)
Button(Food_F,text="➕",width=2,command=lambda: change_qty(E_Spagetti,1)).grid(row=8,column=3)

# Fajitas
Label(Food_F,text="Fajitas (Rs 213)",font=FONT_MAIN,bg=BG_PANEL).grid(row=9,column=0,sticky=W,pady=6)
Button(Food_F,text="➖",width=2,command=lambda: change_qty(E_Fazitas,-1)).grid(row=9,column=1)
Entry(Food_F,textvariable=E_Fazitas,width=5,justify=CENTER,font=FONT_MAIN).grid(row=9,column=2)
Button(Food_F,text="➕",width=2,command=lambda: change_qty(E_Fazitas,1)).grid(row=9,column=3)

###########################################ToTal Cost################################################################################
lblCostofDrinks=Label(Cost_F,font=FONT_MAIN,text='Cost of Drinks\t',bg=BG_PANEL,
                fg='black',justify=CENTER)
lblCostofDrinks.grid(row=0,column=0,sticky=W)
txtCostofDrinks=Entry(Cost_F,bg='white',bd=2,font=FONT_MAIN,
                        insertwidth=2,justify=RIGHT,textvariable=CostofDrinks,state='readonly')
txtCostofDrinks.grid(row=0,column=1)

lblCostofFood=Label(Cost_F,font=FONT_MAIN,text='Cost of Foods  ',bg=BG_PANEL,
                fg='black',justify=CENTER)
lblCostofFood.grid(row=1,column=0,sticky=W)
txtCostofFood=Entry(Cost_F,bg='white',bd=2,font=FONT_MAIN,
                        insertwidth=2,justify=RIGHT,textvariable=CostofFood,state='readonly')
txtCostofFood.grid(row=1,column=1)

lblServiceCharge=Label(Cost_F,font=FONT_MAIN,text='Service Charge',bg=BG_PANEL,
                fg='black',justify=CENTER)
lblServiceCharge.grid(row=2,column=0,sticky=W)
txtServiceCharge=Entry(Cost_F,bg='white',bd=2,font=FONT_MAIN,
                        insertwidth=2,justify=RIGHT,textvariable=ServiceCharge,state='readonly')
txtServiceCharge.grid(row=2,column=1)

lblGST = Label(Cost_F,font=FONT_MAIN,
               text='GST %',bg=BG_PANEL,fg='black')
lblGST.grid(row=3,column=0,sticky=W)

txtGST = Entry(Cost_F,bg='white',bd=2,font=FONT_MAIN,
               justify=RIGHT,textvariable=GST_Percent)
txtGST.grid(row=3,column=1, padx=5, pady=4)

lblDiscount = Label(Cost_F, font=FONT_MAIN,
                    text='Discount %', bg=BG_PANEL, fg='black')
lblDiscount.grid(row=4, column=0, sticky=W)

txtDiscount = Entry(Cost_F, bg='white', bd=2, font=FONT_MAIN,
                    justify=RIGHT, textvariable=Discount_Percent)
txtDiscount.grid(row=4, column=1, padx=5, pady=4)

lblDiscountAmt = Label(Cost_F, font=FONT_MAIN,
                       text='\tDiscount Amt', bg=BG_PANEL, fg='black')
lblDiscountAmt.grid(row=3, column=2, sticky=W)

txtDiscountAmt = Entry(Cost_F, bg='white', bd=2, font=FONT_MAIN,
                       justify=RIGHT, textvariable=DiscountAmount,
                       state='readonly')
txtDiscountAmt.grid(row=3, column=3)

###########################################################Payment information###################################################

lblPaidTax=Label(Cost_F,font=FONT_MAIN,text='\tPaid Tax',bg=BG_PANEL,bd=2,
                fg='black',justify=CENTER)
lblPaidTax.grid(row=0,column=2,sticky=W)
txtPaidTax=Entry(Cost_F,bg='white',bd=2,font=FONT_MAIN,
                        insertwidth=2,justify=RIGHT,textvariable=PaidTax,state='readonly')
txtPaidTax.grid(row=0,column=3)

lblSubTotal=Label(Cost_F,font=FONT_MAIN,text='\tSub Total',bg=BG_PANEL,bd=2,
                fg='black',justify=CENTER)
lblSubTotal.grid(row=1,column=2,sticky=W)
txtSubTotal=Entry(Cost_F,bg='white',bd=2,font=FONT_MAIN,
                        insertwidth=2,justify=RIGHT,textvariable=SubTotal,state='readonly')
txtSubTotal.grid(row=1,column=3)

lblTotalCost=Label(Cost_F,font=FONT_MAIN,text='\tTotal',bg=BG_PANEL,bd=2,
                fg='black',justify=CENTER)
lblTotalCost.grid(row=2,column=2,sticky=W)
txtTotalCost=Entry(Cost_F,bg='white',bd=2,font=FONT_MAIN,
                        insertwidth=2,justify=RIGHT,textvariable=TotalCost,state='readonly')
txtTotalCost.grid(row=2,column=3)

#############################################RECEIPT###############################################################################
txtReceipt=Text(
    Receipt_F,
    width=46,
    height=18,
    bg='white',
    bd=8,
    relief=RIDGE,
    font=('consolas',11)
)
txtReceipt.grid(row=0,column=0, sticky="nsew")

Receipt_F.grid_rowconfigure(0, weight=1)
Receipt_F.grid_columnconfigure(0, weight=1)



def PrintReceipt():
    data = txtReceipt.get("1.0", END)
    if data.strip() == "":
        messagebox.showwarning("Empty","No receipt to print")
        return
    messagebox.showinfo("Print",
        "Receipt sent to printer (simulation).\n"
        "Real printing requires OS printer setup.")

###########################################BUTTONS################################################################################
btnTotal = Button(Buttons_F,text="Total",bg=BTN_COLOR,fg="white",
font=FONT_BOLD,width=10,relief=FLAT,command=CostofItem)
btnTotal.grid(row=0,column=0,padx=5,pady=5)

btnReceipt = Button(Buttons_F,text="Receipt",bg=BTN_COLOR,fg="white",
font=FONT_BOLD,width=10,relief=FLAT,command=Receipt,state=DISABLED)
btnReceipt.grid(row=0,column=1,padx=5,pady=5)

btnReset = Button(Buttons_F,text="Reset",bg=BTN_COLOR,fg="white",
font=FONT_BOLD,width=10,relief=FLAT,command=Reset)
btnReset.grid(row=0,column=2,padx=5,pady=5)

btnExit = Button(Buttons_F,text="Exit",bg=BTN_EXIT,fg="white",
font=FONT_BOLD,width=10,relief=FLAT,command=iExit)
btnExit.grid(row=0,column=3,padx=5,pady=5)

btnSave = Button(Buttons_F,text="Save",bg=BTN_COLOR,fg="white",
font=FONT_BOLD,width=10,relief=FLAT,command=auto_save_receipt)
btnSave.grid(row=1,column=0,padx=5,pady=5)

btnPrint = Button(Buttons_F,text="Print",bg=BTN_COLOR,fg="white",
font=FONT_BOLD,width=10,relief=FLAT,command=PrintReceipt)
btnPrint.grid(row=1,column=1,padx=5,pady=5)

Buttons_F.grid_columnconfigure((0,1,2,3), weight=1)






root.mainloop()
