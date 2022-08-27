# Крестики и нолики

my_board = [1, 2, 3,
            4, 5, 6,
            7, 8, 9]
# Инициализация победных линий
victories = [[0, 1, 2],
             [3, 4, 5],
             [6, 7, 8],
             [0, 3, 6],
             [1, 4, 7],
             [2, 5, 8],
             [0, 4, 8],
             [2, 4, 6]]


def print_my_board():
    print(my_board[0], end=" ")
    print(my_board[1], end=" ")
    print(my_board[2])

    print(my_board[3], end=" ")
    print(my_board[4], end=" ")
    print(my_board[5])

    print(my_board[6], end=" ")
    print(my_board[7], end=" ")
    print(my_board[8])


def motion_player(motion, symbol):
    ind = my_board.index(motion)
    my_board[ind] = symbol


print_my_board()
win1 = 0
win2 = 0
game_over = False
count = 0

while count <= 4:
    if count <=4 and win2!=1:
        motion = int(input("Человек 1, ваш ход: "))
        for i in my_board:
            if i == motion:
                symbol = "X"
                motion_player(motion, symbol)
           
    else:
        break
    print_my_board()
    print(count)
    for i in victories:
        if my_board[i[0]] == "X" and my_board[i[1]] == "X" and my_board[i[2]] == "X":
            print("Победа за первым игроком")
            win1=1
            break
            
    if count !=4 or win1!=1:
        motion = int(input("Человек 2, ваш ход: "))
        for i in my_board:
            if i == motion:
                symbol = "O"
                motion_player(motion, symbol)
    else:
        break
    print_my_board()
    for i in victories: 
        if my_board[i[0]] == "O" and my_board[i[1]] == "O" and my_board[i[2]] == "O":
            print("Победа за вторым игроком") 
            win2=1     
    count+=1
    print(count)


