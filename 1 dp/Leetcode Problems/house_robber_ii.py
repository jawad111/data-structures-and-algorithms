# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

# Example 1:

# Input: nums = [2,3,2]
# Output: 3
# Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
# Example 2:

# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
# Example 3:

# Input: nums = [1,2,3]
# Output: 3
 


import copy


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cache = [-1] * len(nums)
        return self.rob_houses(nums, 0, cache)


    def rob_houses(self, houses, i, cache):
        
        if(len(houses) == 1):
            return houses[0]
        if(i > len(houses) - 1):
            return 0
        
     
        if(cache[i] != -1):
            return cache[i]

        houses_first_empty = copy.deepcopy(houses) 
        houses_last_empty = copy.deepcopy(houses) 

        houses_first_empty[0] = 0
        houses_last_empty[-1] = 0


        cache[i] = max(
            max(houses_first_empty[i] + self.rob_houses(houses_first_empty, i + 2, cache), self.rob_houses(houses_first_empty, i + 1, cache)),
            max(houses_last_empty[i] + self.rob_houses(houses_last_empty, i + 2, cache), self.rob_houses(houses_last_empty, i + 1, cache))
        )

        return cache[i]
    
sol = Solution()
print(sol.rob([200,3,140,20,10]))

#  [1,2,3]
#     /\
    
# 1 + 3  2
         
    


