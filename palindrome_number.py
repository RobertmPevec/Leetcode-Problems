class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        palindrome = x[::-1]
        if x == palindrome:
            return True
        else:
            return False
