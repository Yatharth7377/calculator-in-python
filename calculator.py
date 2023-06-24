import math

print("Calculator Program\n")

while True:
    print("Please select an option:")
    print("1 - Addition")
    print("2 - Subtraction")
    print("3 - Multiplication")
    print("4 - Division")
    print("5 - Exponentiation")
    print("6 - Square root")
    print("7 - Sine")
    print("8 - Cosine")
    print("9 - Tangent")
    print("10 - Logarithm")
    print("11 - Quit")

    choice = input("\nEnter your choice: ")

    if choice == '11':
        print("Exiting...")
        break

    if choice not in ['6', '7', '8', '9', '10']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

    if choice == '1':
        print(num1, "+", num2, "=", (num1 + num2))

    elif choice == '2':
        print(num1, "-", num2, "=", (num1 - num2))

    elif choice == '3':
        print(num1, "*", num2, "=", (num1 * num2))

    elif choice == '4':
        print(num1, "/", num2, "=", (num1 / num2))

    elif choice == '5':
        print(num1, "^", num2, "=", (num1 ** num2))

    elif choice == '6':
        num = float(input("Enter a number: "))
        print("Square root of", num, "=", math.sqrt(num))

    elif choice == '7':
        angle = float(input("Enter an angle in degrees: "))
        print("Sine of", angle, "degrees =", math.sin(math.radians(angle)))

    elif choice == '8':
        angle = float(input("Enter an angle in degrees: "))
        print("Cosine of", angle, "degrees =", math.cos(math.radians(angle)))

    elif choice == '9':
        angle = float(input("Enter an angle in degrees: "))
        print("Tangent of", angle, "degrees =", math.tan(math.radians(angle)))

    elif choice == '10':
        num = float(input("Enter a number: "))
        print("Logarithm of", num, "to base 10 =", math.log10(num))

    else:
        print("Invalid Input")