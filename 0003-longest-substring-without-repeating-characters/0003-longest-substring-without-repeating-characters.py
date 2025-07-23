class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if not s:
            return 0
        res = 1
        l = 0
        r = 1
        check = set([s[l]])
        while l < r and r < len(s):
            if s[r] in check:
                while l < r:
                    check.remove(s[l])
                    l += 1
            check.add(s[r])
            r += 1
            res = max(res, r-l) 
        return res

        