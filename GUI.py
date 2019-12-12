from tkinter import *
from PIL import ImageTk, Image
from tkinter import Tk, filedialog, simpledialog
import platform
import csv

# Root window created, can add more later
# windows within windows.
root = Tk()


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


def fileBrowse(): #open a browse window and display that file on screen
    global my_image
    root.filename = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetype = (("jpeg","*jpg"), ("All Files", "*.*")))
    L1 = Label(frame, text=root.filename) # shows the location of the file opened
    L1.pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    L2 = Label(frame, image=my_image)# shows a Image of the opened file

    L2.pack()

# B2 = my_btn = Button(root, text="Open File", command=fileBrowse)
# B2.pack()


def mazeSize():
    S2 = simpledialog.askinteger('Mazesize', 'Input x & y', initialvalue="5")
    print(S2)


C = Canvas(root, bg="blue", height=750,
           width=700)
coord = 10, 50, 240, 210
arc = C.create_arc(coord, start=0,
                   extent=150, fill="red")
C.pack()


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
edit = Menu(menubar, tearoff=0)
edit.add_command(label="Undo")

edit.add_separator()
# added dropdown options to edit
edit.add_command(label="Cut")
edit.add_command(label="Copy")
edit.add_command(label="Paste")
edit.add_command(label="Delete")
edit.add_command(label="Select All")

# Add "Edit" to menu
menubar.add_cascade(label="Edit", menu=edit)
help = Menu(menubar, tearoff=0)
help.add_command(label="About")
menubar.add_cascade(label="Help", menu=help)

# Maze menu dropdown
maze = Menu(menubar, tearoff=0)
# added dropdown options to maze
maze.add_command(label="New")
maze.add_command(label="Size", command=mazeSize)
maze.add_command(label="Load", command=fileBrowse)  # select a file to load
maze.add_command(label="Run")
# added "Maze" to menu
menubar.add_cascade(label="Maze", menu=maze)

root.config(menu=menubar)


# creation of an instance
app = Window(root)
# mainloop
root.mainloop()
