class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:        
        dic = {}

        dic1 = {}
        for i in nums:
            dic1[i] = i 
        for i in range(0, len(nums)):
            dic1[nums[i]] = float('inf')
            for j in range(i+1, len(nums)):
                temp = nums[j]
                dic1[nums[j]] = float('inf')
                val = -1 * (nums[i] + temp) 
                if val in dic1:
                    if dic1[val] != float("inf"):
                        a = nums[i]
                        b = temp
                        c = val

                        lst_1 = str([a,b,c])
                        lst_2 = str([b,a,c])
                        lst_3 = str([b,c,a])

                        lst_4 = str([c,a,b])
                        lst_5 = str([a,c,b])
                        lst_6 = str([c,b,a])

                        if lst_1 not in dic and lst_2 not in dic and lst_3 not in dic and lst_4 not in dic and lst_5 not in dic and lst_6 not in dic:
                            dic[lst_1] = [a,b,c]
                dic1[nums[j]] = temp

        print(dic)
        return list(dic.values())