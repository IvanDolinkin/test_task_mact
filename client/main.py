import sys
import requests
from PySide6.QtCore import QStringListModel
from PySide6.QtWidgets import QApplication, QMainWindow
from .app_window import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Инициализация
        self.current_page = 1
        self.total_pages = 1
        self.click_count = 0

        # Настройка ComboBox для выбора количества элементов
        self.ui.comboBox.addItems(["5", "10", "20", "50"])
        self.ui.comboBox.setCurrentIndex(0)

        # Подключение сигналов
        self.ui.AddButton.clicked.connect(self.on_add_button_clicked)
        self.ui.GetButton.clicked.connect(self.on_get_button_clicked)
        self.ui.PrevButton.clicked.connect(self.on_prev_button_clicked)
        self.ui.NextButton.clicked.connect(self.on_next_button_clicked)
        self.ui.spinBox.valueChanged.connect(self.on_page_changed)
        self.ui.comboBox.currentTextChanged.connect(self.on_items_per_page_changed)


    def load_items(self):
        try:
            items_per_page = int(self.ui.comboBox.currentText())
            response = requests.get(
                url="http://127.0.0.1:8000/items",
                params={
                    "page": self.current_page,
                    "num_records": items_per_page
                }
            )

            if response.status_code == 200:
                data = response.json()
                self.total_pages = (data["total"] + items_per_page - 1) // items_per_page
                self.update_ui(data)

        except Exception as e:
            print("Ошибка загрузки:", e)

    def update_ui(self, data):
        items_list = [
            f"{item['id']}. {item['name']} | "
            f"{item['date']} {item['time'].split('.')[0]} | "
            f"Кликов: {item['click_count']}"
            for item in data["items"]
        ]

        model = QStringListModel()
        model.setStringList(items_list)
        self.ui.listView.setModel(model)

        # Обновление пагинации
        self.ui.spinBox.blockSignals(True)
        self.ui.spinBox.setMaximum(max(1, self.total_pages))
        self.ui.spinBox.setMinimum(1)
        self.ui.spinBox.setValue(self.current_page)
        self.ui.spinBox.blockSignals(False)

        self.ui.labelOf.setText(f"Of {self.total_pages}")
        self.ui.PrevButton.setEnabled(self.current_page > 1)
        self.ui.NextButton.setEnabled(self.current_page < self.total_pages)

    def on_add_button_clicked(self):
        self.click_count += 1

        item_name = self.ui.lineEdit.text().strip()
        if not item_name:
            return

        try:
            response = requests.post(
                url="http://127.0.0.1:8000/item",
                json={
                    "name": item_name,
                    "click_count": self.click_count
                }
            )
            if response.status_code == 200:
                self.ui.lineEdit.clear()  # Очищаем поле ввода

        except Exception as e:
            print("Ошибка добавления:", e)

    def on_get_button_clicked(self):
        self.load_items()

    def on_prev_button_clicked(self):
        if self.current_page > 1:
            self.current_page -= 1
            self.load_items()

    def on_next_button_clicked(self):
        if self.current_page < self.total_pages:
            self.current_page += 1
            self.load_items()

    def on_page_changed(self, value):
        if 1 <= value <= self.total_pages:
            self.current_page = value
            self.load_items()

    def on_items_per_page_changed(self):
        self.current_page = 1
        self.load_items()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
