from functools import partial
from time import time
from BFS_search import breadth_first_search
from Astar_search import Astar_search
from RBFS_search import recursive_best_first_search
from puzzle_15 import Puzzle15
from puzzle_8 import Puzzle8
import numpy as np
import pandas as pd

puzzle_8_boards = [[1, 3, 4,
                    8, 6, 2,
                    7, 0, 5],
                   [2, 8, 1,
                    0, 4, 3,
                    7, 6, 5],
                   [2, 8, 1,
                    4, 6, 3,
                    0, 7, 5]]

puzzle_15_boards = [
    # 11 steps
    [1,0,2,4,
     9,5,3,8,
     10,7,6,12,
     13,14,11,15],
    # 12 steps
    [5,1,2,4,
     9,7,3,8,
     6,14,10,12,
     13,0,11,15],
    # 13 steps
    [1,3,7,0,
     6,2,8,4,
     5,14,10,12,
     9,13,11,15]]
    # # 14 steps
    # [1, 7, 2, 3,
    #  9, 5, 8, 4,
    #  13, 6, 10, 12,
    #  14, 0, 11, 15]]
    # # 15 steps
    # [1, 7, 2, 4,
    #  9, 5, 3, 8,
    #  10, 0, 11, 12,
    #  6, 13, 14, 15],
    # # 16 steps
    # [1, 6, 2, 3,
    #  5, 0, 11, 4,
    #  13, 7, 9, 8,
    #  14, 15, 10, 12]]


def main():
    configurations = [("BFS", breadth_first_search),
                      ("A_star", Astar_search)]

    puzzle_8_data = []
    puzzle_15_data = []

    run_8_puzzle(0, configurations[0][1], configurations[0][0], 1, [])

    for curr_conf_name, curr_conf_func in configurations:
        print(f'================================{curr_conf_name}================================')
        for board_index in range(len(puzzle_8_boards)):
        # for board_index in [1]:
            print(f'================================{str(board_index)}================================')
            for k in range(1,51):
                # run_8_puzzle(board_index, curr_conf_func, curr_conf_name, k, puzzle_8_data)
                run_15_puzzle(board_index, curr_conf_func, curr_conf_name, k, puzzle_15_data)

    columns = ['Algorithm', 'board_index', 'K', 'generated_nodes', 'average_time', 'total_steps', 'sol_len']

    # puzzle_8_df = pd.DataFrame(puzzle_8_data, columns=columns)
    # puzzle_8_df.to_csv("puzzle_8_results.csv")
    #
    puzzle_15_df = pd.DataFrame(puzzle_15_data, columns=columns)
    puzzle_15_df.to_csv("puzzle_15_results2.csv")



def run_8_puzzle(board_index, curr_conf_func, curr_conf_name, k, puzzle_8_data, num_iters=100):
    run_puzzle(board_index, curr_conf_func, curr_conf_name, k, puzzle_8_data, Puzzle8, puzzle_8_boards, num_iters)


def run_15_puzzle(board_index, curr_conf_func, curr_conf_name, k, puzzle_15_data, num_iters=100):
    run_puzzle(board_index, curr_conf_func, curr_conf_name, k, puzzle_15_data, Puzzle15, puzzle_15_boards, num_iters)


def run_puzzle(board_index, curr_conf_func, curr_conf_name, k, all_puzzle_data, puzzle_type, boards, num_iters):
    all_times = []
    needs_hueristic = curr_conf_name == 'A_star'
    puzzle_type = partial(puzzle_type, needs_hueristic=needs_hueristic)
    for _ in range(num_iters):
        init_puzzle = puzzle_type(boards[board_index], None, None, 0)
        type(init_puzzle).num_of_instances = 0
        total_time, solution, total_steps = curr_conf_func(init_puzzle, k)
        all_times.append(total_time)
    print(
        f"K = {k} | space : {type(init_puzzle).num_of_instances} | total time : {np.average(all_times)} | std time : {np.std(all_times)} | total steps : {total_steps}")
    all_puzzle_data.append(
        [curr_conf_name, board_index, k, type(init_puzzle).num_of_instances + 1, np.average(all_times), total_steps, len(solution)])
#     TODO - add column of solution_len


if __name__ == '__main__':
    main()
