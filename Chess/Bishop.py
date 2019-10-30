import Piece

class Bishop(Piece.Piece):
    def __init__(self,color,pos,board):
        self.name = "Bishop"
        super().__init__(color,pos,board)
        self.moved = False
        self.options=[]
        for i in range(1,8):
            self.options.append((i,i))
            self.options.append((i,-i))
            self.options.append((-i,-i))
            self.options.append((-i,i))

        self.possible_moves = self.gen_moves()


    def gen_moves(self):
        moves=[]
        d_r=False
        u_l=False
        d_l=False
        u_r=False
        for i in self.options:
            if -1 < i[0]+self.x < 8 and -1 < i[1]+self.y < 8:
                if self.board.cells[i[1]+self.y][i[0]+self.x].piece == None:

                    if i[0] > 0 and i[1] > 0 and d_r==False:
                        moves.append((i[0]+self.x,i[1]+self.y))

                    elif i[0] < 0 and i[1] < 0 and u_l==False:
                        moves.append((i[0]+self.x,i[1]+self.y))

                    elif i[0] < 0 and i[1] > 0 and d_l==False:
                        moves.append((i[0]+self.x,i[1]+self.y))

                    elif i[0] > 0 and i[1] < 0 and u_r==False:
                        moves.append((i[0]+self.x,i[1]+self.y))

                else:
                    if i[0] > 0 and i[1] > 0 and d_r==False:
                        if self.board.cells[i[1]+self.y][i[0]+self.x].piece.color != self.color:
                            moves.append((i[0]+self.x,i[1]+self.y))
                        d_r=True

                    elif i[0] < 0 and i[1] < 0 and u_l==False:
                        if self.board.cells[i[1]+self.y][i[0]+self.x].piece.color != self.color:
                            moves.append((i[0]+self.x,i[1]+self.y))
                        u_l=True

                    elif i[0] < 0 and i[1] > 0 and d_l==False:
                        if self.board.cells[i[1]+self.y][i[0]+self.x].piece.color != self.color:
                            moves.append((i[0]+self.x,i[1]+self.y))
                        d_l=True

                    elif i[0] > 0 and i[1] < 0 and u_r==False:
                        if self.board.cells[i[1]+self.y][i[0]+self.x].piece.color != self.color:
                            moves.append((i[0]+self.x,i[1]+self.y))
                        u_r=True

        return moves

    def create_moves(self):
        moves=[]
        d_r=False
        u_l=False
        d_l=False
        u_r=False
        for i in self.options:
            if -1 < i[0]+self.x < 8 and -1 < i[1]+self.y < 8:
                if self.board.cells[i[1]+self.y][i[0]+self.x].piece == None:

                    if i[0] > 0 and i[1] > 0 and d_r==False:
                        self.checker(i,moves)

                    elif i[0] < 0 and i[1] < 0 and u_l==False:
                        self.checker(i,moves)

                    elif i[0] < 0 and i[1] > 0 and d_l==False:
                        self.checker(i,moves)

                    elif i[0] > 0 and i[1] < 0 and u_r==False:
                        self.checker(i,moves)

                else:
                    if i[0] > 0 and i[1] > 0 and d_r==False:
                        if self.board.cells[i[1]+self.y][i[0]+self.x].piece.color != self.color:
                            self.checker(i,moves)
                        d_r=True

                    elif i[0] < 0 and i[1] < 0 and u_l==False:
                        if self.board.cells[i[1]+self.y][i[0]+self.x].piece.color != self.color:
                            self.checker(i,moves)
                        u_l=True

                    elif i[0] < 0 and i[1] > 0 and d_l==False:
                        if self.board.cells[i[1]+self.y][i[0]+self.x].piece.color != self.color:
                            self.checker(i,moves)
                        d_l=True

                    elif i[0] > 0 and i[1] < 0 and u_r==False:
                        if self.board.cells[i[1]+self.y][i[0]+self.x].piece.color != self.color:
                            self.checker(i,moves)
                        u_r=True

        return moves
