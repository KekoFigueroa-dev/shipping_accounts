Shipping Accounts Program
A Python command-line application that simulates logging into a shipping business system. The app allows pre-approved users to calculate shipping costs based on their order size, perform robust input validation, and receive feedback with a cheerful Pikachu ASCII reward!
✨ Features
User Authentication
Only pre-approved usernames may log in (case-insensitive).
Current Shipping Price Display
See all shipping price tiers for different order quantities.
Accurate Cost Calculation
Calculates and displays the total cost of shipping your order.
Robust Input Validation
Handles invalid usernames, non-numeric and negative order values, and input errors gracefully.
Order Confirmation
Easy order placement or cancellation with instant feedback.
ASCII Pikachu Reward
Celebrate your order with a fun Pikachu!
🚀 How to Use
Clone or download this repository.
Open the script in VS Code or your preferred IDE.
Run the program in a Python 3 environment.
Follow the prompts:
Enter a valid username (keko-dev, kevin, donald, john, pepe)
Specify how many items you want to ship (must be a positive integer)
Review the shipping price and confirm your order with y or n
Enjoy your Pikachu ASCII reward!
💻 Example Output
Welcome to the Shipping Accounts Program
This is a sample program with input validation.
The valid usernames are: keko-dev, kevin, donald, john, and pepe.
What is your username: Kevin
Hello Kevin, welcome back to your account!

Current shipping prices are as follows:
Shipping orders 0 to 100:      $5.10 each
Shipping orders 100 to 500:    $5.00 each
Shipping orders 500 to 1000:   $4.95 each
Shipping orders over 1000:     $4.80 each

How many orders would you like to ship: 235
To ship 235 items it will cost you $1175.00 at $5.00 per item
Would you like to place this order? (y/n): y
Okay. Shipping your 235 items!
Thank you for testing my app, here's Pikachu as a reward!

    (\\__/)
    (o^.^)
 z(_(")(")
Pika Pika!

​
⚙️ Technical Details
Language: Python 3
Input Handling: try/except blocks for validation
Business Logic: Price per item changes with order size
Clear Output: All cost figures rounded to two decimal places
User Experience: Simple, flexible, and friendly prompts