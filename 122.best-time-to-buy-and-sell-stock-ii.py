#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#

# @lc code=start
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit = prices[i] - prices[i-1]
                max_profit+=profit
        return max_profit
test = Solution()
print(test.maxProfit([1,3,2,8,4,9]))
# @lc code=end
val = {0: 'Federal Capital Territory', 1: 'Lagos', 2: 'Ogun', 3: 'Oyo'}
def convert_dict(val):
    dic = {y.lower(): x for x, y in val.items()}
    print(dic)
convert_dict(val)

