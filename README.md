# Python

from colorama import init, Fore, Style

# Инициализация colorama для корректного отображения цветов в Windows
init(autoreset=True)

# Приветствие
print(f"{Fore.CYAN}{Style.BRIGHT}Добро пожаловать, Гость!")

# Бесконечный цикл для ввода команд
while True:
    # Ввод текста пользователем зелёным цветом и большими буквами
    user_input = input(f"{Fore.GREEN}{Style.BRIGHT}> ").upper()
    
    # Команда для выхода
    if user_input == "EXIT":
        print(f"{Fore.CYAN}{Style.BRIGHT}До свидания!")
        break
    
    # Любой другой ввод
    else:
        print(f"{Fore.YELLOW}Вы ввели: {user_input}")
