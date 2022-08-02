#https://leetcode.com/problems/two-sum/

import array
#https://leetcode.com/problems/two-sum/

class Solution:
    def twosum(self, nums: array, target: int):
        for i in range(len(nums)):
            for n in range(i + 1, len(nums)):
                if (nums[i] + nums[n] == target):
                    return [i, n]