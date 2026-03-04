import tkinter as tk
from tkinter import messagebox
from database import register_user, login_user

def register():
    username = entry_username.get()
    password = entry_password.get()

    if username == "" or password == "":
        messagebox.showerror("Error", "All fields required")
        return

    register_user(username, password)
    messagebox.showinfo("Success", "User Registered Successfully")

def login():
    username = entry_username.get()
    password = entry_password.get()

    user = login_user(username, password)

    if user:
        messagebox.showinfo("Success", "Login Successful")
    else:
        messagebox.showerror("Error", "Invalid Credentials")

# GUI Window
root = tk.Tk()
root.title("Login System")
root.geometry("350x250")

tk.Label(root, text="Username").pack(pady=5)
entry_username = tk.Entry(root)
entry_username.pack(pady=5)

tk.Label(root, text="Password").pack(pady=5)
entry_password = tk.Entry(root, show="*")
entry_password.pack(pady=5)

tk.Button(root, text="Register", command=register).pack(pady=5)
tk.Button(root, text="Login", command=login).pack(pady=5)

root.mainloop()