from transactions import TransactionManager, Transaction  # Import Transaction class
from datetime import date  # Import date class

class BudgetManager:
    def __init__(self, transaction_manager):
        self.transaction_manager = transaction_manager

    def set_budget(self, category, budget_amount):
        """Sets a monthly budget for a specific category."""
        self.transaction_manager.set_budget(category, budget_amount)

    def get_budget(self, category):
        """Retrieves the budget for a specific category."""
        return self.transaction_manager.get_budget(category)

    def check_budget_exceeded(self, transaction):
        """Checks if the budget for a transaction's category has been exceeded."""
        return self.transaction_manager.check_budget_exceeded(transaction.category, transaction.amount)

if __name__ == "__main__":
    # Example usage (assuming transactions.py exists)
    from transactions import TransactionManager

    transaction_manager = TransactionManager()
    budget_manager = BudgetManager(transaction_manager)

    # Set budgets
    budget_manager.set_budget("Food", 200)
    budget_manager.set_budget("Entertainment", 100)

    # Add a transaction that exceeds the budget
    transaction = Transaction(date.today(), -250, "Restaurant", "Food")  # Use date from datetime
    if not budget_manager.check_budget_exceeded(transaction):
        transaction_manager.add_transaction(transaction)
    else:
        print("Budget exceeded for Food category. Transaction not added.")