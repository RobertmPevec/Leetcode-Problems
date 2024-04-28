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

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for index, n in enumerate(nums):
            for index2, c in enumerate(nums):
                if n + c == target and index != index2:
                    return index, index2


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        prev_map = {}
        for index, n in enumerate(nums):
            diff = target - n
            if diff in prev_map:
                return[prev_map[diff], index]
            prev_map[n] = index
        return None
