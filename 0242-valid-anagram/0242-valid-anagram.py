class Solution(object):
    def isAnagram(self, s, t):
        dic_1 = {}
        dic_2 = {}
        for i in s:
            try:
                dic_1[i] += 1
            except:
                dic_1[i] = 1
        for i in t:
            try:
                dic_2[i] += 1
            except:
                dic_2[i] = 1
        
        return dic_2 == dic_1

        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        