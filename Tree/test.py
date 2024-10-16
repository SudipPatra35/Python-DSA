class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BST:
    def bstFromPreorder(self, preorder):
        self.index = 0  # Initialize index to track current node in preorder traversal
        if not preorder:
            return None
        return self.bstFromPreorderUtil(preorder, float('-inf'), float('inf'))

    def bstFromPreorderUtil(self, preorder, lower, upper):
        if self.index == len(preorder):
            return None
        
        value = preorder[self.index]
        
        if value < lower or value > upper:
            return None
        
        root = Node(value)
        self.index += 1
        
        root.left = self.bstFromPreorderUtil(preorder, lower, value)
        root.right = self.bstFromPreorderUtil(preorder, value, upper)
        
        return root

    def inorder(self, root):
        result = []
        if root:
            result.extend(self.inorder(root.left))
            result.append(root.data)
            result.extend(self.inorder(root.right))
        return result

# Example usage:
if __name__ == "__main__":
    bst = BST()
    preorder = [30, 8, 14, 64, 47, 10, 15]
    root = bst.bstFromPreorder(preorder)
    inorder_result = bst.inorder(root)
    print("Constructed BST from preorder:", inorder_result)
