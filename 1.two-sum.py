#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
from typing import List
# @lc code=start
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         '''if the index of a two items adds up to target, return the index'''
#         for i in range(len(nums)):
#             for j in range(1+i, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]

# using hashmap
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''if the index of a two items adds up to target, return the index'''
        # hashmap = {}
        # # save each element in the hash, and check if the subraction of target 
        # # leads to the current element
        # # {index, elem}
        # for i, n in enumerate(nums):
        #     num = target-n
        #     if num in hashmap:
        #         return [i, hashmap[num]]
        #     hashmap[n] = i
        # return
        hashmap = {}
        # go through each of the number in the list
        # if the target - n is in 
        # for i, n in enumerate(nums):
        #     num = target - n
        #     if n in nums:
        for i, n in enumerate(nums):
            num = target - n
            if num in hashmap:
                return [hashmap[num], i]
            hashmap[n] = i
        return None


# @lc code=end
sol = Solution()
hi = sol.twoSum([3,2,4], 6)
print(hi)