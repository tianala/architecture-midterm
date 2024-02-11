import binary_operations
import conversion

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