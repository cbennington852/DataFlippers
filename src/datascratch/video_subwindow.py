import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QSlider, QMdiSubWindow, QSizePolicy
from PyQt5 import QtWidgets as QtW
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import QUrl, Qt

import os
if sys.platform == "linux" or sys.platform == "linux2":
    os.environ["LIBVA_DRIVER_NAME"] = "fake"


class VideoSubwindow(QMdiSubWindow):
    BASE_HEIGHT = 300
    BASE_WIDTH = 400

    def __init__(self, parent , ptr_to_pipeline_parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.my_parent = ptr_to_pipeline_parent
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        container = QWidget()
        self.setWidget(container)

        self.media_player = QMediaPlayer()
        self.video_widget = QVideoWidget()
        self.resize(VideoSubwindow.BASE_WIDTH , VideoSubwindow.BASE_HEIGHT)

        self.media_player.setVideoOutput(self.video_widget)
        self.media_player.setMedia(QMediaContent(QUrl.fromLocalFile("/home/ella/Documents/GitHub/gui_scikit_learn/python_gui_scikit/Video.mp4")))
        self.media_player.positionChanged.connect(self.position_changed)
        self.media_player.durationChanged.connect(self.duration_changed)

        self.toolbar = QtW.QToolBar()

        self.start_button = QPushButton("Play")
        self.start_button.setIcon(QApplication.instance().style().standardIcon(QtW.QStyle.StandardPixmap.SP_MediaPlay))
        self.start_button.clicked.connect(self.start_video)

        self.pause_button = QPushButton("Pause")
        self.pause_button.setIcon(QApplication.instance().style().standardIcon(QtW.QStyle.StandardPixmap.SP_MediaPause))
        self.pause_button.clicked.connect(self.pause_video)

        self.stop_button = QPushButton("Stop")
        self.stop_button.setIcon(QApplication.instance().style().standardIcon(QtW.QStyle.StandardPixmap.SP_MediaStop))
        self.stop_button.clicked.connect(self.stop_video)

        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.sliderMoved.connect(self.set_position)

        

        layout = QVBoxLayout()
        container.setLayout(layout)
        layout.addWidget(self.video_widget)
        layout.addWidget(self.toolbar)
        self.toolbar.addWidget(self.start_button)
        self.toolbar.addWidget(self.pause_button)
        self.toolbar.addWidget(self.stop_button)
        layout.addWidget(self.slider)

        

    def start_video(self):
        self.media_player.play()

    def pause_video(self):
        self.media_player.pause()

    def stop_video(self):
        self.media_player.stop()

    def set_position(self, position):
        self.media_player.setPosition(position)

    def position_changed(self, position):
        self.slider.setValue(position)

    def duration_changed(self, duration):
        self.slider.setRange(0, duration)

