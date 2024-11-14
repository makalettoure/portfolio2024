# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y

print ("Hello! Welcome to my calculator.")
print("Please choose an operation:")


while True:
    # take input from the user
    choice = input("+, -, * or / ")

    # check if choice is one of the four options
    if choice in ('+', '-', '*', '/'):
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Great! now enter a second number: "))
        except ValueError:
            print("Uh oh. Let's start again.")
            continue 


        if choice == '+':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '-':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '*':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '/':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("That was fun! Should we do another calculation? Yes or No: ")
        if next_calculation in ("no" "n" "N" "No"):
          break
    else:
        print("Invalid Input")