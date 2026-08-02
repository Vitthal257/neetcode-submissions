class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1
        a = s.lower()
        while i<=j:
            while i<j and not a[i].isalnum():
                i+=1
            while i<j and not a[j].isalnum():
                j-=1
            if a[i] != a[j]:
                return False
            i+=1
            j-=1
        return True
        