# answer =input("Did you eat your breakfast today? yes or no ")

# if answer=="yes":
#     print("good job!")
# elif answer=="no":
#     print("you should go eat.")
# else:
#     print("its a yes or no question")

score=0
print("who was the president of the united states from 2012-2016")
print("a =Joe Biden")
print("b = Donald Trump")
print("c = Barack Obama")

answer = input()

if answer=="a":
    print("you are wrong")
elif answer=="b":
    print("you are also wrong")
elif answer=="c":
    print("You are correct")
    score=score+1
else:
    print("that is not an option")



print(" what is 11+63-45x2-34+17")
print("a = 33")
print("b = -33")
print("c = 35")
print("d = -35")
answer = input()
if answer=="b":
    score=score+1
    print("you are correct")
else:
    print("youre wrong")



print("In which country is Casablanca")
print("a = Spain")
print("b = Ibiza")
print("c = Bermuda")
print("d = Morroco")
answer = input()
if answer=="d":
    score=score+1
    print("you are correct")
else:
    print("you are wrong")
    

print ("you got",score,"questions correct")