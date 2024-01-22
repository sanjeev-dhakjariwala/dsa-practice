from typing import *
from TreeNode import *

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []

        def helper(root, curr_sum, temp):
            if not root:
                return
            temp.append(root.val)
            curr_sum += root.val
            if not root.left and not root.right and curr_sum == targetSum:
                res.append(temp[:])

            helper(root.left, curr_sum, temp)
            helper(root.right, curr_sum, temp)
            temp.pop()

        helper(root, 0, [])
        return res

sol = Solution()
root = deserialize("5,4,8,11,null,13,4,7,2,null,null,5,1")
print(sol.pathSum(root, 22))