import matplotlib.pyplot as plt
#import maze_generator
plt.figure()
x_values = range(1, 100)
y_values = [x ** 2 for x in x_values]
print('Points to be plotted {}'.format(list(zip(x_values, y_values)))) 
# The purpose of zip() is to map the similar index of multiple containers
# so that they can be used just using as single entity.
plt.scatter(x_values, y_values, s=100)
plt.show()
