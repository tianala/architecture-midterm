def binary_operations_menu():
    print("\nBinary Operations Menu:")
    print("[1] Division")
    print("[2] Multiplication")
    print("[3] Subtraction")
    print("[4] Addition")
    print("[5] Negative (2's Complement)")

def conversion_menu():
    print("\nNumber System Conversion Menu:")
    print("[1] Binary to X")
    print("[2] Decimal to X")
    print("[3] Octal to X")
    print("[4] Hexadecimal to X")

def main_menu():
    print("\nMain Menu:")
    print("[1] Binary Operations")
    print("[2] Number System Conversion")
    print("[3] Exit")

    binary_operations_menu()
    conversion_menu()

def invalid_choice_message():
    print("Invalid choice. Please enter a valid option.")

def exiting_message():
    print("Exiting program. Goodbye!")
