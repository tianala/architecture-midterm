'''Options for Binary Operation'''

def binary_operations_menu():
    print("\nBinary Operations Menu:")
    print("[1] Division")
    print("[2] Multiplication")
    print("[3] Subtraction")
    print("[4] Addition")
    print("[5] Negative (2's Complement)")

'''Option for Conversion'''

def conversion_menu():
    print("\nNumber System Conversion Menu:")
    print("[1] Binary to X")
    print("[2] Decimal to X")
    print("[3] Octal to X")
    print("[4] Hexadecimal to X")

'''------------------------------------------------------------------------------------------------------------------------------------'''




'''------------------------------------------------------------------------------------------------------------------------------------'''



'''------------------------------------------------------------------------------------------------------------------------------------'''

def main_menu():
    while True:
        print("\nMain Menu:")
        print("[1] Binary Operations")
        print("[2] Number System Conversion")
        print("[3] Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            binary_operations()
        elif choice == 2:
            number_system_conversion()
        elif choice == 3:
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main_menu()


