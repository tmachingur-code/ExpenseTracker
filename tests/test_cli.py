import unittest
from unittest.mock import patch

from models import Expense
from cli import (
    get_menu_choice,
    add_expense,
    delete_expense,
)


class TestCLI(unittest.TestCase):

    @patch("builtins.input", side_effect=["abc", "hello", "2"])
    def test_invalid_menu_input(self, mock_input):
        choice = get_menu_choice()

        self.assertEqual(choice, 2)

    @patch(
        "builtins.input",
        side_effect=[
            "2026-08-20",
            "Food",
            "-50",
            "0",
            "abc",
            "25.50",
            "Lunch",
        ],
    )
    def test_invalid_amounts(self, mock_input):
        expense = add_expense()

        self.assertEqual(expense.amount, 25.50)

    @patch(
        "builtins.input",
        side_effect=[
            "2026-08-20",
            "FOOD",
            "20",
            "Lunch",
        ],
    )
    def test_uppercase_category(self, mock_input):
        expense = add_expense()

        self.assertEqual(expense.category, "FOOD")

    @patch(
        "builtins.input",
        side_effect=[
            "2026-99-50",
            "2026-08-20",
            "Food",
            "25.50",
            "Lunch",
        ],
    )
    def test_invalid_date(self, mock_input):
        expense = add_expense()

        self.assertEqual(expense.date, "2026-08-20")

    @patch(
        "builtins.input",
        side_effect=[
            "20/08/2026",
            "2026-08-20",
            "Food",
            "25.50",
            "Lunch",
        ],
    )
    def test_wrong_date_format(self, mock_input):
        expense = add_expense()

        self.assertEqual(expense.date, "2026-08-20")

    @patch("builtins.input", side_effect=["2"])
    def test_delete_expense(self, mock_input):
        expenses = [
            Expense("2026-08-20", "Food", 15.50, "Lunch"),
            Expense("2026-08-19", "Transport", 2.75, "Bus"),
        ]

        result = delete_expense(expenses)

        self.assertTrue(result)
        self.assertEqual(len(expenses), 1)
        self.assertEqual(expenses[0].category, "Food")

    def test_delete_when_no_expenses(self):
        expenses = []

        result = delete_expense(expenses)

        self.assertFalse(result)
        self.assertEqual(len(expenses), 0)


if __name__ == "__main__":
    unittest.main()