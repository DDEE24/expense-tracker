class Expense:

    def __init__(self, name, category, amount) -> None:
        self.name = name
        self.category = category
        self.amount = amount
    def __intro__(self):
        print(f"{self.name}.{self.category}.{self.amount}")