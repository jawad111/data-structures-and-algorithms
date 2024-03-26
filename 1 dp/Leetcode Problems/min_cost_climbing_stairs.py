class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type nums: List[int]
        :rtype: int
        """
        cache = [-1] * len(cost)
        return min(self.climb(cost, 0, cache), self.climb(cost, 1, cache))
        


    def climb(self , cost, i, cache):

        if (i > len(cost) - 1):
             return 0
        
        if(cache[i] != -1):
            return cache[i]
  
        cache[i] = min(cost[i] + self.climb(cost, i + 1, cache), cost[i] + self.climb(cost, i + 2, cache))
        
        return cache[i]
        
    


