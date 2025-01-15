from datetime import datetime, timedelta

# Part 1: Display the current date and time
def display_current_datetime():
    current_date = datetime.now()
    print(f"Current date and time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")

# Part 2: Calculate a future date
def calculate_future_date():
    days = int(input("Enter the number of days to add to the current date: "))
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")

# Main function to call the parts
def main():
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()

