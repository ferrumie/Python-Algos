#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        ans = 0
        for i in range(len(s)-1, -1, -1):
            num = roman_dict[s[i]]
            if 3 * num < ans:
                ans -= num
            else:
                ans += num
        return ans

# @lc code=end

