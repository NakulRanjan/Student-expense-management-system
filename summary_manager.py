"""Expense analysis and summary functions."""

def show_summary(expenses):
    print("\n--- Expense Summary ---")

    if not expenses:
        print("No expenses available.")
        return

    total = sum(expense["amount"] for expense in expenses)
    category_total = {}

    for expense in expenses:
        category = expense["category"]
        category_total[category] = category_total.get(category, 0) + expense["amount"]

    print(f"Total spending: ₹{total:.2f}")
    print("\nCategory-wise spending:")

    for category, amount in category_total.items():
        percentage = (amount / total) * 100 if total else 0
        print(f"{category}: ₹{amount:.2f} ({percentage:.1f}%)")
