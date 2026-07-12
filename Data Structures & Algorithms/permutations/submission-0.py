class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(path):
            if len(nums) == len(path):
                res.append(path.copy())
                return
            for x in nums:
                if x in path:
                    continue
                path.append(x)
                dfs(path)
                path.pop()
        dfs([])
        return res
        