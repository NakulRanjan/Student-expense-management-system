from expense_manager import add_expense, show_expenses, search_expense, edit_expense, delete_expense
from budget_manager import set_budget, check_budget
from summary_manager import show_summary
from storage import load_data

def main():
    expenses = load_data()

    while True:
        print("\n==============================")
        print("     STUDENT EXPENSE TRACKER")
        print("==============================")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Search Expense")
        print("4. Edit Expense")
        print("5. Expense Summary")
        print("6. Set Monthly Budget")
        print("7. Check Budget")
        print("8. Delete Expense")
        print("9. Exit")
        print("==============================")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            show_expenses(expenses)
        elif choice == "3":
            search_expense(expenses)
        elif choice == "4":
            edit_expense(expenses)
        elif choice == "5":
            show_summary(expenses)
        elif choice == "6":
            set_budget()
        elif choice == "7":
            check_budget(expenses)
        elif choice == "8":
            delete_expense(expenses)
        elif choice == "9":
            print("Thank you for using the Expense Tracker!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
