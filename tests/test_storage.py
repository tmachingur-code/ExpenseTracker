import unittest
import os
import tempfile

from models import Expense
from storage import save_expenses, load_expenses


class TestStorage(unittest.TestCase):

    def setUp(self):
        """Create a temporary file for each test."""

        self.test_file = tempfile.NamedTemporaryFile(
            delete=False
        ).name

    def tearDown(self):
        """Delete the temporary file after each test."""

        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_save_expenses(self):
        expenses = [
            Expense(
                "2026-08-20",
                "Food",
                15.50,
                "Lunch"
            )
        ]

        save_expenses(expenses, self.test_file)

        self.assertTrue(os.path.exists(self.test_file))

    def test_load_expenses(self):
        expenses = [
            Expense(
                "2026-08-20",
                "Food",
                15.50,
                "Lunch"
            ),
            Expense(
                "2026-08-19",
                "Transport",
                2.75,
                "Bus fare"
            )
        ]

        save_expenses(expenses, self.test_file)

        loaded_expenses = load_expenses(self.test_file)

        self.assertEqual(len(loaded_expenses), 2)

        self.assertEqual(
            loaded_expenses[0].date,
            "2026-08-20"
        )

        self.assertEqual(
            loaded_expenses[0].category,
            "Food"
        )

        self.assertEqual(
            loaded_expenses[0].amount,
            15.50
        )

        self.assertEqual(
            loaded_expenses[1].category,
            "Transport"
        )

    def test_load_missing_file(self):
        missing_file = "this_file_does_not_exist.json"

        expenses = load_expenses(missing_file)

        self.assertEqual(expenses, [])


if __name__ == "__main__":
    unittest.main()