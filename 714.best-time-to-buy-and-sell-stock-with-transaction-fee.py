#
# @lc app=leetcode id=714 lang=python3
#
# [714] Best Time to Buy and Sell Stock with Transaction Fee
#

# @lc code=start
from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # buy low sell high
        # buy at the lowest. pop out. sell at the highest, pop out
        # 
        # pick the lowerst starting from
        buy, sell = -prices[0], 0
        for i in range(1, len(prices)):
            first_buy = max(buy, sell-prices[i])
            first_sell = max(sell, buy+prices[i]-fee)
            buy = first_buy
            sell = first_sell
        return sell
sol = Solution()
pr = sol.maxProfit([1,3,2,8,4,9], 2)
print(pr)   
# @lc code=end

