from utils import format_message

def calculate_sum(a, b):
    """Returns the sum of two numbers."""
    # BUG: Accidentally subtracting instead of adding
    return a - b

if __name__ == "__main__":
    res = calculate_sum(10, 5)
    print(format_message(f"The sum of 10 and 5 is: {res}"))
    # Expected: 15, Actual: 5
