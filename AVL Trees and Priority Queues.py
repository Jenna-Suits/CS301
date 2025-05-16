# Week 11: AVL Trees and Priority Queues
# Javier and Jenna
#
-----------------------------------------------------------------------------------
----------------------------------------------------------
# Javier: AVL Trees
# ---------Node Class---------
class Node:
def __init__(self, data):
self.data = data
self.left = None
self.right = None
self.height = 1
# ---------AVLTree Class---------
class AVLTree:
def __init__(self):
self.root = None
# ---------Helper Methods---------
def __getHeight(self, root):
if not root:
return 0
return root.height
# Gets the height of the particular node
def __getBalance(self, root):
if not root:
return 0
return self.__getHeight(root.left) - self.__getHeight(root.right)
# Gets the balance factor of the node
def __leftRotate(self, root):
node1 = root.right
node2 = node1.left
node1.left = root
root.right = node2
root.height = 1 + max(self.__getHeight(root.left),
self.__getHeight(root.right))
node1.height = 1 + max(self.__getHeight(node1.left),
self.__getHeight(node1.right))
return node1
# Performs the left rotation when called
def __rightRotate(self, root):
node1 = root.left
node2 = node1.right
node1.right = root
root.left = node2
root.height = 1 + max(self.__getHeight(root.left),
self.__getHeight(root.right))
node1.height = 1 + max(self.__getHeight(node1.left),
self.__getHeight(node1.right))
return node1
# Perform the right rotation when called
def __getLowest(self, root):
if root is None or root.left is None:
return root
return self.__getLowest(root.left)
# Used by the delete method, this gets the lowest value from the tree
# ---------Insert Method---------
def insert(self, item):
def insertHelper(root, data):
if not root:
return Node(data)
elif data < root.data:
root.left = insertHelper(root.left, data)
else:
root.right = insertHelper(root.right, data)
root.height = 1 + max(self.__getHeight(root.left),
self.__getHeight(root.right))
balance = self.__getBalance(root)
if balance > 1 and data < root.left.data:
return self.__rightRotate(root)
if balance > 1 and data > root.left.data:
root.left = self.__leftRotate(root.left)
return self.__rightRotate(root)
if balance < -1 and data > root.right.data:
return self.__leftRotate(root)
if balance < -1 and data < root.right.data:
root.right = self.__rightRotate(root.right)
return self.__leftRotate(root)
return root
self.root = insertHelper(self.root, item)
# The Runtime for the Average and Worst Case for the insert method would be
O(n) since recursion would have a
# runtime of O(n) which this method uses. The average and the worst would be
the same since the tree would balance
# itself out if needed each insert call.
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
# Average Case: The runtime is O(log N) because it only searches half the list
every time till it finds the correct number.
# Worst Case: The runtime is O(log N) because it only searches half the list
since both insert and delete methods helps
# to balance the tree out.
# ---------Delete Method---------
def delete(self, item):
def deleteHelper(root, data):
if not root:
return root
elif data < root.data:
root.left = deleteHelper(root.left, data)
elif data > root.data:
root.right = deleteHelper(root.right, data)
else:
if root.left is None:
tempNode = root.right
root = None
return tempNode
elif root.right is None:
tempNode = root.left
root = None
return tempNode
tempNode = self.__getLowest(root.right)
root.data = tempNode.data
root.right = deleteHelper(root.right, tempNode.data)
if root is None:
return root
root.height = 1 + max(self.__getHeight(root.left),
self.__getHeight(root.right))
balance = self.__getBalance(root)
if balance > 1 and self.__getBalance(root.left) >= 0:
return self.__rightRotate(root)
if balance > 1 and self.__getBalance(root.left) < 0:
root.left = self.__leftRotate(root.left)
return self.__rightRotate(root)
if balance < -1 and self.__getBalance(root.right) <= 0:
return self.__leftRotate(root)
if balance < -1 and self.__getBalance(root.right) > 0:
root.right = self.__rightRotate(root.right)
return self.__leftRotate(root)
return root
if not self.search(item):
return False
else:
self.root = deleteHelper(self.root, item)
return True
# The Runtime for Average and Worst Case for the delete method would be O(n)
since recursion would have a
# runtime of O(n) which this method uses. The average and the worst would be
the same since the tree would balance
# itself out if needed each delete call.
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
# The Runtime for Average and Worst Case would be O(N) in any form the binary
tree take as the sorted list would
# need to visit each and every item within the Binary Tree no matter what.
# ---------Reverse Sort Method---------
def reverseSortedList(self):
main_list = []
def inorder(root):
if root:
inorder(root.right)
main_list.append(root.data)
inorder(root.left)
inorder(self.root)
return main_list
# The Runtime for Average and Worst Case would be O(N) because no matter what
to reverse sort it
# needs to check each and every item.
#
-----------------------------------------------------------------------------------
----------------------------------------------------------
# Jenna : Priority Queue
class PriorityQueue:
# insert, pop, return Queue:
def __init__(self):
self.heap = []
# insert run time:
# average runtime:O(N) because it has to go through the size of the heap from
the lowest level to the root.
# worst runtime: O(N) because it has to go through the size of the heap from
the lowest level to the root.
def insert(self, item, key):
self.heap.append((key, item))
self._heapify_up(len(self.heap) - 1)
# pop run time:
# average runtime: O(1) because it is just deleting the largest itme not having
to iterate through the heap.
# worst runtime:O(1) because it is just deleting the largest itme not having to
iterate through the heap.
def pop(self):
if not self.heap:
raise IndexError("Error")
tuple = self.heap[0]
self.heap[0] = self.heap[-1]
del self.heap[-1]
self._heapify_down(0)
# returns tuple (key,item)
return tuple
# returnQueue run time:
# average runtime: O(N) because it is iterating through the heap and adding to
the list.
# worst runtime: O(N) because it is iterating through the heap and adding to
the list.
def returnQueue(self):
return [item for key, item in sorted(self.heap, reverse=True)]
# heapify up and down:
def _heapify_up(self, index):
x = (index - 1) // 2
while index > 0 and self.heap[x][0] < self.heap[index][0]:
self.heap[index], self.heap[x] = self.heap[x], self.heap[index]
index = x
x = (index - 1) // 2
def _heapify_down(self, index):
left, right = 2 * index + 1, 2 * index + 2
largest = index
if left < len(self.heap) and self.heap[left][0] > self.heap[largest][0]:
largest = left
if right < len(self.heap) and self.heap[right][0] > self.heap[largest][0]:
largest = right
if largest != index:
self.heap[index], self.heap[largest] = self.heap[largest],
self.heap[index]
self._heapify_down(largest)