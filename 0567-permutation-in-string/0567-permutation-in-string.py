class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dic = {}

        if len(s1)>len(s2):
            return False 
        for i in s1:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1 
        l_1 = len(s1)
        i,j = 0,1
        dic_ = {s2[0]:1}

        while j < len(s1):
            if s2[j] in dic_:
                dic_[s2[j]] += 1
            else:
                dic_[s2[j]] = 1
            j += 1
        print(dic)
        while j < len(s2):
            if dic_ == dic:
                print("da")
                return True
            else:
                if s2[j] in dic_:
                    dic_[s2[j]] += 1
                else:
                    dic_[s2[j]] = 1
                j += 1
                dic_[s2[i]] -= 1
                if not dic_[s2[i]]:
                    dic_.pop(s2[i])
                i += 1
            print(dic_)
        if dic_ == dic:
            return True
        else:
            return False
 






        