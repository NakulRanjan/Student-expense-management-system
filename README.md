# Student Expense Tracker

## Overview
Student Expense Tracker is a Python-based console application that helps students record, manage, search, analyze, and delete their daily expenses. It also provides monthly budget management.

The project uses JSON and text files for lightweight local data storage.

## Features
- Add a new expense
- View all expenses
- Search expenses by category
- Edit an existing expense
- Delete an expense
- Calculate total spending
- View category-wise spending
- Set a monthly budget
- Check remaining budget
- Display budget usage percentage
- Input validation and error handling
- Persistent local storage

## Major Functional Modules

### 1. Expense Management
Handles adding, viewing, searching, editing, and deleting expenses.

### 2. Budget Management
Handles monthly budget creation and budget status checking.

### 3. Expense Analysis
Calculates total spending and category-wise spending percentages.

## Technologies Used
- Python 3
- JSON
- File Handling
- `datetime`
- `unittest`
- Git/GitHub

## Project Structure

```text
Student-Expense-Tracker/
├── main.py
├── models.py
├── storage.py
├── expense_manager.py
├── budget_manager.py
├── summary_manager.py
├── validation.py
├── data/
│   ├── expenses.json
│   └── budget.txt
├── tests/
│   ├── test_models.py
│   ├── test_summary.py
│   └── test_budget.py
├── README.md
├── statement.md
└── requirements.txt
```

## How to Run

1. Install Python 3.
2. Clone or download this repository.
3. Open a terminal in the project folder.
4. Run:

```bash
python main.py
```

## How to Test

Run:

```bash
python -m unittest discover -s tests -v
```

## Data Storage
Expenses are stored in `data/expenses.json` and the monthly budget is stored in `data/budget.txt`.

## Future Enhancements
- Monthly and weekly reports
- Graphical charts
- Export reports to CSV/PDF
- Login/user accounts
- SQLite database
- Desktop or web interface

## Author
Student Project — VITyarthi Build Your Own Project
