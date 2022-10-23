#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        output = [1] * len(nums)

        for i in range(len(output)-1, -1, -1):
            # loop through the output and check the index that follows
            # [1,2,4,3]
            # start from 3, then we have 1 + lis[2] which is 2
            # 1 + lis[1] = 1+2
            # start from 5, end at 4
            # start from 4 end at 4
            # start from 3 wnd at 4, if i is 3, j is 4, 4
            for j in range(i+1, len(nums)):
                # check if j is greater than nums
                if nums[j] > nums[i]:
                    # max between 1 or the val in next index
                    # when i is 3
                    # output i is 3, j is skipped so 1
                    # when i is 2, output i is 4, j is three
                    # but 4 is greater so skipped
                    # when i is 2 ,j is 4
                    # when i is 1, j is 2, 3
                    # for two thats max between 1, 1+output2, 2
                    output[i] = max(output[i], 1 + output[j])
        return max(output)
# @lc code=end

