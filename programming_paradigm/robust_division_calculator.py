import sys

def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        result = numerator / denominator
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return
    except ValueError:
        print("Error: Please enter numeric values only.")
        return
    else:
        print(f"The result of the division is {result}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 robust_division_calculator.py <numerator> <denominator>")
    else:
        safe_divide(sys.argv[1], sys.argv[2])
