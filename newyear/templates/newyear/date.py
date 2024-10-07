from datetime import datetime
from django.shortcuts import render


def get_date():
    now = datetime.now()
    day = now.day
    month = now.month
    year = now.year
    return day,month,year

def get_message():
    # New Year's Date
    new_year_day = 18
    new_year_month = 5

    
    # Get current date
    day, month, year = get_date()
    
    # Determine the message to display
    message = "HAPPY BIRTHDAY MY BABY RUBY!~" if day == new_year_day and month == new_year_month  else "NO!"
    return message

