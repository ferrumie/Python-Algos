#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = float('-inf')
        min_num, max_num = 1, 1
        for num in nums:
            temp = max_num
            max_num = max(num, num*max_num, num*min_num)
            min_num = min(num, num*min_num, num*temp)
            result = max(result, min_num, max_num)
        return result
# @lc code=end

