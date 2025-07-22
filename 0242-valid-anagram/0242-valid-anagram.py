class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic1 = {}
        dic2 = {}

        for i in range(0, len(s)):
            if s[i] not in dic1.keys():
                dic1[s[i]] = 1
            else:
                dic1[s[i]] += 1

        for i in range(0, len(t)):
            if t[i] not in dic2.keys():
                dic2[t[i]] = 1
            else:
                dic2[t[i]] += 1
        

        return dic1 == dic2

        