from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO

def load_image(url):
    try:
        # Отправляем GET-запрос с использованием requests.get()
        response = requests.get(url)
        # Проверяем успешность запроса (код ответа 200)
        response.raise_for_status()
        # Читаем байты из ответа в объект BytesIO
        image_data = BytesIO(response.content)
        # Открываем изображение с помощью PIL
        img = Image.open(image_data)
        # Изменяем размер изображения
        img.thumbnail((600, 480), Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"Ошибка при загрузке изображения: {e}")
        return None


def open_new_window():
    # Вызываем функцию для загрузки изображения
    img = load_image(url)
if img:
    # Создаем новое вторичное окно
    new_window = Toplevel()
    new_window.title("Картинка с котиком")
    new_window.geometry("600x480")

    # Добавляем изображение в новое окно
    label = Label(new_window, image=img)
    label.image = img  # Сохраняем ссылку на изображение
    label.pack()


def exit_app():
    window.destroy()


window = Tk()
window.title("Cats!")
window.geometry("600x520")

# Создаем метку без изображения
label = Label(window)
label.pack()

# Создаем меню
menu_bar = Menu(window)
window.config(menu=menu_bar)

# Добавляем пункты меню
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Загрузить фото", command=open_new_window)
file_menu.add_separator()
file_menu.add_command(label="Выход", command=exit)

url = url = 'https://cataas.com/cat'


window.mainloop()
