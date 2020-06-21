# from PySide2.QtCore import *
# from PySide2.QtGui import *
# from PySide2.QtWidgets import *
from PySide2.QtCore import QTimer
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
import cv2  # OpenCV
import qimage2ndarray  # for a memory leak,see gist
import sys  # for exiting


# Minimal implementation...


def display_frame():
    _, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image = qimage2ndarray.array2qimage(frame)
    label.setPixmap(QPixmap.fromImage(image))


app = QApplication([])
window = QWidget()

# OPENCV

# cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)

# timer for getting frames

timer = QTimer()
timer.timeout.connect(display_frame)
timer.start(100)
label = QLabel('No Camera Feed')
button = QPushButton("Quit")
button.clicked.connect(sys.exit)  # quiter button
layout = QVBoxLayout()
layout.addWidget(button)
layout.addWidget(label)
window.setLayout(layout)
window.show()
app.exec_()

# See also: https://gist.github.com/bsdnoobz/8464000
