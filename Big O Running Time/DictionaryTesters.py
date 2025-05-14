# Member 1: Jair Rodriguez
# Member 2: Aaron Chavez
# Member 3: Carina Fierro-Hernandez
# Member 4: Jenna Suits
# Member 5: Javier A. Arroyo-Solis
import time
import matplotlib.pyplot as plt
timesTested = 20
# create the list from min to max of numbers
def create_list(min, max_limit) -> list:
    return list(range(min, max_limit))
# create dictionary with number as value and index as key 0:0 1:1 2:2
def create_dictionary(min, max_limit) -> dict:
    the_list = create_list(min, max_limit)
    dict = {}
    for index, element in enumerate(the_list):
        dict[index] = element
        return dict
def searchDictionary(the_dic, item):
    if item in the_dic:
        return True
# Function for testing adding into the dictionary
def addingTester(max_limit, step):
    timed_runs_1st = []
    x_vals = []
    for i in range(10, max_limit + step, step):
        x_vals.append(i)
        sum_time = 0
    for j in range(0, timesTested):
        new_dic = create_dictionary(0, i)
        start_time = time.time()
        new_dic[i + 1] = i + 1
        stop_time = time.time()
        elapsed_time = stop_time - start_time
        sum_time += elapsed_time
    elapsed_time = sum_time / timesTested
    timed_runs_1st.append(elapsed_time)
    plt.plot(x_vals, timed_runs_1st, 'r-')
    plt.xlabel('Value of n')
    plt.ylabel('Time(ms)')
    plt.legend(['Adding from the Dictionary'])
    plt.show()
# Function for testing removing from the dictionary
def removingTester(max_limit, step):
    timed_runs_1st = []
    x_vals = []
    for i in range(10, max_limit + step, step):
        x_vals.append(i)
        sum_time = 0
    for j in range(0, timesTested):
        new_dic = create_dictionary(0, i)
        start_time = time.time()
    del new_dic[i - 1]
    stop_time = time.time()
    elapsed_time = stop_time - start_time
    sum_time += elapsed_time
elapsed_time = sum_time / timesTested
timed_runs_1st.append(elapsed_time)
plt.plot(x_vals, timed_runs_1st, 'g-')
plt.xlabel('Value of n')
plt.ylabel('Time(ms)')
plt.legend(['Removing from the Dictionary'])
plt.show()
# Function for testing accessing from the dictionary
def accessingTester(max_limit, step):
    timed_runs_1st = []
    x_vals = []
    for i in range(10, max_limit + step, step):
        x_vals.append(i)
        sum_time = 0
    for j in range(0, timesTested):
        new_dic = create_dictionary(0, i)
        start_time = time.time()
        access = new_dic[i - 1]
        stop_time = time.time()
        elapsed_time = stop_time - start_time
        sum_time += elapsed_time
    elapsed_time = sum_time / timesTested
    timed_runs_1st.append(elapsed_time)
    plt.plot(x_vals, timed_runs_1st, 'b-')
    plt.xlabel('Value of n')
    plt.ylabel('Time(ms)')
    plt.legend(['Accessing from the Dictionary'])
    plt.show()
# Function for testing searching inside the dictionary
def searchingTester(max_limit, step):
    timed_runs_1st = []
    x_vals = []
    for i in range(10, max_limit + step, step):
        x_vals.append(i)
        sum_time = 0
    for j in range(0, timesTested):
        new_dic = create_dictionary(0, i)
        start_time = time.time()
        searchDictionary(new_dic, i - 1)
        stop_time = time.time()
        elapsed_time = stop_time - start_time
        sum_time += elapsed_time
    elapsed_time = sum_time / timesTested
    timed_runs_1st.append(elapsed_time)
    plt.plot(x_vals, timed_runs_1st, 'g-')
    plt.xlabel('Value of n')
    plt.ylabel('Time(ms)')
    plt.legend(['Searching in the Dictionary'])
    plt.show()
# I made each of the test into separate function as performing all four at the same
massively
# affected run time. Just uncomment the one you would like to see perform
max_limit = 1000000
step = max_limit // 100
addingTester(max_limit, step)
# removingTester(max_limit, step)
# accessingTester(max_limit, step)
# searchingTester(max_limit, step)