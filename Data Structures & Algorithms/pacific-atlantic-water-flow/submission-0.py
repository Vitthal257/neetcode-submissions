from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        r = len(heights)
        c = len(heights[0])
        def bfs(starts):
            q = deque(starts)
            visited = set(starts)
            while q:
                for _ in range(len(q)):
                    row,col = q.popleft()
                    for i,j in [(-1,0),(1,0),(0,-1),(0,1)]:
                        di,dj = row+i,col+j
                        if 0<=di<r and 0<=dj<c and (di,dj) not in visited and heights[di][dj]>=heights[row][col]:
                            visited.add((di,dj))
                            q.append((di,dj))

            return visited
        pstarts = [(0,j) for j in range(c)] + [(i,0) for i in range(r)]
        astarts = [(r-1,j) for j in range(c)] + [(i,c-1) for i in range(r)]

        pac = bfs(pstarts)
        atl = bfs(astarts)
        return list(pac & atl)



        