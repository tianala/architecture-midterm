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

'''Functions for binary operation (Division, Multiplication, Subtraction, Addition, Negative (2's Complement))'''

def division():
    pass

def multiplication():
    pass

def subtraction():
    pass

def addition():
    pass

def negative_complement():
    pass

'''Menu for Binary Operation'''
def binary_operations():
    binary_operations_menu()
    operation_choice = int(input("Enter your choice: "))
    
    if operation_choice == 1:
        pass
    elif operation_choice == 2:
        pass
    elif operation_choice == 3:
        pass
    elif operation_choice == 4:
        pass
    elif operation_choice == 5:
        pass
    else:
        print("Invalid choice")


'''------------------------------------------------------------------------------------------------------------------------------------'''

'''Functions for converting binary, decimal, hexadecimal, and octal'''

''''BINARY TO DECIAML, HEXADECIMAL, AND OCTAL'''
def binary_to_decimal(binary):
    decimal = int(binary, 2)
    return decimal

def binary_to_hexadecimal(binary):
    decimal = binary_to_decimal(binary)
    hexadecimal = hex(decimal).lstrip("0x").upper()
    return hexadecimal

def binary_to_octal(binary):
    decimal = binary_to_decimal(binary)
    octal = oct(decimal).lstrip("0o")
    return octal

'''DECIMAL TO BINARY, HEXADECIMAL, AND OCTAL'''
def decimal_to_binary(decimal):
    binary = bin(decimal).lstrip("0b")
    return binary

def decimal_to_hexadecimal(decimal):
    hexadecimal = hex(decimal).lstrip("0x").upper()
    return hexadecimal

def decimal_to_octal(decimal):
    octal = oct(decimal).lstrip("0o")
    return octal

'''HEXADECIMAL TO BINARY, DECIMAL, AND OCTAL'''
def hexadecimal_to_binary(hexadecimal):
    decimal = int(hexadecimal, 16)
    binary = bin(decimal).lstrip("0b")
    return binary

def hexadecimal_to_decimal(hexadecimal):
    decimal = int(hexadecimal, 16)
    return decimal

def hexadecimal_to_octal(hexadecimal):
    decimal = int(hexadecimal, 16)
    octal = oct(decimal).lstrip("0o")
    return octal

'''OCTAL TO BINARY, DECIMAL, AND HEXADECIAL'''
def octal_to_binary(octal):
    decimal = int(octal, 8)
    binary = bin(decimal).lstrip("0b")
    return binary

def octal_to_decimal(octal):
    decimal = int(octal, 8)
    return decimal

def octal_to_hexadecimal(octal):
    decimal = int(octal, 8)
    hexadecimal = hex(decimal).lstrip("0x").upper()
    return hexadecimal

'''Menu for Conversion'''
def number_system_conversion():
    conversion_menu()
    
    conversion_choice = int(input("Enter your choice: "))

    if conversion_choice == 1:
        binary_input = input("Input Binary: ")
        decimal_output = binary_to_decimal(binary_input)
        hexadecimal_output = binary_to_hexadecimal(binary_input)
        octal_output = binary_to_octal(binary_input)
        print("Decimal:   ", decimal_output)
        print("Hexa:      ", hexadecimal_output)
        print("Octal:     ", octal_output)

        
    elif conversion_choice == 2:
        decimal_input = int(input("Input Decimal: "))
        binary_output = decimal_to_binary(decimal_input)
        hexadecimal_output = decimal_to_hexadecimal(decimal_input)
        octal_output = decimal_to_octal(decimal_input)
        print("Binary:    ", binary_output)
        print("Hexa:      ", hexadecimal_output)
        print("Octal:     ", octal_output)

    elif conversion_choice == 3:
        octal_input = input("Input Octal: ")
        binary_output = octal_to_binary(octal_input)
        decimal_output = octal_to_decimal(octal_input)
        hexadecimal_output = octal_to_hexadecimal(octal_input)
        print("Binary:    ", binary_output)
        print("Decimal:   ", decimal_output)
        print("Hexa:      ", hexadecimal_output)

    elif conversion_choice == 4:
        hexadecimal_input = input("Input Hexadecimal: ")
        binary_output = hexadecimal_to_binary(hexadecimal_input)
        decimal_output = hexadecimal_to_decimal(hexadecimal_input)
        octal_output = hexadecimal_to_octal(hexadecimal_input)
        print("Binary:    ", binary_output)
        print("Decimal:   ", decimal_output)
        print("Octal:     ", octal_output)

    else:
        print("Invalid choice")


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


