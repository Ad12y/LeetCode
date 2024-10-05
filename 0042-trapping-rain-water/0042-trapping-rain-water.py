class Solution:
    def trap(self, height: List[int]) -> int:
        r_l = []
        l_r = []
        max_val = height[0]
        for i in range(1, len(height)-1):
            if height[i] > max_val:
                l_r.append(0)
                max_val = height[i]
            else:
                l_r.append(max_val - height[i])
        
        max_val = height[-1]
        for j in range(1, len(height)-1)[::-1]:
            if height[j] > max_val:
                r_l.append(0)
                max_val = height[j]
            else:
                r_l.append(max_val - height[j])

        r_l = r_l[::-1]
        op = 0
        for i in range(0, len(r_l)):
            op += min(l_r[i], r_l[i])

        print(op)
        return op
        

        