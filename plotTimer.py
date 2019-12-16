import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

stepsMinimum = pd.read_csv('TimePlotted/StepsMinimum.csv')
stepsMaximum = pd.read_csv('TimePlotted/StepsMaximum.csv')
stepsAverage = pd.read_csv('TimePlotted/StepsAverage.csv')

mazesize = np.array(stepsMinimum['MazeSize'])
stepsMin = np.array(stepsMinimum['Steps(min)']) # reads data from a csv file
stepsMax = np.array(stepsMaximum['Steps(max)']) # reads data from a csv file
stepsAvg = np.array(stepsAverage['Steps(average)']) # reads data from a csv file

plt.style.use("fivethirtyeight") # plot styling

plt.plot(mazesize, stepsMin, marker="o", label="Minimum number of steps") # plots the data
plt.plot(mazesize, stepsMax, marker="o", label="Maximum number of steps") # need to find out how to plot min steps
plt.plot(mazesize, stepsAvg, marker="o", label="Average number of steps") # need to find out how to plot max steps
# Can not plot becuase x & y needs to be same size

plt.title("Plot showing max, mini, and average iterations for solving the maze.")
plt.xlabel("mazesize(x,y)")
plt.ylabel("Steps(iterations)")
plt.legend()
plt.savefig('TimePlotted/TimePlotted.png')
plt.show()