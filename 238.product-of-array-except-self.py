#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix, # suffix
        # output = [1] * len(nums)
        # prefix = 1

        # for i in range(len(nums)):
        #     output[i] = prefix
        #     prefix *= nums[i]
       
        # postfix = 1
        # for j in range(len(nums)-1, -1, -1):
        #     output[j] *= postfix
        #     postfix *= nums[j]

        # return output

        prefix = 1
        suffix = 1
        final_list = [1] * len(nums)

        for i in range(len(nums)):
            final_list[i] = prefix
            prefix *= nums[i]

        for j in range(len(nums)-1, -1, -1):
            final_list[j] *= suffix
            suffix *= nums[j]
        return final_list







        
# @lc code=end

t = Solution().productExceptSelf([1,2,3,4])
print(t)