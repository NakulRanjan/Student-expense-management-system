"""Data validation and model helpers for the Student Expense Tracker."""

from datetime import datetime

def create_expense(amount, category, description):
    if amount <= 0:
        raise ValueError("Amount must be greater than zero.")

    category = category.strip()
    description = description.strip()

    if not category:
        raise ValueError("Category cannot be empty.")
    if not description:
        raise ValueError("Description cannot be empty.")

    return {
        "amount": round(float(amount), 2),
        "category": category,
        "description": description,
        "date": datetime.now().strftime("%d-%m-%Y")
    }
