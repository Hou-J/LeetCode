# https://leetcode.com/problems/reverse-integer/description/
# 
# Given a 32-bit signed integer, reverse digits of an integer.
# 
# Example 1:
# 
#     Input: 123
#     Output:  321
# Example 2:
# 
#     Input: -123
#     Output: -321
# Example 3:
# 
#     Input: 120
#     Output: 21
# Note:
# Assume we are dealing with an environment which could only hold integers within the 32-bit signed integer range.
# For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result, sign = 0, 1 if x > 0 else -1
        x *= sign
        while x > 0:
            result = result * 10 + (x % 10)
            x //= 10
        return result * sign if result < 0x7fffffff else 0
