#Shipping Accounts Program

valid_user_names = ["keko-dev", "kevin", "donald", "john", "pepe"]

#Valid usernames / Welcome msg
print("Welcome to the Shipping Accounts Program")
print("This is a sample program with input validation, the valid usernames are = keko-dev, kevin, donald, john, and, pepe")


#Input validation
while True: 
    try:
        username_choice = str(input("What is your username: "))
        if username_choice not in valid_user_names:
            print("Please enter a valid username")
            continue
        else:
            print(f"Hello {username_choice}, Welcome back your account!")
            break
    except Exception as e:
        print(f"An error occurred: {e}")


print("Current shipping prices are as follows:\n"
      "\n" \
"Shipping orders 0 to 100:\t\t $5.10 each\n"
"Shipping orders 100 to 500:\t\t $5.00 each\n"
"Shipping orders 500 to 1000:\t\t $4.95 each\n"
"Shipping orders over 1000\t\t $4.80 each\n")

while True:
    order_number = (int(input("How many orders would you like to ship: ")))
    if order_number < 0:
        print("Please enter a postive number of orders")
        continue
    elif order_number <= 100:
        print(f"To ship {order_number} items it will cost you ${float((order_number * 5.10))} at $5.10 per item")
    elif order_number <= 500:
        print(f"To ship {order_number} items it will cost you ${float((order_number * 5.00))} at $5.00 per item")
    elif order_number <= 1000:
        print(f"To ship {order_number} items it will cost you ${float((order_number * 4.95))} at $4.95 per item")
    else:
        print(f"To ship {order_number} items it will cost you ${float((order_number * 4.80))} at $4.80 per item")
    break

while True: 
    order_confirmation =(str(input("Would you like to place this order?: (y/n)")))
    if order_confirmation.lower() == "y":
        print(f"Okay Shipping your {order_number} Items!")
        break
    elif order_confirmation.lower() =="n":
        print("Going back to main menu.")
        break
    else:
        print("Please enter ( y or n )!")
    continue


print("Thank you for testing my app, Here's Pikachu as a reward!")


