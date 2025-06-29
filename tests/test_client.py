import sys
import pytest
from PySide6.QtWidgets import QApplication
from client.main import MainWindow


@pytest.fixture
def app():
    if not QApplication.instance():
        app = QApplication(sys.argv)

    window = MainWindow()
    yield window
    window.close()

def test_ui_initial_state(app):
    print()
    assert app.ui.lineEdit.text() == ""
    assert app.ui.listView.model() is None
    assert app.click_count == 0
    assert app.current_page == 1


def test_combobox_initial_state(app):
    assert app.ui.comboBox.count() == 4          # 4 варианта выбора
    assert app.ui.comboBox.currentText() == "5"  # По умолчанию выбрано 5
    assert app.ui.comboBox.itemText(0) == "5"    # Первый элемент
    assert app.ui.comboBox.itemText(3) == "50"   # Последний элемент


def test_add_button_click_count(app):
    initial_count = app.click_count
    app.on_add_button_clicked()
    assert app.click_count == initial_count + 1
