import sys
import os
import vlc
import time
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel, QSlider

# Указываем путь к установленному VLC
vlc_path = r"C:\Program Files\VideoLAN\VLC"  # Замените на актуальный путь

# Устанавливаем переменные окружения для VLC
os.environ['VLC_PLUGIN_PATH'] = os.path.join(vlc_path, "plugins")
os.environ['LD_LIBRARY_PATH'] = vlc_path

class VideoPlayer(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Минималистичный видеоплеер")
        self.setWindowIcon(QIcon("icon.png"))  # Укажите путь к иконке, если нужна
        self.setGeometry(200, 200, 800, 600)

        # Инициализация VLC
        self.instance = vlc.Instance()
        self.media_player = self.instance.media_player_new()

        # Интерфейс
        self.layout = QVBoxLayout()

        # Кнопка для выбора файла
        self.select_button = QPushButton("Выбрать файл")
        self.select_button.clicked.connect(self.select_file)
        self.layout.addWidget(self.select_button)

        # Метка для отображения пути к файлу
        self.path_label = QLabel("Путь к файлу: ")
        self.layout.addWidget(self.path_label)

        # Кнопки управления
        self.play_button = QPushButton("Воспроизвести")
        self.play_button.clicked.connect(self.toggle_play)
        self.layout.addWidget(self.play_button)

        self.stop_button = QPushButton("Остановить")
        self.stop_button.clicked.connect(self.stop_video)
        self.layout.addWidget(self.stop_button)

        # Ползунок для регулировки громкости
        self.volume_slider = QSlider(Qt.Orientation.Horizontal)
        self.volume_slider.setRange(0, 100)
        self.volume_slider.setValue(50)
        self.volume_slider.valueChanged.connect(self.set_volume)
        self.layout.addWidget(self.volume_slider)

        # Ползунок для регулировки времени
        self.time_slider = QSlider(Qt.Orientation.Horizontal)
        self.time_slider.setRange(0, 100)
        self.time_slider.sliderMoved.connect(self.seek_video)
        self.layout.addWidget(self.time_slider)

        self.setLayout(self.layout)

        # Инициализация переменных
        self.media = None
        self.is_playing = False

    def select_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Выбрать файл", "", "Видео файлы (*.mp4 *.avi *.mkv *.mov)")
        if file_path:
            self.media = self.instance.media_new(file_path)
            self.media_player.set_media(self.media)
            self.path_label.setText(f"Путь к файлу: {file_path}")
            self.time_slider.setValue(0)

    def toggle_play(self):
        if self.media:
            if self.is_playing:
                self.media_player.pause()
                self.play_button.setText("Воспроизвести")
            else:
                self.media_player.play()
                self.play_button.setText("Пауза")
            self.is_playing = not self.is_playing

    def stop_video(self):
        if self.media:
            self.media_player.stop()
            self.is_playing = False
            self.play_button.setText("Воспроизвести")
            self.time_slider.setValue(0)

    def set_volume(self):
        volume = self.volume_slider.value()
        self.media_player.audio_set_volume(volume)

    def seek_video(self):
        if self.media:
            position = self.time_slider.value() / 100
            self.media_player.set_position(position)

    def closeEvent(self, event):
        self.media_player.release()  # Освобождаем ресурсы при закрытии окна
        event.accept()

def main():
    app = QApplication(sys.argv)
    player = VideoPlayer()
    player.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()