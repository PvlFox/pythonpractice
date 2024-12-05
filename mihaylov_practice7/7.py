import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QMenuBar, QAction, QFileDialog, QVBoxLayout, QWidget

class NoteApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Основные настройки окна
        self.setWindowTitle("Приложение для заметок")
        self.setGeometry(100, 100, 600, 400)

        # Текстовый редактор для заметок
        self.text_edit = QTextEdit(self)
        self.setCentralWidget(self.text_edit)

        # Создание меню
        self.init_ui()

    def init_ui(self):
        # Меню
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('Файл')

        # Создание действий для меню
        new_action = QAction('Новая заметка', self)
        new_action.triggered.connect(self.new_note)

        save_action = QAction('Сохранить заметку', self)
        save_action.triggered.connect(self.save_note)

        # Добавление действий в меню
        file_menu.addAction(new_action)
        file_menu.addAction(save_action)

    def new_note(self):
        """Создание новой заметки"""
        self.text_edit.clear()  # Очищаем текущий текст

    def save_note(self):
        """Сохранение заметки в файл"""
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, "Сохранить заметку", "", "Text Files (*.txt);;All Files (*)", options=options)
        if file_name:
            with open(file_name, 'w', encoding='utf-8') as file:
                file.write(self.text_edit.toPlainText())  # Сохраняем текст из редактора


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = NoteApp()
    window.show()
    sys.exit(app.exec_())