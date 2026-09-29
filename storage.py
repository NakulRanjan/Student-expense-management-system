"""File storage functions for expenses and budget."""

import json
from pathlib import Path

DATA_DIR = Path("data")
EXPENSE_FILE = DATA_DIR / "expenses.json"
BUDGET_FILE = DATA_DIR / "budget.txt"

def ensure_data_directory():
    DATA_DIR.mkdir(exist_ok=True)

def load_data():
    ensure_data_directory()
    if not EXPENSE_FILE.exists():
        return []

    try:
        with open(EXPENSE_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data if isinstance(data, list) else []
    except (json.JSONDecodeError, OSError):
        return []

def save_data(expenses):
    ensure_data_directory()
    with open(EXPENSE_FILE, "w", encoding="utf-8") as file:
        json.dump(expenses, file, indent=4)

def save_budget(budget):
    ensure_data_directory()
    with open(BUDGET_FILE, "w", encoding="utf-8") as file:
        file.write(str(budget))

def get_budget():
    ensure_data_directory()
    if not BUDGET_FILE.exists():
        return 0.0

    try:
        with open(BUDGET_FILE, "r", encoding="utf-8") as file:
            return float(file.read().strip())
    except (ValueError, OSError):
        return 0.0
