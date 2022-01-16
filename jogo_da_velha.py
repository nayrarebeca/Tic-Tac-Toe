blank = " "
token = ["X", "O"]

def criarBoard():
    board = [
        [blank, blank, blank],
        [blank, blank, blank],
        [blank, blank, blank],
    ]
    return board


def printBoard(board):
    for i in range(3):
        print("|".join(board[i]))
        if(i < 2):
            print("------")


def getInputValido(message):
    try:
        n = int(input(message))
        if(n >= 1 and n <= 3):
            return n - 1
        else:
            print("The number needs to be between 1-3")
            return getInputValido(message)
    except:
        print("Not a valid number. Try again.")
        return getInputValido(message)


def verificaMovimento(board, i , j):
    if(board[i][j] == blank):
        return True
    else:
        return False


def fazMovimento(board, i, j, player):
    board[i][j] = token[player]


def verifywinner(board):
    # line 
    for i in range(3):
        if(board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] != blank):
            return board[i][0]
    
    # column
    for i in range(3):
        if(board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] != blank):
            return board[0][i]

    # main diagonal
    if(board[0][0] != blank and board[0][0] == board[1][1] and board[1][1] == board[2][2]):
        return board[0][0]

    # secondary diagonal
    if(board[0][2] != blank and board[0][2] == board[1][1] and board[1][1] == board[2][0]):
        return board[0][2]

    for i in range(3):
        for j in range(3):
            if(board[i][j] == blank):
                return False

    return "Nice! It's a tie! "
