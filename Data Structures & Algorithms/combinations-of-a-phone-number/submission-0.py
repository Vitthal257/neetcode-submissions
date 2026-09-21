class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        mapping = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        ans = []
        def backtrack(i, current):
            if i == len(digits):
                ans.append("".join(current))
                return
            for letter in mapping[digits[i]]:
                current.append(letter)
                backtrack(i+1,current)
                current.pop()
        backtrack(0,[])
        return ans
        