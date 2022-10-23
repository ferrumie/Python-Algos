#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        using DP approach bottom up
        if x is > 
        '''
        a = b = 0
        for i in nums:
            # [1,3,4,2]
            # i = 1, temp = 1, a = 0, b = 1
            # i = 3, temp = 3, b = 1 = a, b = 3
            # i = 4, temp = 5, a=3, b =5
            # i = 2, temp = 5
            temp = max(i+a, b)
            a = b
            b = temp
        return b

# @lc code=end

