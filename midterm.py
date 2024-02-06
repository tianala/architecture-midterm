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

'''Menu for binary operation'''
def binary_operations():
    binary_operations_menu()
    operation_choice = int(input("Enter your choice: "))
    
    if operation_choice == 1:
        def binary_division(dividend, divisor):
            dividend_int = int(dividend, 2)
            divisor_int = int(divisor, 2)
            quotient_int = 0
            remainder_int = 0
            for i in range(len(dividend)):
                remainder_int = (remainder_int << 1) | int(dividend[i])
                if remainder_int >= divisor_int:
                    remainder_int -= divisor_int
                    quotient_int |= (1 << (len(dividend) - 1 - i))
            quotient_bin = format(quotient_int, 'b')
            remainder_bin = format(remainder_int, 'b')
            return quotient_bin, remainder_bin

        dividend = input("Enter the dividend in binary: ")
        divisor = input("Enter the divisor in binary: ")
        quotient, remainder = binary_division(dividend, divisor)
        print("Quotient:", quotient)
        print("Remainder:", remainder)
        
    elif operation_choice == 2:
        def binary_multiplication(a, b):
            product = 0
            a_int = int(a, 2)
            b_int = int(b, 2)
            while b_int != 0:
                if b_int & 1:
                    product += a_int
                a_int <<= 1
                b_int >>= 1
            return format(product, 'b')

        factor1 = input("Enter the multiplicand in binary: ")
        factor2 = input("Enter the multiplier in binary: ")
        result = binary_multiplication(factor1, factor2)
        print("Product:", result)
        
    elif operation_choice == 3:
        def binary_subtraction(a, b):
            result_int = int(a, 2) - int(b, 2)
            if result_int == 0:
                return '0'
            elif result_int < 0:
                result_binary = decimal_to_binary(-result_int)
                return '-' + result_binary
            else:
                return decimal_to_binary(result_int)

        minuend = input("Enter the minuend in binary: ")
        subtrahend = input("Enter the subtrahend in binary: ")
        difference = binary_subtraction(minuend, subtrahend)
        print("Difference:", difference)
        
    elif operation_choice == 4:
        def add_binary(a, b):
            max_length = max(len(a), len(b))
            a = '0' * (max_length - len(a)) + a
            b = '0' * (max_length - len(b)) + b

            result = ''
            carry = 0

            for i in range(max_length - 1, -1, -1):
                digit_sum = int(a[i]) + int(b[i]) + carry
                result = str(digit_sum % 2) + result
                carry = digit_sum // 2

            if carry:
                result = '1' + result

            return result

        binary1 = input("Enter the first addend number: ")
        binary2 = input("Enter the second addend number: ")
        print("Sum:", add_binary(binary1, binary2))

    elif operation_choice == 5:
        def twos_complement(binary):
            complement = ''.join('1' if bit == '0' else '0' for bit in binary)
            
            result = ''
            carry = 1
            for bit in complement[::-1]:
                if bit == '0' and carry == 1:
                    result = '1' + result
                    carry = 0
                elif bit == '1' and carry == 1:
                    result = '0' + result
                else:
                    result = bit + result
            
            return result

        binary = input("Enter a binary number: ")
        negative = twos_complement(binary)
        print("Negative (2's complement):", negative)

    else:
        print("Invalid choice")


''''BINARY TO DECIMAL, HEXADECIMAL, AND OCTAL'''
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


