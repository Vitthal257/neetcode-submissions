class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def backtrack(start, current, total):
            if total == target:
                res.append(current[:])
                return
                return current
            if total > target:
                return
            for i in range(start, len(nums)):
                current.append(nums[i])
                backtrack(i, current, total+nums[i])
                current.pop()


        res = []
        current = []
        total = 0
        backtrack(0, current, total)
        return res
