from random import randint, shuffle, choice
import sys
import time
import csv
import platform
import os
import os.path

# this is a stepcounter
# it increments by 1 everytime the search function gets called
# this is why we start at -1 so that the first time it gets called it increments to 0 steps
stepcount = -1
grid = []
# needed for DFS...cls
sys.setrecursionlimit(10000)

# Each maze cell contains a tuple of directions of cells to which it is connected
# Takes a maze and converts it to an array of X's and blanks to represent walls, etc


def convert(maze):
    pretty_maze = [["1"]*(2*len(maze[0])+1) for a in range(2*len(maze)+1)]
    for y, row in enumerate(maze):
        for x, col in enumerate(row):
            pretty_maze[2*y+1][2*x+1] = "0"
            for direction in col:
                pretty_maze[2*y+1+direction[0]][2*x+1+direction[1]] = "0"
    pretty_maze[2*len(maze)-1][2*len(maze[0])-1] = '2'
    return pretty_maze

# Takes a converted maze and pretty prints it


def pretty_print(maze):
    for a in maze:
        string = ""
        for b in a:
            string += b
        print(string)
    print

# Returns an empty maze of given size


def make_empty_maze(width, height):
    maze = [[[] for b in range(width)] for a in range(height)]
    return maze

# Recursive backtracker.
# Looks at its neighbors randomly, if unvisitied, visit and recurse


def DFS(maze, coords=(0, 0)):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    shuffle(directions)
    for direction in directions:
        new_coords = (coords[0] + direction[0], coords[1] + direction[1])
        if (0 <= new_coords[0] < len(maze)) and \
           (0 <= new_coords[1] < len(maze[0])) and \
           not maze[new_coords[0]][new_coords[1]]:
            maze[coords[0]][coords[1]].append(direction)
            maze[new_coords[0]][new_coords[1]].append(
                (-direction[0], -direction[1]))
            DFS(maze, new_coords)
    return maze


def search(x, y):
    if grid[x][y] == '2':
        print("found at %d,%d" % (x, y))
        # Time end here? yes
        return True
    elif grid[x][y] == '1':
        print('wall at %d,%d' % (x, y))
        return (False)
    elif grid[x][y] == '3':
        print('visited at %d,%d' % (x, y))
        return (False)
    increment()
    print('visiting %d,%d' % (x, y))

    # mark as visited
    grid[x][y] = '3'

    # explore neighbors clockwise starting by the one on the right
    if ((x < (len(grid)-1) and search(x+1, y))
        or (y > 0 and search(x, y-1))
        or (x > 0 and search(x-1, y))
            or (y < len(grid)-1 and search(x, y+1))):
        return True
    return False


def increment():
    global stepcount
    stepcount = stepcount+1


def write(maze):
    if platform.system() == 'Windows':
        newline = ''
    else:
        newline = None
    # for filename in os.listdir('SavedMazes'):
    #    number + 1
    files = os.listdir("SavedMazes")
    number = len(files) + 1
    filename = "SavedMazes/mazes_" + str(number) + ".csv"
    with open(filename, 'w', newline=newline) as output_file:
        output_writer = csv.writer(output_file)
        output_writer.writerows(maze)
        return filename


def count_saved_mazes():
    files = os.listdir("SavedMazes")
    print(len(files))


def read():
    with open("SavedMazes/mazes.csv") as f:
        lis = [line.replace("\n", "").split(",")
               for line in f]  # create a list of lists
        return lis


def maze_generate(sizeX, sizeY):
    return convert(DFS(make_empty_maze(sizeX, sizeY)))


def should_we_solve(selfview, userinput):
    if userinput == "yes":
        return True
    elif userinput == "no":
        selfview.endView()
        return False
    else:
        yes_or_no = selfview.invalid_input(
            "Should the program run the solving algorithm?\n")
        should_we_solve(selfview, yes_or_no)


def set_grid(maze):
    global grid
    grid = maze


def get_steps():
    global stepcount
    return stepcount


def reset_steps():
    global stepcount
    stepcount = -1
