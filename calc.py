
runAgain = True

while(runAgain==True):
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

    print("do you still want to calculate? ")
    response = input("eneter yes if you still want to calculate or no if you don't ")

    if response == "no":
        print("okay thats fine I will see you another time")
        runAgain=False