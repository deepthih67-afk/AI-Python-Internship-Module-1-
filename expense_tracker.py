expenses = []


def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter expense amount: "))

    expenses.append({
        "name": name,
        "amount": amount
    })

    print("Expense added successfully!")


def view_expenses():
    if not expenses:
        print("No expenses recorded.")
        return

    print("\nYour Expenses:")

    for expense in expenses:
        print(f"{expense['name']}: ₹{expense['amount']:.2f}")


def show_total():
    total = sum(expense["amount"] for expense in expenses)
    print(f"\nTotal expenses: ₹{total:.2f}")


while True:
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        show_total()
    elif choice == "4":
        print("Thank you for using Expense Tracker!")
        break
    else:
        print("Invalid choice. Please try again.")
