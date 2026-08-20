from datetime import datetime

from models import Expense
from calculator import (
    calculate_total,
    calculate_category_breakdown,
    calculate_monthly_breakdown
)


def display_menu() -> None:
    """Display the main menu of the expense tracker."""
    print("\n" + "=" * 40)
    print("       PERSONAL EXPENSE TRACKER")
    print("=" * 40)
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. View Total Spending")
    print("5. View Category Breakdown")
    print("6. View Monthly Breakdown")
    print("7. Exit")
    print("=" * 40)


def get_menu_choice() -> int:
    """
    Ask the user to select an option from the menu.

    Returns:
        int: The user's selected menu option.
    """
    while True:
        choice = input("Enter your choice (1-7): ").strip()

        if not choice:
            print("Input cannot be empty.")
            continue

        try:
            choice = int(choice)
        except ValueError:
            print("Invalid input. Please enter a number from 1 to 7.")
            continue

        if 1 <= choice <= 7:
            return choice

        print("Please enter a number between 1 and 7.")


def add_expense() -> Expense:
    """
    Collect expense information from the user
    and create an Expense object.

    Returns:
        Expense: A newly created Expense object.
    """
    print("\n--- Add New Expense ---")

    # Get and validate date
    while True:
        date = input("Enter date (YYYY-MM-DD): ").strip()

        try:
            datetime.strptime(date, "%Y-%m-%d")
            break

        except ValueError:
            print("Invalid date. Please use YYYY-MM-DD.")

    # Get and validate category
    while True:
        category = input("Enter category: ").strip()

        if category:
            break

        print("Category cannot be empty.")

    # Get and validate amount
    while True:
        amount_input = input("Enter amount: ").strip()

        try:
            amount = float(amount_input)

            if amount <= 0:
                print("Amount must be greater than zero.")
                continue

            break

        except ValueError:
            print("Invalid amount. Please enter a valid number.")
    # Get and validate description
    while True:
        description = input("Enter description: ").strip()

        if description:
            break

        print("Description cannot be empty.")

    return Expense(
        date=date,
        category=category,
        amount=amount,
        description=description
    )

def display_expenses(expenses: list[Expense]) -> None:
    """
    Display all saved expenses in a readable format.

    Args:
        expenses: A list of Expense objects.
    """
    print("\n--- All Expenses ---")

    if not expenses:
        print("No expenses recorded yet.")
        return

    for index, expense in enumerate(expenses, start=1):
        print(
            f"{index}. "
            f"{expense.date} | "
            f"{expense.category} | "
            f"${expense.amount:.2f} | "
            f"{expense.description}"
        )


def delete_expense(expenses: list[Expense]) -> bool:
    """
    Delete an expense selected by the user.

    Args:
        expenses: A list of Expense objects.

    Returns:
        True if an expense was deleted, otherwise False.
    """
    if not expenses:
        print("\nNo expenses available to delete.")
        return False

    display_expenses(expenses)

    while True:
        try:
            choice = int(
                input("\nEnter the number of the expense to delete: ").strip()
            )

            if 1 <= choice <= len(expenses):
                deleted_expense = expenses.pop(choice - 1)

                print(
                    f"Deleted: {deleted_expense.category} - "
                    f"${deleted_expense.amount:.2f}"
                )

                return True

            print(
                f"Please enter a number between 1 and {len(expenses)}."
            )

        except ValueError:
            print("Invalid input. Please enter a number.")

def display_total(expenses: list[Expense]) -> None:
    """
    Display the total amount spent.

    Args:
        expenses: A list of Expense objects.
    """
    total = calculate_total(expenses)

    print("\n--- Total Spending ---")
    print(f"Total spent: ${total:.2f}")


def display_category_breakdown(expenses: list[Expense]) -> None:
    """
    Display total spending grouped by category.

    Args:
        expenses: A list of Expense objects.
    """
    breakdown = calculate_category_breakdown(expenses)

    print("\n--- Category Breakdown ---")

    if not breakdown:
        print("No expenses recorded yet.")
        return

    for category, total in breakdown.items():
        print(f"{category}: ${total:.2f}")


def display_monthly_breakdown(expenses: list[Expense]) -> None:
    """
    Display total spending grouped by month.

    Args:
        expenses: A list of Expense objects.
    """
    breakdown = calculate_monthly_breakdown(expenses)

    print("\n--- Monthly Breakdown ---")

    if not breakdown:
        print("No expenses recorded yet.")
        return

    for month, total in breakdown.items():
        print(f"{month}: ${total:.2f}")