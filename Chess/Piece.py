import pygame
from os import path,remove

pieces_dir = path.join(path.dirname(__file__), 'Pieces')

def resize(img,size):
    return pygame.transform.scale(img,(int(size[0]),int(size[1])))

class Piece():
    def __init__(self,color,pos,board):
        self.color=color
        self.x,self.y=pos
        self.pos=pos
        self.isClicked=False
        self.board=board
        img = pygame.image.load(path.join(pieces_dir, self.name+self.color+".png"))
        self.img = resize(img,(self.board.cell_width,self.board.cell_height))
        self.rect=self.img.get_rect()
        self.rect.center=(self.x*self.board.cell_width+self.board.cell_width/2+self.board.offset[0],self.y*self.board.cell_height+self.board.cell_height/2+self.board.offset[1])

    def draw(self,screen):
        screen.blit(self.img,self.rect)

    def checker(self,pos,lst):
        sp = self.board.cells[self.y+pos[1]][self.x+pos[0]].piece
        self.transfer((self.x+pos[0],self.y+pos[1]))
        if (self.board.black_king.in_check() and self.color=="B") or (self.board.white_king.in_check()and self.color=="W"):
            self.transfer((self.x-pos[0],self.y-pos[1]),sp)
            return False
        else:
            self.transfer((self.x-pos[0],self.y-pos[1]),sp)
            if lst!=None:
                lst.append((pos[0]+self.x,pos[1]+self.y))
            else:
                return True

    def mover(self,pos):
        self.isClicked = False
        self.board.cells[self.y][self.x].piece=None
        self.board.cells[pos[1]][pos[0]].piece=self
        self.x,self.y = pos
        self.rect.center=(self.x*self.board.cell_width+self.board.cell_width/2+self.board.offset[0],self.y*self.board.cell_height+self.board.cell_height/2+self.board.offset[1])
        self.moved = True


    def move(self,pos):
        self.possible_moves=self.create_moves()

        if pos in self.possible_moves:
            if self.name == "Pawn":

                if pos[0]-self.x==1 and pos[1]-self.y==1:
                    if self.board.cells[self.y+1][self.x+1].piece==None:
                        self.board.cells[self.y][self.x+1].piece = None

                elif pos[0]-self.x==-1 and pos[1]-self.y==1:
                    if self.board.cells[self.y+1][self.x-1].piece==None:
                        self.board.cells[self.y][self.x-1].piece = None

                elif pos[0]-self.x==1 and pos[1]-self.y==-1:
                    if self.board.cells[self.y-1][self.x+1].piece==None:
                        self.board.cells[self.y][self.x+1].piece = None

                elif pos[0]-self.x==-1 and pos[1]-self.y==-1:
                    if self.board.cells[self.y-1][self.x-1].piece==None:
                        self.board.cells[self.y][self.x-1].piece = None

                if abs(pos[1]-self.y)==2:
                    self.mover(pos)
                    self.board.last_move = self
                else:
                    self.mover(pos)
                    self.board.last_move = None

                if self.y==0 or self.y==7:
                    while True:
                        try:
                            piece = input('What piece?: ')
                            piece=piece[0].upper()+piece[1:].lower()
                            self.board.piece_creator(piece,self.color,(self.x,self.y))
                            break
                        except:
                            print('Not a valid piece')
                            continue

            elif self.name=="King" and abs(pos[0]-self.x)==2:
                if pos[0]-self.x==2:
                    self.mover(pos)
                    self.board.cells[self.y][7].piece.mover((pos[0]-1,self.y))
                elif pos[0]-self.x==-2:
                    self.mover(pos)
                    self.board.cells[self.y][0].piece.mover((pos[0]+1,self.y))

            else:
                self.mover(pos)
            return True
        else:
            self.isClicked = False
            self.rect.center=(self.x*self.board.cell_width+self.board.cell_width/2+self.board.offset[0],self.y*self.board.cell_height+self.board.cell_height/2+self.board.offset[1])
            return False


    def transfer(self,pos,sp=None):
        self.board.cells[self.y][self.x].piece=sp
        self.board.cells[pos[1]][pos[0]].piece=self
        self.x,self.y = pos[0],pos[1]
        self.pos = pos
        self.rect.center=(self.x*self.board.cell_width+self.board.cell_width/2+self.board.offset[0],self.y*self.board.cell_height+self.board.cell_height/2+self.board.offset[1])
        for row in self.board.cells:
            for cell in row:
                if cell.piece != None:
                    cell.piece.possible_moves = cell.piece.gen_moves()
