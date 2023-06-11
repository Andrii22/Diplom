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
