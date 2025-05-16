# Week 10: Binary Search Tree
# ---------Node Class---------
class Node:
def __init__(self, data):
self.data = data
self.left = None
self.right = None
# ---------Binary Tree Class---------
class BinaryTree:
def __init__(self):
self.root = None
# ---------Insert Method---------
def insert(self, item):
if not self.root:
self.root = Node(item)
else:
current = self.root
while current:
if item <= current.data:
if current.left:
current = current.left
else:
current.left = Node(item)
return
else:
if current.right:
current = current.right
else:
current.right = Node(item)
return
# Best Case: The Runtime is O(Log N) when the tree is perfectly balance since it
would only need to travel half the tree.
# Average Case: The Runtime is O(Log N) when the tree is random since it would
still only need to travel half the tree.
# Worst Case: The Runtime is O(N) when the tree is fully skewed on one side since
it would need to travel the full tree
# at that point.
# ---------Search Method---------
def search(self, item):
if not self.root:
return False
else:
current = self.root
while current:
if item == current.data:
return True
elif item < current.data:
current = current.left
else:
current = current.right
return False
# Best Case: The runtime is O(log N) because it half the list every time till it
finds the correct number.
# Average Case: The runtime is O(log N) because it half the list every time till it
finds the correct number.
# Worst Case: The runtime is O(N) using recursion to go through each and every node
of the binary tree.
# ---------Sort Method---------
def sortedList(self):
main_list = []
def inorder(root):
if root:
inorder(root.left)
main_list.append(root.data)
inorder(root.right)
inorder(self.root)
return main_list
# The Runtime for Best, Average, and Worst Case would be O(N) in any form the
binary tree take as the sorted list would
# need to visit each and every item within the Binary Tree no matter what.
# ---------Reverse Sort Method---------
def ReverseSortedList(self):
main_list = []
def inorder(root):
if root:
inorder(root.right)
main_list.append(root.data)
inorder(root.left)
inorder(self.root)
return main_list
# The Runtime time for all three best worst and average case would be O(N) because
no matter what to reverse sort it
# needs to check each and every item.