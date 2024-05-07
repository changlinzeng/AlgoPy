from typing import List

from datautil.tree import TreeNode, Tree


def distanceK(root: TreeNode, target: TreeNode, k: int) -> List[int]:

    def _find_target(root: TreeNode, target: TreeNode) -> List[TreeNode]:
        """
        find the path to target
        """
        if root is None:
            return []
        if root == target:
            return [target]
        path = _find_target(root.left, target)
        if len(path) > 0:
            return [root] + path
        path = _find_target(root.right, target)
        if len(path) > 0:
            return [root] + path
        return []

    def _find_child(root: TreeNode, k: int, nodes: List[int]):
        if root is None:
            return
        if k == 0:
            nodes.append(root.val)
            return
        _find_child(root.left, k - 1, nodes)
        _find_child(root.right, k - 1, nodes)

    def _find_distance(root: TreeNode, target: TreeNode, k: int, nodes: List[int]) -> int:
        if root is None:
            return -1
        if root == target:
            return 0

        # find the distance of current node to target
        dist = _find_distance(root.left, target, k, nodes)
        left_side = dist != -1
        if dist == -1:
            dist = _find_distance(root.right, target, k, nodes)

        # target not in the subtree of current node
        if dist == -1:
            return -1

        dist += 1
        if dist == k:
            nodes.append(root.val)
        elif dist < k:
            if left_side:
                # target is on left subtree
                _find_child(root.right, k - dist - 1, nodes)
            else:
                # target is on right subtree
                _find_child(root.left, k - dist - 1, nodes)
        return dist

    # Solution 1
    nodes = []
    _find_child(target, k, nodes)
    _find_distance(root, target, k, nodes)
    return nodes

    # Solution 2
    # nodes = []
    # # find child nodes with distance k to target
    # _find_child(target, k, nodes)
    # path_to_target = _find_target(root, target)
    # 
    # len1 = 0  # distance from ancestor to target
    # index = len(path_to_target) - 2  # skip target
    # while index >= 0:
    #     node = path_to_target[index]
    #     index -= 1
    #     len1 += 1
    #     if len1 == k:
    #         nodes.append(node.val)
    #         break
    #     if node.left in path_to_target:
    #         # find child nodes with distance k - (len(path_to_target) - i - 1) to node on right
    #         _find_child(node.right, k - len1 - 1, nodes)
    #     else:
    #         _find_child(node.left, k - len1 - 1, nodes)
    # return nodes


if __name__ == '__main__':
    # root = Tree.deserialize('3,5,1,6,2,0,8,null,null,7,4')
    # target = Tree.find_node(root, 5)
    root = Tree.deserialize('0,1,2,null,3')
    target = Tree.find_node(root, 3)
    print(distanceK(root, target, 3))
