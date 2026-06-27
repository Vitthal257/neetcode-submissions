class Solution:
    def solve(self, board: List[List[str]]) -> None:
        r = len(board)
        c = len(board[0])
        def dfs(i,j):
            if i<0 or j<0 or i>=r or j>=c:
                return
            if board[i][j] != "O":
                return
            board[i][j] = "T"
            dfs(i,j-1)
            dfs(i,j+1)
            dfs(i-1,j)
            dfs(i+1,j)

        for i in range(r):
            for j in range(c):
                if i == 0 or i == r-1 or j == 0 or j == c-1:
                    if board[i][j] == 'O':
                        dfs(i,j)
        
        for i in range(r):
            for j in range(c):
                if board[i][j] == 'T':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'
        

        