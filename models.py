class Expense:
    def __init__(self, date: str, category: str, amount: float, description: str):
        """
        Initializes a new Expense object.
        """
        self.date = date
        self.category = category
        self.amount = amount
        self.description = description

    def to_dict(self) -> dict:
        """
        Converts the Expense object attributes into a standard Python dictionary.
        This format is easily serialized into JSON by our storage module.
        """
        return {
            "date": self.date,
            "category": self.category,
            "amount": self.amount,
            "description": self.description
        }
