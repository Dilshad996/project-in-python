from tkinter import *
import random
import time

root = Tk()
root.geometry("890x580+0+0")
root.title("RESTAURANT BILLING SYSTEM")
root.configure(bg="#D2B48C")  

Tops = Frame(root, bg="black", width=1600, height=50, relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width=900, height=700, relief=SUNKEN, bg="#D2B48C") 
f1.pack(side=LEFT)

f2 = Frame(root, width=400, height=700, relief=SUNKEN, bg="#D2B48C") 
f2.pack(side=RIGHT)

# ------------------TIME--------------
localtime = time.asctime(time.localtime(time.time()))
# -----------------INFO TOP------------
lblinfo = Label(Tops, font=('times new roman', 30, 'bold'), text="RESTAURANT BILLING", fg="Brown", bd=10, anchor='w')
lblinfo.grid(row=0, column=0)
lblinfo = Label(Tops, font=('times new roman', 20,), text=localtime, fg="steel blue", anchor=W)
lblinfo.grid(row=1, column=0)


def Ref():
    cof = float(Fries.get())
    colfries = float(Largefries.get())
    cob = float(Dessert.get())
    cofi = float(Filet.get())
    cochee = float(Cheese_Dessert.get())
    codr = float(Drinks.get())

    costoffries = cof * 25
    costoflargefries = colfries * 40
    costofDessert = cob * 35
    costoffilet = cofi * 50
    costofcheeseDessert = cochee * 30
    costofdrinks = codr * 35

    costofmeal = "Rs.", str('%.2f' % (costoffries + costoflargefries + costofDessert + costoffilet +
                                      costofcheeseDessert + costofdrinks))
    PayTax = ((costoffries + costoflargefries + costofDessert + costoffilet + costofcheeseDessert +
               costofdrinks) * 0.33)
    Totalcost = (costoffries + costoflargefries + costofDessert + costoffilet +
                 costofcheeseDessert + costofdrinks)
    Ser_Charge = ((costoffries + costoflargefries + costofDessert + costoffilet +
                   costofcheeseDessert + costofdrinks) / 99)
    Service = "Rs.", str('%.2f' % Ser_Charge)
    OverAllCost = "Rs.", str(PayTax + Totalcost + Ser_Charge)
    PaidTax = "Rs.", str('%.2f' % PayTax)

    Service_Charge.set(Service)
    cost.set(costofmeal)
    Tax.set(PaidTax)
    Subtotal.set(costofmeal)
    Total.set(OverAllCost)


def qexit():
    root.destroy()


def reset():
    rand.set("")
    Fries.set("")
    Largefries.set("")
    Dessert.set("")
    Filet.set("")
    Subtotal.set("")
    Total.set("")
    Service_Charge.set("")
    Drinks.set("")
    Tax.set("")
    cost.set("")
    Cheese_Dessert.set("")


# ---------------------------------------------------------------------------------------
rand = StringVar()
Fries = StringVar()
Largefries = StringVar()
Dessert = StringVar()
Filet = StringVar()
Subtotal = StringVar()
Total = StringVar()
Service_Charge = StringVar()
Drinks = StringVar()
Tax = StringVar()
cost = StringVar()
Cheese_Dessert = StringVar()

lblreference = Label(f1, font=('times new roman', 16, 'bold'), text="Order No.", fg="#5C4033", bd=20, anchor='w',
                     bg="#D2B48C")  # Changing background color
lblreference.grid(row=0, column=0)
txtreference = Entry(f1, font=('times new roman', 16, 'bold'), textvariable=rand, bd=6, insertwidth=6, bg="yellow",
                     justify='right')
txtreference.grid(row=0, column=1)

lblfries = Label(f1, font=('times new roman', 16, 'bold'), text=" French Fries ", fg="#000080", bd=10, anchor='w',
                 bg="#D2B48C")  # Changing background color
lblfries.grid(row=2, column=0)
txtfries = Entry(f1, font=('times new roman', 16, 'bold'), textvariable=Fries, bd=6, insertwidth=4, bg="green",
                 justify='right')
txtfries.grid(row=2, column=1)

lblLargefries = Label(f1, font=('times new roman', 16, 'bold'), text="Lunch ", fg="#000080", bd=10, anchor='w',
                      bg="#D2B48C")  # Changing background color
lblLargefries.grid(row=3, column=0)
txtLargefries = Entry(f1, font=('times new roman', 16, 'bold'), textvariable=Largefries, bd=6, insertwidth=4,
                      bg="green", justify='right')
txtLargefries.grid(row=3, column=1)

lblDessert = Label(f1, font=('times new roman', 16, 'bold'), text="Dessert ", fg="#000080", bd=10, anchor='w',
                   bg="#D2B48C")  # Changing background color
lblDessert.grid(row=4, column=0)
txtDessert = Entry(f1, font=('times new roman', 16, 'bold'), textvariable=Dessert, bd=6, insertwidth=4, bg="green",
                   justify='right')
txtDessert.grid(row=4, column=1)

lblFilet = Label(f1, font=('times new roman', 16, 'bold'), text="Pizza ", fg="#000080", bd=10, anchor='w',
                 bg="#D2B48C")  # Changing background color
lblFilet.grid(row=5, column=0)
txtFilet = Entry(f1, font=('times new roman', 16, 'bold'), textvariable=Filet, bd=6, insertwidth=4, bg="green",
                 justify='right')
txtFilet.grid(row=5, column=1)

lblCheese_Dessert = Label(f1, font=('times new roman', 16, 'bold'), text="Cheese Dessert", fg="#000080", bd=10,
                          anchor='w', bg="#D2B48C")  # Changing background color
lblCheese_Dessert.grid(row=6, column=0)
txtCheese_Dessert = Entry(f1, font=('times new roman', 16, 'bold'), textvariable=Cheese_Dessert, bd=6, insertwidth=4,
                          bg="green", justify='right')
txtCheese_Dessert.grid(row=6, column=1)

# --------------------------------------------------------------------------------------
lblDrinks = Label(f1, font=('times new roman', 16, 'bold'), text="Drinks", fg="#000080", bd=10, anchor='w',
                  bg="#D2B48C")  # Changing background color
lblDrinks.grid(row=1, column=0)
txtDrinks = Entry(f1, font=('times new roman', 16, 'bold'), textvariable=Drinks, bd=6, insertwidth=4, bg="green",
                  justify='right')
txtDrinks.grid(row=1, column=1)

lblcost = Label(f1, font=('times new roman', 16, 'bold'), text="Cost", fg="black", bd=10, anchor='w',
                bg="#D2B48C")  # Changing background color
lblcost.grid(row=2, column=2)
txtcost = Entry(f1, font=('times new roman', 16, 'bold'), textvariable=cost, bd=6, insertwidth=4, bg="white",
                justify='right')
txtcost.grid(row=2, column=3)

lblService_Charge = Label(f1, font=('times new roman', 16, 'bold'), text="Service Charge", fg="black", bd=10,
                          anchor='w', bg="#D2B48C")  # Changing background color
lblService_Charge.grid(row=3, column=2)
txtService_Charge = Entry(f1, font=('times new roman', 16, 'bold'), textvariable=Service_Charge, bd=6, insertwidth=4,
                          bg="white", justify='right')
txtService_Charge.grid(row=3, column=3)

lblTax = Label(f1, font=('times new roman', 16, 'bold'), text="Tax", fg="black", bd=10, anchor='w',
               bg="#D2B48C")  # Changing background color
lblTax.grid(row=4, column=2)
txtTax = Entry(f1, font=('times new roman', 16, 'bold'), textvariable=Tax, bd=6, insertwidth=4, bg="white",
               justify='right')
txtTax.grid(row=4, column=3)

lblSubtotal = Label(f1, font=('times new roman', 16, 'bold'), text="Subtotal", fg="black", bd=10, anchor='w',
                    bg="#D2B48C")  # Changing background color
lblSubtotal.grid(row=5, column=2)
txtSubtotal = Entry(f1, font=('times new roman', 16, 'bold'), textvariable=Subtotal, bd=6, insertwidth=4, bg="white",
                    justify='right')
txtSubtotal.grid(row=5, column=3)

lblTotal = Label(f1, font=('times new roman', 16, 'bold'), text="Total", fg="green", bd=10, anchor='w',
                 bg="#D2B48C")  # Changing background color
lblTotal.grid(row=6, column=2)
txtTotal = Entry(f1, font=('times new roman', 16, 'bold'), textvariable=Total, bd=6, insertwidth=4, bg="grey",
                 justify='right')
txtTotal.grid(row=6, column=3)

# -----------------------------------------buttons------------------------------------------
lblTotal = Label(f1, text="", fg="blue",bg="#D2B48C")
lblTotal.grid(row=7, columnspan=3)

btnTotal = Button(f1, padx=16, pady=8, bd=10, fg="black", font=('times new roman', 16, 'bold'), width=10, text="TOTAL",
                  bg="maroon", command=Ref)
btnTotal.grid(row=8, column=1)

btnreset = Button(f1, padx=16, pady=8, bd=10, fg="black", font=('times new roman', 16, 'bold'), width=10, text="RESET",
                  bg="maroon", command=reset)
btnreset.grid(row=8, column=2)

btnexit = Button(f1, padx=16, pady=8, bd=10, fg="black", font=('times new roman', 16, 'bold'), width=10, text="EXIT",
                 bg="maroon", command=qexit)
btnexit.grid(row=8, column=3)

def price():
    roo = Tk()
    roo.geometry("600x220+0+0")
    roo.title("Price List")
    lblinfo = Label(roo, font=('times new roman', 15, 'bold'), text="ITEM", fg="black", bd=5)
    lblinfo.grid(row=0, column=0)
    lblinfo = Label(roo, font=('times new roman', 15, 'bold'), text="_____________", fg="white", anchor=W)
    lblinfo.grid(row=0, column=2)
    lblinfo = Label(roo, font=('times new roman', 15, 'bold'), text="PRICE", fg="black", anchor=W)
    lblinfo.grid(row=0, column=3)
    lblinfo = Label(roo, font=('times new roman', 15, 'bold'), text="French Fries", fg="steel blue", anchor=W)
    lblinfo.grid(row=1, column=0)
    lblinfo = Label(roo, font=('times new roman', 15, 'bold'), text="25", fg="steel blue", anchor=W)
    lblinfo.grid(row=1, column=3)
    lblinfo = Label(roo, font=('times new roman', 15, 'bold'), text="Lunch ", fg="steel blue", anchor=W)
    lblinfo.grid(row=2, column=0)
    lblinfo = Label(roo, font=('times new roman', 15, 'bold'), text="40", fg="steel blue", anchor=W)
    lblinfo.grid(row=2, column=3)
    lblinfo = Label(roo, font=('times new roman', 15, 'bold'), text="Dessert ", fg="steel blue", anchor=W)
    lblinfo.grid(row=3, column=0)
    lblinfo = Label(roo, font=('times new roman', 15, 'bold'), text="35", fg="steel blue", anchor=W)
    lblinfo.grid(row=3, column=3)
    lblinfo = Label(roo, font=('times new roman', 15, 'bold'), text="Pizza ", fg="steel blue", anchor=W)
    lblinfo.grid(row=4, column=0)
    lblinfo = Label(roo, font=('times new roman', 15, 'bold'), text="50", fg="steel blue", anchor=W)
    lblinfo.grid(row=4, column=3)
    lblinfo = Label(roo, font=('times new roman', 15, 'bold'), text="Cheese Dessert", fg="steel blue", anchor=W)
    lblinfo.grid(row=5, column=0)
    lblinfo = Label(roo, font=('times new roman', 15, 'bold'), text="30", fg="steel blue", anchor=W)
    lblinfo.grid(row=5, column=3)
    lblinfo = Label(roo, font=('times new roman', 15, 'bold'), text="Drinks", fg="steel blue", anchor=W)
    lblinfo.grid(row=6, column=0)
    lblinfo = Label(roo, font=('times new roman', 15, 'bold'), text="35", fg="steel blue", anchor=W)
    lblinfo.grid(row=6, column=3)

    roo.mainloop()


btnprice = Button(f1, padx=16, pady=8, bd=10, fg="black", font=('times new roman', 16, 'bold'), width=10, text="PRICE",
                  bg="maroon", command=price)
btnprice.grid(row=8, column=0)

root.mainloop()
