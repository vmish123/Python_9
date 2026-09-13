import sys

from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QHBoxLayout,
    QProgressBar,
    QPushButton,
    QVBoxLayout,
    QWidget, QSizePolicy,
)


class WidgetCheckbox(QWidget):
    def __init__(self):
        super().__init__()

        # Пользовательский интерфейс
        self.setWindowTitle("Чек-боксы")
        self.resize(500, 200)

        # Создание виджетов
        self.progress_bar = QProgressBar()
        self.progress_bar.setValue(50)
        self.button = QPushButton("Кнопка")
        self.button.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed
        )
        self.combo_box = QComboBox()
        self.combo_box.addItems(["Опция 1", "Опция 2", "Опция 3"])
        self.combo_box.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed
        )

        # Создание чек-боксов
        self.chk_progress = QCheckBox()
        self.chk_button = QCheckBox()
        self.chk_combo = QCheckBox()
        self.chk_progress.setChecked(True)
        self.chk_button.setChecked(True)
        self.chk_combo.setChecked(True)

        # Словарь связывающий чек-боксы с виджетами
        self.widget_map = {
            self.chk_progress: self.progress_bar,
            self.chk_button: self.button,
            self.chk_combo: self.combo_box,
        }

        # Главный макет
        main_layout = QVBoxLayout()

        # Горизонтальные макеты: чек-бокс - виджет
        for checkbox, widget in self.widget_map.items():
            row_layout = QHBoxLayout()
            row_layout.addWidget(checkbox)
            row_layout.addWidget(widget)
            main_layout.addLayout(row_layout)

            # Сигнал переключения чек-бокса, связанный с обработчиком
            checkbox.toggled.connect(self.checkbox_handler)  # type: ignore

        self.setLayout(main_layout)

    def checkbox_handler(self, checked):
        # Объект отправителя
        sender_checkbox = self.sender()

        # Виджет связанный с отправителем
        target_widget = self.widget_map.get(sender_checkbox)  # type: ignore

        target_widget.setVisible(checked)


app = QApplication(sys.argv)

window = WidgetCheckbox()
window.show()

app.exec()
