
import copy


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        combination, all_combinations = [], []
        self.combination_sum(candidates, target, combination, all_combinations, 0, 0)
        return all_combinations
    
    def combination_sum(self, nums, target, combination, all_combinations, sum, i):
        
        if(sum == target):
            all_combinations.append(copy.deepcopy(combination))
            return

        if(sum > target or i > (len(nums) - 1)):
            return
        
        # Include current index
        combination.append(nums[i])
        sum = sum + nums[i]
        self.combination_sum(nums, target, combination, all_combinations, sum, i )
        combination.pop()

        # Skip current index
        sum = sum - nums[i]
        self.combination_sum(nums, target, combination, all_combinations, sum, i + 1)


sol = Solution()
print(sol.cs([2,3,6,7], target = 7))