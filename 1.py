import sys

from PyQt6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLineEdit,
    QPushButton,
    QWidget,
)


class WordThrower(QWidget):
    def __init__(self):
        super().__init__()

        # Пользовательский интерфейс
        self.setWindowTitle("Перекидыватель слов")
        self.resize(500, 80)

        # Создание виджетов
        self.input_left = QLineEdit()
        self.input_right = QLineEdit()
        self.btn_transfer = QPushButton("->")
        self.input_right.setReadOnly(True)

        # Создание горизонтального макета, добавление виджетов
        layout = QHBoxLayout()
        layout.addWidget(self.input_left)
        layout.addWidget(self.btn_transfer)
        layout.addWidget(self.input_right)

        # Установка этого макета для главного окна
        self.setLayout(layout)

        # Подключаем сигнал нажатия кнопки к методу обработки
        self.btn_transfer.clicked.connect(self.transfer_text)  # type: ignore

    def transfer_text(self):
        # Логика переноса текста
        if self.btn_transfer.text() == "->":
            # Перенос текста слева направо
            text = self.input_left.text()
            self.input_right.setText(text)
            self.input_left.clear()
            self.input_right.setReadOnly(False)
            self.input_left.setReadOnly(True)
            self.btn_transfer.setText("<-")
        else:
            # Перенос текста справа налево
            text = self.input_right.text()
            self.input_left.setText(text)
            self.input_right.clear()
            self.input_right.setReadOnly(True)
            self.input_left.setReadOnly(False)
            self.btn_transfer.setText("->")


app = QApplication(sys.argv)

window = WordThrower()
window.show()

app.exec()
