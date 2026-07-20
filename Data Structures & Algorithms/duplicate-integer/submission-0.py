class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for i in nums:
            if i in set:
                return True
            seen.add(i)
        return False