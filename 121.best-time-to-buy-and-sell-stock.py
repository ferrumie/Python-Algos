#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # l, r = 0, 1
        # max_profit = 0

        # while r < len(prices):
        #     if prices[r] > prices[l]:
        #         profit = prices[r] - prices[l]
        #         maxp = max(max_profit, profit)
        #         max_profit = maxp
        #     else:
        #         l = r
        #     r+=1
        # return max_profit

        # check for the lowest number
        # check for the highest number after the lowest number
        # calculate the differences
        left = 0
        right = 1
        maax_profit = 0
        while right < len(prices):
            if prices[right] > prices[left]:
                profit = prices[right] - prices[left]
                maxp = max(maax_profit, profit)
                maax_profit=maxp
            else:
                left = right
            right += 1
        return maax_profit
        
# @lc code=end
s = Solution
print(s().maxProfit([7,6,4,3,1]))