#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for r in strs:
            j = [0] * 26
            for c in r:
                j[ord(c) - ord('a')] += 1

            res[tuple(j)].append(r)
            print(res)
        return res.values()
print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
# @lc code=end

