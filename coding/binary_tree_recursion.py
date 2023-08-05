class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorderWalk(node, ret):
    if node is None:
        return
    inorderWalk(node.left, ret)
    ret.append(node.val)
    inorderWalk(node.right, ret)
    return ret


def preorderWalk(node, ret):
    if node is None:
        return
    ret.append(node.val)
    preorderWalk(node.left, ret)
    preorderWalk(node.right, ret)
    return ret


def postorderWalk(node, ret):
    if node is None:
        return
    postorderWalk(node.left, ret)
    postorderWalk(node.right, ret)
    ret.append(node.val)
    return ret


if __name__ == '__main__':
    root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(5, None, TreeNode(6)))
    print('inorder:   ', inorderWalk(root, []))
    print('preorder:  ', preorderWalk(root, []))
    print('postorder: ', postorderWalk(root, []))

