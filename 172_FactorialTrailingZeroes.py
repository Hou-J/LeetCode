# https://leetcode.com/problems/factorial-trailing-zeroes/description/
#
# Given an integer n, return the number of trailing zeroes in n!.
#
# Note: Your solution should be in logarithmic time complexity.

class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        while n > 0:
            ans += int(n/5)
            n = int(n/5)
        return ans