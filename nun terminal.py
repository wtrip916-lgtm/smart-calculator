import time
time.sleep(1)
print("=== SMART CALCULATOR ===")
time.sleep(1)
name = input("Enter your name: ")
print("Welcome " + name + " to the smart calculator")
a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))

choice = input("Choose an operation 1. Addition 2. Subtraction 3. Multiplication 4. Division: ")
if choice == '1':
    print("Result: " + str(a + b))
elif choice == '2':
    print("Result: " + str(a - b))
elif choice == '3':
    print("Result: " + str(a * b))
elif choice == '4':
    if b != 0:
        print("Result: " + str(a / b))
    else:
        print("Error: cannot divide by zero")
