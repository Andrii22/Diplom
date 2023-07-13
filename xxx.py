'''def button_click():
    value = entry.get()
    label.config(text=value)

# Создание экземпляра окна
window = Tk()

# Задание размеров окна

# Запрет изменения размеров окна пользователем
window.resizable(False, False)  # Окно не может изменяться

# Задание названия программы
window.title("Моя программа")

# Задание иконки программы (для Windows)
window.iconbitmap(r"C:\Users\Andrii\Downloads\1.ico")

# Создание надписи
label = Label(window, text="Введите значение:")
label.pack()


# Создание текстового поля
entry = Entry(window)
entry.pack()

# Создание кнопки
button = Button(window, text="Нажмите", command=button_click)
button.pack()'''
#----------------------------------------------------------------------

import tkinter as tk
import sqlite3
from tkinter import messagebox

# Создание базы данных SQLite и соединения
conn = sqlite3.connect('users.db')

# Создание таблицы для хранения пользователей
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users
             (username TEXT NOT NULL UNIQUE, password TEXT NOT NULL)''')
conn.commit()

def login():
    username = username_entry.get()
    password = password_entry.get()

    # Проверка соответствия введенных логина и пароля в базе данных
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = c.fetchone()

    if user:
        messagebox.showinfo("Успех", "Вход выполнен")
    else:
        messagebox.showerror("Ошибка", "Неверный логин или пароль")


# Создание окна
window = tk.Tk()

# Задание размеров окна
window.geometry("600x500")  # Ширина: 600 пикселей, Высота: 500 пикселей

# Запрет изменения размеров окна пользователем
window.resizable(False, False)  # Окно не может изменяться

# Задание названия программы
window.title("Моя программа")

# Задание иконки программы (для Windows)
window.iconbitmap(r"C:\Users\sadmin\Desktop\Private\Diplom-main\Diplom\student.ico")

# Создание и размещение элементов на окне
username_label = tk.Label(window, text="Логин")
username_label.pack()

username_entry = tk.Entry(window)
username_entry.pack()

password_label = tk.Label(window, text="Пароль")
password_label.pack()

password_entry = tk.Entry(window, show="*")
password_entry.pack()

login_button = tk.Button(window, text="Войти", command=login)
login_button.pack()

# Запуск главного цикла обработки событий
window.mainloop()

# Закрытие соединения с базой данных после закрытия окна
conn.close()


'''
# Создание окна
window = tk.Tk()

# Задание размеров окна
window.geometry("600x500")  # Ширина: 600 пикселей, Высота: 500 пикселей

# Запрет изменения размеров окна пользователем
window.resizable(False, False)  # Окно не может изменяться

# Задание названия программы
window.title("Моя программа")

# Задание иконки программы (для Windows)
window.iconbitmap(r"C:\Users\sadmin\Desktop\Private\Diplom-main\Diplom\student.ico")

# Создание и размещение элементов на окне
username_default_text = "Введите логин"
username_label = tk.Label(window, text="Логин")
username_label.pack()

username_entry = tk.Entry(window)
username_entry.pack()

password_label = tk.Label(window, text="Пароль")
password_default_text = "Введите пароль"
password_label.pack()

password_entry = tk.Entry(window, show="*")
password_entry.pack()

#register_button = tk.Button(window, text="Зарегистрироваться", command=create_user)
#register_button.pack()

login_button = tk.Button(window, text="Войти", command=login)
login_button.pack()

# Запуск главного цикла обработки событий
window.mainloop()
'''