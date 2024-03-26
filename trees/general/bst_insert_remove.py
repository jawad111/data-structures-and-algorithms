class TreeNode:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    def insert(self, root, node_value):
        if root is None:
            return TreeNode(node_value)
        if(node_value > root.value):
            root.right = self.insert(root.right, node_value)
        if(node_value < root.value):
            root.left = self.insert(root.left, node_value)
        return root
    

    def remove(self, root, node_value):

        if root is None:
            return None
        
        # Keep Going down and try to find value
        if(node_value > root.value):
            root.right = self.remove(root.right, node_value)
        if(node_value < root.value):
            root.left = self.remove(root.left, node_value)
        
        # if value is found 
        else:
            # if value has less than two children
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left

            # if value has two children (use main root node to understand)
            minimum_node = self.findMinimumNode(root.right)
            root.value = minimum_node.value
            root.right = self.remove(root.right, minimum_node.value)



        # after all conditions execute
        return root



    #Helper Functions
    def findMinimumNode(self, node):
        while (node is not None) and (node.left is not None):
            node = node.left
        return node


            




 

    ################################################################################################################
    ############################################### FOR DISPLAY ONLY ###############################################
    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = "%s" % self.value
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle
        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = "%s" % self.value
            u = len(s)
            first_line = (x + 1) * " " + (n - x - 1) * "_" + s
            second_line = x * " " + "/" + (n - x - 1 + u) * " "
            shifted_lines = [line + u * " " for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2
        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = "%s" % self.value
            u = len(s)
            first_line = s + x * "_" + (n - x) * " "
            second_line = (u + x) * " " + "\\" + (n - x - 1) * " "
            shifted_lines = [u * " " + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2
        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = "%s" % self.value
        u = len(s)
        first_line = (x + 1) * " " + (n - x - 1) * "_" + s + y * "_" + (m - y) * " "
        second_line = (
            x * " " + "/" + (n - x - 1 + u + y) * " " + "\\" + (m - y - 1) * " "
        )
        if p < q:
            left += [n * " "] * (q - p)
        elif q < p:
            right += [m * " "] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * " " + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2
    ################################################################################################################




root = TreeNode(4)

root.insert(root, 6)
root.insert(root, 3)
root.insert(root, 6)
root.insert(root, 2)
root.insert(root, 5)
root.insert(root, 7)


root.display()
print("\n")

root.remove(root, 4)

root.display()

