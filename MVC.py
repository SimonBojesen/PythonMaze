import backend_functionality

class Model(object):
    # initialiser for class in python is like a constructor in java
    #def __init__(self, mazesize):
        #self.mazesize = mazesize

    def maze_gen(self, mazesize):
        backend_functionality.maze_gen(mazesize)

class View(object):
    def input_size()
    #user interaction functionality here
class Controller(object):
    #this is like the facade in java, this class gets the input from the user 
    #and uses it to figure out what backend functions should be run from the model