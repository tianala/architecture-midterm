from menus import conversion_menu

def number_system_conversion():
    conversion_menu()

def binary_to_decimal(binary):
    decimal = int(binary, 2)
    return decimal

def binary_to_hexadecimal(binary):
    decimal = binary_to_decimal(binary)
    hexadecimal = decimal_to_hexadecimal(decimal)
    return hexadecimal

def binary_to_octal(binary):
    decimal = binary_to_decimal(binary)
    octal = decimal_to_octal(decimal)
    return octal

def decimal_to_binary(decimal):
    binary = bin(decimal).lstrip("0b")
    return binary

def decimal_to_hexadecimal(decimal):
    hexadecimal = hex(decimal).lstrip("0x").upper()
    return hexadecimal

def decimal_to_octal(decimal):
    octal = oct(decimal).lstrip("0o")
    return octal

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

