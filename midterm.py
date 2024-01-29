def binary_operations():
    print("""
--------- Menu-2 (Binary Operations) ---------
[1] Division
[2] Multiplication
[3] Subtraction
[4] Addition
[5] Negative (2's Complement)
""")
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

def conversion():
    print("""
--------- Menu-3 (Conversion) ----------------
[1] Binary to X
[2] Decimal to X
[3] Octal to X
[4] Hexadecimal to X
""")
    conversion_choice = int(input("Enter your choice: "))
    
    if conversion_choice == 1:
        pass
    elif conversion_choice == 2:
        pass
    elif conversion_choice == 3:
        pass
    elif conversion_choice == 4:
        pass
    else:
        print("Invalid choice")

def main():
    while True:
        print("""
--------- Menu-1 (Main Menu) ---------------
[1] Binary Operations
[2] Number System Conversion
[3] Exit
""")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            binary_operations()
        elif choice == 2:
            conversion()
        elif choice == 3:
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
