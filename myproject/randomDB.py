import sqlite3
import random
import datetime

# Списки для генерации случайных значений
names = ["Иван", "Петр", "Алексей", "Сергей", "Мария", "Екатерина", "Анна", "Ольга"]
surnames = ["Иванов", "Петров", "Сидоров", "Смирнова", "Кузнецова", "Новикова"]
phones = ["79991234567", "79881234567", "79991234568", "79881234568", "79991234569", "79881234569"]
now = datetime.datetime.now()

# Создание базы данных и таблицы
conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()
c.execute('''CREATE TABLE members
             (id INTEGER PRIMARY KEY,
             name TEXT,
             surname TEXT,
             phone TEXT,
             birthdate DATE,
             lessons INTEGER,
             first_purchase DATE,
             next_purchase DATE,
             valid_absences INTEGER,
             unvalid_absences INTEGER,
             delays INTEGER)''')

# Заполнение таблицы случайными значениями
for i in range(50):
    name = random.choice(names)
    surname = random.choice(surnames)
    phone = random.choice(phones)
    birthdate = datetime.date(random.randint(1960, 2005), random.randint(1, 12), random.randint(1, 28))
    lessons = random.randint(0, 100)
    first_purchase = datetime.date(now.year - random.randint(0, 5), random.randint(1, 12), random.randint(1, 28))
    next_purchase = first_purchase + datetime.timedelta(days=random.randint(30, 365))
    valid_absences = random.randint(0, 10)
    unvalid_absences = random.randint(0, 10)
    delays = random.randint(0, 5)
    c.execute("INSERT INTO clients VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
              (i+1, name, surname, phone, birthdate, lessons, first_purchase, next_purchase,valid_absences, unvalid_absences, delays))

# Сохранение изменений и закрытие соединения
conn.commit()
conn.close()
