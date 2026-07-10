class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, current):
            res.append(current[:])
            for i in range(start, len(nums)):
                current.append(nums[i])
                backtrack(i+1,current)
                current.pop()
        res=[]
        backtrack(0, [])
        return res