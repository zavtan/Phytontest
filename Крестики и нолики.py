# Крестики - нолики
# Компьютер играет в крестики нолики против пользователя
# Глобальные константы

X = 'X'  # сокращенное значение для крестика
O = 'O'  # сокращенное значение для нолика
EMPTY = " "  # пустое поле на игровой доске
TIE = "Ничья"  # состояние ничьей
NUM_SQUARES = 9  # количество полей на доске "Крестиков-ноликов"


def display_instruct():
    """Выводит на экран инструкцию для игрока"""
    print(
        """Добро пожаловать в игру.
        Чтобы сделать ход, введи число от 0 до 8. Числа соответствуют полям доски
        как показано ниже:
        0 | 1 | 2
        ---------
        3 | 4 | 5
        ---------
        6 | 7 | 8
        Начнем игру.\n   """
    )


# Функция задает вопрос "Да" или "Нет", и возвращает "y" или "n". Для выбора хода.
def ask_yes_no(question):
    """Задает вопрос с ответом 'Да' или 'Нет'."""
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response


# Функция запрашивает о вводе числа, лежащего в заданном диапазоне и возвращает число из этого диапазона.
def ask_number(question, low, high):
    """Просит ввести число из диапазона."""
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response


# Функция спрашивает пользователя, желает ли тот оставить первый ход за собой,
# и определяет типы фишек компьютера и игрока.
def pieces():
    """Определяет принадлежность первого хода."""
    go_first = ask_yes_no("Хочешь оставить первый ход за собой? (y или n): ")
    if go_first == "y":
        print("\nХорошо: играй крестиками.")
        human = X
        computer = O
    else:
        print("\nБуду начинать Я.")
        computer = X
        human = O
    return computer, human


# Функция создает новую игровую доску.
def new_board():
    """Создает новую игровую доску"""
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board


# Функция выводит на экран переданную доску.
def display_board(board):
    """Отображает игровую доску на экране"""
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "---------")
    print("\n\t", board[3], "|", board[4], "|", board[5])
    print("\t", "---------")
    print("\n\t", board[6], "|", board[7], "|", board[8], "\n")


# Функция принимает доску и возвращает список доступных ходов.
def legal_moves(board):
    """Создает список доступных ходов"""
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves


# Функция определяет победителя игры
def winner(board):
    """Определяет победителя игры"""
    WAYS_TO_WIN = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (2, 4, 6))
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
        if EMPTY not in board:
            return TIE
    return None


# Функция принимает доску и тип фишек игрока, возвращает номер поля на котором помещена фишка.
def human_move(board, human):
    """Получает ход человека"""
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("Твой ход. Выбери одно из полей (0 - 8):", 0, NUM_SQUARES)
        if move not in legal:
            print("\nЭто поле уже занято. Выбери другое.\n")
        print("Хорошо")
        return move


# Функция принимает доску, тип фишек компьютера и тип фишек игрока, а возвращает ход компьютера.
def computer_move(board, computer, human):
    """Делает ход за игрока."""
    # Создает рабочую копию доски, функция будет менять некоторое значение в списке.
    board = board[:]
    # поля от лучшего к худшему
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    print("Я выберу поле номер", end=" ")
    # создаем список доступных ходов компьютера и проверяем может он выиграть или нет.
    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        board[move] = EMPTY  # выполнив проверку отменим изменения.
    # проверяем не может ли игрок выиграть на следующем ходу.
    for move in legal_moves(board):
        board[move] = human
        # если следующим ходом может победить игрок блокируем этот ход.
        if winner(board) == human:
            print(move)
            return move
        board[move] = EMPTY  # выполнив проверку отменим изменения.

    # Поскольку следующим ходом ни одна сторона не может победить,
    # выберем лучшее из доступных полей.
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move


# Функция принимает тип фишки, которой был сделан последний на данный момент ход.
def next_turn(turn):  # turn принимает значение Х или О и показывает чей был последний ход.
    """Осуществляет переход хода"""
    if turn == X:
        return O
    else:
        return X


# Функция принимает тип фишек победителя игры.
def congrat_winner(the_winner, computer, human):
    """Поздравляет победителя игры"""
    if the_winner != TIE:
        print("Три", the_winner, "в ряд!\n")
    else:
        print("Ничья!\n")
    if the_winner == computer:
        print("Победила машина\n")
    elif the_winner == human:
        print("Победил игрок\n")
    elif the_winner == TIE:
        print("Победила дружба\n")


# Основная часть
def main():
    display_instruct()
    computer, human = pieces()
    turn = X
    board = new_board()
    display_board(board)
    while not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)
    the_winner = winner(board)
    congrat_winner(the_winner, computer, human)


# запуск программы
main()
input("\n\n Нажмите Enter, что-бы выйти.")
