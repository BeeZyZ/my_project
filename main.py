import PySimpleGUI as sg
from module import generate_random_number, is_even
from database import Database

def main():
    # Задаємо кольорову палітру
    sg.theme('LightGreen')

    # Створюємо екземпляр бази даних
    db = Database()

    # Описуємо макет графічного інтерфейсу
    layout = [
        [sg.Text("Натисніть на кнопку, щоб згенерувати випадкове число і перевірити його парність.")],
        [sg.Button("Генерувати число"), sg.Text("", size=(15, 1), key="-OUTPUT-")],
    ]

    # Створюємо вікно з макетом
    window = sg.Window("Графічний інтерфейс", layout)

    # Основний цикл програми
    while True:
        event, values = window.read()

        # Вихід з програми при закритті вікна
        if event == sg.WIN_CLOSED:
            break

        # Обробка події - генерація числа та перевірка парності
        if event == "Генерувати число":
            random_number = generate_random_number()
            window["-OUTPUT-"].update(f"Згенероване число: {random_number}")

            if is_even(random_number):
                sg.popup("Згенероване число парне.")
            else:
                sg.popup("Згенероване число непарне.")

            # Зберігаємо дані в базу даних
            db.save_data(random_number)

    # Закриваємо вікно при завершенні програми
    window.close()

if __name__ == "__main__":
    main()
