import pygame
import Bishop,King,Knight,Pawn,Queen,Rook,Piece


font = pygame.font.match_font("Arial")
def draw_text(surf, text, size, x, y, font, color=(0,0,0)):
    font = pygame.font.Font(font, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x,y)
    surf.blit(text_surface, text_rect)

class Cell():
    def __init__(self,color,rect,offset,piece=None):
        self.color = color
        self.x=rect[0]
        self.y=rect[1]
        self.width=rect[2]
        self.height=rect[3]
        self.posx=self.x*self.width+offset[0]
        self.posy=self.y*self.height+offset[1]
        self.rect=[self.posx,self.posy,self.width,self.height]
        self.piece=piece
        self.offset=offset

    def draw(self,screen):
        pygame.draw.rect(screen,self.color,self.rect)


class Board():
    def __init__(self,size,offset,colorA=(255,255,255),colorB=(0,0,0)):
        self.colorA=colorA
        self.colorB=colorB
        self.width,self.height=size
        self.cell_width=self.width/8
        self.cell_height=self.height/8
        c=self.colorA
        self.cells=[]
        colors = [self.colorA,self.colorB]
        self.turn=0
        self.last_move = None
        self.offset=offset
        r = 0
        for y in range(8):
            t=[]
            c=colors[(r+1)%2]
            r+=1
            for x in range(8):
                c=colors[(r+1)%2]
                r+=1
                t.append(Cell(c,(x,y,self.cell_width,self.cell_height),self.offset))
            self.cells.append(t)

        #-----------------------------------------------------------------------------------#
        lst=[("Rook","B",(0,0)),("Rook","B",(7,0)),("Bishop","B",(2,0)),("Bishop","B",(5,0)),
            ("Knight","B",(6,0)),("Knight","B",(1,0)),("Queen","B",(3,0)),("King","B",(4,0))]
        for i in range(8):
            lst.append(("Pawn","B",(i,1)))
        for i in range(8):
            lst.append(("Pawn","W",(i,6)))

        for i in lst[:8]:
            lst.append((i[0],"W",(i[2][0],7)))
        self.board_setup(lst)
        #-----------------------------------------------------------------------------------#
        for row in self.cells:
            for cell in row:
                if cell.piece!=None:
                    cell.piece.possible_moves = cell.piece.gen_moves()
        self.black_king = self.cells[0][4].piece
        self.white_king = self.cells[7][4].piece

    def piece_creator(self,p,color,pos):
        pieces = {"Bishop" : Bishop.Bishop,"Pawn" : Pawn.Pawn,"Rook" : Rook.Rook, "Knight" : Knight.Knight, "Queen" : Queen.Queen, "King" : King.King}
        self.cells[pos[1]][pos[0]].piece = pieces[p](color,pos,self)

    def board_setup(self,lst):
        for i in lst:
            self.piece_creator(i[0],i[1],i[2])



    def draw(self,screen):
        pygame.draw.rect(screen,self.colorB,(self.offset[0]-3,self.offset[1]-3,self.width+6,self.height+6),7)
        for i in range(8):
            draw_text(screen, chr(65+i), 18, self.offset[0]+self.cell_width*i+self.cell_width/2, self.offset[1]+self.height+10, font, (0,255,255))
            draw_text(screen, str(8-i), 18,self.offset[0]-25, self.offset[1]+self.cell_height*i+self.cell_height/2,font,(0,255,255))
            
        for row in self.cells:
            for cell in row:
                cell.draw(screen)

        for row in self.cells:
            for cell in row:
                if cell.piece != None:
                    cell.piece.draw(screen)
