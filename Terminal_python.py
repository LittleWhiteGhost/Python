import json
import os

DATA_FILE = "data.json"

# Цветовые коды
GREEN = "\033[92m"
RED = "\033[91m"
BLUE = "\033[94m"
RESET = "\033[0m"

# Загрузка данных из файла или создание начального списка
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        people = json.load(f)
else:
    people = [
        {"ФИО": "Митрофанов Никита Дмитриевич", "сколько": 0, "пойдет": False},
        {"ФИО": "Отаев Фаррухжон Умаралиевич", "сколько": 200, "пойдет": True},
        {"ФИО": "Лугаськов Артем Павлович", "сколько": 0, "пойдет": False},
        {"ФИО": "Кулаков Арсений Олегович", "сколько": 0, "пойдет": False},
        {"ФИО": "Коробской Юрий Алексеевич", "сколько": 0, "пойдет": False},
        {"ФИО": "Коротков Андрей Григорьевич", "сколько": 0, "пойдет": False},
        {"ФИО": "Алиев Эмин Эльханович", "сколько": 0, "пойдет": False},
        {"ФИО": "Османкин Кирилл Максимович", "сколько": 0, "пойдет": False},
        {"ФИО": "Дубинин Константин Александрович", "сколько": 0, "пойдет": False},
        {"ФИО": "Коновалов Андрей Дмитриевич", "сколько": 0, "пойдет": False},
        {"ФИО": "Карапетян Севак Лерникович", "сколько": 0, "пойдет": False},
        {"ФИО": "Бадасян Давит Шаамирович", "сколько": 0, "пойдет": False},
        {"ФИО": "Леднева Владислава Дмитриевна", "сколько": 0, "пойдет": False},
        {"ФИО": "Карпенко Диана Александровна", "сколько": 0, "пойдет": False},
        {"ФИО": "Басилашвили Даниил Александрович", "сколько": 700, "пойдет": True},
    ]

# Сохранение данных в файл
def save_data():
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(people, f, ensure_ascii=False, indent=4)
    print(f"{GREEN}Данные успешно сохранены в {DATA_FILE}{RESET}")

# Множество для отметки кто пойдет
def update_went():
    return {p["ФИО"] for p in people if p["пойдет"]}

# Вывод таблицы
def show_table():
    went = update_went()
    line = "-" * 100
    print(line)
    print(f"{BLUE}{'ПРИЮТ':^100}{RESET}")
    print(line)
    print(f"{BLUE}{'№':<4} {'ФИО':<35} {'Сумма':<10} {'Пойдет':<6}{RESET}")
    print(line)
    for i, p in enumerate(people, 1):
        f = p["ФИО"]
        if p["сколько"] == 0:
            money = f"{RED}0 ₽{RESET}"
        else:
            money = f"{GREEN}{p['сколько']:.2f}".rstrip('0').rstrip('.') + " ₽" + RESET
        went_mark = f"{GREEN}✓{RESET}" if f in went else f"{RED}✗{RESET}"
        print(f"{i:<4} {f:<35} {money:<10} {went_mark:<6}")
    print(line)

# Добавление суммы
def add_money():
    for i, p in enumerate(people, 1):
        money = f'{p["сколько"]:.2f}'.rstrip('0').rstrip('.')
        print(f"{i}. {p['ФИО']} (текущая сумма: {money} ₽)")
    try:
        choice = int(input("Введите номер человека: "))
        if 1 <= choice <= len(people):
            amount = float(input("Введите сумму для добавления: "))
            people[choice - 1]["сколько"] += amount
            if people[choice - 1]["сколько"] > 0:
                people[choice - 1]["пойдет"] = True
            save_data()
            print(f"Сумма обновлена для {people[choice - 1]['ФИО']}")
        else:
            print("Неверный номер.")
    except ValueError:
        print("Ошибка ввода.")

# Вычитание суммы
def subtract_money():
    for i, p in enumerate(people, 1):
        print(f"{i}. {p['ФИО']} (Сумма: {p['сколько']} ₽)")
    try:
        choice = int(input("Введите номер человека: "))
        if 1 <= choice <= len(people):
            amount = float(input("Введите сколько вычесть: "))
            people[choice - 1]["сколько"] -= amount
            if people[choice - 1]["сколько"] < 0:
                people[choice - 1]["сколько"] = 0
            save_data()
            print(f"Сумма обновлена для {people[choice - 1]['ФИО']}")
        else:
            print("Неверный номер.")
    except ValueError:
        print("Ошибка ввода.")

# Умножение суммы
def multiply_money():
    for i, p in enumerate(people, 1):
        print(f"{i}. {p['ФИО']} (Сумма: {p['сколько']} ₽)")
    try:
        choice = int(input("Введите номер человека: "))
        if 1 <= choice <= len(people):
            factor = float(input("Введите множитель: "))
            people[choice - 1]["сколько"] *= factor
            save_data()
            print(f"Сумма умножена для {people[choice - 1]['ФИО']}")
        else:
            print("Неверный номер.")
    except ValueError:
        print("Ошибка ввода.")

# Деление суммы
def split_money():
    for i, p in enumerate(people, 1):
        print(f"{i}. {p['ФИО']} (Сумма: {p['сколько']} ₽)")
    try:
        choice = int(input("Введите номер человека: "))
        if 1 <= choice <= len(people):
            parts = int(input("На сколько частей разделить сумму? "))
            if parts == 0:
                print("Ты не первый кто это попробовал 😎")
            elif parts > 0:
                original = people[choice - 1]["сколько"]
                divided = original / parts
                print(f"Сумма {original} ₽ разделена на {parts} частей по {divided:.2f} ₽")
            else:
                print("Количество частей должно быть больше 0.")
        else:
            print("Неверный номер.")
    except ValueError:
        print("Ошибка ввода.")

# Общая сумма
def total_sum():
    total = sum(p["сколько"] for p in people)
    line = "-" * 75
    print(line)
    print(f"{BLUE}{'ОБЩАЯ СУММА ДЛЯ ПРИЮТА: ' + str(int(total)) + ' ₽':^100}{RESET}")
    print(line)

# Изменение статуса "Пойдет"
def change_status():
    for i, p in enumerate(people, 1):
        went_mark = "Да" if p["пойдет"] else "Нет"
        print(f"{i}. {p['ФИО']} (Пойдет: {went_mark})")
    try:
        choice = int(input("Введите номер человека для изменения статуса: "))
        if 1 <= choice <= len(people):
            status_input = input("Установить 'Да' или 'Нет': ").strip().lower()
            if status_input in ["да", "yes", "y"]:
                people[choice - 1]["пойдет"] = True
            elif status_input in ["нет", "no", "n"]:
                people[choice - 1]["пойдет"] = False
            else:
                print("Неверный ввод. Используйте 'Да' или 'Нет'.")
                return
            save_data()
            print(f"Статус обновлён для {people[choice - 1]['ФИО']}")
        else:
            print("Неверный номер.")
    except ValueError:
        print("Ошибка ввода.")

# Показ справки
def show_help():
    line = "-" * 75
    print(line)
    print(f"{BLUE}{'ТЕРМИНАЛ ПРИЮТА - КОМАНДЫ':^75}{RESET}")
    print(line)
    print("1. Управление суммами:")
    print("   add       → Добавить сумму выбранному человеку.")
    print("   subtract  → Вычесть сумму у выбранного человека.")
    print("   multiply  → Умножить сумму выбранного человека.")
    print("   split     → Разделить сумму человека на несколько частей")
    print("                (если делишь на 0, выводится: 'Ты не первый кто это попробовал 😎').")
    print("   total     → Показать общую сумму для приюта.")
    print("\n2. Управление статусом:")
    print("   status    → Изменить статус 'Пойдет' для выбранного человека.")
    print("\n3. Работа с данными:")
    print("   list      → Показать таблицу всех людей с их суммами и статусом.")
    print("   save      → Сохранить все изменения в файл (data.json).")
    print("\n4. Терминал:")
    print("   start     → Запустить терминал для работы с командами.")
    print("   help      → Показать эту справку.")
    print("   exit      → Выйти из терминала с автоматическим сохранением данных.")
    print(line)
    print("Цветовое выделение в таблице:")
    print("   Сумма = 0 ₽  → красный цвет")
    print("   Сумма > 0 ₽  → зелёный цвет")
    print("   Статус 'Пойдет' = Да → зелёная галочка ✓")
    print("   Статус 'Пойдет' = Нет → красный крест ✗")
    print(line)

# Терминал
def terminal():
    running = False
    print("Введите 'start' чтобы начать работу с терминалом.")
    while True:
        cmd = input("> ").strip().lower()
        if cmd == "exit":
            save_data()
            print("Выход из терминала. Данные сохранены.")
            break
        elif cmd == "start":
            running = True
            print("Терминал запущен. Доступные команды: list, add, subtract, multiply, split, status, total, save, help, exit")
        elif not running:
            print("Сначала запустите терминал командой 'start'.")
        elif cmd == "list":
            show_table()
        elif cmd == "add":
            add_money()
        elif cmd == "subtract":
            subtract_money()
        elif cmd == "multiply":
            multiply_money()
        elif cmd == "split":
            split_money()
        elif cmd == "status":
            change_status()
        elif cmd == "total":
            total_sum()
        elif cmd == "save":
            save_data()
        elif cmd == "help":
            show_help()
        else:
            print("Неизвестная команда. Доступные: list, add, subtract, multiply, split, status, total, save, help, exit")

# Запуск терминала
terminal()
