class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        ans = []
        ans.append(0) 
        ans.append(ans[0])
        for i in range(1, len(cost)):
            ans.append(min(ans[i-1] + cost[i-1], ans[i] + cost[i]))
        return ans[-1]

        