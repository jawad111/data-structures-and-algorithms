class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

    def dfs(buying, index):
        
        if(index > len(prices)):
            return 0

        profit = 0

        if(buying):
            buyingProfit = dfs(not buying, index + 1) - prices[index]
            cooldown = dfs(not buying, index + 1)
            profit = max(buyingProfit, cooldown)
        else:
            sellingProfit = dfs(not buying, index + 2) + prices[index]
            cooldown = dfs(not buying, index + 1)
            profit = max(sellingProfit, cooldown)
            
        return profit


dfs(True, 0)

        


