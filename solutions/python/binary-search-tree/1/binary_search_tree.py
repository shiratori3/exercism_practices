class TreeNode:
    def __init__(self, data: str, left=None, right=None):
        self.data = data if data else None
        self.left = left
        self.right = right

    def __str__(self):
        return f'TreeNode(data={self.data}, left={self.left}, right={self.right})'

    def insert(self, num: str):
        if int(num) <= int(self.data):
            if self.left:
                self.left.insert(num)
            else:
                self.left = TreeNode(num)
        else:
            if self.right:
                self.right.insert(num)
            else:
                self.right = TreeNode(num)


class BinarySearchTree:
    def __init__(self, tree_data: list[str]):
        if not tree_data:
            return TreeNode(None)
        for index, num in enumerate(tree_data):
            if index == 0:
                self.tree = TreeNode(num)
            else:
                self.tree.insert(num)

    def data(self):
        print(self.tree)
        return self.tree

    def sorted_data(self):
        def inorder(node, result):
            if node:
                inorder(node.left, result)
                result.append(node.data)
                inorder(node.right, result)
        
        result = []
        inorder(self.tree, result)
        return result
