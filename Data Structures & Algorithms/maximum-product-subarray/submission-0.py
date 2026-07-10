class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #kadane algo
        minnum = nums[0]
        maxnum = nums[0]
        res = nums[0]
        for i in range(1,len(nums)):
            temp = maxnum
            maxnum = max(nums[i], maxnum*nums[i], minnum*nums[i])
            minnum = min(nums[i], temp*nums[i], minnum*nums[i])
            res = max(maxnum,res)
        return res
