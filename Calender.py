import calendar

def print_calendar():
    # Get the year from the user
    year = int(input("Enter the year: "))

    # Validate the input
    if year < 1:
        print("Invalid year. Please enter a valid positive year.")
        return

    # Print the calendar for the specified year
    cal = calendar.TextCalendar()
    print(f"\nCalendar for the year {year}:\n")
    for month in range(1, 13):
        month_calendar = cal.formatmonth(year, month)
        print(month_calendar)

if __name__ == "__main__":
    print_calendar()
