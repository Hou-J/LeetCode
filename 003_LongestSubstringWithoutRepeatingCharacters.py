# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
#
# Given a string, find the length of the longest substring without repeating characters.
#
# Examples:
#
#   Given "abcabcbb", the answer is "abc", which the length is 3.
#
#   Given "bbbbb", the answer is "b", with the length of 1.
#
#   Given "pwwkew", the answer is "wke", with the length of 3.
#   Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        longestSub = ""
        for i in range(len(s)):
            if s[i] in longestSub:
                result = max(result, len(longestSub))
                longestSub = longestSub[longestSub.index(s[i]) + 1:]
            longestSub += s[i]
        result = max(result, len(longestSub))
        return result
