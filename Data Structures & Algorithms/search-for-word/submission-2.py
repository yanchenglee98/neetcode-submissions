class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dir = [(0,1), (1,0),(-1,0),(0,-1)]
        n = len(word)
        h = len(board)
        w = len(board[0])
        def dfs(r, c, k):
            if k == len(word):
                return True
            if r < 0 or c < 0 or r >=h or c >= w or board[r][c] != word[k]: 
                return False
            
            temp = board[r][c]
            board[r][c] = "#"
            res = False
            for x,y in dir:
                res = res or dfs(r+x, c+y, k+1)
            board[r][c] = temp
            return res
        for r in range(h):
            for c in range(w):
                if dfs(r,c,0): return True
        return False

        