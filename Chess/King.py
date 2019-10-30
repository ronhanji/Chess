import Piece

class King(Piece.Piece):
    def __init__(self,color,pos,board):
        self.name = "King"
        super().__init__(color,pos,board)
        self.moved = False
        self.options=[(0,1),(0,-1),(1,0),(-1,0),(-1,1),(-1,-1),(1,1),(1,-1)]
        self.possible_moves = self.gen_moves()

    def gen_moves(self):
        moves=[]
        for i in self.options:
            if -1 < i[0]+self.x < 8 and -1 < i[1]+self.y < 8:
                piece = self.board.cells[i[1]+self.y][i[0]+self.x].piece
                if (piece != None and piece.color != self.color) or piece==None:
                    moves.append((i[0]+self.x,i[1]+self.y))
        return moves

    def in_check(self):
        for row in self.board.cells:
            for cell in row:
                if cell.piece!=None:
                    for move in cell.piece.possible_moves:
                        if move == self.pos and cell.piece.color!=self.color:
                            return True

        return False

    def create_moves(self):
        moves=[]
        if not self.moved:
            if self.board.cells[self.y][0].piece!=None:
                if not self.board.cells[self.y][0].piece.moved:
                    l= self.checker((0,0),None) and self.checker((-1,0),None) and self.checker((-2,0),None)
                    if l:
                        moves.append((self.x-2,self.y))

            if self.board.cells[self.y][7].piece!=None:
                if not self.board.cells[self.y][7].piece.moved:
                    l = self.checker((0,0),None) and self.checker((1,0),None) and self.checker((2,0),None)
                    if l:
                        moves.append((self.x+2,self.y))

        for i in self.options:
            if -1 < i[0]+self.x < 8 and -1 < i[1]+self.y < 8:
                piece = self.board.cells[i[1]+self.y][i[0]+self.x].piece
                if (piece != None and piece.color != self.color) or piece==None:
                    self.checker(i,moves)
        return moves
