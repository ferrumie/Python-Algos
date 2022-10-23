#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset = set()
        a = 0
        res = 0

        for b in range(len(s)):
            while s[b] in hashset:
                hashset.remove(s[a])
                a += 1
            hashset.add(s[b])
            res = max(res, b-a+1)
        return res


# @lc code=end

