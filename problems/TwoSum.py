import '../util'

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        len = len(nums)
        i = 0
        while i < len:
            for j in range(i+1, len):
                if nums[i] + num[j] == target:
                    return [i, j]
            i += 1
        return false
