class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val = prices[0]
        max_diff = 0

        for i in range(1, len(prices)):
            if prices[i] < min_val:
                min_val = prices[i]
            else:
                max_diff = max(max_diff, prices[i] - min_val)

        return max_diff
