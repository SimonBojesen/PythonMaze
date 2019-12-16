import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv('numberOfSteps.csv')
steps = np.array(data['Steps(nodes)']) # reads data from a csv file
#mazesize = np.array(data['MazeSize'])
print(steps)

steps5 = [23,26,20,21,30]
steps10 = [23,26,20,21,30]
steps15 = [23,26,20,21,30]
steps20 = [23,26,20,21,30]
steps25 = [23,26,20,21,30]


plt.style.use("fivethirtyeight") # plot styling

x_mazesize = [5,10,15,20,25]
y_steps = steps

#min = np.min(steps5,steps10,steps15,steps20,steps25)
#max = np.max(steps5,steps10,steps15,steps20,steps25)
#median = np.median(steps5,steps10,steps15,steps20,steps25)

plt.plot(x_mazesize, steps, marker="o", label="Steps") # plots the data
#plt.plot(x_mazesize, min, marker="o", label="Steps") # need to find out how to plot min steps
#plt.plot(x_mazesize, max, marker="o", label="Steps") # need to find out how to plot max steps
#plt.plot(x_mazesize, median, marker="o", label="Steps") # need to find out how to plot median steps
# Can not plot becuase x & y needs to be same size

plt.title("Plot showing max, mini, and average iterations for solving the maze.")
plt.xlabel("mazesize(x,y)")
plt.ylabel("Steps(iterations)")

plt.legend()
#plt.grid(True)

plt.savefig('Plots/plot.png')

plt.show()

#print(min, max, median)