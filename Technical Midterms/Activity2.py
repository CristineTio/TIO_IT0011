from datetime import datetime

def format_date(date_str):
    try:
        date_obj = datetime.strptime(date_str, "%m/%d/%Y")
        formatted_date = date_obj.strftime("%B %d, %Y")
        return formatted_date
    except ValueError:
        return "Invalid date format. Please use mm/dd/yyyy."

# Get user input
date_input = input("Enter the date (mm/dd/yyyy): ")
print("Date Output:", format_date(date_input))
