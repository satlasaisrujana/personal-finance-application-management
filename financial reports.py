from datetime import date, timedelta
from collections import defaultdict
import calendar

class TransactionManager:
    # ... (previous methods from the previous code) ...

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

if __name__ == "__main__":
    # Create an instance of TransactionManager
    transaction_manager = TransactionManager()

    # ... (rest of your example usage) ...