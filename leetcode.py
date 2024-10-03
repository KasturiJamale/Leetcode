# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def mirrorImage(leftnode, rightnode):
    if leftnode is None and rightnode is None:
        return True
    elif leftnode is None or rightnode is None:
        return False
    return (leftnode.val == rightnode.val) and mirrorImage(leftnode.left, rightnode.right) and mirrorImage(
        leftnode.right, rightnode.left)


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        return mirrorImage(root.left, root.right)
