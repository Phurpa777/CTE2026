''''#task 1
# Node class
class Node:
    def __init__(self, value):
        self.value = value        # Value of the node
        self.left = None          # Left child reference
        self.right = None         # Right child reference
# Binary Tree class
class BinaryTree:
    def __init__(self, root_value=None):
        if root_value is None:
            self.root = None      # Empty tree
        else:
            self.root = Node(root_value)   # Tree with root node
# Example usage
tree = BinaryTree()
if tree.root is None:
    print("Created new Binary Tree")
    print("Root:", tree.root)'''
#task 2
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    # 1. Height of tree (max depth)
    def height(self, node):
        if node is None:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))

    # 2. Total number of nodes
    def size(self, node):
        if node is None:
            return 0
        return 1 + self.size(node.left) + self.size(node.right)

    # 3. Count leaf nodes
    def count_leaves(self, node):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 1
        return self.count_leaves(node.left) + self.count_leaves(node.right)

    # 4. Check full binary tree (each node has 0 or 2 children)
    def is_full_binary_tree(self, node):
        if node is None:
            return True
        
        if node.left is None and node.right is None:
            return True
        
        if node.left and node.right:
            return (self.is_full_binary_tree(node.left) and
                    self.is_full_binary_tree(node.right))
        
        return False

    # 5. Check complete binary tree
    def is_complete_binary_tree(self):
        if self.root is None:
            return True
        
        queue = [self.root]
        end = False
        
        while queue:
            current = queue.pop(0)
            
            if current is None:
                end = True
            else:
                if end:
                    return False
                
                queue.append(current.left)
                queue.append(current.right)
        
        return True


# Example Tree Creation
tree = BinaryTree(Node(1))
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)


# Example Output
print("Tree Height:", tree.height(tree.root))
print("Total Nodes:", tree.size(tree.root))
print("Leaf Nodes Count:", tree.count_leaves(tree.root))
print("Is Full Binary Tree:", tree.is_full_binary_tree(tree.root))
print("Is Complete Binary Tree:", tree.is_complete_binary_tree())