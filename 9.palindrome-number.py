#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start


class Solution:
    def isPalindrome(self, x: int) -> bool:
        stored_num = x
        reversed_num = 0
        while stored_num > 0:
            remainder = stored_num % 10
            reversed_num = reversed_num * 10 + remainder
            stored_num = stored_num//10
        return reversed_num == x
        
# @lc code=end