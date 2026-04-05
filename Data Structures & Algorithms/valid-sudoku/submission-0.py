class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check horizontal
        n = len(board)
        for x in range(n):
            s = set()
            for y in range(n):
                if board[x][y] == ".": continue
                if board[x][y] in s:
                    return False
                s.add(board[x][y])

        # check vertical 
        for y in range(n):
            s = set()
            for x in range(n):
                if board[x][y] == ".": continue
                if board[x][y] in s:
                    return False
                s.add(board[x][y])
        
        # check 3x3 
        for x in range(0, n, 3):
            for y in range(0, n, 3):
                s = set()
                for i in range(0, 3):
                    for j in range(0, 3):
                        if board[x+i][y+j] == ".": continue
                        if board[x+i][y+j] in s:
                            return False
                        s.add(board[x+i][y+j])
        return True
        