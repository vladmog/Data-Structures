# Our notes from our research
import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
  
    # Insert the given value into the tree
    def insert(self, value):
        # < go left
        if not self.left and value < self.value:
          self.left = BinarySearchTree(value)
        # >= go right
        elif not self.right and value >= self.value:
          self.right = BinarySearchTree(value)

        elif value < self.value:
          self.left.insert(value)
        elif value >= self.value:
          self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        #To search a given key in Binary Search Tree, we first compare it with root, 
        # if the key is present at root, we return root. If key is greater than root's key, 
        # we recur for right subtree of root node. Otherwise we recur for left subtree.
        if self.value == target:
            return True
        elif target < self.value and self.left:
            return self.left.contains(target)
        elif target >= self.value and self.right:
            return self.right.contains(target)
        elif target < self.value and not self.left:
            return False
        elif target >= self.value and not self.right:
            return False

    # Return the maximum value found in the tree
    def get_max(self):
        # Go right until you can go right no further
        if not self.right:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # visit every node exactly one time
        # go left until you can't anymore, then
        # go back and go right
        # in here somewhere, you want to call cb(node)
        self.value = cb(self.value)
        if self.left and self.right:
            self.left = self.left.for_each(cb)
            self.right = self.right.for_each(cb)

        elif self.left:
            self.left = self.left.for_each(cb)
            
        elif self.right:
            self.right = self.right.for_each(cb)


    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass