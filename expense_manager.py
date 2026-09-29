"""Expense management operations."""

from models import create_expense
from storage import save_data

def add_expense(expenses):
    print("\n--- Add Expense ---")
    try:
        amount = float(input("Enter amount: "))
        category = input("Enter category: ")
        description = input("Enter description: ")
        expense = create_expense(amount, category, description)
        expenses.append(expense)
        save_data(expenses)
        print("Expense added successfully!")
    except ValueError as error:
        print("Error:", error)

def show_expenses(expenses):
    print("\n--- Your Expenses ---")
    if not expenses:
        print("No expenses added yet.")
        return

    for index, expense in enumerate(expenses, start=1):
        print(f"\nExpense {index}")
        print("Amount      :", f"₹{expense['amount']:.2f}")
        print("Category    :", expense["category"])
        print("Description :", expense["description"])
        print("Date        :", expense["date"])

def search_expense(expenses):
    print("\n--- Search Expense ---")
    category = input("Enter category: ").strip().lower()
    found = False

    for expense in expenses:
        if expense["category"].lower() == category:
            print(f"₹{expense['amount']:.2f} | {expense['description']} | {expense['date']}")
            found = True

    if not found:
        print("No expense found in this category.")

def edit_expense(expenses):
    print("\n--- Edit Expense ---")
    if not expenses:
        print("No expenses available.")
        return

    show_expenses(expenses)
    try:
        number = int(input("\nEnter expense number to edit: "))
        if not 1 <= number <= len(expenses):
            print("Invalid expense number.")
            return

        current = expenses[number - 1]
        amount_text = input(f"Enter new amount [{current['amount']}]: ").strip()
        category = input(f"Enter new category [{current['category']}]: ").strip()
        description = input(f"Enter new description [{current['description']}]: ").strip()

        amount = float(amount_text) if amount_text else current["amount"]
        category = category if category else current["category"]
        description = description if description else current["description"]

        updated = create_expense(amount, category, description)
        updated["date"] = current["date"]
        expenses[number - 1] = updated
        save_data(expenses)
        print("Expense updated successfully.")
    except ValueError as error:
        print("Error:", error)

def delete_expense(expenses):
    print("\n--- Delete Expense ---")
    if not expenses:
        print("No expenses available.")
        return

    show_expenses(expenses)
    try:
        number = int(input("\nEnter expense number to delete: "))
        if 1 <= number <= len(expenses):
            deleted = expenses.pop(number - 1)
            save_data(expenses)
            print(f"Expense for ₹{deleted['amount']:.2f} deleted successfully.")
        else:
            print("Invalid expense number.")
    except ValueError:
        print("Please enter a valid number.")
