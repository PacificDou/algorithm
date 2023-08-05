class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorderWalk_V2(root, ret):
    if root is None:
        return

    stack = [TreeNode('dummy', None, root)]
    while len(stack) > 0:
        node = stack.pop().right
        while node is not None:
            stack.append(node)
            node = node.left

        if len(stack) > 0:
            ret.append(stack[-1].val)

    return ret

def inorderWalk(root, ret):
    if root is None:
        return

    stack = [root]
    while len(stack) > 0:
        # push left child
        while stack[-1].left:
            stack.append(stack[-1].left)

        # pop node until has right child
        while stack:
            node = stack.pop()
            ret.append(node.val)
            if node.right:
                stack.append(node.right)
                break

    return ret



def preorderWalk(root, ret):
    if root is None:
        return

    stack = [root]
    while len(stack) > 0:
        node = stack.pop()
        ret.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return ret


# modified from https://www.geeksforgeeks.org/iterative-postorder-traversal-using-stack/
def postorderWalk(root, ret):
    if root is None:
        return

    stack = [root, root]
    while stack:
        node = stack.pop()
        # expand children of node
        if stack and node == stack[-1]:
            if node.right is not None:
                stack.extend([node.right, node.right])
            if node.left is not None:
                stack.extend([node.left, node.left])
        else:
            ret.append(node.val)

    return ret

def postorderWalk_v2(root, ret):
    if root is None:
        return

    stack = [[root, 0]]
    while len(stack) > 0:
        if stack[-1][1] == 1:
            node, _ = stack.pop()
            ret.append(node.val)
        else:
            node, _ = stack[-1]
            stack[-1][1] = 1
            if node.right:
                stack.append([node.right, 0])
            if node.left:
                stack.append([node.left, 0])

    return ret


# modified from https://www.geeksforgeeks.org/iterative-postorder-traversal-using-stack/
def postorderWalk_v3(root, ret):
    if root is None:
        return

    stack = [root]
    while len(stack) > 0:

        node = stack[-1]
        if stack[-1].right is not None:
            stack.pop()
            stack.append(node.right)
            stack.append(node)

        while node.left is not None:
            if node.left.right is not None:
                stack.append(node.left.right)
            stack.append(node.left)
            node = stack[-1]

        while len(stack) > 0:
            node = stack.pop()
            # if right child has not been visited yet
            if len(stack) > 0 and node.right == stack[-1]:
                stack.pop()
                stack.append(node)
                stack.append(node.right)
                break
            else:
                ret.append(node.val)

    return ret


if __name__ == '__main__':
    root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(5, None, TreeNode(6)))
    print('inorder:   ', inorderWalk(root, []))
    print('inorder:   ', inorderWalk_v2(root, []))
    print('preorder:  ', preorderWalk(root, []))
    print('postorder: ', postorderWalk(root, []))
    print('postorder: ', postorderWalk_v2(root, []))
    print('postorder: ', postorderWalk_v3(root, []))


