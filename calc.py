num1 = int(input("enter the first number: "))
num2 = int(input("enter the second number: "))
op = input("enter an operation")


if (op == "+"):
    print(num1 + num2)
elif (op == "-"):
    print(num1 - num2)
elif (op == "x"):
    print (num1 * num2)
elif (op == "/"):
    print(num1 / num2)
else:
    print("that is not an option")