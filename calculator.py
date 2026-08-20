from models import Expense


def calculate_total(expenses: list[Expense]) -> float:
    """
    Calculate the total amount spent across all expenses.

    Args:
        expenses: A list of Expense objects.

    Returns:
        The total amount spent.
    """
    return sum(expense.amount for expense in expenses)


def calculate_category_breakdown(expenses: list[Expense]) -> dict[str, float]:
    """
    Calculate total spending for each category.

    Categories are normalized so that different capitalization
    or extra spaces are treated as the same category.

    Args:
        expenses: A list of Expense objects.

    Returns:
        A dictionary mapping category names to their total spending.
    """
    breakdown = {}

    for expense in expenses:
        category = expense.category.strip().title()

        if category not in breakdown:
            breakdown[category] = 0.0

        breakdown[category] += expense.amount

    return breakdown


def calculate_monthly_breakdown(expenses: list[Expense]) -> dict[str, float]:
    """
    Calculate total spending for each month.

    The month is extracted from the first seven characters
    of the date in YYYY-MM-DD format.

    Args:
        expenses: A list of Expense objects.

    Returns:
        A dictionary mapping YYYY-MM to total spending.
    """
    breakdown = {}

    for expense in expenses:
        month = expense.date[:7]

        if month not in breakdown:
            breakdown[month] = 0.0

        breakdown[month] += expense.amount

    return breakdown