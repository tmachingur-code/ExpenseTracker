from storage import load_expenses, save_expenses

from cli import (
    display_menu,
    get_menu_choice,
    add_expense,
    display_expenses,
    delete_expense,
    display_total,
    display_category_breakdown,
    display_monthly_breakdown
)


FILEPATH = "expenses.json"


def main() -> None:
    """Run the Personal Expense Tracker application."""

    # Load saved expenses when the program starts
    expenses = load_expenses(FILEPATH)

    print("\nWelcome to the Personal Expense Tracker!")

    while True:
        display_menu()

        choice = get_menu_choice()

        if choice == 1:
            # Add Expense
            expense = add_expense()
            expenses.append(expense)

            save_expenses(expenses, FILEPATH)

            print("Expense added successfully.")

        elif choice == 2:
            # View Expenses
            display_expenses(expenses)

        elif choice == 3:
            # Delete Expense
            deleted = delete_expense(expenses)

            if deleted:
                save_expenses(expenses, FILEPATH)

        elif choice == 4:
            # View Total Spending
            display_total(expenses)

        elif choice == 5:
            # View Category Breakdown
            display_category_breakdown(expenses)

        elif choice == 6:
            # View Monthly Breakdown
            display_monthly_breakdown(expenses)

        elif choice == 7:
            # Exit
            print("\nThank you for using the Personal Expense Tracker!")
            break


if __name__ == "__main__":
    main()