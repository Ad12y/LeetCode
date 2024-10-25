class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def check(string):
            if len(string) == 1 or string == string[::-1]:
                return True
            return False
        self.res = []
        def recur(lst, i):
            if i > len(s)-1:
                self.res.append(lst[::])
                return
            for j in range(i, len(s)):
                if check(s[i:j+1]):
                    lst.append(s[i:j+1])
                    recur(lst, j+1)
                    lst.pop()
                
        recur([], 0)
        return self.res