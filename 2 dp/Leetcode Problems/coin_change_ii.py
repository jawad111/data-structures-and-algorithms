class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        cache = {}
        return self.dfs(coins, amount, 0, 0, cache)


    # unbounded knapsack
    def dfs(self, coins, amount, sum, i, cache):

        if(i >= len(coins) or sum > amount):
            return 0

        if(sum == amount):
            return 1

        if((i, sum) in cache):
            return cache[(i, sum)]
        
        

        cache[(i,sum)] = self.dfs(coins, amount, sum, i + 1, cache) + self.dfs(coins, amount, sum + coins[i], i, cache)
            

        return cache[(i, sum)]