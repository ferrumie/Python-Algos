#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_count = {}
        res = 0
        l = 0
        for r in range(len(s)):
            char_count[s[r]] = 1 + char_count.get(s[r], 0)
            while (r-l+1) - max(char_count.values()) > k:
                char_count[s[l]] -= 1
            res = max(res, r-l+1)
        return res


        
# @lc code=end

