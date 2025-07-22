class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for i in strs:
            lst = [0]*26
            for j in i:
                lst[ord(j) - ord("a")] += 1
            dic[tuple(lst)] = [i] + dic.get(tuple(lst), [])
        return list(dic.values())