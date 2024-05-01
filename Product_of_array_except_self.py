def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    # slow speed
    multiply = 1
    numb_list = []
    for n, i in enumerate(nums):
        number = nums[n + 1:] + nums[:n]
        for c in number:
            multiply *= c
        numb_list.append(multiply)
        multiply = 1
    return numb_list
