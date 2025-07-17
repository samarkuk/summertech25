board =[]
for i in range (3):
    slot = []
    for j in range (3):
        slot.append(" ")
    board.append(slot)

moves=0
player="X"

while(moves>=0 and moves<9) :
    print("  " + board[0][0]+ ' | ' + board[0][1] + ' | ' + board[0][2])
    print("---------")
    print(" " + board [1][0]+ ' | ' + board[1][1] +' | ' + board [1][2])
    print("---------")
    print(" " + board [2][0]+ ' | ' + board[2][1] +' | ' + board [2][2])
    
    print("Lets play! ")
    row = int(input("Enter the row you would like your piece placed (0-2) "))
    col = int(input("Enter the column you would like your piece placed (0-2) "))

    board[row][col] = player
    moves = moves + 1

    if board[0][0]== player and board[0][1]== player and board [0][2] == player:
        print("Player", player, "wins!")
        break
    elif board [1][0]== player and board[1][1]== player and board[1][2]== player:
        print("Player", player, "wins!")
        break
    elif board[2][0]== player and board[2][1]== player and board [2][2]== player:  
        print("Player", player, "wins!!")
        break
    elif board[0][0]== player and board[1][0]== player and board [2][0] == player:
        print("Player", player, "wins!")
        break
    elif board [0][1]== player and board[1][1]== player and board[2][1]== player:
        print("Player", player, "wins!")
        break
    elif board[0][2]== player and board[1][2]== player and board [2][2]== player:    
        print("Player", player, "wins!")
        break
    elif board [0][0]== player and board[1][1]== player and board[2][2]== player:
        print("Player", player, "wins!")
        break
    elif board[0][2]== player and board[1][1]== player and board [2][0]== player:    
        print("Player", player, "wins!")
        break
    
    if player == "X":
        player = "O"
    else:
        player = "X"

if moves == 9:
    print("Its a Tie")




