import Piece
class Rook(Piece.Piece):
    def __init__(self,color,pos,board):
        self.name = "Rook"
        super().__init__(color,pos,board)
        self.moved = False
        self.options=[]
        for i in range(1,8):
            self.options.append((0,i))
            self.options.append((i,0))
            self.options.append((0,-i))
            self.options.append((-i,0))
        self.possible_moves = self.gen_moves()

    def gen_moves(self):
        moves=[]
        p_h=False
        n_h=False
        p_v=False
        n_v=False
        for i in self.options:
            if -1 < i[0]+self.x < 8 and -1 < i[1]+self.y < 8:
                if self.board.cells[i[1]+self.y][i[0]+self.x].piece == None:
                    if i[0] > 0 and p_h==False:
                        moves.append((i[0]+self.x,i[1]+self.y))
                    elif i[0] < 0 and n_h==False:
                        moves.append((i[0]+self.x,i[1]+self.y))
                    elif i[1] > 0 and p_v==False:
                        moves.append((i[0]+self.x,i[1]+self.y))
                    elif i[1] < 0 and n_v==False:
                        moves.append((i[0]+self.x,i[1]+self.y))

                else:
                    if i[0] > 0 and p_h==False:
                        if self.board.cells[i[1]+self.y][i[0]+self.x].piece.color != self.color:
                            moves.append((i[0]+self.x,i[1]+self.y))
                        p_h=True
                    elif i[0] < 0 and n_h==False:
                        if self.board.cells[i[1]+self.y][i[0]+self.x].piece.color != self.color:
                            moves.append((i[0]+self.x,i[1]+self.y))
                        n_h=True
                    elif i[1] > 0 and p_v==False:
                        if self.board.cells[i[1]+self.y][i[0]+self.x].piece.color != self.color:
                            moves.append((i[0]+self.x,i[1]+self.y))
                        p_v=True
                    elif i[1] < 0 and n_v==False:
                        if self.board.cells[i[1]+self.y][i[0]+self.x].piece.color != self.color:
                            moves.append((i[0]+self.x,i[1]+self.y))
                        n_v=True

        return moves

    def create_moves(self):
        moves=[]
        p_h=False
        n_h=False
        p_v=False
        n_v=False
        for i in self.options:
            if -1 < i[0]+self.x < 8 and -1 < i[1]+self.y < 8:
                if self.board.cells[i[1]+self.y][i[0]+self.x].piece == None:
                    if i[0] > 0 and p_h==False:
                        self.checker(i,moves)

                    elif i[0] < 0 and n_h==False:
                        self.checker(i,moves)

                    elif i[1] > 0 and p_v==False:
                        self.checker(i,moves)

                    elif i[1] < 0 and n_v==False:
                        self.checker(i,moves)

                else:
                    if i[0] > 0 and p_h==False:
                        if self.board.cells[i[1]+self.y][i[0]+self.x].piece.color != self.color:
                            self.checker(i,moves)

                            p_h=True
                    elif i[0] < 0 and n_h==False:
                        if self.board.cells[i[1]+self.y][i[0]+self.x].piece.color != self.color:
                            self.checker(i,moves)
                            n_h=True

                    elif i[1] > 0 and p_v==False:
                        if self.board.cells[i[1]+self.y][i[0]+self.x].piece.color != self.color:
                            self.checker(i,moves)
                            p_v=True
                    elif i[1] < 0 and n_v==False:
                        if self.board.cells[i[1]+self.y][i[0]+self.x].piece.color != self.color:
                            self.checker(i,moves)
                            n_v=True

        return moves
