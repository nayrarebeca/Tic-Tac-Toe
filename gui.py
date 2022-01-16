import pygame

from jogo_da_velha import criarBoard, fazMovimento,  getInputValido, \
                            printBoard, verifywinner,  verificaMovimento

from minimax import movimentoIA

pygame.font.init()


def draw_board(win, board):
    height = 600
    width = 600
    tamanho = 600/3

    for i in range(1, 3):
        pygame.draw.line(win, (0, 0 ,0), (0, i *  tamanho), (width, i * tamanho), 3)
        pygame.draw.line(win, (0, 0 ,0), (i * tamanho, 0), (i * tamanho, height), 3)

    for i in range(3):
        for j in range(3):
            font = pygame.font.SysFont("comicsans", 100)

            x = j * tamanho
            y = i * tamanho

            text = font.render(board[i][j], 1, (128, 0, 0))
            win.blit(text, ((x + 75), (y + 75)))


def redraw_window(win, board):
    win.fill((255, 255, 255))
    draw_board(win, board)

def main():
    win = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Tic-Tac-Toe")

    board = criarBoard()

    redraw_window(win, board)
    pygame.display.update()

    player = 0
    winner = verifywinner(board)
    
    while(not winner):
        printBoard(board)
        if(player == 0):
            played = False
            while(not played):
                for event in pygame.event.get():
                    if(event.type == pygame.QUIT):
                        return
                    elif(event.type == pygame.MOUSEBUTTONUP):
                        pos = pygame.mouse.get_pos()
                        i = int(pos[1]/200)
                        j = int(pos[0]/200)
                        played = True
        else:
            i,j = movimentoIA(board, player)
        
        if(verificaMovimento(board, i, j)):
            fazMovimento(board, i, j, player)
            player = (player + 1)%2
        
        winner = verifywinner(board)
        redraw_window(win, board)
        pygame.display.update()

    while(True):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                return

main()
