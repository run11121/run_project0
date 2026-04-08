# Создаем два поля 10x10, заполненные водой '~'
# Поле игрока 1 и поле игрока 2
board1 = [['~'] * 10 for _ in range(10)]
board2 = [['~'] * 10 for _ in range(10)]


# Функция для вывода поля (чтобы не копировать код дважды)
# show_board - показать доску, hide - скрыть корабли соперника (заменить ■ на ~)
def print_board(board, hide_ships=False):
    print("   1 2 3 4 5 6 7 8 9 10")  # Нумерация столбцов
    for i in range(10):
        print(i + 1, end=" ")  # Нумерация строк
        for j in range(10):
            cell = board[i][j]
            if hide_ships and cell == '■':
                print('~', end=" ")  # Скрываем корабль
            else:
                print(cell, end=" ")
        print()
    print()


# --- ЭТАП 1: РАССТАНОВКА КОРАБЛЕЙ ---
print("=== РАССТАНОВКА КОРАБЛЕЙ ===")
print("Каждый игрок ставит 3 корабля (размером 1 клетка).")
print("Вводите координаты от 1 до 10.")

# Расстановка для Игрока 1
print("\n--- Игрок 1, расставь свои 3 корабля ---")
ships_p1 = 0
while ships_p1 < 3:
    print_board(board1)
    r = int(input(f"Корабль {ships_p1 + 1}. Строка: ")) - 1
    c = int(input(f"Корабль {ships_p1 + 1}. Столбец: ")) - 1

    if 0 <= r <= 9 and 0 <= c <= 9:
        if board1[r][c] == '~':
            board1[r][c] = '■'
            ships_p1 += 1
        else:
            print("Тут уже стоит корабль! Выбери другую клетку.")
    else:
        print("Координаты вне поля (1-10)!")

# Очистка экрана (просто много пустых строк, чтобы Игрок 2 не видел расстановку Игрока 1)
print("\n" * 50)
print("Передайте ход Игроку 2!")
input("Нажмите Enter, когда Игрок 2 будет готов...")

# Расстановка для Игрока 2
print("\n--- Игрок 2, расставь свои 3 корабля ---")
ships_p2 = 0
while ships_p2 < 3:
    print_board(board2)
    r = int(input(f"Корабль {ships_p2 + 1}. Строка: ")) - 1
    c = int(input(f"Корабль {ships_p2 + 1}. Столбец: ")) - 1

    if 0 <= r <= 9 and 0 <= c <= 9:
        if board2[r][c] == '~':
            board2[r][c] = '■'
            ships_p2 += 1
        else:
            print("Тут уже стоит корабль! Выбери другую клетку.")
    else:
        print("Координаты вне поля (1-10)!")

print("\n" * 50)
print("=== НАЧАЛО БОЯ ===")

# Счетчики попаданий
hits_p1 = 0  # Сколько Игрок 1 попал по Игроку 2
hits_p2 = 0  # Сколько Игрок 2 попал по Игроку 1
total_ships = 3

# --- ЭТАП 2: БОЙ ---
current_player = 1  # Ходит первый

while True:
    print("\n" * 2)
    if current_player == 1:
        print("--- ХОД ИГРОКА 1 ---")
        print("Поле противника (Игрок 2):")
        print_board(board2, hide_ships=True)  # Скрываем корабли врага

        r = int(input("Строка выстрела: ")) - 1
        c = int(input("Столбец выстрела: ")) - 1

        if 0 <= r <= 9 and 0 <= c <= 9:
            target = board2[r][c]
            if target == 'X' or target == 'T':
                print("Ты уже стрелял сюда! Ход переходит.")
                current_player = 2
            elif target == '■':
                print(">>> ПОПАДАНИЕ! <<<")
                board2[r][c] = 'X'  # Метка попадания
                hits_p1 += 1

                current_player = 2
            elif target == '~':
                print(">>> МИМО. <<<")
                board2[r][c] = 'T'  # Метка промаха
                current_player = 2
        else:
            print("Мимо поля! Ход переходит.")
            current_player = 2

    else:  # Ход Игрока 2
        print("--- ХОД ИГРОКА 2 ---")
        print("Поле противника (Игрок 1):")
        print_board(board1, hide_ships=True)

        r = int(input("Строка выстрела: ")) - 1
        c = int(input("Столбец выстрела: ")) - 1

        if 0 <= r <= 9 and 0 <= c <= 9:
            target = board1[r][c]
            if target == 'X' or target == 'T':
                print("Ты уже стрелял сюда! Ход переходит.")
                current_player = 1
            elif target == '■':
                print(">>> ПОПАДАНИЕ! <<<")
                board1[r][c] = 'X'
                hits_p2 += 1
                current_player = 1
            elif target == '~':
                print(">>> МИМО. <<<")
                board1[r][c] = 'T'
                current_player = 1
        else:
            print("Мимо поля! Ход переходит.")
            current_player = 1

    # Проверка победы
    if hits_p1 == total_ships:
        print("\n🎉 ПОБЕДА ИГРОКА 1! Все корабли противника потоплены!")
        break
    if hits_p2 == total_ships:
        print("\n🎉 ПОБЕДА ИГРОКА 2! Все корабли противника потоплены!")
        break

print("Игра окончена.")