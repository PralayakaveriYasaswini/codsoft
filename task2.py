def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def calculator():
    while True:
        print("Simple Calculator")
        print("Operations: +, -, *, /")
        
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            print(f"Addition: {add(num1, num2)}")
            print(f"Subtraction: {subtract(num1, num2)}")
            print(f"Multiplication: {multiply(num1, num2)}")
            print(f"Division: {divide(num1, num2)}")
            
            cont = input("Do you want to perform another calculation? (y/n): ")
            if cont.lower() != 'y':
                print("Exiting calculator.")
                break
        except ValueError:
            print("Invalid input! Please enter numeric values.")

if __name__ == "__main__":
    calculator()

            
