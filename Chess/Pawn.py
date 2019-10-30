import Piece

class Pawn(Piece.Piece):
    def __init__(self,color,pos,board):
        self.name = "Pawn"
        super().__init__(color,pos,board)
        self.moved = False
        if self.color=="B":
            self.options=[(0,1),(0,2)]
        else:
            self.options=[(0,-1),(0,-2)]
        self.possible_moves = self.gen_moves()

    def gen_moves(self):
        moves=[]
        if self.moved and len(self.options)>1:
            self.options = self.options[:-1]

        for i in self.options:
            if -1 < i[0]+self.x < 8 and -1 < i[1]+self.y < 8:
                if self.board.cells[i[1]+self.y][i[0]+self.x].piece == None:
                    moves.append((i[0]+self.x,i[1]+self.y))
                else:
                    break

        if self.color=="B":
            if 1<=self.x<=6 and self.y<=6:
                if self.board.cells[self.y+1][self.x+1].piece != None:
                    if self.board.cells[self.y+1][self.x+1].piece.color != self.color:
                        moves.append((self.x+1,self.y+1))

                if self.board.cells[self.y+1][self.x-1].piece != None:
                    if self.board.cells[self.y+1][self.x-1].piece.color != self.color:
                        moves.append((self.x-1,self.y+1))

            elif self.x < 1 and self.y<=6:
                if self.board.cells[self.y+1][self.x+1].piece != None:
                    if self.board.cells[self.y+1][self.x+1].piece.color != self.color:
                        moves.append((self.x+1,self.y+1))
            elif self.x > 6 and self.y<=6:
                if self.board.cells[self.y+1][self.x-1].piece != None:
                    if self.board.cells[self.y+1][self.x-1].piece.color != self.color:
                        moves.append((self.x-1,self.y+1))

        else:
            if 1<=self.x<=6:
                if self.board.cells[self.y-1][self.x+1].piece != None:
                    if self.board.cells[self.y-1][self.x+1].piece.color != self.color:
                        moves.append((self.x+1,self.y-1))

                if self.board.cells[self.y-1][self.x-1].piece != None:
                    if self.board.cells[self.y-1][self.x-1].piece.color != self.color:
                        moves.append((self.x-1,self.y-1))

            elif self.x < 1:
                if self.board.cells[self.y-1][self.x+1].piece != None:
                    if self.board.cells[self.y-1][self.x+1].piece.color != self.color:
                        moves.append((self.x+1,self.y-1))
            elif self.x > 6:
                if self.board.cells[self.y-1][self.x-1].piece != None:
                    if self.board.cells[self.y-1][self.x-1].piece.color != self.color:
                        moves.append((self.x-1,self.y-1))

        return moves

    def create_moves(self):
        moves=[]
        if self.moved and len(self.options)>1:
            self.options = self.options[:-1]

        for i in self.options:
            if -1 < i[0]+self.x < 8 and -1 < i[1]+self.y < 8:
                piece = self.board.cells[i[1]+self.y][i[0]+self.x].piece
                if piece == None:
                    self.checker(i,moves)
                else:
                    break

        if self.color=="B":
            if self.board.last_move!=None:
                if self.board.last_move.color=="W":
                    if self.board.last_move.x-self.x==1 and self.board.last_move.y-self.y==0:
                        self.checker((1,1),moves)
                    elif self.board.last_move.x-self.x==-1 and self.board.last_move.y-self.y==0:
                        self.checker((-1,1),moves)
            if 1<=self.x<=6:
                piece = self.board.cells[self.y+1][self.x+1].piece
                if piece != None:
                    if piece.color != self.color:
                        self.checker((1,1),moves)

                piece = self.board.cells[self.y+1][self.x-1].piece
                if piece != None:
                    if piece.color != self.color:
                        self.checker((-1,1),moves)

            elif self.x < 1:
                piece = self.board.cells[self.y+1][self.x+1].piece
                if piece != None:
                    if piece.color != self.color:
                        self.checker((1,1),moves)

            elif self.x > 6:
                piece = self.board.cells[self.y+1][self.x-1].piece
                if piece != None:
                    if piece.color != self.color:
                        self.checker((-1,1),moves)

        else:
            if self.board.last_move!=None:
                if self.board.last_move.color=="B":
                    if self.board.last_move.x-self.x==1 and self.board.last_move.y-self.y==0:
                        self.checker((1,-1),moves)
                    elif self.board.last_move.x-self.x==-1 and self.board.last_move.y-self.y==0:
                        self.checker((-1,-1),moves)
            if 1<=self.x<=6:
                piece = self.board.cells[self.y-1][self.x+1].piece
                if piece != None:
                    if piece.color != self.color:
                        self.checker((1,-1),moves)

                piece = self.board.cells[self.y-1][self.x-1].piece
                if piece != None:
                    if piece.color != self.color:
                        self.checker((-1,-1),moves)

            elif self.x < 1:
                piece = self.board.cells[self.y-1][self.x+1].piece
                if piece != None:
                    if piece.color != self.color:
                        self.checker((1,-1),moves)

            elif self.x > 6:
                piece = self.board.cells[self.y-1][self.x-1].piece
                if piece != None:
                    if piece.color != self.color:
                        self.checker((-1,-1),moves)

        return moves
