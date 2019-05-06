class Solution:
    def isValidBST(self, root):
        self.prev = None
        self.help(root)

    def help(self, root):
        self.prev = None
        return self.helper(root)

    def helper(self, root):
        if root is None:
            return True
        if not self.helper(root.left):
            return False
        if self.prev and self.prev.val >= root.val:
            return False
        self.prev = root
        return self.helper(root.right)