class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j = 0, 1
        longest = 1
        if not len(s):
            return 0
        set_ = {s[0]}
        while j < len(s):
            if i == j:
                set_.add(s[i])
                j += 1 
            elif (s[i]!=s[j]) and (s[j] not in set_):
                set_.add(s[j])
                j += 1
                longest = max(longest, j-i) 
                print(set_)
            else:
                set_.remove(s[i])
                i += 1

        return longest

        