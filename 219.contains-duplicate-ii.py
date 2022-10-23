#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashset = {}
        for i,n in enumerate(nums):
            if nums[i] in hashset and abs(i-hashset[n]) <= k:
                return True
            hashset[n] = i
        return False
        
# @lc code=end

