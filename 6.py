import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QGridLayout,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.is_error_state = False  # Флаг состояния ошибки
        self.left_operand = ""  # Левая часть выражения
        self.pending_operator = ""  # Ожидающая операция
        self.new_input = True  # Флаг ввода нового числа

        # Пользовательский интерфейс
        self.setWindowTitle("Калькулятор")
        self.setFixedSize(300, 400)

        main_layout = QVBoxLayout()

        # Поле экрана
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        # Выравнивание текста
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        # Увеличим шрифт для удобства
        self.display.setStyleSheet("font-size: 24px; padding: 10px;")
        main_layout.addWidget(self.display)

        # Макет для кнопок
        grid_layout = QGridLayout()

        # Раскладка кнопок
        buttons_layout = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['C', '0', '.', '+']
        ]

        # Создание кнопок
        for row_indx, row in enumerate(buttons_layout):
            for col_indx, btn_text in enumerate(row):
                btn = QPushButton(btn_text)
                btn.setMinimumHeight(50)
                btn.setStyleSheet("font-size: 18px;")
                btn.clicked.connect(self.on_button_clicked)  # type: ignore
                grid_layout.addWidget(btn, row_indx, col_indx)

        # Отдельная кнопка "="
        btn_equals = QPushButton("=")
        btn_equals.setMinimumHeight(50)
        btn_equals.setStyleSheet("font-size: 20px; font-weight: bold; background-color: #4CAF50;")
        btn_equals.clicked.connect(self.on_button_clicked)  # type: ignore
        grid_layout.addWidget(btn_equals, len(buttons_layout), 0, 1, 4)

        main_layout.addLayout(grid_layout)
        self.setLayout(main_layout)

    def on_button_clicked(self):
        # Обработчик нажатия кнопки
        sender_button = self.sender()
        btn_text = sender_button.text()  # type: ignore

        # Сброс калькулятора после ошибки
        if self.is_error_state:
            self.display.clear()
            self.is_error_state = False
            self.left_operand = ""
            self.pending_operator = ""
            self.new_input = True

        if btn_text == 'C':
            self.display.clear()
            self.left_operand = ""
            self.pending_operator = ""
            self.new_input = True

        elif btn_text in ['+', '-', '*', '/']:
            # Если экран пуст или ожидается новое число, минус считается знаком числа
            if btn_text == '-' and (self.display.text() == "" or self.new_input):
                self.display.setText("-")
                self.new_input = False
                return

            # Вычисление промежуточного результата при повторном вводе оператора
            if self.pending_operator and not self.new_input:
                self.calculate_result()

            # Запоминаем текущее число или промежуточный результат и нажатый знак
            self.left_operand = self.display.text()
            self.pending_operator = btn_text
            self.new_input = True  # Изменение флага ввода нового числа

        elif btn_text == '=':
            if self.pending_operator and not self.new_input:
                self.calculate_result()
            self.pending_operator = ""
            self.left_operand = ""
            self.new_input = True

        else:
            # Обработка цифр и точки
            if self.new_input:
                self.display.clear()
                self.new_input = False

            current_text = self.display.text()
            self.display.setText(current_text + btn_text)

    def calculate_result(self):
        # Метод вычисления результата
        right_operand = self.display.text()

        expression = f"{self.left_operand}{self.pending_operator}{right_operand}"

        try:
            result = eval(expression)

            if isinstance(result, float) and result.is_integer():
                result = int(result)

            self.display.setText(str(result))

        except ZeroDivisionError:
            self.display.setText("Деление на ноль")
            self.is_error_state = True
        except Exception:
            self.display.setText("Ошибка")
            self.is_error_state = True


app = QApplication(sys.argv)

window = Calculator()
window.show()

app.exec()
