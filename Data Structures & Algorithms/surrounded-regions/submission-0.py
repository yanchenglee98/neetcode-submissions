# hint
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        DIR = [(1,0), (0,1), (-1,0), (0,-1)]
        n,m = len(board), len(board[0])
        def dfs(r,c):
            if r < 0 or r >=n or c < 0 or c >=m or board[r][c] != 'O':
                return 
            board[r][c] = '#'
            for x, y in DIR:
                dfs(r+x, c+y)
        
        for r in range(n):
            if board[r][0] == 'O':
                dfs(r, 0)
            if board[r][m-1] == 'O':
                dfs(r, m-1)
        for c in range(m):
            if board[0][c] == 'O':
                dfs(0, c)
            if board[n-1][c] == 'O':
                dfs(n-1, c)
        for r in range(n):
            for c in range(m):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == '#':
                    board[r][c] = 'O'