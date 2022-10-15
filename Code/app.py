import sys

from PyQt6.QtCore import *
from PyQt6.QtWidgets import *


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('MyApp')
        button = QPushButton('Push me!!')
        self.setFixedSize(QSize(400, 300))
        self.setCentralWidget(button)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
