from collections import deque
# Week 5
# Jenna Suits
# Carina Fierro-Hernandez
# Aaron Chavez
# Javier A. Arroyo-Solis
# Problem 1
def smallestMultiple(N, S):
queue = deque()
queue.append("")
found = False
while queue != [] and found == False:
current = queue.popleft()
for i in S:
sy = current + str(i)
if int(sy) % N == 0:
print("Found it:", sy)
found = True
queue.append(sy)
# For the first problem, The runtime would be O(n * 2) since it would need to
iterate through the queue
# with a while loop and a for loop inside of it resulting in a runtime of O(n * 2).
# Problem 2
def MazeSolver(M, D):
adjacent_cell = []
rowNum = [-1, 0, 0, 1]
colNum = [0, -1, 1, 0]
mazeX = len(M)
mazeY = len(M[0])
visit = [[False for i in range(mazeY)] for j in range(mazeX)]
queue = deque([(0, 0, [(0, 0)])])
while queue:
x, y, path = queue.popleft()
if (x, y) == D:
return path
if M[x][y] == 0 or visit[x][y]:
continue
visit[x][y] = True
for i in range(4):
newX, newY = x + rowNum[i], y + colNum[i]
if (0 <= newX < mazeX) and (0 <= newY < mazeY):
adjacent_cell.append((newX, newY))
for item in adjacent_cell:
queue.append((item[0], item[1], path + [item]))
return None
# Running Time:
# The Runtime for this program would be O(n^2) in the worst case scenario. The
leading cause of this
# is the size of the maze and the location the user would want to look for. A
larger maze to look
# through as well as a location further away will make the runtime larger.
# Problem 3
def StringOperator(string, operations):
new_string = ""
string_list = [letter for letter in string]
for letter in operations:
if letter == 'P':
char = string_list.pop(0)
new_string = new_string + char
if letter == 'R':
string_list.reverse()
return new_string
# Running Time:
# The runtime for this program would be O(n^2) in the worst case scenario. The
leading cause of this is the
# operation string as the length of it may cause the reverse method to occur more
frequently which increases
# the runtime of the program.