import copy


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return self.permute_helper(nums, 0)
    


    def permute_helper(self, nums, i):
        if (i == len(nums)):
            return [[]]
        
        current_permutations = []
        previous_permutations = self.permute_helper(nums, i + 1)

        for prev_permutation in previous_permutations:
            for j in range(len(prev_permutation) + 1):
                permutation_copy = copy.deepcopy(prev_permutation)
                permutation_copy.insert(j, nums[i])
                current_permutations.append(permutation_copy)

        return current_permutations


sol = Solution()
print(sol.permute([1,2,3]))


