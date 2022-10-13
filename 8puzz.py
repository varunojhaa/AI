from prettytable import PrettyTable
import numpy as np

def print_puzzel(puzzel):
    p = PrettyTable()
    for row in puzzel:
        p.add_row(row)

    print(p.get_string(header=False, border=True))

def search_empty_tile(puzzel):
    for i,row in enumerate(puzzel):
        for j,column in enumerate(row):
            if column == 0:
                return (i,j)

def misplaced_tiles(current_state):
    final_state = np.array([[ 2, 5, 3 ],[ 4, 8, 0 ],[ 7, 1, 6 ]])

    misplaced_tiles = (final_state == current_state)
    return np.size(misplaced_tiles) - np.sum(misplaced_tiles)

def possible_moves(empty_tile):
    row,col = empty_tile
    free = []

    if row > 0:
        free.append((row - 1, col))
    if col > 0:
        free.append((row, col - 1))
    if row < 2:
        free.append((row + 1, col))
    if col < 2:
        free.append((row, col + 1))

    return free

def compare_puzzel(compare_puzzel,list_of_puzzel):
    if len(list_of_puzzel) == 0:
        return [False, False]
    else:
        for puzzel in list_of_puzzel:
            return (True if np.array_equal(puzzel,compare_puzzel) else False for puzzel in list_of_puzzel)

def trace_path(node):
    path = [node]
    while node.g != 0:
        path.insert(0,node.parent)
        node = node.parent
    return path

class Puzzel:
    def __init__ (self,puzzel,parent):
        self.puzzel = puzzel
        self.parent = parent

        if self.parent != None:
            self.g = self.parent.g + 1
        else:
            self.g = 0

        self.h = misplaced_tiles(self.puzzel)
        self.empty_tile = search_empty_tile(self.puzzel)

def Greedy(puzzel,goal_state):
    frontier = []
    visited_puzzel = []
    visited_child = []
    frontier_puzzel = []

    frontier.append(puzzel)

    while frontier:
        current_state = frontier.pop(0)

        if np.array_equal(current_state.puzzel,solved_puzzel):
            path = trace_path(current_state)
            path_cost = current_state.g
            break

        moves = []
        moves = possible_moves(current_state.empty_tile)

        children = []

        for move in moves:
            change_puzzel = np.copy(current_state.puzzel)
            num = change_puzzel[move]
            empty_pos = current_state.empty_tile
            change_puzzel[move] = 0
            change_puzzel[empty_pos] = num
            child = Puzzel(change_puzzel,current_state)
            children.append(child)

        for child in children:
            if any(compare_puzzel(child.puzzel,visited_puzzel)) or any(compare_puzzel(child.puzzel,frontier_puzzel)):
                pass
            else:
                frontier.append(child)
                frontier_puzzel.append(child.puzzel)

        frontier = sorted(frontier, key=lambda x: x.h, reverse=False)

        visited_puzzel.append(current_state.puzzel)
        visited_child.append(current_state)

    return path, len(visited_child), path_cost

if __name__ == "__main__":

    initial_configuration = np.array([[ 0, 2, 3 ],[ 4, 5, 6 ],[ 7, 8, 1 ]])
    solved_puzzel = np.array([[ 2, 5, 3 ],[ 4, 8, 0 ],[ 7, 1, 6 ]])

    puzzel = Puzzel(initial_configuration,None)
    path,visited_nodes, path_cost = Greedy(puzzel,solved_puzzel)

    for node in path:
        print_puzzel(node.puzzel)
        
    print("Number of visited nodes:",visited_nodes)

    print("Path cost:",path_cost)