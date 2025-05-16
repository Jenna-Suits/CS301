# Member 1: Jair Rodriguez
# Member 2: Aaron Chavez
# Member 3: Carina Fierro-Hernandez
# Member 4: Jenna Suits
# Member 5: Javier A. Arroyo-Solis
# Stack Class - Jenna Suits
class Stack:
# Stack constructor
def _init_(self):
self._index = []
# PUSH: adds a new item to the top of the stack. It takes the item as an input
parameter and returns nothing
def push(self, item):
self._index.insert(0, item)
# running time: O(1) because of it just adding a new item onto the stack it
does not change the index of any other item it simply just adds it.
# POP: removes the top item from the stack and returns it. If there is no
item, returns None. It takes no input, and the stack is modified.
def pop(self):
if len(self._index) == 0:
raise Exception("Error: empty stack")
return self._index.pop(0)
# running time: O(1) because it is just taking the last item in the list
without changing any indexes.
# PEEK: returns the top item from the stack without removing it from the stack.
It takes no input, returns the top item and does not modify the stack.
def peek(self):
if len(self._index) == 0:
raise Exception("Error: empty stack")
return self._index[0]
# running time: O(1) because the function just looks at the top of the list
which is the first one out, which means there is no need to
# iterate through any other items.
# isEmpty: returns True if there are no items in the stack, False if there are
no items in it. It takes no input, and returns a Boolean value
def isEmpty(self):
if len(self._index) == 0:
raise Exception("Error: empty stack")
# running time:O(1) because it checks the length with one operation.
# SIZE: returns the size of the stack i.e. the current number of items in it.
It takes no input, and returns an integer.
def size(self):
return len(self._index)
# running time: O(1) because it checks the length in one operation.
# Queue Class - Carina Fierro-Hernandez
class Queue:
def __init__(self):
self.new_queue = []
def enqueue(self, item):
self.new_queue.append(item)
# Running time is O(1), since it is only adding the element to the end of the
list.
def dequeue(self):
if self.isEmpty():
return None
else:
return self.new_queue.pop(0)
# Running time is O(n), since the elements are getting shifted over one spot
each time after the removal.
def isEmpty(self):
if len(self.new_queue) == 0:
return True
else:
return False
# Running time is O(1), since it is only checking if the queue is empty or not.
def size(self):
return len(self.new_queue)
# Running time is O(1), since it just checks how long the list is.
# Deque Class - Aaron Chavez
class Deque:
def __init__(self):
self.items = []
# The running time of adding to front is O(n)
def addFront(self, item):
self.items.insert(0, item)
# The running time of adding to the rear is O(1)
def addRear(self, item):
self.items.append(item)
# The running time of removing from front is O(n)
def removeFront(self):
if self.isEmpty() == True:
return None
else:
return self.items.pop(0)
# The running time of removing from rear is O(1)
def removeRear(self):
if self.isEmpty() == True:
return None
else:
self.items.pop()
# The running time for checking if empty O(1)
def isEmpty(self):
if len(self.items) == 0:
return True
else:
return False
# The running time for size check is O(1)
def size(self):
return len(self.items)
# Linked List Class - Jair Rodriguez
class Node:
def __init__(self, item = None, nextNode = None):
self.item = item
self.nextNode = nextNode
class Linked_List:
def __init__(self):
self.head = None
self.size = 0
def add(self, item):
addNode = Node(item, self.head)
self.head = addNode
self.size += 1
# The runtime for the add method is O(1) because it only needs to initialize
and reinitialize
# the added items without moving any other item.
def remove(self, item):
currentNode = self.head
previousNode = None
while (currentNode != None):
if (currentNode.item == item):
if (previousNode != None):
previousNode.nextNode = currentNode.nextNode
else:
self.head = currentNode.nextNode
self.size -= 1
return
previousNode = currentNode
currentNode = currentNode.nextNode
raise KeyError(f"{item} not in the list")
# If the item is not in the list, it raises a KeyError
# The runtime for the remove method is O(n) as it needs to move to the position
of the item the
# user want to remove with the use of a while loop.
def search(self, item):
currentNode = self.head
while (currentNode != None):
if (currentNode.item == item):
return True
currentNode = currentNode.nextNode
return False
# The runtime for the search method is O(n) as it uses a while loop to search
for the item
# the user is looking for.
def isEmpty(self):
return self.size == 0
# The runtime for the isEmpty method is O(1) as it just checks the value of the
size
# attribute which keeps tracks of the size of the list.
def size(self):
return self.size
# The runtime for the size method is O(1) as it just return the value of the
size attribute.
def append(self, item):
addNode = Node(item)
if (self.head == None):
self.head = addNode
else:
currentNode = self.head
while (currentNode.nextNode != None):
currentNode = currentNode.nextNode
currentNode.nextNode = addNode
self.size += 1
# The runtime for the append method is O(n) as it needs to move to the end of
the
# linked list in order to add something at the end of the linked list.
def index(self, item):
currentNode = self.head
position = 0
while (currentNode != None):
if (currentNode.item == item):
return position
currentNode = currentNode.nextNode
position += 1
raise KeyError(f"{item} not in the list")
# If the item is not found, it raises a KeyError
# The runtime for the index method is O(n) as it uses a while loop in order to
search
# and return the desired item within the linked list.
def insert(self, position, item):
if (position < 0 or position > self.size):
raise ValueError("Invalid position")
#If the list is too short, then it raises a ValueError
if (position == 0):
self.add(item)
else:
currentNode = self.head
for i in range(position - 1):
currentNode = currentNode.nextNode
addNode = Node(item, currentNode.nextNode)
currentNode.nextNode = addNode
self.size += 1
# The insert method has a runtime of O(n) since it uses a for loop with a range
of
# the desired positions which may results in a longer time if it wants to
insert something
# at the end.
def pop(self):
if (self.isEmpty()):
raise ValueError("List is empty")
#If the list is empty, it raises a ValueError
item = self.head.item
self.head = self.head.nextNode
self.size -= 1
return item
# The pop method has a runtime of O(1) since it only need to change the values
of
# certain variables.
def pop(self, position):
if (self.isEmpty()):
raise ValueError("List is empty")
# If the list is empty, it raises a ValueError
if (position < 0 or position >= self.size):
raise ValueError("Invalid position")
# If invalid position in the list, it raises a ValueError
if (position == 0):
return self.pop()
currentNode = self.head
for i in range(position - 1):
currentNode = currentNode.nextNode
item = currentNode.nextNode.item
currentNode.nextNode = currentNode.nextNode.nextNode
#skip the item we want to remove by updating the next reference of the current item
to skip over the item being removed.
self.size -= 1
return item
# The pop(positions) method has a runtime of O(n) since it needs to move to the
# desired position in order to remove and return the desire item.
# Doubly Linked List Class - Javier A. Arroyo-Solis
class Node:
def __init__(self, item):
self.item = item
self.prev = None
self.next = None
class DoubleLinked_List:
def __init__(self):
self.head = None
def add(self, item):
if self.head is None:
new_node = Node(item)
new_node.prev = None
self.head = new_node
else:
new_node = Node(item)
self.head.prev = new_node
new_node.next = self.head
self.head = new_node
new_node.prev = None
# The Big O Runtime for the add method would be O(1) since all it needs to do
is changes the
# references of the previous head node and the new node
def remove(self, item):
curr = self.head
while curr:
if curr.item == item and curr == self.head:
if not curr.next:
self.head = None
return
else:
nextnode = curr.next
curr.next = None
nextnode.prev = None
self.head = nextnode
return
elif curr.item == item:
if curr.next:
nextnode = curr.next
prevnode = curr.prev
prevnode.next = nextnode
nextnode.prev = prevnode
curr.next = None
curr.prev = None
return
else:
prevnode = curr.prev
prevnode.next = None
curr.prev = None
return
curr = curr.next
raise KeyError("This Double Linked List does not contain " + str(item))
# The Big O Runtime for the remove method would be O(n) as it would need to
search for the item with
# the use of a while loop staring at the heading meaning it would need go
through the whole doubly linked list
# to remove something at the end (worst case).
def search(self, item):
curr = self.head
while curr:
if curr.item == item:
return True
curr = curr.next
return False
# The Big O Runtime for the search method would be O(n) as it will need to
search the whole list if
# the item it's looking for is at the end of the list.
def isEmpty(self):
if not self.head:
return True
else:
return False
# The Big O Runtime for the isEmpty method would be O(1) since it only need to
check if the head node is
# None or if it contains something.
def size(self):
counter = 0
if not self.head:
return counter
else:
curr = self.head
while curr:
counter += 1
curr = curr.next
return counter
# The Big O Runtime for the size method would be O(n) since it needs to count
each item in the list
# and thus the bigger the list, the longer it takes to count each of the items.
def append(self, item):
if self.head is None:
new_node = Node(item)
new_node.prev = None
self.head = new_node
else:
new_node = Node(item)
curr = self.head
while curr.next:
curr = curr.next
curr.next = new_node
new_node.prev = curr
new_node.next = None
# The Big O Runtime for the append method would be O(n) since it needs to move
to the end of the list
# meaning a longer list will take more time to add something at the end.
def index(self, item):
counter = 0
curr = self.head
while curr:
if curr.item == item:
return counter
counter += 1
curr = curr.next
raise KeyError("This item")
# The Big O Runtime for the index method would be O(n) because it uses a while
loop to search
# for the item's position.
def insert(self, position, item):
if position > self.size() - 1:
raise ValueError("The position is out of range.")
if position == 0:
self.add(item)
return
counter = 0
curr = self.head
while curr:
if counter == position:
new_node = Node(item)
prevnode = curr.prev
prevnode.next = new_node
new_node.prev = prevnode
curr.prev = new_node
new_node.next = curr
return
counter += 1
curr = curr.next
# The Big O Runtime for the insert method would be O(n) because it uses a while
loop to search for
# the position the item the user wants to add into the list at that position.
def pop(self):
if self.isEmpty():
raise ValueError("The list is empty")
curr = self.head
while curr.next:
curr = curr.next
prevnode = curr.prev
prevnode.next = None
curr.prev = None
return curr.item
# The Big O Runtime for the pop() method would be O(n) because it uses a
similar method as the append
# method with the difference being it removes that item and returns the same
item.
def pop(self, pos):
if self.isEmpty():
raise ValueError("The list is empty")
curr = self.head
counter = 0
while curr:
if counter == pos:
self.remove(curr.item)
return curr.item
counter += 1
curr = curr.next
# The Big O Runtime for the pop(pos) method would be O(n) because it uses a
similar method as the inserting
# method with the difference being it removes that item at that position and
returns the same item.
###################################################################################
########################################################
# QUESTIONS:
# Do you think Python’s internal representation of a list is a linked-list, a
double-linked list, or something else? Why or why not?
# We think that Python's internal representation of a list is a combination of
linked-list and double-linked list, because there are certain
# methods that only linked list and double linked lists will allow to work,
which are utilised in the internal representation of the list.
# For stack explain which type of list (python list, linked list or double-linked
list) would give the best big O running time?
# For stack doubly-linked list would give the best running time because it is
only necessary to know what is behind the current node,
# seeing as a stack is LIFO (Last in first out), the running time would be O(n)
because for searching it iterates through each node meanwhile
# having pop and peek which removes the last item and sees the previous one as
well, which is a function of the double-linked list.
# For queue explain which type of list (python list, linked list or double-linked
list) would give the best big O running time?
# Double Linked list would give the best running time, because it would take
less time, since it is not searching the elements
# and finding which ones to delete or looking for the end to append the new
item. Also, the elements would not have to shift over causing more running time.
# For dequeue explain which type of list (python list, linked list or double-linked
list) would give the best big O running time?
# Double linked list would give the best Big O running time, because it allows
the items to be added or removed from both the head and the tail of the deque with
a big O running time of O(1).
# The other types of list are not as efficient for both the beginning and the
end.
# This is key for a dequeue because in dequeues you want to be able to insert
or remove from both the beginning and the end.