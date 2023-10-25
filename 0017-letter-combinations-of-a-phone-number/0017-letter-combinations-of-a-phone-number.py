class Solution(object):
    def letterCombinations(self, digits):
        dic = keyboard = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"}
        stack = []
        res = []

        def recur(i):
            if len(digits) == 0:
                return res
            if i>=len(digits):
                res.append(''.join(stack[:]))
                return 
            
            for j in dic[digits[i]]:
                stack.append(j)
                recur(i+1)
                stack.pop()

        recur(0)
        return res 

        """
        :type digits: str
        :rtype: List[str]
        """
        