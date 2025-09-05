"""SPLITTING COMPLEX TASKS

You're creating a monthly report for a cafe's sales.
Instead of putting all logic in one place, break it down.

Task: Write a function generate_report() that calls:
    1. fetch_sales()
    2. filter_valid_order()
    3. summarize_data"""


def fetch_sales():
    print("Fecthing the sales data")

def filter_valid_order():
    print("Filtering valid sales data")

def summarize_data():
    print("Summarizing sales data")

def generate_report():
    fetch_sales()
    filter_valid_order()
    summarize_data()
    print("Report is ready")

generate_report()