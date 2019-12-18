from PIL import ImageTk, Image
from tkinter import Tk, filedialog, simpledialog, Frame, LabelFrame, Label, Button, Menu
import platform
import csv
import MVC

# Root window created, can add more later
# windows within windows.
root = Tk()
c = MVC.Controller(MVC.Model(), MVC.View())

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    # Creation of init_window
    def init_window(self):

        # changing the title of our master widget
        self.master.title("GUI")


def popup():
    S1 = simpledialog.askstring('Input file name', 'file name')
    # prints the string typed in by the user, make a funtion to save the file by that name.
    print(S1)
    if platform.system() == 'Windows':
        newline = ''
    else:
        newline = None
    with open("maze.csv", 'w', newline=newline) as output_file:
        output_writer = csv.writer(output_file)

        output_writer.writerows(S1)


def mazeSizeX():
    X = simpledialog.askinteger('Mazesize', 'Input x', initialvalue="5")
    return X

def mazeSizeY():
    Y = simpledialog.askinteger('Mazesize', 'Input y', initialvalue="5")
    return Y

def maze_gen():
    global L1
    global L2
    X = mazeSizeX()
    Y = mazeSizeY()
    maze = c.build_a_maze_GUI(X, Y)
    filename = c.save_maze(maze)
    L1.config(text=filename)
    f = open(filename)
    L2.config(text=f.read())
    
def fileBrowse(): #open a browse window and display that file on screen
    global L1
    global L2
    root.filename = filedialog.askopenfilename(initialdir = "/SavedMazes", title = "Select a File", filetype = (("csv","*csv"), ("All Files", "*.*")))
    #L1 = Label(frame, text=root.filename) # shows the location of the file opened
    L1.config(text=root.filename)
    file3 = root.filename
    f = open(file3)
    L2.config(text=f.read())

frame = LabelFrame(root, padx=5, pady=5)
frame.pack(padx=10, pady=10)
L1 = Label(frame)
L2 = Label(frame)
L1.pack()
L2.pack()
#C = Canvas(frame, bg="blue", height=600, width=600)
#C.pack()

B1 = Button(root, text="Save placeholder", command=popup)
B1.pack()

# Creating a menu
menubar = Menu(root)
file = Menu(menubar, tearoff=0)
# added dropdown options to file
file.add_command(label="New")
file.add_command(label="Open")
file.add_command(label="Save")
file.add_command(label="Save as...")
file.add_command(label="Close")

file.add_separator()
# adds a command to the menu option, calling it exit, and the
# command it runs on event is client_exit
file.add_command(label="Exit", command=root.quit)
# added "file" to menu
menubar.add_cascade(label="File", menu=file)
# Maze menu dropdown
maze = Menu(menubar, tearoff=0)
# added dropdown options to maze
maze.add_command(label="New", command=maze_gen)
maze.add_command(label="Load", command=fileBrowse)  # select a file to load
maze.add_command(label="Run")
# added "Maze" to menu
menubar.add_cascade(label="Maze", menu=maze)

root.config(menu=menubar)


# creation of an instance
app = Window(root)
# mainloop
root.mainloop()



