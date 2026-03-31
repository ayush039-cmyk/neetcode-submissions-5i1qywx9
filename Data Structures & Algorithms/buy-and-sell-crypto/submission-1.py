class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l , r = 0 , 1
        masP = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                masP = max(masP,profit)
            else:
                l = r
            r += 1
        return masP