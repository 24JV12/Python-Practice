import random, os  # Imports 'random' for ID generation and 'os' for clearing the screen.
customers_info = [] # List to store all customer account information

def clear(): os.system('cls' if os.name == 'nt' else 'clear') # Clears the screen for better readability

def open_account(customers_info):
    # Opens a new account by collecting the user's name, pin, and generating a unique ID.
    name = input("Your Name? ")
    # Loop to ensure the user enters a valid 4-digit PIN
    while True:
        pin = input("A Four-Digit Pincode? ")
        if len(pin) == 4 and pin.isdigit():  # Validates the PIN
            pin = int(pin)
            break
        else: print("Only Four Digits Allowed!")
    # Loop to generate a unique 4-digit ID for the new user
    while True:
        identity = random.randint(1000, 9999)
        # Checks if ID is unique
        if all(identity != customer["id"] for customer in customers_info): break
    # Adds the new customer to the database with initial balance of ₹0
    customers_info.append({"name": name, "id": identity, "pin": pin, "amount": 0}), print(f"Account created successfully! ID: {identity}")

def close_account(customers_info):
    # Closes an account after verifying the ID and PIN
    customer = check_id(int(input("ID: ")))
    if customer:
        if input("Are you sure you want to delete it? (Y/n) ").lower() == "y": customers_info.remove(customer), print("Account Deleted.") # Removes the customer if they confirm deletion
        else: print("Canceled Closure.")
    else: print("Account not found or incorrect PIN.")

def check_id(identity):
    # Checks if an ID exists and verifies the user's PIN
    for customer in customers_info:
        if identity == customer['id']: 
            pin = int(input(f"Enter your pincode for '{customer['name']}': "))
            if pin == customer["pin"]: return customer  # Returns customer data if PIN matches
            else:
                print("Incorrect PIN.")
                return None
    print("ID Not Found.")
    return None

def exchange(customer, amount, deposit):
    # Manages deposit and withdrawal operations for a customer
    if amount <= 0:  # Validates that the amount is positive
        print("Amount must be positive.")
        return
    if not deposit and amount > customer["amount"]:  # Checks for sufficient balance
        print("Insufficient balance.")
        return

    # Asks for confirmation of transaction
    action = 'deposit' if deposit else 'withdraw'
    if input(f"Confirm to {action} ₹{amount}? (Y/n): ").lower() == "y":
        # Updates the customer balance based on deposit or withdrawal
        customer["amount"] += amount if deposit else -amount
        print(f"Transaction successful! New Balance: ₹{customer['amount']}")
    else: print("Transaction canceled.")

def reveal(customer): print(f"\nName: {customer['name']}\nID: {customer['id']}\nBalance: ₹{customer['amount']}\n") 
# Displays the customer's account details

# Main loop to handle user commands
while True:
    cmd = input("~$ ").split()  # Reads the command and splits it into parts
    if not cmd: continue
    action = cmd[0].lower()  # Main action from the command  
    # For checking ID and accessing account functions
    if action in ["atm"]:
        if len(cmd) < 2:  # Checks if ID is provided
            print("Please provide an ID.")
            continue
        customer = check_id(int(cmd[1]))  # Finds customer by ID
        if customer:
            while True:
                sub_cmd = input("> ").split()  # Gets subcommands like withdraw, deposit, etc.
                if not sub_cmd: continue
                
                sub_action = sub_cmd[0].lower()
                if sub_action == "exit": break  # Exit sub-menu
                elif sub_action in ["withdraw", "wtdw"] and len(sub_cmd) > 1: exchange(customer, int(sub_cmd[1]), False)  # Withdraw money
                elif sub_action in ["deposit", "dpst"] and len(sub_cmd) > 1: exchange(customer, int(sub_cmd[1]), True)  # Deposit money
                elif sub_action in ["reveal", "rvel", "show"]: reveal(customer)  # Show account details
                elif sub_action in ["cls", "clear", "clean"]: clear()  # Clears the screen
                else: print(f"'{sub_action}' is not a recognized command.")
                    
    elif action in ["new", "create", "open"]: open_account(customers_info)  # Opens new account
    elif action in ["close", "del", "rem"]: close_account(customers_info)  # Closes account
    elif action in ["cls", "clear", "clean"]: clear()  # Clears the screen
    elif action in ["exit"]: break  # Exits the main loop
    else: print("Error! Command not recognized.")
