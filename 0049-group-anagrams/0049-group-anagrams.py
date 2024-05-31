class Solution(object):
    def groupAnagrams(self, strs):

        result = {}
        for i in strs:
            alp = [0]*26
            for j in i:
                alp[ord(j) - ord('a')] += 1
            try:
                result[tuple(alp)].append(i)
            except:
                result[tuple(alp)] = [i]
                
        return result.values()
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        