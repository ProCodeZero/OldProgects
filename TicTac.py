import random


def drawBoard(board):
    # Эта функция выводит на экран игровое поле, клетки которого будут заполняться.
    # board - это список из 10 строк, для прорисовки игрового поля (индекс 0 игнорируется).
    print(board[7] + '|' + board[8] + '|' + board[8])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])


def inputPlayerLetter():
    # Игрок выбирает букву.
    # Возвращает список, в котором буква игрока - первый элемент, а буква компьютера - второй.
    letter = ''
    while not (letter == 'x' or letter == 'o'):
        print('Choose "X" or "O"')
        letter = input().upper()

        # Первым элементом списка является буква игрока, вторым - буква компьютера.
        if letter == 'X':
            return ['X', 'O']
        else:
            return ['O', 'X']


def whoGoesFirst():
    # Выбор, кто ходит первым через рандом.
    if random.randint(0, 1) == 0:
        return 'Компьютер'
    else:
        return 'Человек'


def makeMove(board, letter, move):
    board[move] = letter


def isWinner(board, letter):
    # Эта функция проверяет игровое поле и возвращает True, если игрок выиграл.
    return ((board[7] == letter and board[8] == letter and board[9] == letter) or
            (board[4] == letter and board[5] == letter and board[6] == letter) or
            (board[1] == letter and board[2] == letter and board[3] == letter) or
            (board[7] == letter and board[4] == letter and board[1] == letter) or
            (board[8] == letter and board[5] == letter and board[2] == letter) or
            (board[9] == letter and board[6] == letter and board[3] == letter) or
            (board[7] == letter and board[5] == letter and board[3] == letter) or
            (board[9] == letter and board[5] == letter and board[1] == letter))


def getBoardCopy(board):
    # Создает копию игрового поля и возвращает его.
    boardCopy = []
    for i in board:
        boardCopy.append(i)
        return boardCopy


def isSpaceFree(board, move):
    # Возвращает True, если сделан ход в свободную клетку.
    return board[move] == ' '


def getPlayerMove(board):
    # Разрешение игроку сделать ход.
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('Ваш следующий ход? (1-9)')
        move = input()
    return int(move)


def chooseRandomMoveFromList(board, movesList):
    # Возвращает допустимый ход, учитывая список сделанных ходов и список заплненных клеток.
    # Возвращает значение None, если нет допустимых ходов.
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

        if len(possibleMoves) != 0:
            return random.choice(possibleMoves)
        else:
            return None


def getComputerMove(board, computerLetter):
    # Учитывая заполнение игрового поля и букву компьютера, определяет допустимый ход и возвращает его.
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    # Алгоритм для ИИ:
    # Проверка - победим ли мы, сделав следующий ход.
    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, computerLetter, i)
            if isWinner(boardCopy, computerLetter):
                return i

    # Проверяем - победит ли игрок, сделав следующий ход, и блокируем его.
    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, playerLetter, i)
            if isWinner(boardCopy, playerLetter):
                return i

    # Пробуем занять один из углов, если есть свободные.
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move is not None:
        return move

    # Пробуем занять центр, если он свободен.
    if isSpaceFree(board, 5):
        return 5

    # Делаем ход по одной стороне.
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])


def isBoardFull(board):
    # Возвращает True, если клетка на игровом поле занята. В противном случае, возвращает False.
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True


print('Игра "Крестики-нолики"')

while True:
    # Перезагрузка игрового поля
    theBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('' + turn + ' ходит первым.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'Человек':
            # Ход игрока.
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('Ура! Вы выиграли!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('Ничья!')
                    break
                else:
                    turn = 'Компьютер'

        else:
            # Ход компьютера
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('Компьютер победил! Вы проиграли.')
                gameIsPlaying = False

            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('Ничья')
                    break
                else:
                    turn = 'Человек'

    print('Сыграем еще раз? (да или нет)')
    if not input().lower().startswith('д'):
        break
