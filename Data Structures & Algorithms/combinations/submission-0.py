class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(i , comb):
            if len(comb)== k:
                res.append(comb.copy())
                return

            for l in range(i,n+1):
                comb.append(l)
                backtrack(l+1 , comb)
                comb.pop()
                
        backtrack(1,[])
        return res
