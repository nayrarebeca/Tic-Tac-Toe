from jogo_da_velha import criarBoard, fazMovimento,  getInputValido, \
                            printBoard, verifywinner,  verificaMovimento

from minimax import movimentoIA

player = 0 # jogador 1
board = criarBoard()
winner = verifywinner(board)
while(not winner):
    printBoard(board)
    print("---------------")
    i = getInputValido("Choose line: ")
    j = getInputValido("Choose column: ")
    
    if(verificaMovimento(board, i, j)):
        fazMovimento(board, i, j, player)
        player = (player + 1)%2
    else:
        print("This position is already taken. Try again.")
    
    winner = verifywinner(board)

printBoard(board)
print("The winner is = ", winner)
print("_______________")