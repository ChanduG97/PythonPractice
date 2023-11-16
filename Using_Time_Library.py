import time
def display_time_and_date():
    # Get the current time in HH:MM:SS format
    current_time = time.strftime("%H:%M:%S", time.localtime())

    # Get the current day (0-6, where Monday is 0 and Sunday is 6)
    current_day = time.strftime("%A", time.localtime())

    # Get the current date in DD/MM/YYYY format
    current_date = time.strftime("%d/%m/%Y", time.localtime())

    # Display the results
    print("Current Time:", current_time)
    print("Current Day:", current_day)
    print("Current Date:", current_date)


# Call the function to display time and date
display_time_and_date()


'''
OUTPUT : 

Current Time: 17:21:31
Current Day: Thursday
Current Date: 16/11/2023

Process finished with exit code 0

'''