import pygame
import random
import Board
import Piece
from os import path,remove
import timer

WIDTH = 950
HEIGHT = 800
FPS = 30

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess")
clock = pygame.time.Clock()

def main():
    while True:
        try:
            white_time=int(input("How many seconds for white?: "))
            break
        except:
            print("Please enter a valid integer")
            continue

    while True:
        try:
            black_time=int(input("How many seconds for black?: "))
            break
        except:
            print("Please enter a valid integer")
            continue


    board = Board.Board((752,752),offset=(50,0),colorB=(87,25,7))

    running = True
    s=None
    colors = ["W","B"]
    white_moves=[]
    black_moves=[]
    white_timer=timer.Timer((board.width+50+board.offset[0],board.offset[1]+board.height-50),24,white_time)
    black_timer=timer.Timer((board.width+50+board.offset[0],board.offset[1]+50),24,black_time)
    c_w = FPS
    c_b = FPS
    while running:
        clock.tick(FPS)
        if board.turn==0:
            c_w-=1
            if c_w==0:
                c_w=FPS
                white_timer.update()
        else:
            c_b-=1
            if c_b==0:
                c_b=FPS
                black_timer.update()

        mp=pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:

                mp=pygame.mouse.get_pos()
                for row in board.cells:
                    for cell in row:
                        if cell.piece != None:
                            if (mp[0]-board.offset[0])//board.cell_width == cell.x and (mp[1]-board.offset[1])//board.cell_height == cell.y and cell.piece.color == colors[board.turn]:
                                cell.piece.isClicked=True
                                s=cell.piece

            if event.type == pygame.MOUSEBUTTONUP:
                if s!= None:
                    white_moves=[]
                    black_moves=[]
                    pos=(int((mp[0]-board.offset[0])//board.cell_width),int((mp[1]-board.offset[1])//board.cell_height))
                    if s.move(pos):
                        board.turn = (board.turn+1) % 2
                        for row in board.cells:
                            for cell in row:
                                if cell.piece != None:
                                    if cell.piece.color=="W":
                                        white_moves.append(len(cell.piece.create_moves()))
                                    elif cell.piece.color=="B":
                                        black_moves.append(len(cell.piece.create_moves()))
                    s=None

        if s != None:
            s.rect.center=mp

        if sum(white_moves)==0 and len(white_moves)!=0 or sum(black_moves)==0 and len(black_moves)!=0:
            if board.white_king.in_check():
                print("Black Wins")
                return
            elif board.black_king.in_check():
                print("White Wins")
                return
            else:
                print('Tie')
                return
        elif black_timer.time<=-1:
            print("White Wins")
            return

        elif white_timer.time<=-1:
            print("Black Wins")
            return


        screen.fill((15,15,15))
        board.draw(screen)
        white_timer.draw(screen)
        black_timer.draw(screen)
        pygame.display.flip()

    return

main()
