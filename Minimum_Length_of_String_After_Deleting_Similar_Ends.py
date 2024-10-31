#1750 Minimum Length of String After Deleting Similar Ends
"""
Given a string s consisting only of characters 'a', 'b', and 'c'. You are asked to apply the following algorithm on the string any number of times:

Pick a non-empty prefix from the string s where all the characters in the prefix are equal.
Pick a non-empty suffix from the string s where all the characters in this suffix are equal.
The prefix and the suffix should not intersect at any index.
The characters from the prefix and suffix must be the same.
Delete both the prefix and the suffix.
Return the minimum length of s after performing the above operation any number of times (possibly zero times).
"""
class Solution(object):
    def minimumLength(self, s):
        while len(s) > 1 and s[0] == s[-1]:
            s = s.strip(s[0])
        return len(s)


        #Time Complexity O(n^2)
        """
        :type s: str
        :rtype: int
        """
