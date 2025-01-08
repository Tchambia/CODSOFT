# Calculator with Basic Arithmetic Operations
def display_calculator_menu():
    print("\n--- Calculator Menu ---")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

def perform_calculation(choice):
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        if choice == "1":
            print(f"Result: {num1} + {num2} = {num1 + num2}")
        elif choice == "2":
            print(f"Result: {num1} - {num2} = {num1 - num2}")
        elif choice == "3":
            print(f"Result: {num1} * {num2} = {num1 * num2}")
        elif choice == "4":
            if num2 == 0:
                print("Error: Division by zero is not allowed!")
            else:
                print(f"Result: {num1} / {num2} = {num1 / num2}")
        else:
            print("Invalid operation!")
    except ValueError:
        print("Invalid input! Please enter numeric values.")

# Main program loop
while True:
    display_calculator_menu()
    choice = input("\nEnter your choice (1-5): ").strip()
    if choice in ["1", "2", "3", "4"]:
        perform_calculation(choice)
    elif choice == "5":
        print("\nGoodbye!")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 5.")
