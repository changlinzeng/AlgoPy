from typing import Optional, List

from datautil.tree import TreeNode, Tree


def recoverTree(root: Optional[TreeNode]) -> None:

    def _dfs(node: Optional[TreeNode],
             parent: Optional[TreeNode],
             prev: List[Optional[TreeNode]],  # tuple of (node, parent)
             swapped: List[tuple[TreeNode, TreeNode]]) -> None:
        if node is None:
            return
        _dfs(node.left, node, prev, swapped)
        if prev[0] is not None and node.val < prev[0].val:
            if len(swapped) == 0:
                swapped.append((prev[0], prev[1]))
            if len(swapped) == 2:
                swapped.pop()
            swapped.append((node, parent))
        prev[0] = node
        prev[1] = parent
        _dfs(node.right, node, prev, swapped)

    swapped = []
    _dfs(root, None, [None, None], swapped)

    node1, node2 = swapped[0][0], swapped[1][0]
    node1.val, node2.val = node2.val, node1.val


if __name__ == '__main__':
    root = Tree.deserialize('1,3,null,null,2')
    recoverTree(root)
    print('a')
