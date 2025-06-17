import sys
from division_calculator import safe_divide

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 main-1.py <numerator> <denominator>")
        sys.exit(1)

    try:
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])
        result = safe_divide(num1, num2)
        print("Result:", result)
    except ValueError:
        print("Error: Please enter valid numbers.")
