from tkinter import Tk, Canvas, Frame, Label, Entry, Button, Scrollbar, Listbox, Menu, filedialog, simpledialog
import MVC

window_width = 1500
windows_height = 700
text_log = ""

c = MVC.Controller(MVC.Model(), MVC.View())

def mazeSizeX():
    X = simpledialog.askinteger('Mazesize', 'Input x', initialvalue="5")
    return X

def mazeSizeY():
    Y = simpledialog.askinteger('Mazesize', 'Input y', initialvalue="5")
    return Y

def maze_gen():
    global filename_label
    global maze_label
    X = mazeSizeX()
    Y = mazeSizeY()
    maze = c.build_a_maze_GUI(X, Y)
    filename = c.save_maze(maze)
    filename_label.config(text=filename)
    f = open(filename)
    maze_label.config(text=f.read())

def fileBrowse(): #open a browse window and display all files on screen
    global filename_label
    global maze_label
    root.filename = filedialog.askopenfilename(initialdir = "/SavedMazes", title = "Select a File", filetype = (("csv","*csv"), ("All Files", "*.*")))
    filename = root.filename
    filename_label.config(text=root.filename)
    f = open(filename)
    maze_label.config(text=f.read())


class Subscriber:
    def __init__(self, function):
        self.function = function

    def update(self, message):
        self.function(message)

class Publisher:
    def __init__(self):
        self.subscribers = set()

    def register(self, who):
        self.subscribers.add(who)

    def unregister(self, who):
        self.subscribers.discard(who)

    def dispatch(self, message):
        for subscriber in self.subscribers:
            subscriber.update(message)


root = Tk()
root.title('MazesGUI')
canvas = Canvas(root, width=window_width, height=windows_height, relief='raised')
canvas.pack()

#menu
menubar = Menu(root)
# Maze menu dropdown
maze = Menu(menubar, tearoff=0)
# added dropdown options to maze
maze.add_command(label="New", command=maze_gen)
maze.add_command(label="Load", command=fileBrowse)  # select a file to load
maze.add_command(label="Run")
# added "Maze" to menu
menubar.add_cascade(label="Maze", menu=maze)

root.config(menu=menubar)

#main frame for showing maze + buttons
main_frame = Frame(root, bg="#4C7676")
main_frame.place(relwidth=0.5, relheight=1, relx=0.25)
filename_frame = Frame(main_frame, bd=1, bg="black")
filename_frame.place(relwidth=0.8, relheight=0.05, relx=0.1)
filename_label = Label(filename_frame)
filename_label.place(relwidth=1, relheight=1)
maze_frame = Frame(main_frame, bd=1, bg="black")
maze_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.05)
maze_label = Label(maze_frame)
maze_label.place(relwidth=1, relheight=1)
button_solve = Button(main_frame, text='Solve Maze', command="solve_single_mazes", bg='#5AA04B', fg='black', activebackground="#244E1B", font=('helvetica', 9, 'bold'))
button_solve.place(relwidth=0.2, relheight=0.08, relx=0.1, rely=0.85)

left_frame = Frame(root, bg="#4C7676")
left_frame.place(relwidth=0.25, relheight=1)


right_frame = Frame(root, bg="#4C7676")
right_frame.place(relwidth=0.25, relheight=1, relx=0.75)

root.mainloop()