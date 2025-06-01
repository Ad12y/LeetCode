class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        count = 0
        for i in range(0, m+n):
            if nums1[i] == 0:
                nums1[i] = nums2[count]
                count += 1
            if count == n:
                break
        print(nums1.sort())