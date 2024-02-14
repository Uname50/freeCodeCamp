# This exercise is aimed at practicing tree traversal by building a binary search tree

# Binary search tree is a data structure in which each node has at most two children, with the left child containing values less than the parent node, and the right child containing values greater that the parent node, allowing for efficient searching and sorting operations 

class TreeNode:
    def __init__(self, key):
        self.key = key

        # initially, the node has no other nodes aroung it
        self.right = None
        self.left = None

class BinarySearchTree:
    def __init__(self) -> None:
        
        # The root attribute represents the root node of the binary search tree. Since this is the constructor when a new BinarySearchTree object is created, it starts with an empty tree, so the root attribute is set to None
        self.root = None

    # define a mechanism to insert nodes in the tree. This method will be called by the user. The key parameter will be the key value to insert into the binary search tree
    def insert(self, key):
        pass