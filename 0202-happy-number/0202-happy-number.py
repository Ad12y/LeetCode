class Solution:
    def isHappy(self, n: int) -> bool:
        def find_sum(n):
            sum_ = 0
            while n!=0:
                sum_ += (n%10)**2
                n = n//10 
            return sum_
        set_ = set()
        res = n
        while True:
            res = find_sum(res) 
            if res == 1.0:
                return True
            else:
                if res in set_:
                    return False 
                else:
                    set_.add(res)
        return 

        