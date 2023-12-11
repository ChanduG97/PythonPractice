import calendar

def is_leap_year(year):
    # Function to check if a year is a leap year
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def print_calendar():
    # Get the year from the user
    year = int(input("Enter the year: "))

    # Validate the input
    if year < 1:
        print("Invalid year. Please enter a valid positive year.")
        return

    # Check if the year is a leap year
    if is_leap_year(year):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")
    print('-'*50)

    # Print the calendar for the specified year
    cal = calendar.TextCalendar()
    print(f"\nCalendar for the year {year}:\n")
    for month in range(1, 13):
        month_calendar = cal.formatmonth(year, month)
        print(month_calendar)
print('-'*50)
if __name__ == "__main__":
    print_calendar()
