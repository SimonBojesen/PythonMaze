#Authored by Grant Slatton on 2013 September 15
#All code is released to the public domain under the terms of [http://unlicense.org]

from random import randint, shuffle, choice
import time
import sys
import os
os.system("cls")

#needed for DFS...
sys.setrecursionlimit(10000)

#Each maze cell contains a tuple of directions of cells to which it is connected

def convert(maze):
    pretty_maze = [["1"]*(2*len(maze[0])+1) for a in range(2*len(maze)+1)]
    for y,row in enumerate(maze):
        for x,col in enumerate(row):
            pretty_maze[2*y+1][2*x+1] = '\u001b[31m0\u001b[37m'
            for direction in col:
                pretty_maze[2*y+1+direction[0]][2*x+1+direction[1]] ='0' # color red for 0 & means you can move between
    return pretty_maze

#Takes a converted maze and pretty prints it
def pretty_print(maze):
    for a in convert(maze):
        string = ""
        for b in a:
            string += b
        print (string)
    print ("")

#Returns an empty maze of given size
def make_empty_maze(width, height):
    maze = [[[] for b in range(width)] for a in range(height)]
    return maze

#Recursive backtracker. 
#Looks at its neighbors randomly, if unvisitied, visit and recurse
def DFS(maze, coords=(0,0)):
    directions = [(0,1),(1,0),(0,-1),(-1,0)]
    shuffle(directions)
    for direction in directions:
        new_coords = (coords[0] + direction[0], coords[1] + direction[1])
        if (0 <= new_coords[0] < len(maze)) and \
           (0 <= new_coords[1] < len(maze[0])) and \
           not maze[new_coords[0]][new_coords[1]]:
            maze[coords[0]][coords[1]].append(direction)
            maze[new_coords[0]][new_coords[1]].append((-direction[0], -direction[1]))
            DFS(maze, new_coords)
          #  maze[new_coords[2][]]endCoord=(maze.index(size)
            
          # printer første index - find metode til at få fat i sidste index og derefter sæt det til 2
            #print(maze[0][0])    
    return maze

def search(x, y):
    if maze[x][y] == 2:
        print ('found at %d,%d' % (x, y))
        return True
    elif maze[x][y] == 1:
        print ('wall at %d,%d' % (x, y))
        return False
    elif maze[x][y] == 3:
        print ('visited at %d,%d' % (x, y))
        return False

    print ('visiting %d,%d' % (x, y))

    # mark as visited
    maze[x][y] = 3

    # explore neighbors clockwise starting by the one on the right
    if ((x < len(maze)-1 and search(x+1, y))
        or (y > 0 and search(x, y-1))
        or (x > 0 and search(x-1, y))
        or (y < len(maze)-1 and search(x, y+1))):
        return True
    return False

size = 5

print("DFS:")
maze = DFS(make_empty_maze(size,size))
print(maze)
pretty_print(maze)
search(0, 0)
