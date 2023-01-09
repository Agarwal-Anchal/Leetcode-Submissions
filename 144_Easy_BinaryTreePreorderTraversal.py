# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        pre_order=[]
        def preOrder(root):
            if root==None:
                return None
            else:
                pre_order.append(root.val)
                if root.left: preOrder(root.left)
                if root.right: preOrder(root.right)
            return 0
        preOrder(root)
        return pre_order
