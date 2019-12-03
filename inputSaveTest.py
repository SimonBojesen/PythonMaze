import tkinter as tk
from tkinter import simpledialog

def get_pass():
    # inform function to use external/global variable when you use `=`
    global user_password

    # `user_password_var` is global variable too
    # but it doesn't need `global user_password_var` 
    # because it doesn't need `=` to assign value.

    result = simpledialog.askstring("Password Entry", "Enter your password here:")

    user_password = result
    # or
    user_password_var.set(result)
    # or
    if result != '123456':
        label['text'] = "ERROR: password is incorrect"
    else:
        label['text'] = "password is OK"

# --- main ---

root = tk.Tk()

# it creates global variable 
user_password = ''
# or
user_password_var = tk.StringVar()

label = tk.Label(root)
label.pack()

submitButton = tk.Button(root, text="Start", command=get_pass)
submitButton.pack()

# both variables are empty before `mainloop`

root.mainloop()

# both variables have value after `mainloop`

# print after you exit program
print(user_password)
print(user_password_var.get())