#Authored by Grant Slatton on 2013 September 15
#All code is released to the public domain under the terms of [http://unlicense.org]

from random import randint, shuffle, choice
import sys
import os
os.system("cls")

#needed for DFS...
sys.setrecursionlimit(10000)

#Each maze cell contains a tuple of directions of cells to which it is connected

#Takes a maze and converts it to an array of X's and blanks to represent walls, etc
#def convert(maze):
    #pretty_maze = [["1"]*(len(maze[0])) for a in range(len(maze))]
    #for y,row in enumerate(maze):
      #  for x,col in enumerate(row):
       #     pretty_maze[y][x] = "0"
        #    for direction in col:
         #       pretty_maze[y+direction[0]][x+direction[1]] = "0"
   # return pretty_maze

def convert(maze):
    pretty_maze = [["1"]*(2*len(maze[0])+1) for a in range(2*len(maze)+1)]
    for y,row in enumerate(maze):
        for x,col in enumerate(row):
            pretty_maze[2*y+1][2*x+1] = "0"
            for direction in col:
                pretty_maze[2*y+1+direction[0]][2*x+1+direction[1]] = '\u001b[31m0\u001b[37m'
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
    return maze

def binary(maze):
    directions = [(1,0), (0,1)]
    for y, row in enumerate(maze):
        for x, col in enumerate(row):
            if y == len(maze)-1 and x == len(row)-1:
                maze[y][x] = []
                return maze
            if y == len(maze)-1:
                direction = directions[1]
            elif x == len(row)-1:
                direction = directions[0]
            else:
                direction = choice(directions)
            maze[y][x] = [direction]
size = 3
print("DFS:")
pretty_print(DFS(make_empty_maze(size,size)))
print("binary:")
pretty_print(binary(make_empty_maze(size,size)))