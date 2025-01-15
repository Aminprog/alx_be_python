def safe_divide(numerator, denominator):
    try:
        # Convert inputs to floats
        numerator = float(numerator)
        denominator = float(denominator)

        # Attempt division
        if denominator == 0:
            return "Error: Cannot divide by zero."
        return f"The result of the division is {numerator / denominator}"

    except ValueError:
        # Handle non-numeric inputs
        return "Error: Please enter numeric values only."

