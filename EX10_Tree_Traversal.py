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
        
        # the root attribute represents the root node of the binary search tree. Since this is the constructor when a new BinarySearchTree object is created, it starts with an empty tree, so the root attribute is set to None
        self.root = None

    # define a mechanism to insert nodes in the tree. This method will be called by the user. The key parameter will be the key value to insert into the binary search tree
    def insert(self, key):
        self.root = self._insert(self.root, key)

    # helper function and does the actual insertion. This method is recursive, meaning it calls itself to traverse the tree until the appropriate location for the new node is found
    def _insert(self, node, key):
        
        # check if the node parameter is None. If it is, this means that the method has reached a leaf node or an empty spot in the tree where the new node should be inserted
        if node is None:
            return TreeNode(key)
        
        # Checking the principle for binary trees: 
        # Values smaller than the key are placed in the left subtree
        # Values greater than the key are placed in the right subtree
        if key < node.key:
            # if True, the new node should be placed in the left subtree
            node.left = self._insert(node.left, key)
        elif key > node.key:
            # otherwise, the new node should be inserted in the right subtree
            node.right = self._insert(node.right, key)

        # after the insertion process is complete, update the tree structure at the higher levels of the recursive call stack
        return node
    
    # method with search functionality
    def search(self, key):

        # self.root: This is the root of the binary search tree. The search starts from the root.
        # key: This is the value that the user wants to find in the binary search tree 
        return self._search(self.root, key)
    
    def _search(self, node, key):
        # base case for the recursive search
        # if node is None: This indicates that the search has reached the end of a branch without finding the key 
        # if node.key == key: This means that the key has been found in the current node 
        if node is None or node.key == key:
            return node 
        
        # check if the target key is less than the key of the current node
        if key < node.key:
            return self._search(node.left, key)
        
        # otherwise 
        return self._search(node.right, key)
    
    # method to delete nodes
    def delete(self, key):
        # the deletion operation might result in a new root (for example, if the node to be deleted is the current root) 
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        
        # when the current node is None, the key to be deleted was not found
        if node is None:
           return node 
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)

        # handle the case if the node has 2 children
        else:
           
           # when node.left is None, there is no left child. Therefore, return the right child from the new if block as a replacement
            if node.left is None:
                return node.right
            
            # same for the right child
            elif node.right is None:
                return node.left
            
            # if neither condition is met, the node has both children. To choose a successor, find the min value to the right subtree, which will be the in-order successor of the current node 
            node.key = self._min_value(node.right)

            # after finding the minimum value, you will need to recursively delete the node with the minimum value from the right subtree. This step ensures that the node with the minimum value is removed from the tree while maintaining the binary search tree (BST) property
            node.right = self._delete(node.right, node.key)

        # return the current node
        return node
    
    def _min_value(self, node):

        # to find the smallest value in the right subtree, iterate through the left children of the given node until reaching the leftmost (smallest) node in the subtree
        while node.left is not None:
            self.node = node.left
        
        # once the leftmost node is found (that is, when node.left becomes None), the loop exits. Return the key of the leftmost node, which represents the minimum value in the given subtree
        return node.key
    
    # method for performing an in-order traversal of the binary search tree. It returns the keys of the nodes in sorted order
    def inorder_traversal(self):

        # list to store the keys of the nodes in sorted order
        result = []

        # start the traversal from the root of the binary search tree (self.root), and the result list will be passed to accumulate the keys during the traversal
        self._inorder_traversal(self.root, result)

        # return the sorted list of keys
        return result
    
    # node: current node being considered during the traversal
    # result: list to which the keys are appended in sorted order
    def _inorder_traversal(self, node, result):
        
        # check if the current node (node) is not empty
        if node: 
            self._inorder_traversal(node.left, result)

            # append the key of the current node to the result list
            result.append(node.key)