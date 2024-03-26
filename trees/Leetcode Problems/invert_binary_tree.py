# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        for i in range(len(root)):

            left_child = 2 * i + 1
            right_child = 2 * i + 2
            #swap childred

            if(left_child <= len(root) and right_child <= len(root)):
                temp = root[left_child]
                root[left_child] = root[right_child]
                root[right_child] = temp



        return root 
        


sol = Solution()
print(sol.invertTree([4,2,7,1,3,6,9]))