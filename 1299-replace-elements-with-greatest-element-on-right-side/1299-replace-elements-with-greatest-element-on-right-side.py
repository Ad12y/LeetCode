class Solution(object):
    def replaceElements(self, arr):
        right_max = arr[-1]
        for i in range(len(arr)-2,-1,-1):
            temp = arr[i] 
            arr[i] = right_max
            if temp > right_max:
                right_max = temp
        arr[-1] = -1 
        return arr
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        