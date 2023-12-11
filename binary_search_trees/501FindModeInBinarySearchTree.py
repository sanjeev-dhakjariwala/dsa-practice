class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMode(self, root):
        def inOrderTraversal(node):
            nonlocal current_val, current_count, max_count, modes

            if not node:
                return

            inOrderTraversal(node.left)

            # Update current value and count
            if node.val == current_val:
                current_count += 1
            else:
                current_val = node.val
                current_count = 1

            # Update modes based on current count and max count
            if current_count == max_count:
                modes.append(node.val)
            elif current_count > max_count:
                modes = [node.val]
                max_count = current_count

            inOrderTraversal(node.right)

        if not root:
            return []

        current_val, current_count, max_count, modes = float('inf'), 0, 0, []

        inOrderTraversal(root)

        return modes


# Example usage
sol = Solution()

# Example tree
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(2)

print(sol.findMode(root))  # Output: [2]
