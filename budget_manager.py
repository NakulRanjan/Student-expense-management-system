"""Monthly budget management."""

from storage import save_budget, get_budget

def set_budget():
    print("\n--- Set Budget ---")
    try:
        budget = float(input("Enter your monthly budget: "))
        if budget <= 0:
            print("Budget must be greater than zero.")
            return
        save_budget(budget)
        print("Budget saved successfully!")
    except ValueError:
        print("Please enter a valid amount.")

def check_budget(expenses):
    print("\n--- Budget Status ---")
    budget = get_budget()

    if budget <= 0:
        print("Please set your budget first.")
        return

    total = sum(expense["amount"] for expense in expenses)
    remaining = budget - total
    used_percentage = (total / budget) * 100

    print(f"Monthly budget : ₹{budget:.2f}")
    print(f"Total spent    : ₹{total:.2f}")
    print(f"Remaining      : ₹{remaining:.2f}")
    print(f"Budget used    : {used_percentage:.1f}%")

    if remaining > 0:
        print("Status: You are within your budget.")
    elif remaining == 0:
        print("Status: You have used your complete budget.")
    else:
        print("Status: You have exceeded your budget.")
