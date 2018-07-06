def maximum(number1,number2):
    if number1> number2:
        return number1
    else:
        return number2

number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))

print("Maximum is",maximum(number1,number2))
