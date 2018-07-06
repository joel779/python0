from decimal import *

print("Menu: ")
print("1 - Add")
print("2 - Subtract")
print("3 - Multiply")
print("4 - Divide")
print("5 - Square")
print("6 - Power")

menu_option=int(input("Enter Calculation: "))

no1=int(input("Enter first number: "))
no2=int(input("Enter second number: "))


if menu_option ==1:
    print(Decimal(no1 + no2))
elif menu_option ==2:
    print(Decimal(no1 - no2))
elif menu_option ==3:
    print(Decimal(no1 * no2))
elif menu_option ==4:
    print(Decimal(no1 / no2))
elif menu_option ==5:
    print(Decimal(no1 * no1))
elif menu_option ==6:
    print(Decimal(no1 ** no2))
else:
    print("Invalid selection")
