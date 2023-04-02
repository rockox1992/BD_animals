import sqlite3
import OOP_Animals

db = sqlite3.connect('Animals.db')  # создаем нашу базу данных и подключимся

sql = db.cursor()  # Для работы с базой вызываем курсор

# Создание таблицы Cat
sql.execute("""CREATE TABLE IF NOT EXISTS cat(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT,
	Command TEXT,
    Birthday TEXT,
    cls_animals TEXT)
            """)
db.commit()  # Подтверждаем что нам нада таблица

# Создание таблицы dog
sql.execute("""CREATE TABLE IF NOT EXISTS dog(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT,
	Command TEXT,
    Birthday TEXT,
    cls_animals TEXT)
            """)
db.commit()  # Подтверждаем что нам нада таблица

# Создание таблицы hamster
sql.execute("""CREATE TABLE IF NOT EXISTS hamster(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT,
	Command TEXT,
    Birthday TEXT,
    cls_animals TEXT)
            """)
db.commit()  # Подтверждаем что нам нада таблица

# Создание таблицы camel
sql.execute("""CREATE TABLE IF NOT EXISTS camel(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT,
	Command TEXT,
    Birthday TEXT,
    cls_animals TEXT)
            """)
db.commit()  # Подтверждаем что нам нада таблица

# Создание таблицы horse
sql.execute("""CREATE TABLE IF NOT EXISTS horse(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT,
	Command TEXT,
    Birthday TEXT,
    cls_animals TEXT)
            """)
db.commit()  # Подтверждаем что нам нада таблица

# Создание таблицы donkey
sql.execute("""CREATE TABLE IF NOT EXISTS donkey(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT,
	Command TEXT,
    Birthday TEXT,
    cls_animals TEXT)
            """)
db.commit()  # Подтверждаем что нам нада таблица


# Декоратор счетчик запуска функции
def count(func):
    """
    Декоратор - счётчик
    """

    counters = {}

    def wrapper(er=None, *args, **kwargs):
        counters[func] = counters.get(func, 0) + 1
        print(f'Функция {func.__name__} вызвана {counters[func]} раз')
        return func(*args, **kwargs)

    return wrapper


# счетчик правильно выполненной команды add_animal()
cnt = 0


# @count
def add_animal():
    oop_a = OOP_Animals.xyz().split(", ")
    type_animal = oop_a[-1::]
    date_animal = oop_a[:-1]
    try:
        cnt_spase = 0 # счетчик данных в колонке
        for date in date_animal[:-1]:
            if ''.join(date).isalnum():
                cnt_spase += 1
                if cnt_spase == 3:
                    sql.execute(f"INSERT INTO {''.join(type_animal)}"
                                f"(name, Command, Birthday, cls_animals) VALUES (?, ?, ?, ?)", date_animal)
                    db.commit()
                    global cnt
                    cnt += 1
            else:
                raise Exception("Не заполнены колонки!")
    except Exception as err:
        print(err)
        return add_animal()


print("Данные добавлены!", cnt)


# Добавление команды животному
def add_command():
    try:
        table_animal = show()
        name_animal = input('Введите имя животного, которому надо добавить команду: ')
        sql.execute(f"UPDATE {table_animal} SET Command = Command || ' ' || '{input('Введите команду: ')}' WHERE name ="
                    f"'{name_animal}'")
        db.commit()
        print("Добавление выполнено!")
    except sqlite3.OperationalError:
        print("Колонки с таким именем нет!")
        pass


# # Добавление в таблицу dog
# def add_dog():
#     oop_a = OOP_Animals.xyz().split(", ")
#     dog = oop_a[-1::]
#     print(''.join(dog))
#     sql.execute(f"INSERT INTO {''.join(dog)}(name, Command, Birthday, cls_animals) VALUES (?, ?, ?, ?)", oop_a[:-1])
#     db.commit()
#
#
# # Добавление в таблицу hamster
# def add_hamster():
#     oop_a = OOP_Animals.xyz().split(", ")
#     sql.execute(f"INSERT INTO hamster(name, Command, Birthday, cls_animals) VALUES (?, ?, ?, ?)", oop_a[:-1])
#     db.commit()
#
#
# # Добавление в таблицу horse
# def add_horse():
#     oop_a = OOP_Animals.xyz().split(", ")
#     sql.execute(f"INSERT INTO horse(name, Command, Birthday, cls_animals) VALUES (?, ?, ?, ?)", oop_a[:-1])
#     db.commit()
#
#
# # Добавление в таблицу camel
# def add_camel():
#     oop_a = OOP_Animals.xyz().split(", ")
#     sql.execute(f"INSERT INTO camel(name, Command, Birthday, cls_animals) VALUES (?, ?, ?, ?)", oop_a[:-1])
#     db.commit()
#
#
# # Добавление в таблицу donkey
# def add_donkey():
#     oop_a = OOP_Animals.xyz().split(", ")
#     sql.execute(f"INSERT INTO donkey(name, Command, Birthday, cls_animals) VALUES (?, ?, ?, ?)", oop_a[:-1])
#     db.commit()


# Просмотр команд животного
def sh_command():
    try:
        table_animal = show_name()
        name_animal = input('Введите имя животного, чьи команды вы хотите посмотреть: ')
        sql.execute(f"SELECT Command FROM {table_animal} WHERE name = '{name_animal}'")
        print(sql.fetchall())
        db.commit()
    except sqlite3.OperationalError:
        print("Колонки с таким именем нет!")
        pass


# Просмотр имени животных
def show_name():
    try:
        name = input("В ведите название типа животного: ")
        sql.execute(f"SELECT name FROM {name}")
        print(sql.fetchall())
        return name
        db.commit()
    except sqlite3.OperationalError:
        print("Колонки с таким именем нет!")
        pass


# Просмотр всей таблицы в зависимости от типа животного
def show():
    name = input("В ведите название типа животного: ")
    for value in sql.execute(f"SELECT * FROM {name}"):
        print(value)
    return name
    db.commit()


# Просмотр названий всех таблиц
def show_tables():
    sql.execute("""SELECT name FROM sqlite_master WHERE type='table'""")
    tables = sql.fetchall()
    for table in tables:
        if table == ('sqlite_sequence',):
            continue
        else:
            print(table)
