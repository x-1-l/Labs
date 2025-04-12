import tkinter as tk
import random
import string

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Генератор паролей")

        self.length_label = tk.Label(root, text="Длина пароля:")
        self.length_label.pack()

        self.length_entry = tk.Entry(root)
        self.length_entry.pack()

        self.uppercase_var = tk.BooleanVar()
        self.lowercase_var = tk.BooleanVar()
        self.digits_var = tk.BooleanVar()
        self.special_var = tk.BooleanVar()

        self.uppercase_check = tk.Checkbutton(root, text="Включить большие буквы", variable=self.uppercase_var)
        self.uppercase_check.pack()

        self.lowercase_check = tk.Checkbutton(root, text="Включить маленькие буквы", variable=self.lowercase_var)
        self.lowercase_check.pack()

        self.digits_check = tk.Checkbutton(root, text="Включить цифры", variable=self.digits_var)
        self.digits_check.pack()

        self.special_check = tk.Checkbutton(root, text="Включить специальные символы", variable=self.special_var)
        self.special_check.pack()

        self.generate_button = tk.Button(root, text="Сгенерировать пароль", command=self.generate_password)
        self.generate_button.pack()

        self.password_label = tk.Label(root, text="")
        self.password_label.pack()

    def generate_password(self):
        length = int(self.length_entry.get())
        characters = ""

        if self.uppercase_var.get():
            characters += string.ascii_uppercase
        if self.lowercase_var.get():
            characters += string.ascii_lowercase
        if self.digits_var.get():
            characters += string.digits
        if self.special_var.get():
            characters += string.punctuation

        if characters:
            password = ''.join(random.choice(characters) for _ in range(length))
            self.password_label.config(text=f"Сгенерированный пароль: {password}")
        else:
            self.password_label.config(text="Выберите хотя бы один тип символов.")

if __name__ == "__main__":
    root = tk.Tk()
    password_generator = PasswordGenerator(root)
    root.mainloop()
