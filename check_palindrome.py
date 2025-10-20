class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        my_string = str(x)
        reverse_string = my_string[::-1]
        if my_string == reverse_string:
            return True
        else:
            return False
