# Javier A. Arroyo-Solis
# Jenna Suits
# Week 8: Sorting Lists
# Javier
# Insertion Sort
def Insertion_Sort(list_of_items):
sorted_items = [list_of_items.pop(0)]
while list_of_items:
current_num = list_of_items.pop(0)
for num in range(0, len(sorted_items)):
if current_num < sorted_items[num]:
sorted_items.insert(num, current_num)
break
elif current_num >= sorted_items[len(sorted_items) - 1]:
sorted_items.append(current_num)
break
return sorted_items
list_for_insertion = [54, 94, 66, 29, 85, 43, 93, 34, 71, 86]
sorted_list = Insertion_Sort(list_for_insertion)
print(sorted_list)
# Insertion Sort: The runtime for this code in the worst case scenario is O(n^3)
since
# it's iterates the two list through two loops, and it uses the insert() which has
a runtime
# of O(n)
# -------------------------------------------------------------
# Jenna
# Bubble Sort
def Bubble_Sort(list_of_items):
# boolean of if items are flipped
flip = False
# compare each index to others and flip if it is the largest
for i in range(len(list_of_items) - 1):
for j in range(0, len(list_of_items) - i - 1):
if list_of_items[j] > list_of_items[j + 1]:
flip = True
list_of_items[j], list_of_items[j + 1] = list_of_items[j + 1],
list_of_items[j]
if not flip:
return
list_for_bubble = [4, 6, 9, 10, 4, 6, 3, 1, 8]
Bubble_Sort(list_for_bubble)
print(list_for_bubble)
# Bubble Sort running time: O(n^2) because it is iterating through the length of
the list twice with two for loops.
# -------------------------------------------------------------
# Javier
# Selection Sort
def Selection_Sort(list_of_items):
for i in range(len(list_of_items) - 1, -1, -1):
largest = i
for j in range(0, i):
if list_of_items[largest] < list_of_items[j]:
largest = j
temp = list_of_items[i]
list_of_items[i] = list_of_items[largest]
list_of_items[largest] = temp
return list_of_items
list_for_selection = [54, 94, 66, 29, 85, 43, 93, 34, 71, 86]
sorted_list = Selection_Sort(list_for_selection)
print(sorted_list)
# Selection Sort: The runtime for this code in the worst case scenario is O(n^2)
since
# it iterates through the length of the list twice with the use of a nested for
loops
# -------------------------------------------------------------
# Jenna
# Merge Sort
def Merge_Sort(list_of_items):
if len(list_of_items) > 1:
mid = len(list_of_items) // 2
left = list_of_items[:mid]
right = list_of_items[mid:]
# call on both sections
Merge_Sort(left)
Merge_Sort(right)
# use x,y,z to iterate through each section and resulting list
x = y = z = 0
while x < len(left) and y < len(right):
if left[x] < right[y]:
list_of_items[z] = left[x]
x += 1
else:
list_of_items[z] = right[y]
y += 1
z += 1
while x < len(left):
list_of_items[z] = left[x]
x += 1
z += 1
while y < len(right):
list_of_items[z] = right[y]
y += 1
z += 1
list_for_merge = [4, 6, 9, 10, 4, 6, 3, 1, 8]
Merge_Sort(list_for_merge)
print(list_for_merge)
# Merge Sort running time: O(nlogn) because splitting the list in half is log of n
# and when merging creates O(n) making the running time O(nlogn)
# -------------------------------------------------------------