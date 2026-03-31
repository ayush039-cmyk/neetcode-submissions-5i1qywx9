class Solution:
    def maxProfit(self, price: List[int]) -> int:
        s = []
        profit = 0
        for i in range(0,len(price)-1):
                if price[i+1] > price[i]:
                    profit += price[i+1] - price[i]
        return profit