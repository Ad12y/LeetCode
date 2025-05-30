class Solution:
    def trap(self, height: List[int]) -> int:
        l_r = [0]*len(height) 
        r_l = [0]*len(height) 
        max_l = 0
        max_r = 0

        for i in range(0, len(height)):
            if max_l > height[i]:
               l_r[i] =  max_l - height[i]
            max_l = max(max_l, height[i])

        for i in range(0, len(height))[::-1]:
            if max_r > height[i]:
               r_l[i] =  max_r - height[i]
            max_r = max(max_r, height[i])
        ans = 0
        for i in range(0, len(height)):
            ans += min(l_r[i], r_l[i])    

        return ans 