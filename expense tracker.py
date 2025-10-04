import csv
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt


def log_expense(date, category, amount, description):
	with open('expenses.csv', 'a', newline="") as file:
		writer = csv.writer(file)
		writer.writerow([date, category, amount, description])

# Example
#log_expense(datetime.now().strftime("%Y-%m-%d"), "Food", 200.00, "Transport to cafe")
#print("Expense Logged!")

def load_expenses():
	return pd.read_csv("expenses.csv", names=["Date", "Category", "Amount", "Description"])