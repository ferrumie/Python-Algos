#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        data = [amount+1] * (amount+1)
        # set base
        data[0] = 0
        for i in range(1, amount+1):
            for j in coins:
                if i-j >= 0:
                    data[i] = min(data[i], 1 + data[i-j])
        return data[amount] if data[amount] != amount+1 else -1

        
test = Solution().coinChange([1, 3, 4, 5], 7)
print(test)
# @lc code=end