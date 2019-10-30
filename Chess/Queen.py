import Piece

class Queen(Piece.Piece):
    def __init__(self,color,pos,board):
        self.name = "Queen"
        super().__init__(color,pos,board)
        self.moved = False
        self.options=[]
        for i in range(1,8):
            self.options.append((i,i))
            self.options.append((i,-i))
            self.options.append((-i,-i))
            self.options.append((-i,i))
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
        d_r=False
        u_l=False
        d_l=False
        u_r=False

        for i in self.options:
            if -1 < i[0]+self.x < 8 and -1 < i[1]+self.y < 8:
                if self.board.cells[i[1]+self.y][i[0]+self.x].piece == None:
                    if i[0] > 0 and i[1]==0 and p_h==False:
                        moves.append((i[0]+self.x,i[1]+self.y))

                    elif i[0] < 0 and i[1]==0 and n_h==False:
                        moves.append((i[0]+self.x,i[1]+self.y))

                    elif i[1] > 0 and i[0]==0 and p_v==False:
                        moves.append((i[0]+self.x,i[1]+self.y))

                    elif i[1] < 0 and i[0]==0 and n_v==False:
                        moves.append((i[0]+self.x,i[1]+self.y))

                    elif i[0] > 0 and i[1] > 0 and d_r==False:
                        moves.append((i[0]+self.x,i[1]+self.y))

                    elif i[0] < 0 and i[1] < 0 and u_l==False:
                        moves.append((i[0]+self.x,i[1]+self.y))

                    elif i[0] < 0 and i[1] > 0 and d_l==False:
                        moves.append((i[0]+self.x,i[1]+self.y))

                    elif i[0] > 0 and i[1] < 0 and u_r==False:
                        moves.append((i[0]+self.x,i[1]+self.y))

                else:
                    if i[0] > 0 and i[1]==0 and p_h==False:
                        if self.board.cells[i[1]+self.y][i[0]+self.x].piece.color != self.color:
                            moves.append((i[0]+self.x,i[1]+self.y))
                        p_h=True

                    elif i[0] < 0 and i[1]==0 and n_h==False:
                        if self.board.cells[i[1]+self.y][i[0]+self.x].piece.color != self.color:
                            moves.append((i[0]+self.x,i[1]+self.y))
                        n_h=True

                    elif i[1] > 0 and i[0]==0 and p_v==False:
                        if self.board.cells[i[1]+self.y][i[0]+self.x].piece.color != self.color:
                            moves.append((i[0]+self.x,i[1]+self.y))
                        p_v=True

                    elif i[1] < 0 and i[0]==0 and n_v==False:
                        if self.board.cells[i[1]+self.y][i[0]+self.x].piece.color != self.color:
                            moves.append((i[0]+self.x,i[1]+self.y))
                        n_v=True

                    elif i[0] > 0 and i[1] > 0 and d_r==False:
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
        p_h=False
        n_h=False
        p_v=False
        n_v=False
        d_r=False
        u_l=False
        d_l=False
        u_r=False

        for i in self.options:
            if -1 < i[0]+self.x < 8 and -1 < i[1]+self.y < 8:
                if self.board.cells[i[1]+self.y][i[0]+self.x].piece == None:
                    if i[0] > 0 and i[1]==0 and p_h==False:
                        self.checker(i,moves)

                    elif i[0] < 0 and i[1]==0 and n_h==False:
                        self.checker(i,moves)

                    elif i[1] > 0 and i[0]==0 and p_v==False:
                        self.checker(i,moves)

                    elif i[1] < 0 and i[0]==0 and n_v==False:
                        self.checker(i,moves)

                    elif i[0] > 0 and i[1] > 0 and d_r==False:
                        self.checker(i,moves)

                    elif i[0] < 0 and i[1] < 0 and u_l==False:
                        self.checker(i,moves)

                    elif i[0] < 0 and i[1] > 0 and d_l==False:
                        self.checker(i,moves)

                    elif i[0] > 0 and i[1] < 0 and u_r==False:
                        self.checker(i,moves)

                else:
                    if i[0] > 0 and i[1]==0 and p_h==False:
                        if self.board.cells[i[1]+self.y][i[0]+self.x].piece.color != self.color:
                            self.checker(i,moves)
                        p_h=True

                    elif i[0] < 0 and i[1]==0 and n_h==False:
                        if self.board.cells[i[1]+self.y][i[0]+self.x].piece.color != self.color:
                            self.checker(i,moves)
                        n_h=True

                    elif i[1] > 0 and i[0]==0 and p_v==False:
                        if self.board.cells[i[1]+self.y][i[0]+self.x].piece.color != self.color:
                            self.checker(i,moves)
                        p_v=True

                    elif i[1] < 0 and i[0]==0 and n_v==False:
                        if self.board.cells[i[1]+self.y][i[0]+self.x].piece.color != self.color:
                            self.checker(i,moves)
                        n_v=True

                    elif i[0] > 0 and i[1] > 0 and d_r==False:
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
