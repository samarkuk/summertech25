# farrahsB = input("what did you eat for breakfast today Farrahh?")



from random import randint
while (True):

    print("Let's play RockPaperScissors")
    print("Press:")
    print("0: Rock")
    print("1: paper")
    print("2: scissors")
    print("Shoot! ")
    computer = randint(0,2)
    user = int(input())

    if computer == 0:
        if user ==1 :
            print("You win, the computer chose rock")
        elif user == 2 :
            print("you lose the computer chose rock")

    elif computer == 1 :
        if user == 2 :
            print("you win the computer chose paper")
        elif user == 0 :
            print("you lose the computer chose paper")
    elif computer == 2 :
        if user == 0 :
            print("you win the computer chose scissors")
        elif user == 1 :
            print("you lose the computer chose scissors")
            
    elif computer == user:
        print("Great effort you both tied")
    if user >2 : 
        print("that is not an option. Try again")
        continue
        

    print("do you want to continue playiong?")
    z = input("enter yes if you want to keep on playing or enter no if you don't")

    if z == "yes":
        print("okay great lets keep on playing")
    if z == "no" :
        print("no problem we can play later")
        break