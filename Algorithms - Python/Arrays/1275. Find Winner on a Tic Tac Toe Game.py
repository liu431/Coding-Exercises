class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        # split moves to A and B
        movesA, movesB = [], []
        for i in range(len(moves)):
            if i % 2 == 0:
                movesA.append(moves[i])
            else:
                movesB.append(moves[i])
        # check diag win
        def diag(moves):
            if [0,0] in moves and [1,1] in moves and [2,2] in moves:
                return True
            if [0,2] in moves and [1,1] in moves and [2,0] in moves:
                return True            
        if diag(movesA):
            print('d')
            return "A"
        if diag(movesB):
            return "B"
        
        # check row win
        rowA = [i[0] for i in movesA]
        rowB = [i[0] for i in movesB]
        rowActs = [rowA.count(i) for i in set(rowA)]
        rowBcts = [rowB.count(i) for i in set(rowB)]
        if rowActs and max(rowActs) == 3:
            return "A"
        if rowBcts and max(rowBcts) == 3:
            return "B"        
        # check column win
        colA = [i[1] for i in movesA]
        colB = [i[1] for i in movesB]
        colActs = [colA.count(i) for i in set(colA)]
        colBcts = [colB.count(i) for i in set(colB)]
        if colActs and max(colActs) == 3:
            return "A"
        if colBcts and max(colBcts) == 3:
            return "B"          
        
        # no one wins
        if len(moves) == 9:
            return "Draw"
        else:
            return "Pending"
