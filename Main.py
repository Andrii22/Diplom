import tkinter as tk
import mysql.connector
from tkinter import messagebox
from ttkthemes import ThemedTk
from tkhtmlview import HTMLLabel
from tkinter import ttk
import socket
from datetime import datetime

# Подключение к базе данных MySQL
conn = mysql.connector.connect(
    host="85.10.205.173", #https://www.db4free.net/phpMyAdmin/index.php?route=/sql&pos=0&db=kubg_diplom&table=login_monitoring
    user="kubg_diplom",
    password="yyEvOmhV",
    database="kubg_diplom"
)
cursor = conn.cursor()

# Создание таблицы для мониторинга входа
create_table_query = """
CREATE TABLE IF NOT EXISTS login_monitoring (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(20),
    ip_address VARCHAR(15),
    login_time DATETIME DEFAULT CURRENT_TIMESTAMP
)
"""
cursor.execute(create_table_query)

def center_window(window):
    # Получение размеров экрана
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Расчет координат верхнего левого угла окна для центрирования
    window_width = window.winfo_width()
    window_height = window.winfo_height()
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    # Установка новых координат окна
    window.geometry(f"+{x}+{y}")


def validate_login():
    username = username_entry.get()
    password = password_entry.get()

    if not username or not password:
        messagebox.showerror("Ошибка", "Введите логин и пароль")
    elif len(username) < 3 or len(username) > 20:
        messagebox.showerror("Ошибка", "Длина логина должна быть от 3 до 20 символов")
    elif len(password) < 3 or len(password) > 20:
        messagebox.showerror("Ошибка", "Длина пароля должна быть от 3 до 20 символов")
    else:
        login()


def login():
    username = username_entry.get()
    password = password_entry.get()

    # Проверка соответствия введенных логина и пароля в базе данных
    query = "SELECT * FROM users WHERE user=%s AND pass=%s"  # Здесь изменено имя столбца
    cursor.execute(query, (username, password))
    user = cursor.fetchone()

    if user:
        # Запись информации о входе в таблицу login_monitoring
        ip_address = socket.gethostbyname(socket.gethostname())
        insert_query = "INSERT INTO login_monitoring (username, ip_address) VALUES (%s, %s)"
        cursor.execute(insert_query, (username, ip_address))
        conn.commit()

        messagebox.showinfo("Успех", "Вход выполнен")
        # Закрытие текущего окна
        window.destroy()
        main_window(username)  # Передача имени пользователя в main_window()
    else:
        messagebox.showerror("Ошибка", "Неверный логин или пароль")


def button_clicked(button_name):
    print(f"Кликнута кнопка {button_name}")


def main_window(username):
    # Создание нового окна для приветствия
    welcome_window = ThemedTk(theme="equilux")

    # Задание размеров окна
    welcome_window.geometry("600x500")  # Ширина: 600 пикселей, Высота: 500 пикселей

    # Запрет изменения размеров окна пользователем
    welcome_window.resizable(False, False)  # Окно не может изменяться
    # Центрирование окна при открытии
    welcome_window.update()
    center_window(welcome_window)

    # Задание названия программы
    welcome_window.title("Асистент вчителя информатики")

    # Задание иконки программы (для Windows)
    welcome_window.iconbitmap(r"C:\Users\sadmin\Desktop\Private\Diplom-main\Diplom\student01.ico")

    # Вывод приветственной информации
    welcome_label = tk.Label(welcome_window, text="Ассистент вчителя информатики", font=("Times New Roman", 16))
    welcome_label.pack()

    welcome_username_label = tk.Label(welcome_window, text="Добро пожаловать, " + username, font=("Times New Roman", 12))
    welcome_username_label.pack(anchor=tk.NE)

    # Create an HTMLLabel widget
    html_label = HTMLLabel(welcome_window)
    html_label.pack()

     # Чтение содержимого файла
    with open(r"C:\Users\sadmin\Desktop\Private\Diplom-main\Diplom\front\main.html", "r") as file:
        html_content = file.read()

    # Установка HTML-контента в виджете
    html_label.set_html(html_content)

    # Создание и размещение кнопок
    button_name = "Открыть календарь"
    button = ttk.Button(welcome_window, text=str(button_name), width=30, command=lambda name=button_name: button_clicked(name))
    button.pack(side=tk.LEFT, padx=85, pady=85, ipadx=25, ipady=25)

    # Запуск главного цикла обработки событий нового окна
    welcome_window.mainloop()


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

login_button = tk.Button(window, text="Войти", command=validate_login)
login_button.pack()

# Закрытие соединения с базой данных после закрытия окна
def on_closing():
    cursor.close()
    conn.close()
    window.destroy()

window.protocol("WM_DELETE_WINDOW", on_closing)

# Центрирование окна при открытии
window.update()
center_window(window)

# Запуск главного цикла обработки событий
window.mainloop()
