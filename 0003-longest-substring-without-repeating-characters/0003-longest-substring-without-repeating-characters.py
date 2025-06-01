class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 1
        max_len = 1
        if s == "":
            return 0
        if len(s) == 1:
            return max_len
        while r != len(s):
            if s[r] in s[l:r] and l<r:
                l += 1
            else:
                r += 1  
            max_len = max(max_len, r-l) 
        return max_len  