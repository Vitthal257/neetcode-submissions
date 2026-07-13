class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, current, total):
            if total == target:
                res.append(current[:])
                return
            if total > target:
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue  # skip duplicate
                current.append(candidates[i])
                backtrack(i+1, current, total+candidates[i]) 
                current.pop() 
        candidates.sort()

        res = []
        current = []
        total = 0
        backtrack(0,current,total)
        return res
