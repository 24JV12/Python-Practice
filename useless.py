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
        identity = random.randint(1000, 9999)
        if all(identity != customer["id"] for customer in customers_info):
            break
    
    customers_info.append({"name": name, "id": identity, "pin": pin, "amount": 0})
    print(f"Account created successfully! ID: {identity}")

def close_account(customers_info):
    customer = check_id(int(input("ID: ")))
    if customer:
        if input("Are you sure you want to delete it? (Y/n) ").lower() == "y": customers_info.remove(customer), print("Account Deleted.")
        else: print("Canceled Closure.")
    else: print("Account not found or incorrect PIN.")

def check_id(identity):
    for customer in customers_info:
        if identity == customer['id']: 
            pin = int(input(f"Enter your pincode for '{customer['name']}': "))
            if pin == customer["pin"]: return customer
            else: 
                print("Incorrect PIN.")
                return None
    print("ID Not Found.")
    return None

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
    if not cmd: continue

    action = cmd[0].lower()
    
    if action in ["id"]:
        if len(cmd) < 2:
            print("Please provide an ID.")
            continue
        customer = check_id(int(cmd[1]))
        if customer:
            while True:
                sub_cmd = input("> ").split()
                if not sub_cmd: continue
                
                sub_action = sub_cmd[0].lower()
                if sub_action == "exit": break
                elif sub_action in ["withdraw", "wtdw"] and len(sub_cmd) > 1: exchange(customer, int(sub_cmd[1]), False)
                elif sub_action in ["deposit", "dpst"] and len(sub_cmd) > 1: exchange(customer, int(sub_cmd[1]), True)
                elif sub_action in ["reveal", "rvel", "show"]: reveal(customer)
                elif sub_action in ["cls", "clear", "clean"]: clear()
                else: print(f"'{sub_action}' is not a recognized command.")
    elif action in ["new", "create", "open"]: open_account(customers_info)
    elif action in ["close", "del", "rem"]: close_account(customers_info)
    elif action in ["cls", "clear", "clean"]: clear()
    elif action in ["exit"]: break
    else: print("Error! Command not recognized.")
