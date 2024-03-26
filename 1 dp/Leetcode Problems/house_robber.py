class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.rob_houses(nums, 0, {})


    def rob_houses(self, houses, i, cache):

        if(i > len(houses) - 1):
            return 0
        
        if(i in cache):
            return cache[i]


        cache[i] = max(houses[i] + self.rob_houses(houses, i + 2, cache), self.rob_houses(houses, i + 1, cache))

        return cache[i]
                