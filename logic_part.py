row_1 = [" ", " ", " "]
row_2 = [" ", " ", " "]
row_3 = [" ", " ", " "]
#
print(row_1)
print(row_2)
print(row_3)
list_of_rows = [row_1, row_2, row_3]

def winner_for_row(row_1,row_2,row_3):
    if row_1[0] == "x" and row_1[1] == "x" and row_1[2] == "x":
        print("player 1 wins")
        return True
    elif row_1[0] == "o" and row_1[1] == "o" and row_1[2] == "o":
        print("player 2 wins")
        return True
    elif row_2[0] == "x" and row_2[1] == "x" and row_2[2] == "x":
        print("player 1 wins")
        return True
    elif row_2[0] == "o" and row_2[1] == "o" and row_2[2] == "o":
        print("player 2 wins")
        return True
    elif row_3[0] == "x" and row_3[1] == "x" and row_3[2] == "x":
        print("player 1 wins")
        return True
    elif row_3[0] == "o" and row_3[1] == "o" and row_3[2] == "o":
        print("player 2 wins")
        return True

def winner_for_columns(row_1,row_2,row_3):
    if row_1[0] == "x" and row_2[0] == "x" and row_3[0] == "x":
        return True
    elif row_1[0] == "o" and row_2[0] == "o" and row_3[0] == "o":
        return True
    elif row_1[1] == "x" and row_2[1] == "x" and row_3[1] == "x":
        return True
    elif row_1[1] == "o" and row_2[1] == "o" and row_3[1] == "o":
        return True
    elif row_1[2] == "x" and row_2[2] == "x" and row_3[2] == "x":
        return True
    elif row_1[2] == "o" and row_2[2] == "o" and row_3[2] == "o":
        return True

def winner_for_diagonal(row_1,row_2,row_3,):
    if row_1[0] == "x" and row_2[1] == "x" and row_3[2] == "x":
        return  True
    elif row_1[0] == "o" and row_2[1] == "o" and row_3[2] == "o":
        return True
    elif row_1[2] == "x" and row_2[1] == "x" and row_3[0] == "x":
        return  True
    elif row_1[2] == "o" and row_2[1] == "o" and row_3[0] == "o":
        return True


def is_occupied_for_p1(list_of_rows,player1_choosen_row,player_1_position ):
    if player1_choosen_row == 1:
        return list_of_rows[player1_choosen_row - 1][player_1_position - 1] != " "
    elif player1_choosen_row == 2:
        return list_of_rows[player1_choosen_row - 1][player_1_position - 1] != " "
    elif player1_choosen_row == 3:
        return list_of_rows[player1_choosen_row - 1][player_1_position - 1] != " "


def is_occupied_for_p2(list_of_rows,player2_choosen_row,player_2_position ):
    if player2_choosen_row == 1:
        return list_of_rows[player2_choosen_row - 1][player_2_position - 1] != " "
    elif player2_choosen_row == 2:
        return list_of_rows[player2_choosen_row - 1][player_2_position - 1] != " "
    elif player2_choosen_row == 3:
        return list_of_rows[player2_choosen_row - 1][player_2_position - 1] != " "


box1 = {}
game = True
while game:
    player_1 = True
    player1_choosen_row = int(input("Enter the row for player 1 = x:"))
    player_1_position = int(input("Enter the position to update (1, 2 or 3) player 1: "))
    if is_occupied_for_p1(list_of_rows, player1_choosen_row, player_1_position):
        print("That position is already occupied. Please choose a different position.")
        player_1 = False

    else:
        player_1_symbol = "x"
        player_1_choice = list_of_rows[player1_choosen_row - 1]  # this is now the row
        player_1_choice[player_1_position - 1] = player_1_symbol

    if player_1:
        print(row_1)
        print(row_2)
        print(row_3)

        # player 1 algorithm ##########
        count_in_row_1 = 0
        count_in_row_2 = 0
        count_in_row_3 = 0
        for i in row_1:
            if i != " ":
                count_in_row_1 += 1
        for j in row_2:
            if j != " ":
                count_in_row_2 += 1
        for k in row_3:
            if k != " ":
                count_in_row_2 += 1

        if count_in_row_1 + count_in_row_2 + count_in_row_3 == 9:
            print("Draw")
            game = False
            break
        elif winner_for_row(row_1, row_2, row_3):
            print("Game over!")
            game = False
            break
        elif winner_for_columns(row_1, row_2, row_3):
            print("Game over!")
            game = False
            break
        elif winner_for_diagonal(row_1, row_2, row_3):
            print("Game over!")
            game = False
            break
####### player 2
        game2 = True
        while game2:
            player_2 = True
            player2_choosen_row = int(input("Enter the row for player 2 = o :"))
            player_2_position = int(input("Enter the position to update (1, 2 or 3) for player 2: "))
            if is_occupied_for_p2(list_of_rows,player2_choosen_row,player_2_position ):
                print("That position is already occupied. Please choose a different position.")
                player_2 = False

            else:
             #player_1_symbol = input("Enter player 1 symbol (x or o): ")
                player_2_symbol = "o"
                player_2_choice = list_of_rows[player2_choosen_row - 1]  # this is now the row
                player_2_choice[player_2_position - 1] = player_2_symbol
                if player_2:
                    print(row_1)
                    print(row_2)
                    print(row_3)
                    ##### check if the rows are full
                ######### player 2 algorithm
                    for i in row_1:
                        if i != " ":
                            count_in_row_1 += 1
                    for j in row_2:
                        if j != " ":
                            count_in_row_2 += 1
                    for k in row_3:
                        if k != " ":
                            count_in_row_2 += 1

                    if count_in_row_1 + count_in_row_2 + count_in_row_3 == 9:
                        print("Draw!")
                        game = False
                    elif winner_for_row(row_1, row_2, row_3):
                        print("Game over!")
                        game = False
                    elif winner_for_columns(row_1, row_2, row_3):
                        print("Game over!")
                        game = False
                    elif winner_for_diagonal(row_1, row_2, row_3):
                        print("Game over!")
                        game = False
                    game2 = False