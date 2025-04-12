
import tkinter as tk
from tkinter import messagebox


users = {}

def register_user():
    username = entry_username_reg.get()
    password = entry_password_reg.get()
    
    if username in users:
        messagebox.showerror("Ошибка", "Пользователь уже существует")
    else:
        users[username] = password
        messagebox.showinfo("Успех", "Пользователь зарегистрирован")
        registration_window.destroy()

def open_registration_window():
    global registration_window
    registration_window = tk.Toplevel(root)
    registration_window.title("Регистрация")

    tk.Label(registration_window, text="Логин:").pack()
    global entry_username_reg
    entry_username_reg = tk.Entry(registration_window)
    entry_username_reg.pack()

    tk.Label(registration_window, text="Пароль:").pack()
    global entry_password_reg
    entry_password_reg = tk.Entry(registration_window, show="*")
    entry_password_reg.pack()

    tk.Button(registration_window, text="Зарегистрироваться", command=register_user).pack()

def authorize_user():
    username = entry_username.get()
    password = entry_password.get()

    if username in users and users[username] == password:
        messagebox.showinfo("Успех", "Авторизация успешна")
    else:
        messagebox.showerror("Ошибка", "Неверный логин или пароль")

# Основное окно
root = tk.Tk()
root.title("Авторизация")

tk.Label(root, text="Логин:").pack()
entry_username = tk.Entry(root)
entry_username.pack()

tk.Label(root, text="Пароль:").pack()
entry_password = tk.Entry(root, show="*")
entry_password.pack()

tk.Button(root, text="Авторизоваться", command=authorize_user).pack()
tk.Button(root, text="Регистрация", command=open_registration_window).pack()

root.mainloop()
```
