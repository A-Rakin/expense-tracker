💰 Expense Tracker (Python CLI)

A simple command-line Expense Tracker built in Python to help you record, analyze, and visualize your spending habits.
This tool logs daily expenses, provides category-wise summaries, and generates insightful charts to track your financial trends over time.

🚀 Features

✅ Log Expenses Easily – Add expenses with date, category, amount, and description.
✅ View Summaries – Get a quick breakdown of total spending by category.
✅ Visualize Spending – Generate pie charts for category-wise spending and bar charts for monthly trends.
✅ Persistent Storage – All expenses are saved in a CSV file for easy management and portability.

🧠 How It Works

Expenses are stored in a CSV file (expenses.csv).

Each expense record includes:

Date (e.g., 2025-10-04)

Category (e.g., Food, Transport, Utilities)

Amount (numeric)

Description (optional note)

The app loads the CSV into a pandas DataFrame for analysis and visualization.

🛠️ Installation & Setup
1. Clone the Repository
git clone https://github.com/<your-username>/expense-tracker.git
cd expense-tracker

2. Install Required Libraries

Make sure you have Python 3 installed. Then run:

pip install pandas matplotlib

3. Run the Application
python expense_tracker.py

📋 Menu Options
Option	Action
1	Log an Expense
2	View Expense Summary
3	Plot Expenses by Category (Pie Chart)
4	Plot Monthly Trends (Bar Chart)
5	Exit
📊 Example Outputs
1️⃣ Expense Summary
Expense Summary:
Category
Food           500.0
Transport      200.0
Entertainment  300.0

2️⃣ Pie Chart – Expenses by Category

Displays spending distribution by category.

3️⃣ Bar Chart – Monthly Expense Trends

Shows monthly spending trends across all categories.

🧾 Example CSV Structure

expenses.csv

2025-10-01,Food,250.00,Lunch at cafe
2025-10-02,Transport,120.00,Bus fare
2025-10-02,Entertainment,400.00,Movie night

🧑‍💻 Code Structure
expense_tracker.py
├── log_expense()              # Record a new expense
├── load_expenses()            # Load data from CSV
├── summarize_expenses()       # Show total expenses by category
├── plot_expenses_by_category()# Pie chart of category-wise expenses
├── plot_monthly_trends()      # Bar chart of monthly totals
└── main()                     # Interactive command-line interface

🧰 Technologies Used

Python 3

Pandas – Data manipulation and grouping

Matplotlib – Data visualization

CSV – Simple data persistence

🪪 License

This project is licensed under the MIT License – feel free to use, modify, and distribute.

⭐ Contribute

Contributions are welcome!
If you’d like to enhance features, fix bugs, or improve visuals:

Fork the repo 🍴

Create a new branch 🌿

Submit a pull request 🔁
