import time
from queue import PriorityQueue, Queue
import numpy as np


def Astar_search(initial_state, thread_number=1):
    count = 0
    explored = []
    start_node = initial_state
    q, q_temp = PriorityQueue(), Queue()
    q.put((start_node.evaluation_function, count, start_node))
    i = 0
    total_steps = 0
    total_time = np.float64(0)
    threads_list_times = []

    while not q.empty():
        t0 = time.perf_counter()
        i += 1
        node = q.get()
        node = node[2]
        children = node.generate_child()
        for child in children:
            if child.state not in explored:
                q_temp.put(child)

        t1 = time.perf_counter()
        diff = t1 - t0
        threads_list_times.append(diff)

        if i == thread_number or q.empty():
            total_time += max(threads_list_times)
            threads_list_times = []
            i = 0
            total_steps += 1

            while not q_temp.empty():
                curr_node = q_temp.get()
                count += 1
                if curr_node.goal_test():
                    return total_time, curr_node.find_solution(), total_steps
                q.put((curr_node.evaluation_function, count, curr_node))
    return
