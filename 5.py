import sys

from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QHBoxLayout,
    QLabel,
    QPlainTextEdit,
    QPushButton,
    QSpinBox,
    QVBoxLayout,
    QWidget,
)


class Restaurant(QWidget):
    # Словарь с меню
    menu = {
        "Блюдо 1": 350,
        "Блюдо 2": 420,
        "Блюдо 3": 380,
        "Блюдо 4": 950,
        "Блюдо 5": 250,
        "Блюдо 6": 120,
    }

    def __init__(self):
        super().__init__()
        # Список для хранения ссылок на виджеты каждого блюда
        self.menu_widgets = []

        # Пользовательский интерфейс
        self.setWindowTitle("Ресторан")

        main_layout = QVBoxLayout()

        lbl_title = QLabel("Меню ресторана:")
        main_layout.addWidget(lbl_title)

        # Строки для каждого блюда
        for dish_name, price in self.menu.items():
            row_layout = QHBoxLayout()

            # Чекбокс выбора блюда
            checkbox = QCheckBox(f"{dish_name} ({price} руб.)")

            # Спинбокс для количества
            spinbox = QSpinBox()
            spinbox.setMinimum(1)
            spinbox.setEnabled(False)  # Изначально отключен, пока не стоит галочка

            checkbox.toggled.connect(spinbox.setEnabled)  # type: ignore

            row_layout.addWidget(checkbox)
            row_layout.addStretch()
            row_layout.addWidget(QLabel("Кол-во:"))
            row_layout.addWidget(spinbox)

            main_layout.addLayout(row_layout)

            # Ссылки на виджеты и блюда, чтобы потом посчитать стоимость
            self.menu_widgets.append({
                "name": dish_name,
                "price": price,
                "checkbox": checkbox,
                "spinbox": spinbox
            })

        # Кнопка оформления заказа
        self.btn_order = QPushButton("Оформить заказ")
        self.btn_order.clicked.connect(self.make_order)  # type: ignore
        main_layout.addWidget(self.btn_order)

        # Текстовое поле для вывода заказа
        self.receipt_text = QPlainTextEdit()
        self.receipt_text.setReadOnly(True)
        main_layout.addWidget(self.receipt_text)

        self.setLayout(main_layout)

    def make_order(self):
        # Обработчик кнопки заказа
        receipt_lines = ["КАССОВЫЙ ЧЕК", ""]
        total_order_sum = 0
        items_selected = False

        # Проходимся по всем блюдам в сохраненном списке
        for item in self.menu_widgets:
            # Если галочка стоит
            if item["checkbox"].isChecked():
                items_selected = True

                name = item["name"]
                price = item["price"]
                quantity = item["spinbox"].value()

                # Подсчёт стоимости блюда
                item_total = price * quantity
                total_order_sum += item_total

                # Формирование строки чека
                receipt_lines.append(f"{name}")
                receipt_lines.append(f"{quantity} порц. х {price} руб. = {item_total} руб.")
                receipt_lines.append("")

        if not items_selected:
            self.receipt_text.setPlainText("Нет выбранных блюд")
            return

        # Вывод итоговой суммы
        receipt_lines.append("-" * 20)
        receipt_lines.append(f"К ОПЛАТЕ: {total_order_sum} руб.")

        # Объединение списка строк в единый текст
        final_text = "\n".join(receipt_lines)
        self.receipt_text.setPlainText(final_text)


app = QApplication(sys.argv)

window = Restaurant()
window.show()

app.exec()
