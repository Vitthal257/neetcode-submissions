class Solution:
    def rob(self, nums: List[int]) -> int:
        def robbing(nums):
            rob1,rob2 = 0,0
            for i in range(len(nums)):
                rob1,rob2 = rob2, max(nums[i]+rob1, rob2)
            return max(rob1, rob2)
        
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        case1 = robbing(nums[1:])
        case2 = robbing(nums[:-1])
        return max(case1,case2)