
import copy

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        current_set, all_subsets = [], []
        self.helper(nums, current_set, all_subsets, 0)
        print(all_subsets)
        return all_subsets




    def helper(self, nums, current_set, all_subsets, i):

        if(i >= len(nums)):
            all_subsets.append(copy.deepcopy(current_set))
            return

        #include current index
        current_set.append(nums[i])
        self.helper(nums, current_set, all_subsets, i + 1)
        current_set.pop()

        #not include current index
        self.helper(nums, current_set, all_subsets, i + 1)
    


sol = Solution()
sol.subsets([1,2,3])