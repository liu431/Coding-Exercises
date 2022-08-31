class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Validate Sodoku by the following 3 rules
        ## Each row must contain the digits 1-9 without repetition.
        for row in board:
            dic = {}
            for rowItem in row:
                if rowItem != '.':
                    if rowItem not in dic:
                        dic[rowItem] = 1
                    else:
                        return False
                    
        ## Each column must contain the digits 1-9 without repetition.
        for col in range(9):
            dic = {}
            for colItem in [row[col] for row in board]:
                if colItem != '.':
                    if colItem not in dic:
                        dic[colItem] = 1
                    else:
                        return False
        ## Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
        for sub_i in [0, 3, 6]:
            for sub_j in [0, 3, 6]:
                dic = {}
                boxitems = sum([i[sub_j: sub_j + 3] for i in board[sub_i: sub_i + 3]], [])
                for item in boxitems:
                    if item != '.':
                        if item not in dic:
                            dic[item] = 1
                        else:
                            return False
        
        # All rules checked -> Is valid Sakodu        
        return True
