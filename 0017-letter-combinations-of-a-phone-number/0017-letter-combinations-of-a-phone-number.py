class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"}
        res = []
        def backtrack(string, i):
            if len(string) == len(digits):
                if len(string):
                    res.append(string)
            if i >= len(digits):
                return
            for j in dic[digits[i]]:
                backtrack(string+j, i+1)

        backtrack("", 0)
        return res

            
        