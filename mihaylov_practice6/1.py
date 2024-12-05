import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Инициализация компонентов окна
        self.setWindowTitle("Пример с кнопкой и меткой")
        self.setGeometry(300, 300, 400, 200)

        # Создание кнопки и метки
        self.button = QPushButton("Нажми меня!", self)
        self.label = QLabel("Текст метки", self)

        # Применение CSS-стилей к кнопке и метке
        self.button.setStyleSheet("""
            QPushButton {
                background-color: lightblue;
                font-size: 18px;
                padding: 10px;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: lightgreen;
            }
        """)
        self.label.setStyleSheet("""
            QLabel {
                font-size: 20px;
                color: darkblue;
            }
        """)

        # Создание макета и добавление виджетов
        layout = QVBoxLayout()
        layout.addWidget(self.button)
        layout.addWidget(self.label)

        # Установка макета для окна
        self.setLayout(layout)

        # Подключение сигнала кнопки к слоту
        self.button.clicked.connect(self.on_button_click)

    def on_button_click(self):
        # Изменение текста метки
        self.label.setText("Кнопка нажата!")

        # Динамическое изменение стилей виджетов
        self.change_style()

    def change_style(self):
        # Изменение стиля метки
        self.label.setStyleSheet("""
            QLabel {
                font-size: 22px;
                color: red;
                font-weight: bold;
            }
        """)
        
        # Изменение стиля кнопки
        self.button.setStyleSheet("""
            QPushButton {
                background-color: yellow;
                font-size: 20px;
                padding: 15px;
                border-radius: 15px;
            }
            QPushButton:hover {
                background-color: orange;
            }
        """)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Создание и отображение главного окна
    window = MainWindow()
    window.show()

    # Запуск приложения
    sys.exit(app.exec_())