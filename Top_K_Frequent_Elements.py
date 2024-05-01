class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        numb_dict = {}
        output_list = []
        for n in nums:
            if n in numb_dict:
                numb_dict[n] += 1
            else:
                numb_dict[n] = 1
        sorted_items = sorted(numb_dict.items(),key=lambda item: item[1], reverse=True)
        for i in range(k):
            output_list.append(sorted_items[i][0])
        return output_list



