class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxreach = nums[0]
        for i in range(len(nums)):
            if i>maxreach:
                return False
            maxreach = max(maxreach, i+nums[i])
        return True