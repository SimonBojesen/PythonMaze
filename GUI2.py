from tkinter import Tk, Canvas, Frame, Label, Entry, Button, Scrollbar, Listbox, Menu, filedialog, simpledialog, END, messagebox
import MVC
import os
window_width = 1500
windows_height = 700

mazes = []
c = MVC.Controller(MVC.Model(), MVC.View())


class MazeSizeTooLow(Exception):
    pass


class MazeSizeTooHigh(Exception):
    pass


def mazeSizeX():
    X = simpledialog.askinteger('Mazesize', 'Input x', initialvalue="5")
    if(X < 5):
        messagebox.showinfo(
            "UPS try again!", "Minum size for generating a maze is: 5")
        raise MazeSizeTooLow(X)
    if(X > 30):
        messagebox.showinfo(
            "UPS try again!", "Maximum size for generating a maze is: 30")
        raise MazeSizeTooHigh(X)
    return X


def mazeSizeY():
    Y = simpledialog.askinteger('Mazesize', 'Input y', initialvalue="5")
    if(Y < 5):
        messagebox.showinfo(
            "UPS try again!", "Minum size for generating a maze is: 5")
        raise MazeSizeTooLow(Y)
    if(Y > 30):
        messagebox.showinfo(
            "UPS try again!", "Maximum size for generating a maze is: 30")
        raise MazeSizeTooHigh(Y)
    return Y


def maze_gen():
    X = mazeSizeX()
    Y = mazeSizeY()
    maze = c.build_a_maze_GUI(X, Y)
    filename = c.save_maze(maze)
    filename_label.config(text=filename)
    f = open(filename)
    maze_label.config(text=f.read())
    load_mazes()


def load_mazes():
    global mazes
    listbox_mazes.delete(0, END)
    mazes = os.listdir('SavedMazes')
    for maze in mazes:
        listbox_mazes.insert(END, maze)
    listbox_mazes.place(relwidth=1, relheight=1)


def get_maze():
    global mazes
    path = 'SavedMazes/'
    maze_index = 0
    tuple_index = listbox_mazes.curselection()
    for value in tuple_index:
        maze_index = value
    filename = mazes[maze_index]
    filename_label.config(text=filename)
    f = open(path + filename)
    maze_label.config(text=f.read())


def update_observer_text(text):
    observer_label.config(text=text)


class Subscriber:
    def __init__(self, update_observer_text):
        self.update_observer_text = update_observer_text

    def update(self, message):
        self.update_observer_text(message)


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


pub = Publisher()
sub = Subscriber(update_observer_text)
pub.register(sub)

root = Tk()
root.title('MazesGUI')
canvas = Canvas(root, width=window_width,
                height=windows_height, relief='raised')
canvas.pack()

# main frame for showing maze + buttons
main_frame = Frame(root, bg='#4C7676')
main_frame.place(relwidth=0.5, relheight=1, relx=0.25)
filename_frame = Frame(main_frame, bd=1, bg='black')
filename_frame.place(relwidth=0.8, relheight=0.05, relx=0.1)
filename_label = Label(filename_frame, bg='beige')
filename_label.place(relwidth=1, relheight=1)
maze_frame = Frame(main_frame, bd=1, bg='black')
maze_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.05)
maze_label = Label(maze_frame)
maze_label.place(relwidth=1, relheight=1)
button_create = Button(main_frame, text='Create maze', command=maze_gen,
                       bg='#5AA04B', fg='black', activebackground='#244E1B', font=('verdana', 12))
button_create.place(relwidth=0.4, relheight=0.08, relx=0.1, rely=0.85)
button_solve = Button(main_frame, text='Solve maze', command="solve_single_mazes",
                      bg='#5AA04B', fg='black', activebackground='#244E1B', font=('verdana', 12))
button_solve.place(relwidth=0.4, relheight=0.08, relx=0.5, rely=0.85)

# here we have the left frame where we have tried to use observer pattern
# we write stuff to the user in here like we would normally do in the console
left_frame = Frame(root, bg='#4C7676')
left_frame.place(relwidth=0.25, relheight=1)
top_label_left = Label(left_frame, text='Observer',
                       bg='#4C7676', font=('verdana', 10))
top_label_left.place(relx=0.1, rely=0.01)
observer_frame_padding = Frame(left_frame, bd=1, bg='black')
observer_frame_padding.place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.88)
observer_label = Label(observer_frame_padding, font=('verdana', 10))
observer_label.place(relwidth=1, relheight=1)

right_frame = Frame(root, bg='#4C7676')
right_frame.place(relwidth=0.25, relheight=1, relx=0.75)
top_label_right = Label(right_frame, text='Mazes',
                        bg='#4C7676', font=('verdana', 10))
top_label_right.place(relx=0.1, rely=0.01)
mazes_frame_padding = Frame(right_frame, bd=1, bg='black')
mazes_frame_padding.place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.8)
mazes_mainframe = Frame(mazes_frame_padding)
mazes_mainframe.place(relwidth=1, relheight=1)
listbox_mazes = Listbox(mazes_mainframe, selectbackground='black')
select_maze = Button(right_frame, text='Select maze', command=get_maze,
                     bg='#5AA04B', fg='black', activebackground='#244E1B', font=('verdana', 12))
select_maze.place(relx=0.1, rely=0.85, relwidth=0.8, relheight=0.08)

load_mazes()
root.mainloop()
