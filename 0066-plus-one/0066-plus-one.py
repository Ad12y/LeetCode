class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        lst = []
        for i in digits[::-1]:
            lst.append((i+carry)%10)
            carry = (i + carry)//10
        if carry:
            lst.append(carry)
        return lst[::-1]



        