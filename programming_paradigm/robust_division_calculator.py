import sys

def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)      # convert to float explicitly
        denominator = float(denominator)  # convert to float explicitly
        
        result = numerator / denominator
        
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None
    except ValueError:
        print("Error: Non-numeric value provided.")
        return None
    else:
        print(f"Result: {result}")
        return result

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 robust_division_calculator.py <numerator> <denominator>")
    else:
        safe_divide(sys.argv[1], sys.argv[2])
