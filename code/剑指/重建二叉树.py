"""
给定：
前序遍历是：[3, 9, 20, 15, 7]
中序遍历是：[9, 3, 15, 20, 7]

返回：[3, 9, 20, null, null, 15, 7, null, null, null, null]
返回的二叉树如下所示：
    3
   / \
  9  20
    /  \
   15   7
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder) == 0:
            return None
        elif len(preorder) == 1:
            return TreeNode(preorder[0])
        else:
            root = TreeNode(preorder[0])
            root.left = self.buildTree(preorder[1:inorder.index(preorder[0])+1], inorder[:inorder.index(preorder[0])])
            root.right = self.buildTree(preorder[inorder.index(preorder[0])+1:], inorder[inorder.index(preorder[0])+1:])
            return root
print(0==None)