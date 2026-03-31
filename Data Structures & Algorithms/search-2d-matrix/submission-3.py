class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            l = 0
            h = len(i) - 1
            while l <= h:  # fix: was h >= l (same thing, but more importantly...)
                m = (h+l) // 2
                if i[m] == target:
                    return True
                elif i[m] > target:
                    h = m-1
                else:
                    l = m + 1
        return False