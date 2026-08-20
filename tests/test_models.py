import unittest

from models import Expense


class TestExpense(unittest.TestCase):

    def test_expense_creation(self):
        expense = Expense(
            "2026-08-20",
            "Food",
            15.50,
            "Lunch"
        )

        self.assertEqual(expense.date, "2026-08-20")
        self.assertEqual(expense.category, "Food")
        self.assertEqual(expense.amount, 15.50)
        self.assertEqual(expense.description, "Lunch")

    def test_to_dict(self):
        expense = Expense(
            "2026-08-20",
            "Food",
            15.50,
            "Lunch"
        )

        expected = {
            "date": "2026-08-20",
            "category": "Food",
            "amount": 15.50,
            "description": "Lunch"
        }

        self.assertEqual(expense.to_dict(), expected)


if __name__ == "__main__":
    unittest.main()