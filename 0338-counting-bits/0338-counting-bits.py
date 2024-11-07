class Solution:
    def countBits(self, n: int) -> List[int]:

        def fun(n):
            count = 0
            while n:
                if n&1:
                    count += 1
                n = n>>1
            return count 
        lst = []
        for i in range(0, n+1):
            lst.append(fun(i))
        return lst

        