from TreeNode import *
from typing import *


class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        def is_pseudo_palindrome(freq_count):
            odd_count = 0
            for count in freq_count.values():
                if count % 2 != 0:
                    odd_count += 1
                if odd_count > 1:
                    return False
            return True

        def dfs(node, freq_count):
            if not node:
                return 0

            freq_count[node.val] += 1

            # If it's a leaf node, check if the path is pseudo-palindromic
            if not node.left and not node.right:
                count = 1 if is_pseudo_palindrome(freq_count) else 0
            else:
                # Recursively explore left and right subtrees
                count = dfs(node.left, freq_count.copy()) + \
                    dfs(node.right, freq_count.copy())

            freq_count[node.val] -= 1  # Backtrack

            return count

        # Start DFS from the root with an empty frequency count
        return dfs(root, {digit: 0 for digit in range(1, 10)})


sol = Solution()
root = deserialize("2,3,1,3,1,null,1")
print(sol.pseudoPalindromicPaths(root))
