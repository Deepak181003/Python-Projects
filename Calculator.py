# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    return x / y

# Function to display menu and get user choice
def get_user_choice():
    print("\n===== CALCULATOR MENU =====")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("===========================")
    return input("Enter your choice (1/2/3/4): ")

# Main program
print("Welcome to Professional Calculator")

while True:
    try:
        num1 = float(input("\nEnter first number: "))
        num2 = float(input("Enter second number: "))
        operation = get_user_choice()

        if operation == '1':
            result = add(num1, num2)
            operator = '+'
        elif operation == '2':
            result = subtract(num1, num2)
            operator = '-'
        elif operation == '3':
            result = multiply(num1, num2)
            operator = '*'
        elif operation == '4':
            result = divide(num1, num2)
            operator = '/'
        else:
            print("Invalid choice! Please enter a valid operation number.")
            continue

        print(f"\n{num1} {operator} {num2} = {result}\n")

        # Ask user if they want to continue
        another_calculation = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
        if another_calculation != 'yes':
            print("\nThank you for using the Professional Calculator. Goodbye!")
            break

    except ValueError:
        print("\nInvalid input! Please enter valid numbers.")
    except Exception as e:
        print(f"\nError: {str(e)}")

