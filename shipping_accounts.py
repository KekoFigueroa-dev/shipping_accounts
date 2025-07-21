# Shipping Accounts Program

# List of valid usernames for system authentication
valid_user_names = ["keko-dev", "kevin", "donald", "john", "pepe"]

# Display a welcome message and valid usernames
print("Welcome to the Shipping Accounts Program")
print("This is a sample program with input validation.")
print("The valid usernames are: keko-dev, kevin, donald, john, and pepe.")

# ---- User Authentication Block ----
while True:
    try:
        username_choice = input("What is your username: ").strip()
        user_lookup = [name.lower() for name in valid_user_names]
        if username_choice.lower() not in user_lookup:
            print("Please enter a valid username")
            continue
        else:
            print(f"Hello {username_choice}, welcome back to your account!")
            break
    except Exception as e:
        print(f"An error occurred: {e}")


# ---- Display Current Shipping Price Tiers ----
print("\\nCurrent shipping prices are as follows:")
print("Shipping orders 0 to 100:      $5.10 each")
print("Shipping orders 100 to 500:    $5.00 each")
print("Shipping orders 500 to 1000:   $4.95 each")
print("Shipping orders over 1000:     $4.80 each\\n")
print("\n")


# ---- Prompt User for Order Quantity and Compute Cost ----
while True:
    try:
        order_number = int(input("How many orders would you like to ship: "))
        if order_number <= 0:
            print("Please enter a positive number of orders")
            continue
        # Determine the correct price per item based on order size
        if order_number <= 100:
            cost_per_item = 5.10
        elif order_number <= 500:
            cost_per_item = 5.00
        elif order_number <= 1000:
            cost_per_item = 4.95
        else:
            cost_per_item = 4.80

        # Calculate and display total shipping cost
        total_cost = round(order_number * cost_per_item, 2)
        print(f"To ship {order_number} items it will cost you ${total_cost:.2f} at ${cost_per_item:.2f} per item")
        break
    except ValueError:
        print("Please enter a valid integer for the number of orders.")


# ---- Confirm Order Placement with User ----
while True:
    order_confirmation = input("Would you like to place this order? (y/n): ").strip().lower()
    if order_confirmation == "y":
        print(f"Okay. Shipping your {order_number} items!")
        break
    elif order_confirmation == "n":
        print("Going back to main menu.")
        break
    else:
        print("Please enter (y or n)!")

# Fun ASCII art reward
print("Thank you for testing my app, here's Pikachu as a reward!")

print(r"""
⠀⠀  (\\__/)
⠀⠀  (o^.^)
⠀⠀z(_(")(")
Pika Pika!
""")

