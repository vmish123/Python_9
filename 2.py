import sys

from PyQt6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLineEdit,
    QPushButton,
    QWidget,
)


class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        # Пользовательский интерфейс
        self.setWindowTitle("Калькулятор")
        self.resize(500, 80)

        # Создание виджетов
        self.expression = QLineEdit()
        self.btn_calculate = QPushButton("Вычислить")
        self.result = QLineEdit()
        self.result.setReadOnly(True)

        # Создание горизонтального макета, добавление виджетов
        layout = QHBoxLayout()
        layout.addWidget(self.expression)
        layout.addWidget(self.btn_calculate)
        layout.addWidget(self.result)

        # Установка этого макета для главного окна
        self.setLayout(layout)

        # Подключаем сигнал нажатия кнопки к методу обработки
        self.btn_calculate.clicked.connect(self.calculate)  # type: ignore

    def calculate(self):
        # Логика вычисления
        expression = self.expression.text()

        # Завершение, если выражения нет
        if not expression.strip():
            self.result.clear()
            return

        try:
            result = str(eval(expression))
            self.result.setText(result)
        except Exception:
            self.expression.clear()
            self.result.clear()
            return


app = QApplication(sys.argv)

window = Calculator()
window.show()

app.exec()
