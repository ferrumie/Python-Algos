#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
from typing import List

# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         prefix = ''
#         sorted_strs = sorted(strs)
#         print(sorted_strs)
#         for i in range(len(min(strs))):
#             a = strs[0][i]
#             if all(c[i] == a for c in strs):
#                 prefix +=a
#             else:
#                 break
#         return prefix

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        # sort the strings
        # zip the first and last string
        # loop through the zip and append the value to prefix if the tuple contains equal letters
        strs.sort()
        for x, y in zip(strs[0], strs[-1]):
            if x == y:
                prefix += x
            else:
                break
        return prefix

# @lc code=end

