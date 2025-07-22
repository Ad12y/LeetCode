class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # dic = {}
        # for i in range(0, len(strs)):
        #     lst = [0]*26
        #     for j in strs[i]:
        #         print(ord(j)%96)
        #         print(j)
        #         lst[ord(j)%ord("a")] += 1
        #     if tuple(lst) in dic:
        #         dic[tuple(lst)].append(strs[i])
        #     else:
        #         dic[tuple(lst)] = [strs[i]]

        # return list(dic.values())
        hash = defaultdict(list)
        for str in strs:
            hash["".join(sorted(str))].append(str)
        return list(hash.values())