class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        self.res = []
        if digits == "":
            return []

        def recur(lst, i):
            if i > len(digits)-1:
                self.res.append("".join(lst))
                return
            for j in dic[digits[i]]:
                lst.append(j)
                recur(lst, i+1)
                lst.pop()
        recur([],0)
        return self.res


        