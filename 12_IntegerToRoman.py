# https://leetcode.com/problems/integer-to-roman/description/
#
# Given an integer, convert it to a roman numeral.
#
# Input is guaranteed to be within the range from 1 to 3999.

class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        numbers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        letters = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        result = ""
        for i in range(len(numbers)):
            if num >= numbers[i]:
                count = num / numbers[i]
                num = num % numbers[i]
                for j in range(int(count)):
                    result += letters[i]
        return result
