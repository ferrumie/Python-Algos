#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start


class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        reverse the memoization
        '''
        a = b = 1
        for i in range(n-1):
            temp = a
            a = a + b
            b = temp
        return a    
            
# @lc code=end

