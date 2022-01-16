from jogo_da_velha import blank, token, verifywinner

def movimentoIA(board, player):
    possibilidades = getPosicoes(board)
    melhor_valor = None
    melhor_movimento = None
    for possibilidade in possibilidades:
        board[possibilidade[0]][possibilidade[1]] = token[player]
        valor = minimax(board, player)
        board[possibilidade[0]][possibilidade[1]] = blank
        if(melhor_valor is None):
            melhor_valor = valor
            melhor_movimento = possibilidade
        elif(player == 0):
            if(valor > melhor_valor):
                melhor_valor = valor
                melhor_movimento = possibilidade
        elif(player == 1):
            if(valor < melhor_valor):
                melhor_valor = valor
                melhor_movimento = possibilidade

    return melhor_movimento[0], melhor_movimento[1]

def getPosicoes(board):
    posicoes = []
    for i in range(3):
        for j in range(3):
            if(board[i][j] == blank):
                posicoes.append([i, j])
    
    return posicoes

score = {
    "EMPATE": 0,
    "X": 1,
    "O": -1
}

def minimax(board, player):
    winner = verifywinner(board)
    if(winner):
        return score[winner]
    player = (player + 1)%2
    
    possibilidades = getPosicoes(board)
    melhor_valor = None
    for possibilidade in possibilidades:
        board[possibilidade[0]][possibilidade[1]] = token[player]
        valor = minimax(board, player)
        board[possibilidade[0]][possibilidade[1]] = blank

        if(melhor_valor is None):
            melhor_valor = valor
        elif(player == 0):
            if(valor > melhor_valor):
                melhor_valor = valor
        elif(player == 1):
            if(valor < melhor_valor):
                melhor_valor = valor

    return melhor_valor