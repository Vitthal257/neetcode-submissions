class Solution:
    def isValid(self, s: str) -> bool:
        dic = {"}":"{",")":"(", "]":"["}
        stk = []
        # 
        for i in s:
            if i in dic:
                if len(stk)==0 or stk[-1] != dic[i]:
                    return False
                stk.pop()
            else:
                stk.append(i)

        return len(stk)==0
            
