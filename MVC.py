import backend_functionality
import time

#We have chosen to use the model as a kind of facade that uses the functionality 
#in backend_functionality class and returns the output back to the controller. 
class Model(object):
    def maze_gen(self, sizeX, sizeY):
        return backend_functionality.maze_generate(sizeX, sizeY)

    def solve_a_maze_GUI(self, observer):
        return backend_functionality.search_GUI(1, 1, observer)

    def pretty_print(self, maze):
        return backend_functionality.pretty_print(maze)

    def should_solve(self, selfview, userinput):
        return backend_functionality.should_we_solve(selfview, userinput)

    def save_maze(self, maze):
        return backend_functionality.write(maze)

    def load_maze(self, filename):
        return backend_functionality.read(filename)

    def solve_maze(self):
        return backend_functionality.search(1, 1)

    def set_maze(self, maze):
        backend_functionality.set_grid(maze)

    def get_steps(self):
        steps = backend_functionality.get_steps()
        backend_functionality.reset_steps()
        return steps
        
    def count(self):
        backend_functionality.count_saved_mazes()

class View(object):
    def input_mazesize(self):
        print ('Welcome!')
        sizeX = int(input("To generate a maze insert a width: "))
        sizeY = int(input("To generate a maze insert a height: "))
        return str(sizeX) + "-" + str(sizeY)
    
    @staticmethod
    def endView(self):
        print('Goodbye!')

    def input_yes_or_no(self, string):
        return str(input(string + "yes/no: "))
    
    def invalid_input(self, string):
        return str(input("Your input is invalid\n" + string + "yes/no: "))

class Controller(object):
    def __init__(self, model, view):
        self.view = view
        self.model = model

    def build_a_maze_CONSOLE(self):
        mazesizes = self.view.input_mazesize().split("-")
        maze = self.model.maze_gen(int(mazesizes[0]), int(mazesizes[1]))
        self.model.pretty_print(maze)
        return maze

    def solve_a_maze_CONSOLE(self, maze):
        userinput = self.view.input_yes_or_no("Should the program run the solving algorithm?\n")
        true_or_false = self.model.should_solve(self.view, userinput)
        if true_or_false == False:
            #Ask user if he wants to save the labyrinth for later
            userinput = self.view.input_yes_or_no("Should we save the labyrinth for later?\n")
            true_or_false = self.model.should_solve(self.view, userinput)
            if true_or_false == False:
                return maze
            else:
                self.model.save_maze(maze)
                return maze
        else:
            #Run maze through the solver
            self.model.set_maze(maze)
            start = time.time()
            self.model.solve_maze()
            stop = time.time()
            elapsedTime = stop-start
            steps = self.model.get_steps()
            self.model.reset_steps()
            print("number of iterations: ", steps)
            print("time taken to solve the maze in microseconds: ", elapsedTime*1000000)

    def build_a_maze_GUI(self, x, y):
        return self.model.maze_gen(x, y)
    
    def solve_a_maze_GUI(self, observer, maze):
        self.model.set_maze(maze)
        start = time.time()
        self.model.solve_a_maze_GUI(observer)
        stop = time.time()
        elapsedTime = stop-start
        array = [self.model.get_steps(), elapsedTime*1000000]
        
        return array

    def save_maze(self, maze):
        return self.model.save_maze(maze)
        
    def read_maze(self, filename):
        return self.model.load_maze(filename)


        
        
#this stuff here is for testing the code NOTHING ELSE!!!
#when building the GUI call the do this kinda code inside there instead of here :)
#c = Controller(Model(), View())
#maze = c.build_a_maze_CONSOLE()
#c.solve_a_maze_CONSOLE(maze)
