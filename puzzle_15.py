class Puzzle15:
    PUZZLE_SIZE = 4
    goal_state = [1, 2, 3, 4,
                  5, 6, 7, 8,
                  9, 10, 11, 12,
                  13, 14, 15, 0]
    heuristic = None
    evaluation_function = None
    needs_hueristic = False
    num_of_instances = 0

    def __init__(self, state, parent, action, path_cost, needs_hueristic=False):
        self.parent = parent
        self.state = state
        self.action = action
        if parent:
            self.path_cost = parent.path_cost + path_cost
        else:
            self.path_cost = path_cost
        if needs_hueristic:
            self.needs_hueristic = True
            self.generate_heuristic()
            self.evaluation_function = self.heuristic + self.path_cost
        Puzzle15.num_of_instances += 1

    def __str__(self):
        return str(self.state[0:4]) + '\n' + \
               str(self.state[4:8]) + '\n' + \
               str(self.state[8:12]) + '\n' + \
               str(self.state[12:16])

    def generate_heuristic(self):
        self.heuristic = 0
        for num in range(1, Puzzle15.PUZZLE_SIZE ** 2):
            distance = abs(self.state.index(num) - self.goal_state.index(num))
            i = int(distance / Puzzle15.PUZZLE_SIZE)
            j = int(distance % Puzzle15.PUZZLE_SIZE)
            self.heuristic = self.heuristic + i + j

    def goal_test(self):
        if self.state == self.goal_state:
            return True
        return False

    @staticmethod
    def find_legal_actions(i, j):
        legal_action = ['U', 'D', 'L', 'R']
        if i == 0:  # up is disable
            legal_action.remove('U')
        elif i == Puzzle15.PUZZLE_SIZE - 1:  # down is disable
            legal_action.remove('D')
        if j == 0:
            legal_action.remove('L')
        elif j == Puzzle15.PUZZLE_SIZE - 1:
            legal_action.remove('R')
        return legal_action

    def generate_child(self):
        children = []
        x = self.state.index(0)
        i = int(x / Puzzle15.PUZZLE_SIZE)
        j = int(x % Puzzle15.PUZZLE_SIZE)
        legal_actions = self.find_legal_actions(i, j)

        for action in legal_actions:
            new_state = self.state.copy()
            if action is 'U':
                new_state[x], new_state[x - Puzzle15.PUZZLE_SIZE] = new_state[x - Puzzle15.PUZZLE_SIZE], new_state[x]
            elif action is 'D':
                new_state[x], new_state[x + Puzzle15.PUZZLE_SIZE] = new_state[x + Puzzle15.PUZZLE_SIZE], new_state[x]
            elif action is 'L':
                new_state[x], new_state[x - 1] = new_state[x - 1], new_state[x]
            elif action is 'R':
                new_state[x], new_state[x + 1] = new_state[x + 1], new_state[x]
            children.append(Puzzle15(new_state, self, action, 1, self.needs_hueristic))
        return children

    def find_solution(self):
        solution = []
        solution.append(self.action)
        path = self
        while path.parent != None:
            path = path.parent
            solution.append(path.action)
        solution = solution[:-1]
        solution.reverse()
        return solution
