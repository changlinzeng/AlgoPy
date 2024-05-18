from datautil.tree import TreeNode


def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """
    TODO The same solution gets timeout in python but not in java
    """
    def _find_node(root: TreeNode, target: TreeNode) -> bool:
        if root is None:
            return False
        if root == target:
            return True
        if _find_node(root.left, target):
            return True
        return _find_node(root.right, target)

    if root in [p, q]:
        return root

    # p and q are in the left subtree or right subtree
    if _find_node(root.left, p) and _find_node(root.left, q):
        return lowestCommonAncestor(root.left, p, q)
    if _find_node(root.right, p) and _find_node(root.right, q):
        return lowestCommonAncestor(root.right, p, q)

    return root
