from typing import Optional, List


class TreeNode:
    def __init__(self, val: int = None):
        self.val = val
        self.left = None
        self.right = None

    def serialize(self) -> str:
        """
        :return: str representing the level order traversal result of the tree
        """
        ser = []
        q = [self]
        while len(q) > 0:
            node = q[0]
            q = q[1:]
            if node is None:
                ser.append('null')
                continue
            ser.append(str(node.val))
            q.append(node.left)
            q.append(node.right)

        # drop trailing nulls
        for i in reversed(range(len(ser))):
            if ser[i] != 'null':
                return ','.join(ser[:i + 1])
        return ','.join(ser)

    def preorder(self) -> str:
        def _preorder(node: TreeNode) -> str:
            if node is None:
                return ''
            ser = str(node.val)
            if node.left is not None:
                ser = f'{ser},{_preorder(node.left)}'
            if node.right is not None:
                ser = f'{ser},{_preorder(node.right)}'
            return ser
        return _preorder(self)

    def inorder(self) -> str:
        def _inorder(node: TreeNode) -> str:
            if node is None:
                return ''
            ser = f'{node.val}'
            if node.left is not None:
                ser = f'{_inorder(node.left)},{ser}'
            if node.right is not None:
                ser = f'{ser},{_inorder(node.right)}'
            return ser
        return _inorder(self)


class Tree:
    def __init__(self):
        self.root = TreeNode()

    @staticmethod
    def deserialize(data: str) -> Optional[TreeNode]:
        """
        :param data: str representing the level order representation of the tree
        :return: root node of the tree
        """
        vals = data.split(',')
        if vals[0] == 'null':
            return None
        root = TreeNode(int(vals[0]))
        q = [root]
        i = 1
        while len(q) > 0 and i < len(vals):
            parent = q[0]
            q = q[1:]
            left_val = vals[i]
            if left_val != 'null':
                left = TreeNode(int(left_val))
                parent.left = left
                q.append(left)

            i += 1
            if i < len(vals):
                right_val = vals[i]
                if right_val != 'null':
                    right = TreeNode(int(right_val))
                    parent.right = right
                    q.append(right)
                i += 1
        return root

    @staticmethod
    def from_preorder_inorder(preorder: str, inorder: str) -> Optional[TreeNode]:
        def build(preorder: List[int], pos: dict, start: int, end: int, index: int) -> Optional[TreeNode]:
            """
            :param start: start index in inorder
            :param end: end index in inorder
            :param index: current index in preorder
            """
            if start > end:
                return None
            parent = TreeNode(int(preorder[index]))
            inorder_index = pos[preorder[index]]
            left_len = inorder_index - start
            right_parent = index + left_len + 1  # index of right parent
            parent.left = build(preorder, pos, start, inorder_index - 1, index + 1)
            parent.right = build(preorder, pos, inorder_index + 1, end, right_parent)
            return parent
        inorder_arr = [int(v) for v in inorder.split(',')]
        preorder_arr = [int(v) for v in preorder.split(',')]
        inorder_pos = {}
        for i, v in enumerate(inorder_arr):
            inorder_pos[v] = i
        return build(preorder_arr, inorder_pos, 0, len(inorder_arr) - 1, 0)

    @staticmethod
    def find_node(root: TreeNode, val: int) -> Optional[TreeNode]:
        if root is None:
            return None
        if root.val == val:
            return root
        if (node := Tree.find_node(root.left, val)) is not None:
            return node
        if (node := Tree.find_node(root.right, val)) is not None:
            return node
        return None
