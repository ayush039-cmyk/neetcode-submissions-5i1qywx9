class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # 1. Start l at 1, not 0
        l, r = 1, max(piles)
        res = r
        
        while l <= r:
            k = (l + r) // 2
            
            # Defensive check: if k is 0 (though l=1 prevents this), avoid crash
            if k == 0: 
                l = 1
                continue

            hours = 0
            for p in piles:
                # 2. Use integer math for ceiling to avoid float issues
                hours += (p + k - 1) // k
            
            if hours <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res