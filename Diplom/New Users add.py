import sqlite3

conn = sqlite3.connect('users.db')
c = conn.cursor()

# Ввод данных с клавиатуры
username = input("Введите логин: ")
password = input("Введите пароль: ")

# Выполнение SQL-запроса для добавления данных
c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))

# Сохранение изменений и закрытие соединения
conn.commit()
conn.close()


