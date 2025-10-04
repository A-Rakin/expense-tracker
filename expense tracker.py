import csv
from datetime import datetime


def log_expense(date, category, amount, description):
	with open('expenses.csv', 'a', newline="") as file:
		writer = csv.writer(file)
		writer.writerow([date, category, amount, description])

# Example
log_expense(datetime.now().strftime("%Y-%m-%d"), "Food", 200.00, "Transport to cafe")
print("Expense Logged!")