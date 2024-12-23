# Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize the row counter
row = 0

# Use a while loop for rows
while row < size:
    # Use a for loop to print asterisks for each column
    for col in range(size):
        print("*", end="")
    # Print a newline after each row
    print()
    # Increment the row counter
    row += 1

