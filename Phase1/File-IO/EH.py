# 7. Error Handling — try/except

try:
    result = 10/0

except ZeroDivisionError:
    print("You can't divide by zero.")


try:
    num = int(input("Enter number: "))
    print(num)

except ValueError:
    print("Please enter only numbers.")


try:
    file = open("data.csv")

except FileNotFoundError:
    print("Dataset not found.")