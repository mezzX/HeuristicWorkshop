import random
import copy
import numpy as np

def mk_string(board):
    '''
    This takes a numpy array and returns a string representation
    ex. 1. 2. 3.
        4. 5. 6.   =   '123456780'
        7. 8. 0.

    Params
    ======
        board(np.array) : The board to be converted into a string
    '''
    s = ''
    for n in np.nditer(board):
        s += str(int(n))

    return s

class PuzzleSolver():
    def __init__(self, size):
        '''
        Initialize parameters and creates solution board.

        Params
        ======
            size (int): Number of pieces in the grid along 1 axis.
        '''

        self.size = size
        self.frontier = {} # Dict of states that have been expanded into but not yet explored
        self.explored = {} # Dict of states that have already been explored
        self.mk_answer()

    def mk_answer(self):
        '''
        Creates a 2d np.array containing the solution.
        We set the gap to 0 and increase all the other values by 1
        to make the gap easier to find later both visually and during runtime.
        '''
        self.answer = np.zeros((self.size, self.size))
        num = 1
        for r in range(self.size):
            for c in range(self.size):
                self.answer[r][c] = num
                num += 1

        self.answer[-1][-1] = 0

    def import_puzzle(self, state):
        '''
        Converts the current board state from the GUI to a 2d np.array and adds it to the frontier. 
        We use the current location to figure out where in the np.array the value will go.
        We use the correct location to figure out the value to input into the np.array
        
        Params
        ======
            state(list): A list containing all the tile objects
        '''
        self.puzzle = np.zeros((self.size, self.size))
        for tile in state.tiles:
            # current tile position
            c_loc = tile.pos
            # correct tile position
            r_loc = tile.cor_pos
            self.puzzle[c_loc[0]][c_loc[1]] = self.answer[r_loc[0]][r_loc[1]]
        '''
        Data structure for the frontier and explored is as follows:
        frontier[key] = [Estimated Score, [Moves Taken], board]
        key(str) : A string representation of the current board
        Estimated Score(int) : The estimated path cost remaining to the goal 
                               using the Manhattan Distance Heuristic
        Moves Taken(list) : The moves taken to get the current board state from the
                            original state. The lenght of the list is used to 
                            calculate the path cost so far
        '''
        self.frontier[mk_string(self.puzzle)] = [self.score_board(self.puzzle), [], self.puzzle]

    def shuffle(self, n, seed):
        '''
        Returns a random tile order by taking n number of random actions starting from the solution board.
        prev_action is used to make sure that no 2 consecutive moves cancel each other out.
        
        Params
        ======
            n(int) : The number of random moves to generate before returning.
            seed(int) : The seed used for shuffling the board. Only used if > 0.
        '''

        if seed > 0:
            random.seed(seed)
        prev_action = None
        board = self.answer
        tile_order = []
        for _ in range(n):
            actions = self.get_actions(board)
            if prev_action in actions:
                actions.pop(actions.index(prev_action))
            action = random.choice(actions)
            prev_action = action
            board = self.sim_board(board, action)

        for i in np.nditer(board):
            tile_order.append(int(i))

        return tile_order

    def find_gap(self, board):
        '''
        Finds the coordinates of the gap of the given board.
        np.argmin returns the index of the lowest value in an array as though it was a flatten list.
        We need to convert that value into (row, column) coordinates

        Params
        ======
            board(np.array) : The board to find the gap of
        '''
        coord = np.argmin(board)
        row = coord // self.size
        col = coord % self.size
        self.gap = (row, col)

    def get_actions(self, board):
        '''
        Finds all valid actions from the given board state
        ex. 1. 2. 3.
            4. 5. 0. = ['Right', 'Down', 'Up']
            7. 8. 6.

        Params
        ======
            board(np.array)  : The board to find the valid actions of
        '''
        actions = []
        self.find_gap(board)
        if self.gap[1] > 0:
            actions.append('Right')

        if self.gap[0] > 0:
            actions.append('Down')

        if self.gap[1] < self.size - 1:
            actions.append('Left')

        if self.gap[0] < self.size - 1:
            actions.append('Up')

        return actions

    def sim_board(self, board, action):
        '''
        Applies the given action to a shallow copy of the given board to create a new board

        Params
        ======
        board(np.array) : The board to be copied and have the action applied to
        action(str) : The action to be to the board.
                      Valid actions are: 'Up', 'Down', 'Right', 'Left'.
        '''
        self.find_gap(board)
        if action == 'Up':
            coords = (self.gap[0]+1, self.gap[1])

        if action == 'Down':
            coords = (self.gap[0]-1, self.gap[1])

        if action == 'Right':
            coords = (self.gap[0], self.gap[1]-1)

        if action == 'Left':
            coords = (self.gap[0], self.gap[1]+1)

        # The value of the tile being moved.
        tile = board[coords]
        new_board = copy.copy(board)
        # Replacing the gap with the value of the tile being moved.
        new_board[self.gap] = tile
        # Replacing the value of the tile being moved with 0.
        new_board[coords] = 0

        return new_board

    def score_board(self, board):
        '''
        This is the heuristic function used to estimate the remaining path cost for the given board.
        For each tile we calculate the Manhattan Distance between the current location and correct location.
        Distance = sum(|xi1 - xi2| + |yi1 - yi2|)
            where : x1 = Current tile position
                    x2 = Correct tile position
            for i = 0 : self.size**2

        Params
        ======
        board(np.array) : The board to calculate the score for
        '''

        '''
        TODO
        ====
        For each tile:
            Find the current location.
            Find the correct location.
            Calculate the Manhattan Distance between those two locations.
        Return the sum of the Manhattan Distance over all the tiles
        '''
        raise NotImplementedError

    def expand(self, key):
        '''
        Expanding the given board by taking all valid actions not yet taken
        
        Data structure for the frontier and explored is as follows:
        explored[key] = [Estimated Score, [Moves Taken], board]
        key(str) : A string representation of the current board
        Estimated Score(int) : The estimated path cost remaining to the goal 
                               using the Manhattan Distance Heuristic
        Moves Taken(list) : The moves taken to get the current board state from the
                            original state. The lenght of the list is used to 
                            calculate the path cost so far
        
        Params
        ======
        key(str) : The string representation of the board being expanded
        '''

        '''
        TODO
        ====
        Get the np.array of the board being expanded.
        Get all the valid actions for the given board
        Iterate through all the valid actions and creating a new board for each action.
        Check that the new board hasn't been already expanded into before proceeding.
        Add the new board to the frontier
        Add the expanded board to explored and remove it from the frontier
        '''
        raise NotImplementedError

    def get_total_cost(self, entry):
        '''
        Here we will calculate the total cost of the give Path
        Cost = G + H
        Where G is the total cost of the Path thus far
        And H is the estimated cost of the remaining distance to the goal

        Params
        ======
            entry(list) : The dictionary entry for the board we want to get the total cost for.
                          It has the following structure:
                          [Estimated Score, [Moves Taken], board]
                          G = len(entry[1])
                          H = entry[0]
        '''

        '''
        TODO
        ====
        Return the total path cost for the given entry
        '''
        raise NotImplementedError

    def explore(self):
        '''
        We explore the state space by expanding a board in the frontier
        that has the lowest total cost. 
        '''
        
        '''
        TODO
        ====
        Calculate the total path cost for all boards in the frontier
        Expand the cheapest path
        '''
        raise NotImplementedError

    def solve(self, state):
        '''
        We find the solution by using a guided search through all
        the possible board combinations until a solution is found.
        We return a list with all the actions need to reach the solution from the starting board state.

        Params
        ======
            state(list): A list containing all the tile objects
        '''
        self.import_puzzle(state)
        while True:
            if mk_string(self.answer) in self.explored.keys():
                return self.explored[mk_string(self.answer)][1]
            else:
                self.explore()
                print("{} nodes in the frontier and {} nodes explored".format(len(self.frontier.keys()), len(self.explored.keys())))