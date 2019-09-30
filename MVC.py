import backend_functionality

class Model(object):
    # initialiser for class in python is like a constructor in java
    # def __init__(self, mazesize):
        # self.mazesize = mazesize

    def maze_gen(self, mazesize):
        return backend_functionality.maze_gen(mazesize)

class View(object):
    # user print functionality here
    def startView(self):
        print ('Welcome!')
    def endView(self):
        print ('Goodbye!')

class Controller(object):
    def start(self):
        v = View()
        v.startView()
        size = int(input("To generate a maze insert a mazesize: "))
        print(size)

c = Controller()
c.start()
