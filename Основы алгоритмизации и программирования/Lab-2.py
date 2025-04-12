import random

def угадай_число():

  secret_number = random.randint(1, 10)
  attempts = 3

  print("Угадай число от 1 до 10 за 3 попытки.")

  for attempt in range(attempts):
    guess = int(input(f"Попытка {attempt + 1}: Введите число: "))

    if guess == secret_number:
      print(f"Ты угадал число. Количество попыток: {attempt + 1}")
      return

    elif guess < secret_number:
      print("Число больше.")

    else:
      print("Число меньше.")

  print(f"Попытки закончились. Загаданное число было {secret_number}.")

if __name__ == "__main__":
  угадай_число()
