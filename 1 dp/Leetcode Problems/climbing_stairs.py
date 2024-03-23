class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        cache = {}
        return self.foo(n, 0, 0, cache)

    def foo(self, total_steps, current_step, total, cache):

        total = total + current_step 

        if(total == total_steps):
            return 1

        if(total > total_steps):
            return 0
        
        if (total < total_steps):

            if((current_step, total) in cache):
                return cache[(current_step, total)]


            cache[(current_step, total)] = self.foo(total_steps, 1, total, cache) + self.foo(total_steps, 2, total, cache)

            
        return cache[(current_step, total)]
        
