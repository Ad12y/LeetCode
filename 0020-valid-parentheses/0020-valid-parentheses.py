class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        dic = {"(":")", "[":"]","{":"}"}
        if len(s) == 1:
            return False

        for i in range(0, len(s)):
            if s[i] in dic.values() and len(stack) == 0 :
                return False
            if s[i] in dic.keys():
                stack.append(s[i])
            elif len(stack) and  dic[stack[-1]] == s[i]:
                stack.pop()
        if not stack:
            return True 
        else:
            return False 


        