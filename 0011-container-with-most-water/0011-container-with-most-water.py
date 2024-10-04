class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        max_ = 0

        while (l<r):
            val = min(height[l], height[r]) * (r-l)
            print(val)
            max_ = max(max_,val)
            if height[l]<height[r]:
                l += 1
            else:
                r -= 1
        return max_
        



        