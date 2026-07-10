class Solution:
    def countBits(self, n: int) -> List[int]:
        bits = [0]*(n+1)
        for i in range(n+1):
            bits[i] = bits[i>>1] + (i&1)
        return bits