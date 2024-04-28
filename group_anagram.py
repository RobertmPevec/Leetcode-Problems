def group_anagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    word_dict = {}
    assorted_list = []
    index_list = enumerate(strs)
    for index, n in enumerate(strs):
        word_dict[n] = index
        assorted_list.append("".join(sorted(n)))
    for i in range(len(assorted_list)-1):
        if i == assorted_list[i]:
#come back to this

