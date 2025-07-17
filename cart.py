# listOfFruits = ["banana", "apple" , "pear", "papaya", "tomato", "mango", "orange", "grapefruit","pomelo","blackberry", "blueberry","blackberry"]
# print(listOfFruits[0])
# print(listOfFruits[len(listOfFruits)-1], "at position", len(listOfFruits)-1)

cart = []

print(cart)
while(True):
    item = input("Press (A) if you would like to add items or (R) to remove items from your Shopping Cart? Type (D) if you're done shopping. ")
   

    if item.upper() == "A": 
        item =input("What would you like to add? ")

        if item.lower() == "bleh" or item.lower()=="blah":
            print("that is not an item")
            continue
        else:
            cart.append(item)
        print(cart)


    elif item.upper() == "R":
        item =input("What would you like to remove? ")
        cart.remove(item)
        print(cart)
      

    elif item.lower() == "d":
        print(cart)
        print("Thanks for shopping!")
        break

    else:
        print(cart)
        print("Thanks for shopping!")
        break
   