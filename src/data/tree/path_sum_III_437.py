from typing import Optional

from datautil.tree import TreeNode, Tree


def pathSum(root: Optional[TreeNode], targetSum: int) -> int:
    num_tree = 0

    def _dfs(node: Optional[TreeNode], target: int) -> None:
        if node is None:
            return
        _find_path(node, target)
        _dfs(node.left, target)
        _dfs(node.right, target)

    def _find_path(node: Optional[TreeNode], target: int) -> None:
        if node is None:
            return
        if target == node.val:
            nonlocal num_tree
            num_tree += 1
        _find_path(node.left, target - node.val)
        _find_path(node.right, target - node.val)

    _dfs(root, targetSum)
    return num_tree


if __name__ == '__main__':
    print(pathSum(Tree.deserialize('10,5,-3,3,2,null,11,3,-2,null,1'), 8))
    print(pathSum(Tree.deserialize('-2,null,-3'), -2))
    print(pathSum(Tree.from_preorder_inorder('1,2,3,4,5', '1,2,3,4,5'), 3))
