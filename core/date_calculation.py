"""
Date Calculation

Developer: Dev Team.
Last Modified Date:
"""
from datetime import datetime, timedelta


def date_calculation(input_date=None):
    """
    This function will returns the valid draw date from the given
    input date.

    Input: Optional supplied date input date.
    :return: Valid date of next draw.
    """
    try:
        input_date = datetime.strptime(input_date, "%d/%m/%Y") if input_date else datetime.now()
    except ValueError:
        raise ValueError("Invalid Input Format!")
    week_day = input_date.weekday()
    days = abs(week_day - 5)
    if 0 <= week_day <= 2:
        days = abs(week_day-2)
    elif week_day == 6:
        days = abs(week_day-3)
    return (input_date + timedelta(days=days)).strftime("%d/%m/%Y")

if __name__ == "__main__":
    print (date_calculation("date"))