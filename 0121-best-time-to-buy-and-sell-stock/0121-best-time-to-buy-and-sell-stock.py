class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val = prices[0]
        max_dif = 0
        for i in range(1 ,len(prices)):
            if prices[i] < min_val:
                min_val = prices[i]
            else:
                max_dif = max(max_dif,prices[i]-min_val)

        print(max_dif)
        return max_dif
        