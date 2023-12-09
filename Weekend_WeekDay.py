import datetime

def define_day(day):
    # List of weekend days
    weekends = ['Saturday', 'Sunday']

    # Convert day to datetime object
    dt = datetime.datetime.strptime(day, '%A').date()

    # Check if day is a weekday or a weekend
    if dt.strftime('%A') in weekends:
        return "Weekend"
    else:
        return "Weekday"

# Accept day from end user
day = input("Enter a day: ")

# Call the function with the accepted day
print(define_day(day))