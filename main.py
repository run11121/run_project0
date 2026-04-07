game = [['*' for _ in range(3)] for _ in range(3)]

def print_game():
    for i in range(3):
        for j in range(3):
            print(game[i][j], end = " ")
        print()
    print()

def check(symbol):
    for i in range(3):
        if game[i][0] == symbol and game[i][1] == symbol and game[i][2] == symbol:
            return True
    for j in range(3):
        if game[0][j] == symbol and game[1][j] == symbol and game[2][j] == symbol:
            return True
    if game[0][0] == symbol and game[1][1] == symbol and game[2][2] == symbol:
        return True
    if game[0][2] == symbol and game[1][1] == symbol and game[2][0] == symbol:
        return True
    return False

check_win = False
count_moves = 0

while check_win == False and count_moves < 9:
    print_game()
    print("Ход Игрока 1 (+)")
    i = int(input("Введите строку (0-2): "))
    j = int(input("Введите столбец (0-2): "))

    if game[i][j] == "*":
        game[i][j] = "+"
        count_moves += 1
        check_win = check("+")
        if check_win == True:
            print_game()
            print("Игрок 1 победил!")
            break
    else:
        print("Занято, ход пропущен!")

    if count_moves == 9:
        break

    print_game()
    print("Ход Игрока 2 (0)")
    i = int(input("Введите строку (0-2): "))
    j = int(input("Введите столбец (0-2): "))

    if game[i][j] == "*":
        game[i][j] = "0"
        count_moves += 1
        check_win = check("0")
        if check_win == True:
            print_game()
            print("Игрок 2 победил!")
            break
    else:
        print("Занято, ход пропущен!")

if check_win == False and count_moves == 9:
    print_game()
    print("Ам ням")