#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # combine the two lists
        # loop through the list, if current value is greater than
        # the next value, then make the next value = current value
        newlist = ListNode()
        temp_list = newlist

        if not list1:
            return list2
        if not list2:
            return list1

        while list1 and list2:
            if list1.val < list2.val:
                temp_list.next = list1
                list1 = list1.next
            else:
                temp_list.next = list2
                list2 = list2.next
            temp_list = temp_list.next
        temp_list.next = list1 if list1 else list2
        return newlist.next
# @lc code=end

