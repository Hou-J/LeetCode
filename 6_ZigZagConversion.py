# https://leetcode.com/problems/zigzag-conversion/description/
#
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
#
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
# Write the code that will take a string and make this conversion given a number of rows:
#
# string convert(string text, int nRows);
# convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows > len(s) or numRows <= 1:
            return s
        zigzag = [[] for i in range(numRows)]
        row, step = 0, 1
        for c in s:
            zigzag[row] += c,
            if row == 0:
                step = 1
            elif row == numRows - 1:
                step = -1
            row += step

        result = ""
        for i in zigzag:
            for j in i:
                result+=j
        return result