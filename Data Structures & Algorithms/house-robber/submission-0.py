class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        dp = [float('-inf')]*(n)
        def dfs(i):
            if i>=n:
                return 0
            if dp[i] != float('-inf'):
                return dp[i]
            else:
                dp[i] = max(nums[i]+dfs(i+2), dfs(i+1))
            return dp[i]
            
        return dfs(0)
        

       


        