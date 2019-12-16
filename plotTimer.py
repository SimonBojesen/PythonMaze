import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

timeMinimum = pd.read_csv('TimePlotted/TimeMinimum.csv')
timeMaximum = pd.read_csv('TimePlotted/TimeMaximum.csv')
timeAverage = pd.read_csv('TimePlotted/TimeAverage.csv')

mazesize = np.array(timeMinimum['MazeSize'])
timeMin = np.array(timeMinimum['Time(min)']) # reads data from a csv file
timeMax = np.array(timeMaximum['Time(max)']) # reads data from a csv file
timeAvg = np.array(timeAverage['Time(average)']) # reads data from a csv file

plt.style.use("fivethirtyeight") # plot styling

plt.plot(mazesize, timeMin, marker="o", label="Minimum time to solve") 
plt.plot(mazesize, timeMax, marker="o", label="Maximum time to solve") 
plt.plot(mazesize, timeAvg, marker="o", label="Average time to solve") 
# Can not plot becuase x & y needs to be same size

plt.title("Plot showing max, mini, and average iterations for solving the maze.")
plt.xlabel("mazesize(x,y)")
plt.ylabel("Time(μs)")
plt.legend()
plt.savefig('TimePlotted/TimePlotted.png')
plt.show()