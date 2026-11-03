# [10 1 5 6 7 1]
#  ^

# Solution: Brute force: O(n^2). check all combinations

# Idea: Have to check all numbers at least once. Best is probably O(n)

# Solution: Find minmum to the left with maximum to the right
# Iterate through each number starting from left to right. If there's a new minimum, then set it to that one. 

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_left = prices[0]
        max_profit = 0

        for price in prices:
            if price < min_left:
                min_left = price
            else:
                curr_profit = price - min_left
                if curr_profit > max_profit:
                    max_profit = curr_profit


        return max_profit
                

