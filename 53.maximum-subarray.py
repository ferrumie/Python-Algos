#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        brute force.
        a loop from the first
        another from the last inside the first.
        then replace the sum with the max between the first and the blah
        so for 5,4,3, 2
        loop from 5
        then sum from 5 to 2,
        sum from 5, 3
        sum from 5, 4
        then sum from 4 to 2
        
        '''
        max_sum = -100000
        cur_sum = 0
        for i in nums:
            cur_sum += i
            if cur_sum > max_sum:
                max_sum = cur_sum
            if cur_sum < 0:
                cur_sum = 0
        return max_sum

                
        
# @lc code=end
s = Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
print(s)

