class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, root, key):
        if not root:
            return TreeNode(key)
        
        if key < root.value:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        
        root.height = 1 + max(self._get_height(root.left), self._get_height(root.right))
        balance = self._get_balance(root)

        # Perform rotations if necessary
        if balance > 1:
            if key < root.left.value:
                return self._right_rotate(root)
            else:
                root.left = self._left_rotate(root.left)
                return self._right_rotate(root)
        if balance < -1:
            if key > root.right.value:
                return self._left_rotate(root)
            else:
                root.right = self._right_rotate(root.right)
                return self._left_rotate(root)
        
        return root

    def _get_height(self, node):
        return node.height if node else 0

    def _get_balance(self, node):
        return self._get_height(node.left) - self._get_height(node.right)

    def _left_rotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def _right_rotate(self, y):
        z = y.left
        T3 = z.right

        z.right = y
        y.left = T3

        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))

        return z

    def inorder_traversal(self, root):
        if root:
            self.inorder_traversal(root.left)
            print(root.value, end=" ")
            self.inorder_traversal(root.right)

if __name__ == "__main__":
    avl_tree = AVLTree()
    keys = [10, 20, 30, 40, 50, 25]
    for key in keys:
        avl_tree.root = avl_tree.insert(avl_tree.root, key)

    print("Inorder traversal of AVL tree:")
    avl_tree.inorder_traversal(avl_tree.root)
