from datetime import date, timedelta
from collections import defaultdict
import calendar

class Transaction:
    def __init__(self, date, amount, description, category):
        self.date = date
        self.amount = amount
        self.description = description
        self.category = category

class TransactionManager:
    def __init__(self):
        self.transactions = []
        self.budgets = {}  # Dictionary to store budgets for each category

    def add_transaction(self, transaction):
        self.transactions.append(transaction)
        self.check_budget_exceeded(transaction.category, transaction.amount)

    def update_transaction(self, transaction_index, new_amount, new_description, new_category):
        if 0 <= transaction_index < len(self.transactions):
            self.transactions[transaction_index].amount = new_amount
            self.transactions[transaction_index].description = new_description
            self.transactions[transaction_index].category = new_category
            self.check_budget_exceeded(new_category, new_amount)  # Recheck budget after update
        else:
            print(f"Invalid transaction index: {transaction_index}")

    def delete_transaction(self, transaction_index):
        if 0 <= transaction_index < len(self.transactions):
            del self.transactions[transaction_index]
        else:
            print(f"Invalid transaction index: {transaction_index}")

    def get_transactions_by_date(self, start_date, end_date):
        return [t for t in self.transactions if start_date <= t.date <= end_date]

    def get_transactions_by_category(self, category):
        return [t for t in self.transactions if t.category == category]

    def get_total_expenses(self):
        return sum(t.amount for t in self.transactions if t.amount < 0)

    def get_total_income(self):
        return sum(t.amount for t in self.transactions if t.amount > 0)

    def generate_monthly_report(self, year, month):
        start_date = date(year, month, 1)
        end_date = date(year, month, calendar.monthrange(year, month)[1])
        monthly_transactions = self.get_transactions_by_date(start_date, end_date)

        total_income = sum(t.amount for t in monthly_transactions if t.amount > 0)
        total_expenses = sum(t.amount for t in monthly_transactions if t.amount < 0)
        savings = total_income + total_expenses

        print(f"Monthly Report for {start_date.strftime('%B %Y')}")
        print(f"Total Income: {total_income}")
        print(f"Total Expenses: {total_expenses}")
        print(f"Savings: {savings}")

        # Categorized expenses
        categorized_expenses = defaultdict(float)
        for t in monthly_transactions:
            if t.amount < 0:
                categorized_expenses[t.category] += t.amount
        print("Categorized Expenses:")
        for category, amount in categorized_expenses.items():
            print(f"{category}: {amount}")

    def generate_yearly_report(self, year):
        start_date = date(year, 1, 1)
        end_date = date(year, 12, 31)
        yearly_transactions = self.get_transactions_by_date(start_date, end_date)

        total_income = sum(t.amount for t in yearly_transactions if t.amount > 0)
        total_expenses = sum(t.amount for t in yearly_transactions if t.amount < 0)
        savings = total_income + total_expenses

        print(f"Yearly Report for {year}")
        print(f"Total Income: {total_income}")
        print(f"Total Expenses: {total_expenses}")
        print(f"Savings: {savings}")

    def set_budget(self, category, budget_amount):
        self.budgets[category] = budget_amount

    def get_budget(self, category):
        return self.budgets.get(category, 0)  # Return 0