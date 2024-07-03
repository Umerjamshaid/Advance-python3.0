from datetime import datetime
import calendar


def find_day_of_week(date_str: str) -> str:
    date = datetime.strptime(date_str, "%Y-%m-%d")
    return date.strftime("%A")
print(find_day_of_week("2024-07-3"))

