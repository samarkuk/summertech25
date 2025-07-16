from random import randint

playAgain = True

while(playAgain==True):
    print("you have to pick a limit for the number of guesses")
    guesslimit = int(input("enter a guesslimit for you"))
    numGenerator = randint(1,10)
    guess=-1
    tries=0

    while guess!=numGenerator:

        guess=int(input("guess the number "))
        tries = tries + 1
    

        if guess < numGenerator:
            print("too low")
        elif guess > numGenerator:
            print("too high")

        if tries == guesslimit and guess!=numGenerator:
            print("Game over! Youve reached the limit")
            print("the number was",numGenerator)
            break


    if guess==numGenerator:
        print("ding ding ding great job you guessed the number")

    print("do you want to keep on playing? ")
    answer = input("enter yes if nyou want to keep on playing or enter no if you do not want to keep on playing")
    if answer == "yes":
        print("great lets keep on playing")
    if answer == "no":
        print("thats okay you can play later")
        break







