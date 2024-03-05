# Pizza order app
# Author Joseph Brown
# Date 2/24/24
# Version 1

# importing
import tkinter as tk


# Create window
root = tk.Tk()

# Set title
root.title("Vito's Build Your Own Pizza")

# Set window size
root.geometry("1480x1080+300+300")

# widgets

# main label vars
title = tk.Label(root, text='Welcome to Vito\'s Build Your Own Pizza!',
                 font='arial 36 bold', justify='center', padx=80)
catchPhrase = tk.Label(root, text='"We\'re gonna make you a pizza you can\'t refuse!"',
                       font='arial 16 bold underline', justify='center', pady=25)
subTitle = tk.Label(root, text='--Place Order Here!--',
                    font='arial 36 bold underline', pady=25)

# main label grid
title.grid(row=0, column=5, sticky='nsew')
catchPhrase.grid(row=3, column=5, sticky='nsew')
subTitle.grid(row=4, column=5, sticky='nsew')

# radio buttons

# create StringVar() for radio buttons
option1 = tk.StringVar # delivery/carry-out buttons
option2 = tk.StringVar # crust size selection buttons

def carryout_or_delivery():
    selected_option = option1.get()

# delivery/carry-out radio buttons
frame1 = tk.Frame(root)
deliverCarry = tk.Label(root, text='Select Carry-Out or Delivery',
         font='arial 14 bold', justify='center', pady=5)
carryoutInp = tk.Radiobutton(frame1, text='Carry-Out', font='12',
                           variable='option1', value='Carry-Out', command=carryout_or_delivery)
deliveryInp = tk.Radiobutton(frame1, text='Delivery', font='12',
                           variable='option1', value='Delivery', command=carryout_or_delivery)

# delivery/carry-out grid
deliverCarry.grid(row=5, column=5, sticky='nsew')
carryoutInp.pack(side='left')
deliveryInp.pack(side='left')
frame1.grid(row=6, column=5)

# name/address vars
nameVar = tk.StringVar(root)
addressVar = tk.StringVar(root)
nameLabel = tk.Label(root, text="Name", font='arial 16 bold')
addressLabel = tk.Label(root, text="Address", font='arial 16 bold')
nameInp = tk.Entry(root, textvariable=nameVar, width=100)
addressInp = tk.Entry(root, textvariable=addressVar, width=100)

# name/address labels and inputs into grid
nameLabel.grid(row=10, column=5)
nameInp.grid(row=9, column=5)
addressLabel.grid(row=12, column=5)
addressInp.grid(row=11, column=5)

def size():
    selected_option = option2.get()


# pizza size selection radio buttons
frame2 = tk.Frame(root)
size = tk.Label(root, text='Select Size',
         font='arial 16 bold underline', justify='center', pady=15)
small = tk.Radiobutton(frame2, text='$6 (Small/12 inch)', font='12',
                       variable='option2', value='Small', command=size)
medium = tk.Radiobutton(frame2, text='$8 (Medium/14 inch)', font='12',
                        variable='option2', value='Medium', command=size)
large = tk.Radiobutton(frame2, text='$10 (Large/16 inch)', font='12',
                        variable='option2', value='Large', command=size)
xLarge = tk.Radiobutton(frame2, text='$12 (Extra Large/18 inch)', font='12',
                        variable='option2', value='Extra Large', command=size)

# size selection grid
size.grid(row=13, column=5)
small.pack(side='left')
medium.pack(side='left')
large.pack(side='left')
xLarge.pack(side='left')
frame2.grid(row=14, column=5)

# toppings label
toppings = tk.Label(text='Toppings', font='arial 20 bold', justify='center', pady=15)
topCharge = tk.Label(text='Toppings are $0.50 each, premium toppings are $1.00 each. All pizzas come with mozzerella'
                          ' and provolone cheeses.',
                     font='arial 12 bold', bg='yellow', pady=10)

#toppings grid
toppings.grid(row=15, column=5)
topCharge.grid(row=16, column=5)

# meats
meats = tk.Label(text='Meats', font='arial 18 bold underline')
pepperoni = tk.Checkbutton(text='Pepperoni', font=10)
sausage = tk.Checkbutton(text='Sausage', font=10)
salami = tk.Checkbutton(text='Salami', font=10)
bacon = tk.Checkbutton(text='Bacon', font=10)
ham = tk.Checkbutton(text='Ham', font=10)
chicken = tk.Checkbutton(text='Chicken', font=10)

# meats grid
meats.grid(row=18, column=0)
pepperoni.grid(row=19, column=0)
sausage.grid(row=20, column=0)
salami.grid(row=21, column=0)
bacon.grid(row=22, column=0)
ham.grid(row=23, column=0)
chicken.grid(row=24, column=0)

# vegetable toppings
vegetables = tk.Label(text='Vegetables', font='arial 18 bold underline')
onion = tk.Checkbutton(text='Onion', font=10)
spinach = tk.Checkbutton(text='Spinach', font=10)
tomato = tk.Checkbutton(text='Tomato', font=10)
mushrooms = tk.Checkbutton(text='Mushroom', font=10)
bananaPeps = tk.Checkbutton(text='Banana Pepper', font=10)
greenPeps = tk.Checkbutton(text='Green Pepper', font=10)
jalapeno = tk.Checkbutton(text='Jalapeno', font=10)
garlic = tk.Checkbutton(text='Garlic Clove', font=10)
olive = tk.Checkbutton(text='Olive', font=10)

# vegetable grid
vegetables.grid(row=18, column=5)
onion.grid(row=19, column=5)
spinach.grid(row=20, column=5)
tomato.grid(row=21, column=5)
mushrooms.grid(row=22, column=5)
bananaPeps.grid(row=23, column=5)
greenPeps.grid(row=24, column=5)
jalapeno.grid(row=25, column=5)
garlic.grid(row=26, column=5)
olive.grid(row=27, column=5)

# premium toppings
premium = tk.Label(text='Premium', font='arial 18 bold underline')
parm = tk.Checkbutton(text='Parmesean Cheese', font=10)
goatCheese = tk.Checkbutton(text='Goat Cheese', font=10)
fetta = tk.Checkbutton(text='Fetta Cheese', font=10)
pineapple = tk.Checkbutton(text='Pineapple', font=10)
alfredo = tk.Checkbutton(text='Alfredo Sauce', font=10)
oliveOil = tk.Checkbutton(text='Olive Oil Drizzle', font=10)

# premium topping grid
premium.grid(row=18, column=7)
parm.grid(row=19, column=7)
goatCheese.grid(row=20, column=7)
fetta.grid(row=21, column=7)
pineapple.grid(row=22, column=7)
alfredo.grid(row=23, column=7)
oliveOil.grid(row=24, column=7)

#submit button
submitBtn = tk.Button(root, text='Submit Order')
outputVar = tk.StringVar(value='')
outputLine = tk.Label(root, textvariable=outputVar, anchor='w', justify='left')

submitBtn.grid(row=26, column=7)

def order_submit():
    '''Run when user finishes order'''
    #vars use 'get()'
    name = nameVar.get()
  
    message += f'Thank you for your order, (name)! \n'

submitBtn.configure(command=order_submit)

# columnconfigure
root.columnconfigure(1, weight=1)

# row configure
root.rowconfigure(100, weight=1)

root.mainloop()