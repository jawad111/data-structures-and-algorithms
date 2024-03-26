class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.climb(n, 0, {})


    def climb(self, total_stairs, stair, cache):
        if(stair == total_stairs):
             return 1
        if(stair > total_stairs):
             return 0
        if(stair in cache):
            return cache[stair]
        
        cache[stair]= self.climb(total_stairs, stair + 1, cache) + self.climb(total_stairs, stair + 2, cache)

        return cache[stair]