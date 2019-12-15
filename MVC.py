import backend_functionality

class Model(object):
    # initialiser for class in python is like a constructor in java
    # def __init__(self, mazesize):
        # self.mazesize = mazesize

    def maze_gen(self, sizeX, sizeY):
        return backend_functionality.maze_generate(sizeX, sizeY)

    def pretty_print(self, maze):
        return backend_functionality.pretty_print(maze)

class View(object):
    # user print functionality here
    def user_input_mazesize(self):
        print ('Welcome!')
        sizeX = int(input("To generate a maze insert a width: "))
        sizeY = int(input("To generate a maze insert a height: "))
        return str(sizeX) + "-" + str(sizeY)
    def endView(self):
        print ('Goodbye!')

class Controller(object):
    def __init__(self, model, view):
        self.view = view
        self.model = model

    def start(self):
        mazesizes = self.view.user_input_mazesize().split("-")
        maze = self.model.maze_gen(int(mazesizes[0]), int(mazesizes[1]))
        self.model.pretty_print(maze)

c = Controller(Model(), View())
c.start()
