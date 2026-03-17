pizza_name = input("Enter the name of a pizza: ").title()
#qty = input("Enter quantity : ")

pizza_menu = {
    "Onion Pizza" : 150,
    "Cheese Pizza" : 200,
    "Tomato Pizza" : 250,
    "Veg Pizza" : 180
}

if pizza_name in pizza_menu:
    qty = input("Enter quantity : ")

    if qty.isdigit():
     qty = int(qty)

     price_per_pizza = pizza_menu[pizza_name]
     total_bill = price_per_pizza * qty        

     print("\n--------------Bill--------------")
     print("Pizza Name: ", pizza_name)
     print("price per pizza: ", price_per_pizza)
     print("Quantity: ", qty)
     print("Total Bill: ", total_bill)

    else:
     print("Invalid Quantity! Please enter a number.")  
else:
    print("Pizza not avaiable in menu! Please Enter like this: Onion Pizza, Cheese Pizza, Tomato Pizza, Veg Pizza")
