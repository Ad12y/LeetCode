class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [i.lower() for i in s if i.isalnum()] 
        st = 0
        end = len(s) - 1
        while st<end:
            if s[st]!=s[end]:
                return False
            else:
                st+=1
                end-=1
        return True


        