class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == h:
            return max(piles)
        min_val = math.ceil((sum(piles)/h))
        max_val = max(piles)
        res = float('inf')
        while min_val <= max_val:
            mid = int((min_val+max_val)/2)
            hours_taken = 0
            for pile in piles:
                hours_taken += math.ceil(pile/mid)
            if hours_taken > h:
                min_val = mid+1
            else:
                res = min(res, mid)
                max_val = mid-1
        return res


        
        