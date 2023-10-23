class Solution(object):
    def lengthOfLongestSubstring(self, s):
        i = 0
        j = 1
        max_ = 1
        if len(s) == 0:
            return 0
        while j<len(s):
            if s[j] not in s[i:j]:
                j += 1 
                max_ = max(max_,j-i)
            else:
                i += 1

        print(max_)
        return max_

        """
        :type s: str
        :rtype: int
        """
        