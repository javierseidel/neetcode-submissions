# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        count = k
        val = 0
        def dfs(root):
            nonlocal count
            nonlocal val
            if not root:
                return
            dfs(root.left)
            count -= 1
            if count == 0:
                val = root.val
                return
            dfs(root.right)

        if k == 0:
            return root.val
        dfs(root)
        return val

        # return arr[k-1]

