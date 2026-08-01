class Solution:
    def jump(self, nums: List[int]) -> int:
        maxreach = nums[0]
        steps = 0
        bor = 0
        for i in range(len(nums)-1):
            maxreach = max(maxreach, nums[i]+i)
            if i == bor:
                steps +=1
                bor = maxreach
            
        return steps

        