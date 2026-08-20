import json
from models import Expense


def save_expenses(expenses_list: list[Expense], filepath: str) -> None:
    """
    Save a list of Expense objects to a JSON file.

    Args:
        expenses_list: List of Expense objects to save.
        filepath: Path of the JSON file.
    """
    # Convert Expense objects into dictionaries
    dict_list = [expense.to_dict() for expense in expenses_list]

    try:
        with open(filepath, "w") as file:
            json.dump(dict_list, file, indent=4)

    except OSError as e:
        print(f"Error saving expenses: {e}")


def load_expenses(filepath: str) -> list[Expense]:
    """
    Load expenses from a JSON file and reconstruct Expense objects.

    Args:
        filepath: Path of the JSON file.

    Returns:
        A list of Expense objects.
    """
    try:
        with open(filepath, "r") as file:
            raw_data = json.load(file)

        # Convert dictionaries back into Expense objects
        expenses = []

        for item in raw_data:
            expense = Expense(
                date=item["date"],
                category=item["category"],
                amount=float(item["amount"]),
                description=item["description"]
            )

            expenses.append(expense)

        return expenses

    except FileNotFoundError:
        # The file doesn't exist yet, so start with an empty list
        return []

    except (json.JSONDecodeError, KeyError, TypeError, ValueError) as e:
        print(f"Error loading expenses: {e}")
        return []

    except OSError as e:
        print(f"Error reading expenses: {e}")
        return []