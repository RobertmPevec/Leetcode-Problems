class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        position1 = 0
        while position1 < len(nums) - 1:
            for position2 in range(position1 + 1, len(nums)):
                if nums[position1] + nums[position2] == target:
                    return [position1, position2]
            position1 += 1
        return []
