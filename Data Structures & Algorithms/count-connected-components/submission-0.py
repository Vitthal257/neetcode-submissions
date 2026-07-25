from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        map = defaultdict(list)
        for u,v in edges:
            map[u].append(v)
            map[v].append(u)
        def dfs(node):
            visited.add(node)
            for nei in map[node]:
                if nei not in visited:
                    dfs(nei)
        visited = set()
        count =0
        for i in range(n):
            if i not in visited:
                dfs(i)
                count+=1
        
        return count

            
        
 


        


        