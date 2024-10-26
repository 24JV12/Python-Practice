import random, os

customers_info = []

def clear(): os.system('cls' if os.name == 'nt' else 'clear')

def open_account(customers_info):
    name = input("Your Name? ")
    while True:
        pin = input("A Four-Digit Pincode? ")
        if len(pin) == 4 and pin.isdigit():
            pin = int(pin)
            break
        else: print("Only Four Digits Allowed!")
    
    while True:
        identity = random.randint(10, 99)
        if all(identity != customer["id"] for customer in customers_info): break
    
    customers_info.append({"name": name, "id": identity, "pin": pin, "amount": 0})
    print(f"Account created successfully! ID: {identity}")

def close_account(customers_info):
    identity = int(input("ID: "))
    customer = check_id(identity)
    
    if customer and confirm_id(customer):
        confirmation = input("Are you sure you want to delete it? (Y/n) ").lower()
        if confirmation == "y": customers_info.remove(customer), print("Account Deleted.")
        else: print("Canceled Closure.")
    else: print("Account not found or incorrect PIN.")

def check_id(identity):
    for customer_info in customers_info:
      if identity == customer_info['id']: return customer_info
    print("ID Not Found.")
    return None

def confirm_id(customer):
    pin = int(input(f"Enter your pincode for '{customer['name']}': "))
    if pin == customer["pin"]: return True
    else: 
        print("Incorrect PIN.")
        return False

def exchange(customer, amount, deposit):
    if amount <= 0: 
        print("Amount must be positive.")
        return
    if not deposit and amount > customer["amount"]: 
        print("Insufficient balance.")
        return

    action = 'deposit' if deposit else 'withdraw'
    if input(f"Confirm to {action} ₹{amount}? (Y/n): ").lower() == "y":
        customer["amount"] += amount if deposit else -amount
        print(f"Transaction successful! New Balance: ₹{customer['amount']}")
    else: print("Transaction canceled.")

def reveal(customer): print(f"\nName: {customer['name']}\nID: {customer['id']}\nBalance: ₹{customer['amount']}\n")

while True:
    cmd = input("~$ ").split()
    action = cmd[0].lower()
    
    if action in ["id"]:
        customer = check_id(int(cmd[1]))
        if customer and confirm_id(customer):
            while True:
                sub_cmd = input("> ").split()
                action = sub_cmd[0].lower()
                if action == "exit": break
                elif action in ["withdraw", "wtdw"]: exchange(customer, int(sub_cmd[1]), False)
                elif action in ["deposit", "dpst"]: exchange(customer, int(sub_cmd[1]), True)
                elif action in ["reveal", "rvel", "show"]: reveal(customer)
                elif action == "clear": clear()
                else: print(f"'{action}' is not a recognized command.")
    elif action in ["new", "create", "open"]: open_account(customers_info)
    elif cmd[0] in ["close", "del", "rem"]: close_account(customers_info)
    else: print("Error! Command not recognized.")
