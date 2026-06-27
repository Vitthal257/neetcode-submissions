from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return
        r = len(grid)
        c = len(grid[0])
        q = deque()
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 0:
                    q.append((i,j))

        while q:
            for _ in range(len(q)):
                ni,nj = q.popleft()
                for i,j in [(-1,0), (0,1),(1,0),(0,-1)]:
                    di = ni+i
                    dj = nj+j
                    if 0<=di<r and 0<=dj<c and grid[di][dj] == 2147483647:
                        grid[di][dj] = grid[ni][nj]+1
                        q.append((di, dj))

        return