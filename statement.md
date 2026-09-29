# Project Statement

## Project Title
Student Expense Tracker

## Problem Statement
Students often make multiple small daily payments for food, travel, education, entertainment, and other activities. Without a simple tracking system, it can become difficult to know where money is being spent and whether the monthly budget is being followed.

The Student Expense Tracker provides a simple console-based solution for recording expenses, viewing spending information, managing a monthly budget, and generating category-wise summaries.

## Scope
The project focuses on personal expense management using a Python console application and local file storage. It is designed for individual student use.

## Target Users
- College students
- Students living away from home
- Students who want to monitor daily spending

## High-Level Features
- Expense creation and storage
- Expense viewing
- Category-based search
- Expense editing and deletion
- Total and category-wise analysis
- Monthly budget management
- Budget status calculation
- Input validation and error handling

## Functional Modules
1. Expense Management
2. Budget Management
3. Expense Analysis

## Non-Functional Requirements
1. **Usability:** The menu-driven interface should be easy to understand.
2. **Reliability:** Expense information should remain available after restarting the application.
3. **Maintainability:** The application should be divided into separate Python modules.
4. **Error Handling:** Invalid input should be handled without terminating the application unexpectedly.
5. **Resource Efficiency:** Local JSON/text storage keeps the application lightweight.

## Input and Output
### Inputs
- Expense amount
- Category
- Description
- Menu choices
- Monthly budget

### Outputs
- Expense records
- Spending summaries
- Category-wise totals
- Budget status

## Workflow
User starts the application → selects an operation → enters required data → application validates/processes the data → data is saved when required → result is displayed → user returns to the main menu.
