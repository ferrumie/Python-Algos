#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        stack = []
        
        # loop through the string
        # if the bracket is a key in the dict append to list
        # pop out the list once a matching bracket is found

        for i in s:
            if i in '[{(':
                stack.append(i)
            # the brackets must be orderly closed, so the first close
            # bracket must be same bracket appended last
            elif len(stack) == 0 or i != parentheses[stack.pop()]:
                return False
        return len(stack) == 0
# @lc code=end

