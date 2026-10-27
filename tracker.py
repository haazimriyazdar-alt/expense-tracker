import json

FILE = "expenses.json"

def load_expenses():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_expenses():
    with open(FILE, "w") as f:
        json.dump(expenses, f)

expenses = load_expenses()

def add_expense():
    name = input("What did you spend on? ")
    category = input("Category (food, travel, other): ")
    amount = float(input("How much? £"))
    expenses.append({"name": name, "category": category, "amount": amount})
    save_expenses()
    print("Added!")

def show_expenses():
    total = 0
    totals_by_category = {}
    for item in expenses:
        category = item.get("category", "other")
        print(item["name"], "(" + category + ") - £", item["amount"])
        total += item["amount"]
        totals_by_category[category] = totals_by_category.get(category, 0) + item["amount"]
    print("Total: £", total)
    print("By category:")
    for category, amount in totals_by_category.items():
        print(" ", category, "- £", amount)

while True:
    choice = input("1) Add  2) Show  3) Quit: ")
    if choice == "1":
        add_expense()
    elif choice == "2":
        show_expenses()
    elif choice == "3":
        break
    else:
        print("Please type 1, 2 or 3")