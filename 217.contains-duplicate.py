#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # solution 1
        # s = set(nums)
        # if len(s) == len(nums):
        #     return False
        # return True

        # solution 2 hashset
        hashset = set()
        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        return False
            
        
# @lc code=end

