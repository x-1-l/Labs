import tkinter as tk

# Курс
exchange_rate = 99.0

def convert_to_rub():
    try:
        dollars = float(entry_dollars.get())
        rubles = dollars * exchange_rate
        label_result.config(text=f"{dollars} USD = {rubles:.2f} RUB")
    except ValueError:
        label_result.config(text="Введите корректное число")

def convert_to_usd():
    try:
        rubles = float(entry_rubles.get())
        dollars = rubles / exchange_rate
        label_result.config(text=f"{rubles} RUB = {dollars:.2f} USD")
    except ValueError:
        label_result.config(text="Введите корректное число")

# Создание основного окна
root = tk.Tk()
root.title("Конвертор валют")

# Ввод долларов
label_dollars = tk.Label(root, text="Введите сумму в долларах (USD):")
label_dollars.pack()

entry_dollars = tk.Entry(root)
entry_dollars.pack()

button_convert_to_rub = tk.Button(root, text="Конвертировать в рубли", command=convert_to_rub)
button_convert_to_rub.pack()

# Ввод рублей
label_rubles = tk.Label(root, text="Введите сумму в рублях (RUB):")
label_rubles.pack()

entry_rubles = tk.Entry(root)
entry_rubles.pack()

button_convert_to_usd = tk.Button(root, text="Конвертировать в доллары", command=convert_to_usd)
button_convert_to_usd.pack()

# Метка для отображения результата
label_result = tk.Label(root, text="")
label_result.pack()

# Запуск основного цикла приложения
root.mainloop()
