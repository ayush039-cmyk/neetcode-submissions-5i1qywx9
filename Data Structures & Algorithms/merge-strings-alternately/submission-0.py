class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        a = 0
        b = 0
        n = min(len(word1), len(word2))
        res = ""
        while a < n:
            res += word1[a] + word2[b]  
            a += 1
            b += 1

        if len(word1) > len(word2):
            res += word1[a:] 
        else:
            res += word2[b:]

        return res