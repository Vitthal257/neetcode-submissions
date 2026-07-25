class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = list(range(len(edges)+1))
        def find(x):
            if parent[x] !=x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x,y):
            px,py = find(x), find(y)
            if px == py:
                return False
            parent[px] = py
            return True

        for x,y in edges:
            if union(x,y) == False:
                return [x,y]