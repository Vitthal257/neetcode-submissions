class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0]*(len(temperatures))
        stk = []
        for i, temp in enumerate(temperatures):
            while stk and temp > stk[-1][0]:
                oldtemp,j = stk.pop()
                ans[j] = (i-j)
            stk.append((temp,i))

        return ans
        