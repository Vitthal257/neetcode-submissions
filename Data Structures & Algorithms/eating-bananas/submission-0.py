class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(k):
            return sum((p+k-1)//k for p in piles) <=h

        low = 1
        high = max(piles)
        result = high
        while low<=high:
            mid = (high+low)//2
            if check(mid):
                result = mid
                high = mid-1
            else:
                low = mid+1
        return result
        