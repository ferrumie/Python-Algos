#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import List, Optional


class Solution:
    def addTwoNumbers(self, l1: Optional[List], l2: Optional[List]) -> Optional[List]:
        # reverse the lists
        l1_reverse = l1[::]
        l2_reverse = l2[::]
        l1 = int("".join(map(str, l1_reverse)))
        l2 = int("".join(map(str, l2_reverse)))
        print(l1, l2)
        
# @lc code=end

