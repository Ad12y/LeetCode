class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:        
        if len(piles) == h:
            return max(piles)
        elif h/len(piles) >= 2:
            print("dfd")
            return math.ceil((sum(piles)/h))    
        elif len(piles) < h:
            piles.sort()
            last = h - len(piles) +1
            return piles[-last]
        