class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        r , c = len(board) , len(board[0])
        path = set()

        def dfs(ro,co,i):
            if i == len(word):
                return True
            if (ro<0 or co<0 or ro >= r or co >= c or word[i] != board[ro][co] or (ro,co) in path):
                return False

            path.add((ro,co))
            res = (dfs(ro+1,co,i+1) or dfs(ro,co+1,i+1) or dfs(ro-1,co,i+1) or dfs(ro,co-1,i+1)) 
            path.remove((ro,co))

            return res

        for ri in range(r):
            for ci in range(c):
                if dfs(ri,ci,0):
                    return True
        return False
