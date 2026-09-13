import sys

from PyQt6.QtWidgets import (
    QApplication,
    QGridLayout,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

morse = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', 'Стереть': 'ERASE'
}


class Morse(QWidget):
    def __init__(self):
        super().__init__()

        # Пользовательский интерфейс
        self.setWindowTitle("Азбука Морзе")

        # Главный макет
        main_layout = QVBoxLayout()

        # Виджет с полем вывода результата
        self.output_field = QLineEdit()
        self.output_field.setReadOnly(True)
        main_layout.addWidget(self.output_field)

        # Макет для кнопок
        grid_layout = QGridLayout()

        # Создание кнопок в цикле
        for index, letter in enumerate(morse.keys()):
            button = QPushButton(letter)

            # Сигнал нажатия кнопки, привязанный к обработчику
            button.clicked.connect(self.append_morse)  # type: ignore

            # Вычисляем позицию в сетке (по 6 кнопок в ряд)
            row = index // 3  #
            col = index % 3  #

            # Добавление кнопки на макет
            grid_layout.addWidget(button, row, col)

        main_layout.addLayout(grid_layout)
        self.setLayout(main_layout)

    def append_morse(self):
        # Обработчик нажатой кнопки
        # Получение отправителя
        sender_button = self.sender()

        # Получение ключа отправителя
        letter = sender_button.text()  # type: ignore

        morse_char = morse[letter]

        # Получаем текущий текст из поля
        current_text = self.output_field.text()

        if morse_char == 'ERASE':
            new_text = ""
        elif current_text:
            new_text = f"{current_text} {morse_char}"
        else:
            new_text = morse_char

        self.output_field.setText(new_text)


app = QApplication(sys.argv)

window = Morse()
window.show()

app.exec()
