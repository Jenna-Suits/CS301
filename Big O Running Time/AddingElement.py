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
def addElement(thelist, insertion):
    thelist.insert(insertion, 34)
def tester(max_limit, step):
    timed_runs_1st = []
    timed_runs_2nd = []
    timed_runs_3rd = []
    x_vals = []
    for i in range(0, max_limit + step, step):
        x_vals.append(i)
        # time the first function with the current value of n
        sum_time = 0
        for j in range(0, timesTested):
            new_list = create_list(0, i)
            start_time = time.time()
            addElement(new_list, 0)
            stop_time = time.time()
            elapsed_time = stop_time - start_time
            sum_time += elapsed_time
        elapsed_time = sum_time / timesTested
        timed_runs_1st.append(elapsed_time)
        sum_time = 0
        for j in range(0, timesTested):
            new_list = create_list(0, i)
            start_time = time.time()
            addElement(new_list, i // 2)
            stop_time = time.time()
            elapsed_time = stop_time - start_time
            sum_time += elapsed_time
        elapsed_time = sum_time / timesTested
        timed_runs_2nd.append(elapsed_time)
        sum_time = 0
        for j in range(0, timesTested):
            new_list = create_list(0, i)
            start_time = time.time()
            addElement(new_list, i - 1)
            # new_list.append(34)
            stop_time = time.time()
        elapsed_time = stop_time - start_time
        sum_time += elapsed_time
        elapsed_time = sum_time / timesTested
        timed_runs_3rd.append(elapsed_time)
    plt.plot(x_vals, timed_runs_1st, 'r-')
    plt.plot(x_vals, timed_runs_2nd, 'b-')
    plt.plot(x_vals, timed_runs_3rd, 'g-')
    plt.xlabel('Value of n')
    plt.ylabel('Time(ms)')
    plt.legend(['Add at the start', 'Add at the middle', 'Add at the end'])
    plt.show()
    
max_limit = 1000000
step = max_limit // 100
tester(max_limit, step)