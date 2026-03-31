class Solution:
    def ispalind(self,s:str) -> bool:
        l = 0
        r = len(s) - 1

        while l<r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return False
        return True

    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        if self.ispalind(s):
            return True
        else:
            for i in range(len(s)):
                d = s[:i] + s[i+1:]
                if self.ispalind(d):
                    return True
            if self.ispalind(s):
                return True
        return False