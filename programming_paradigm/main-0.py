import sys
from bank_account import BankAccount

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main-0.py <command:amount>")
        return

    command_input = sys.argv[1]
    
    if ':' not in command_input:
        print("Invalid format. Use command:amount")
        return

    command, value = command_input.split(':')

    try:
        amount = float(value)
    except ValueError:
        print("Amount must be a number.")
        return

    account = BankAccount()

    if command == "deposit":
        account.deposit(amount)
        account.display_balance()
    elif command == "withdraw":
        if account.withdraw(amount):
            print("Withdrawal successful.")
        else:
            print("Insufficient funds.")
        account.display_balance()
    else:
        print("Unknown command. Use 'deposit' or 'withdraw'.")

if __name__ == "__main__":
    main()
