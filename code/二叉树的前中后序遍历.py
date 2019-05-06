def preorderTraversal(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    value = []
    help = []
    while len(help) != 0 or root is not None:
        while root is not None:
            value.append(root.val)
            help.append(root)
            root = root.left
        root = help.pop()
        root = root.right
    return value


def inorderTraversal(root):
        # 一个栈 如果栈不为空或者root也不为空的时候一直压root.left直到root为None
        # 然后弹出一个值将root改为弹出值的right
        res = []
        if root is not None:
            stack1 = []
            while len(stack1) > 0 or root is not None:
                if root is not None:
                    stack1.append(root)
                    root = root.left
                else:
                    root = stack1.pop()
                    res.append(root.val)
                    root = root.right
        return res


def postorderTraversal(root):
        # 两个栈一个按照根左右的方式如  第二个接收所有从第一个栈中出来的的元素
        # 然后弹出
        res = []
        if root is None:
            return res
        stack1 = []
        stack2 = []
        stack1.append(root)
        while len(stack1) > 0:
            node = stack1.pop()
            stack2.append(node)
            if node.left is not None:
                stack1.append(node.left)
            if node.right is not None:
                stack1.append(node.right)
        while len(stack2) > 0:
            res.append(stack2.pop().val)
        return res