import Piece

class Knight(Piece.Piece):
    def __init__(self,color,pos,board):
        self.name = "Knight"
        super().__init__(color,pos,board)
        self.moved = False
        self.options=[(-2,-1),(2,-1),(2,1),(-2,1),(-1,-2),(1,-2),(-1,2),(1,2)]
        self.possible_moves = self.gen_moves()


    def gen_moves(self):
        moves=[]
        for i in self.options:
            if -1 < i[0]+self.x < 8 and -1 < i[1]+self.y < 8:
                piece = self.board.cells[i[1]+self.y][i[0]+self.x].piece
                if piece != None:
                    if piece.color != self.color:
                        moves.append((i[0]+self.x,i[1]+self.y))
                else:
                    moves.append((i[0]+self.x,i[1]+self.y))
        return moves

    def create_moves(self):
        moves=[]
        for i in self.options:
            if -1 < i[0]+self.x < 8 and -1 < i[1]+self.y < 8:
                piece = self.board.cells[i[1]+self.y][i[0]+self.x].piece
                if piece != None:
                    if piece.color != self.color:
                        self.checker(i,moves)
                else:
                    self.checker(i,moves)
        return moves
