import unittest

from models import Expense
from calculator import (
    calculate_total,
    calculate_category_breakdown,
    calculate_monthly_breakdown
)


class TestCalculator(unittest.TestCase):

    def setUp(self):
        """Create sample expenses used by multiple tests."""

        self.expenses = [
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
            ),
            Expense(
                "2026-08-18",
                "Education",
                120.00,
                "ML textbook"
            ),
            Expense(
                "2026-08-10",
                "Food",
                10.00,
                "Dinner"
            )
        ]

    def test_calculate_total(self):
        total = calculate_total(self.expenses)

        self.assertEqual(total, 148.25)

    def test_category_breakdown(self):
        breakdown = calculate_category_breakdown(self.expenses)

        expected = {
            "Food": 25.50,
            "Transport": 2.75,
            "Education": 120.00
        }

        self.assertEqual(breakdown, expected)

    def test_category_case_and_spacing(self):
        expenses = [
            Expense("2026-08-20", " food ", 10.00, "Lunch"),
            Expense("2026-08-20", "FOOD", 20.00, "Dinner")
        ]

        breakdown = calculate_category_breakdown(expenses)

        self.assertEqual(
            breakdown,
            {"Food": 30.00}
        )

    def test_monthly_breakdown(self):
        breakdown = calculate_monthly_breakdown(self.expenses)

        expected = {
            "2026-08": 148.25
        }

        self.assertEqual(breakdown, expected)


if __name__ == "__main__":
    unittest.main()