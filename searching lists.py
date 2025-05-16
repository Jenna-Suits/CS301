# Week 7
# Jenna Suits
# Javier A. Arroyo-Solis
# Binary Search
def search_sorted_list(sorted_list, item):
# assign left right and middle of the list to an index
left = 0
right = len(sorted_list)
mid = (left + right) // 2
# if the item is not in list return False
if len(sorted_list) == 1 and sorted_list[0] != item:
return False
# if mid = item then returns that index
if sorted_list[mid] == item:
return mid
elif sorted_list[mid] < item:
sorted_list = sorted_list[mid:right]
x = search_sorted_list(sorted_list, item)
return x + mid if x != False else x
elif sorted_list[mid] > item:
sorted_list = sorted_list[left:mid]
x = search_sorted_list(sorted_list, item)
return x + left if x != False else x
# HashList
# HashList(length) creates a new empty HashList of the given length.
class HashList:
def __init__(self, length):
self.list = [None] * length
self.length = length
# hashfunction(item) tells you which slot the item is assigned to.
# The Big O Runtime of the hashfunction method would be O(1) because it only
returns the value
# of a single operation.
def hashfunction(self, item):
return item % self.length
# put(item) adds the given item to the list. If the list is full, it throws an
error.
# The Big O runtime of the put method would be O(1) in the best-case scenario
as it would only need
# to assign that item at that slot. In the worse-case scenario, it would be
O(n) since it would need
# to iterate through the whole list to show that it's full.
def put(self, item):
slot = self.hashfunction(item)
if self.list[slot] is None:
self.list[slot] = item
else:
next_slot = self.hashfunction(item + 1)
while self.list[next_slot] is not None:
next_slot = self.hashfunction(next_slot + 1)
if next_slot == slot:
raise Exception("HashTable is full")
if self.list[next_slot] is None:
self.list[next_slot] = item
# contains(item) returns True if the given item is in the list, and False
otherwise. Make sure
# your method still works in the extreme case in which the list is entirely full
and the given item isn’t in the list.
# The Big O runtime of the contains method would be O(1) in the best-case
scenario as it would only need
# to show that item is in that slot. In the worse-case scenario, it would be
O(n) since it would need
# to iterate through the whole list to show the item is not there.
def contains(self, item):
slot = self.hashfunction(item)
if self.list[slot] == item:
return True
else:
next_slot = self.hashfunction(item + 1)
while self.list[next_slot] != item:
next_slot = self.hashfunction(next_slot + 1)
if next_slot == slot:
return False
if self.list[next_slot] == item:
return True
# items() returns a list of all items in the HashList
# The Big O runtime of the item method would be O(n) in relations to the length
of the list
# as it need to check each item in the list to see if it's something or just
None.
def item(self):
return_list = []
for i in self.list:
if i is not None:
return_list.append(i)
return return_list
# How would you modify the hash table into a dictionary?
# In order to convert the HashList so that it uses a dictionary instead is first
change the
# constructor so that it creates a dictionary with the keys being numbers in
ascending order and
# the items for those keys being None. The hashfunction, put, and item methods
would stay the same with only
# minor changes but the contains method could use the contains (in) to make the
runtime from O(n) to O(1).