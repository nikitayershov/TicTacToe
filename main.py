

cells = "         "
M = [[cells[0], cells[1], cells[2]],
     [cells[3], cells[4], cells[5]],
     [cells[6], cells[7], cells[8]]]

print('---------')
print("|" + " " + M[0][0] + " " + M[0][1] + " " + M[0][2] + " " + "|")

print("|" + " " + M[1][0] + " " + M[1][1] + " " + M[1][2] + " " + "|")

print("|" + " " + M[2][0] + " " + M[2][1] + " " + M[2][2] + " " + "|")
print('---------')
while True:
    x_move = input("Enter the coordinates: ")
    x_move = x_move.split()

    while not (x_move[0].isdigit() and x_move[1].isdigit()):
        print("You should enter numbers!")
        x_move = input("Enter the coordinates: ")
        x_move = x_move.split()
    x_move = [int(x) for x in x_move]

    while not (0 <= x_move[0] - 1 <= 2 and 0 <= x_move[1] - 1 <= 2):
        print("Coordinates should be from 1 to 3!")
        x_move = input("Enter the coordinates: ")
        x_move = x_move.split()
        x_move = [int(x) for x in x_move]

    while M[x_move[0] - 1][x_move[1] - 1] == "X" or M[x_move[0] - 1][x_move[1] - 1] == "O":
        print("This cell is occupied! Choose another one!")
        x_move = input("Enter the coordinates: ")
        x_move = x_move.split()
        x_move = [int(x) for x in x_move]

    M[x_move[0] - 1][x_move[1] - 1] = "X"
    print('---------')
    print("|" + " " + M[0][0] + " " + M[0][1] + " " + M[0][2] + " " + "|")

    print("|" + " " + M[1][0] + " " + M[1][1] + " " + M[1][2] + " " + "|")

    print("|" + " " + M[2][0] + " " + M[2][1] + " " + M[2][2] + " " + "|")
    print('---------')
    num_x = 0
    num_o = 0
    num_space = 0
    for x in range(0, 3):
        for y in range(0, 3):
            if M[x][y] == "X":
                num_x += 1
            elif M[x][y] == "O":
                num_o += 1
            elif M[x][y] == "_" or M[x][y] == " ":
                num_space += 1

    firs_row_x, sec_row_x, third_row_x = 0, 0, 0
    firs_row_o, sec_row_o, third_row_o = 0, 0, 0
    firs_col_x, sec_col_x, third_col_x = 0, 0, 0
    firs_col_o, sec_col_o, third_col_o = 0, 0, 0
    for x in range(0, 3):
        if M[0][x] == "X":
            firs_row_x += 1
        if M[1][x] == "X":
            sec_row_x += 1
        if M[2][x] == "X":
            third_row_x += 1
        if M[0][x] == "O":
            firs_row_o += 1
        if M[1][x] == "O":
            sec_row_o += 1
        if M[2][x] == "O":
            third_row_o += 1
        if M[x][0] == "X":
            firs_col_x += 1
        if M[x][1] == "X":
            sec_col_x += 1
        if M[x][2] == "X":
            third_col_x += 1
        if M[x][0] == "O":
            firs_col_o += 1
        if M[x][1] == "O":
            sec_col_o += 1
        if M[x][2] == "O":
            third_col_o += 1

    diagonal_left_x, diagonal_right_x = 0, 0
    diagonal_left_o, diagonal_right_o = 0, 0

    if M[0][0] == "X" and M[1][1] == "X" and M[2][2] == "X":
        diagonal_left_x = 3
    if M[0][0] == "O" and M[1][1] == "O" and M[2][2] == "O":
        diagonal_left_o = 3
    if M[0][2] == "X" and M[1][1] == "X" and M[2][0] == "X":
        diagonal_right_x = 3
    if M[0][2] == "O" and M[1][1] == "O" and M[2][0] == "O":
        diagonal_right_o = 3

    M_wins_x = [[firs_row_x, sec_row_x, third_row_x, diagonal_left_x],
                [firs_col_x, sec_col_x, third_col_x, diagonal_right_x]]
    M_wins_o = [[firs_row_o, sec_row_o, third_row_o, diagonal_left_o],
                [firs_col_o, sec_col_o, third_col_o, diagonal_right_o]]
    x_win = 0
    o_win = 0

    for x in range(2):
        for y in range(4):
            if M_wins_x[x][y] == 3:
                x_win += 1
            if M_wins_o[x][y] == 3:
                o_win += 1

    if -1 <= num_x - num_o <= 1:
        if x_win == 1 and o_win != 1:
            print("X wins")
            break
        if o_win == 1 and x_win != 1:
            print("O wins")
            break
        if x_win >= 1 and o_win >= 1:
            print("Impossible")
            break
        if x_win == 0 and o_win == 0 and num_x + num_o != 9:
            print("Game not finished")
        if x_win == 0 and o_win == 0 and num_x + num_o == 9:
            print("Draw")
            break
    o_move = input("Enter the coordinates: ")
    o_move = o_move.split()

    while not (o_move[0].isdigit() and o_move[1].isdigit()):
        print("You should enter numbers!")
        o_move = input("Enter the coordinates: ")
        o_move = o_move.split()
    o_move = [int(o) for o in o_move]

    while not (0 <= o_move[0] - 1 <= 2 and 0 <= o_move[1] - 1 <= 2):
        print("Coordinates should be from 1 to 3!")
        o_move = input("Enter the coordinates: ")
        o_move = o_move.split()
        o_move = [int(o) for o in o_move]

    while M[o_move[0] - 1][o_move[1] - 1] == "X" or M[o_move[0] - 1][o_move[1] - 1] == "O":
        print("This cell is occupied! Choose another one!")
        o_move = input("Enter the coordinates: ")
        o_move = o_move.split()
        o_move = [int(o) for o in o_move]

    M[o_move[0] - 1][o_move[1] - 1] = "O"
    print('---------')
    print("|" + " " + M[0][0] + " " + M[0][1] + " " + M[0][2] + " " + "|")

    print("|" + " " + M[1][0] + " " + M[1][1] + " " + M[1][2] + " " + "|")

    print("|" + " " + M[2][0] + " " + M[2][1] + " " + M[2][2] + " " + "|")
    print('---------')
    num_x = 0
    num_o = 0
    num_space = 0
    for x in range(0, 3):
        for y in range(0, 3):
            if M[x][y] == "X":
                num_x += 1
            elif M[x][y] == "O":
                num_o += 1
            elif M[x][y] == "_" or M[x][y] == " ":
                num_space += 1

    firs_row_x, sec_row_x, third_row_x = 0, 0, 0
    firs_row_o, sec_row_o, third_row_o = 0, 0, 0
    firs_col_x, sec_col_x, third_col_x = 0, 0, 0
    firs_col_o, sec_col_o, third_col_o = 0, 0, 0
    for x in range(0, 3):
        if M[0][x] == "X":
            firs_row_x += 1
        if M[1][x] == "X":
            sec_row_x += 1
        if M[2][x] == "X":
            third_row_x += 1
        if M[0][x] == "O":
            firs_row_o += 1
        if M[1][x] == "O":
            sec_row_o += 1
        if M[2][x] == "O":
            third_row_o += 1
        if M[x][0] == "X":
            firs_col_x += 1
        if M[x][1] == "X":
            sec_col_x += 1
        if M[x][2] == "X":
            third_col_x += 1
        if M[x][0] == "O":
            firs_col_o += 1
        if M[x][1] == "O":
            sec_col_o += 1
        if M[x][2] == "O":
            third_col_o += 1

    diagonal_left_x, diagonal_right_x = 0, 0
    diagonal_left_o, diagonal_right_o = 0, 0

    if M[0][0] == "X" and M[1][1] == "X" and M[2][2] == "X":
        diagonal_left_x = 3
    if M[0][0] == "O" and M[1][1] == "O" and M[2][2] == "O":
        diagonal_left_o = 3
    if M[0][2] == "X" and M[1][1] == "X" and M[2][0] == "X":
        diagonal_right_x = 3
    if M[0][2] == "O" and M[1][1] == "O" and M[2][0] == "O":
        diagonal_right_o = 3

    M_wins_x = [[firs_row_x, sec_row_x, third_row_x, diagonal_left_x],
                [firs_col_x, sec_col_x, third_col_x, diagonal_right_x]]
    M_wins_o = [[firs_row_o, sec_row_o, third_row_o, diagonal_left_o],
                [firs_col_o, sec_col_o, third_col_o, diagonal_right_o]]
    x_win = 0
    o_win = 0

    for x in range(2):
        for y in range(4):
            if M_wins_x[x][y] == 3:
                x_win += 1
            if M_wins_o[x][y] == 3:
                o_win += 1

    if -1 <= num_x - num_o <= 1:
        if x_win == 1 and o_win != 1:
            print("X wins")
            break
        if o_win == 1 and x_win != 1:
            print("O wins")
            break
        if x_win >= 1 and o_win >= 1:
            print("Impossible")
            break
        if x_win == 0 and o_win == 0 and num_x + num_o != 9:
            print("Game not finished")
        if x_win == 0 and o_win == 0 and num_x + num_o == 9:
            print("Draw")
            break


# cells = raw_input("Enter cells: ")
# M = [[cells[0], cells[1], cells[2]],
#      [cells[3], cells[4], cells[5]],
#      [cells[6], cells[7], cells[8]]]
#
# print('---------')
# print("|" + " " + M[0][0] + " " + M[0][1] + " " + M[0][2] + " " + "|")
#
# print("|" + " " + M[1][0] + " " + M[1][1] + " " + M[1][2] + " " + "|")
#
# print("|" + " " + M[2][0] + " " + M[2][1] + " " + M[2][2] + " " + "|")
# print('---------')
# num_x = 0
# num_o = 0
# num_space = 0
# for x in range(0, 9):
#     if cells[x] == "X":
#         num_x += 1
#     elif cells[x] == "O":
#         num_o += 1
#     elif cells[x] == "_" or cells[x] == " ":
#         num_space += 1
#
# firs_row_x, sec_row_x, third_row_x = 0, 0, 0
# firs_row_o, sec_row_o, third_row_o = 0, 0, 0
# firs_col_x, sec_col_x, third_col_x = 0, 0, 0
# firs_col_o, sec_col_o, third_col_o = 0, 0, 0
# for x in range(0, 3):
#     if M[0][x] == "X":
#         firs_row_x += 1
#     if M[1][x] == "X":
#         sec_row_x += 1
#     if M[2][x] == "X":
#         third_row_x += 1
#     if M[0][x] == "O":
#         firs_row_o += 1
#     if M[1][x] == "O":
#         sec_row_o += 1
#     if M[2][x] == "O":
#         third_row_o += 1
#     if M[x][0] == "X":
#         firs_col_x += 1
#     if M[x][1] == "X":
#         sec_col_x += 1
#     if M[x][2] == "X":
#         third_col_x += 1
#     if M[x][0] == "O":
#         firs_col_o += 1
#     if M[x][1] == "O":
#         sec_col_o += 1
#     if M[x][2] == "O":
#         third_col_o += 1
#
# diagonal_left_x, diagonal_right_x = 0, 0
# diagonal_left_o, diagonal_right_o = 0, 0
#
# if cells[0] == "X" and cells[4] == "X" and cells[8] == "X":
#     diagonal_left_x = 3
# if cells[0] == "O" and cells[4] == "O" and cells[8] == "O":
#     diagonal_left_o = 3
# if cells[2] == "X" and cells[4] == "X" and cells[6] == "X":
#     diagonal_right_x = 3
# if cells[2] == "O" and cells[4] == "O" and cells[6] == "O":
#     diagonal_right_o = 3
#
# M_wins_x = [[firs_row_x, sec_row_x, third_row_x, diagonal_left_x],
#             [firs_col_x, sec_col_x, third_col_x, diagonal_right_x]]
# M_wins_o = [[firs_row_o, sec_row_o, third_row_o, diagonal_left_o],
#             [firs_col_o, sec_col_o, third_col_o, diagonal_right_o]]
# x_win = 0
# o_win = 0
#
# for x in range(2):
#     for y in range(4):
#         if M_wins_x[x][y] == 3:
#             x_win += 1
#         if M_wins_o[x][y] == 3:
#             o_win += 1
#
# if -1 <= num_x - num_o <= 1:
#     if x_win == 1 and o_win != 1:
#         print("X wins")
#     if o_win == 1 and x_win != 1:
#         print ("O wins")
#     if x_win >= 1 and o_win >= 1:
#         print("Impossible")
#     if x_win == 0 and o_win == 0 and num_x + num_o != 9:
#         print("Game not finished")
#     if x_win == 0 and o_win == 0 and num_x + num_o == 9:
#         print("Draw")
# else:
#     print("Impossible")
#
# x_move = raw_input("Enter the coordinates: ")
# x_move = x_move.split()
#
# while not (x_move[0].isdigit() and x_move[1].isdigit()):
#     print("You should enter numbers!")
#     x_move = raw_input("Enter the coordinates: ")
#     x_move = x_move.split()
# x_move = [int(x) for x in x_move]
#
# while not (0 <= x_move[0] - 1 <= 2 and 0 <= x_move[1] - 1 <= 2):
#     print("Coordinates should be from 1 to 3!")
#     x_move = raw_input("Enter the coordinates: ")
#     x_move = x_move.split()
#     x_move = [int(x) for x in x_move]
#
# while M[x_move[0] - 1][x_move[1] - 1] == "X" or M[x_move[0] - 1][x_move[1] - 1] == "O":
#     print("This cell is occupied! Choose another one!")
#     x_move = raw_input("Enter the coordinates: ")
#     x_move = x_move.split()
#     x_move = [int(x) for x in x_move]
#
# M[x_move[0] - 1][x_move[1] - 1] = "X"
# print('---------')
# print("|" + " " + M[0][0] + " " + M[0][1] + " " + M[0][2] + " " + "|")
#
# print("|" + " " + M[1][0] + " " + M[1][1] + " " + M[1][2] + " " + "|")
#
# print("|" + " " + M[2][0] + " " + M[2][1] + " " + M[2][2] + " " + "|")
# print('---------')
