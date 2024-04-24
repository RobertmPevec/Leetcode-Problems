# lowest space solution
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        length = len(nums)
        for n in range(length - 1):
            if nums[n] == nums[n + 1]:
                return True
        return False

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        number_list = []
        for n in nums:
            if n in number_list:
                return True
            number_list.append(n)
        return False

# fastest solution:
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False