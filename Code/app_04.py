import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QStackedLayout
from PyQt6.QtGui import QPalette, QColor


class Color(QWidget):

    def __init__(self, color):  # color: str
        super(Color, self).__init__()
        self.setAutoFillBackground(True)  # 用背景颜色自动填充窗口

        palette = self.palette()  # 设置默认的全局调色板
        palette.setColor(QPalette.ColorRole.Window, QColor(color))  # 更改当前调色板颜色为新的颜色
        self.setPalette(palette)  # 应用调色板，让每一个不同的部件填充我们设定的颜色


# QVBoxLayout vertically arranged widgets

'''
class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        layout = QVBoxLayout()  # 创建实例

        layout.addWidget(Color('blue'))  # 给布局添加背景颜色

        widget = QWidget()  # 创建虚拟部件
        widget.setLayout(layout)  # 将部件与部件结合起来
        self.setCentralWidget(widget)
'''
'''
class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        layout = QVBoxLayout()

        layout.addWidget(Color('red'))
        layout.addWidget(Color('green'))
        layout.addWidget(Color('blue'))

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

'''
# QHBoxLayout
'''
class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        layout = QHBoxLayout()

        layout.addWidget(Color('red'))
        layout.addWidget(Color('green'))
        layout.addWidget(Color('blue'))

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
'''

# Nesting layouts

'''
class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        layout1 = QHBoxLayout()  # 主视图
        layout2 = QVBoxLayout()  # 左视图
        layout3 = QVBoxLayout()  # 右视图

        layout1.setContentsMargins(0, 0, 0, 0)  # 单个部件的(左, 上, 右, 下)边距
        layout1.setSpacing(10)  # 每个部件与其他部件的距离

        layout2.addWidget(Color('red'))
        layout2.addWidget(Color('yellow'))
        layout2.addWidget(Color('purple'))

        layout1.addLayout(layout2)

        layout1.addWidget(Color('green'))

        layout3.addWidget(Color('red'))
        layout3.addWidget(Color('purple'))

        layout1.addLayout(layout3)

        widget = QWidget()
        widget.setLayout(layout1)
        self.setCentralWidget(widget)
'''

# QGridLayout widgets arranged in a grid
'''
class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        layout = QGridLayout()  # 创建布局

        layout.addWidget(Color('red'), 0, 0)  # 将红色的块放到指定位置
        layout.addWidget(Color('green'), 1, 0)
        layout.addWidget(Color('blue'), 1, 1)
        layout.addWidget(Color('purple'), 2, 1)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
'''

# QStackedLayout multiple widgets in the same space
'''
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        layout = QStackedLayout()

        layout.addWidget(Color("red"))
        layout.addWidget(Color("green"))
        layout.addWidget(Color("blue"))
        layout.addWidget(Color("yellow"))

        layout.setCurrentIndex(3)  # 设置当前可见的布局

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
'''
'''
import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QStackedLayout,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        pagelayout = QVBoxLayout()  # 主视图
        button_layout = QHBoxLayout()  # 创建切换按钮的布局
        self.stacklayout = QStackedLayout()  # 创建显示内容的堆叠布局

        pagelayout.addLayout(button_layout)  # 上面添加按钮
        pagelayout.addLayout(self.stacklayout)  # 下面添加显示的颜色块

        btn = QPushButton("red")  # 创建控制红色的按钮，接受按下信息并将堆叠布局切换到红色
        btn.pressed.connect(self.activate_tab_1)
        button_layout.addWidget(btn)  # 将按钮添加到切换按钮的布局
        self.stacklayout.addWidget(Color("red"))  # 将红色添加到堆叠布局

        btn = QPushButton("green")
        btn.pressed.connect(self.activate_tab_2)
        button_layout.addWidget(btn)
        self.stacklayout.addWidget(Color("green"))

        btn = QPushButton("yellow")
        btn.pressed.connect(self.activate_tab_3)
        button_layout.addWidget(btn)
        self.stacklayout.addWidget(Color("yellow"))

        widget = QWidget()
        widget.setLayout(pagelayout)
        self.setCentralWidget(widget)

    def activate_tab_1(self):
        self.stacklayout.setCurrentIndex(0)

    def activate_tab_2(self):
        self.stacklayout.setCurrentIndex(1)

    def activate_tab_3(self):
        self.stacklayout.setCurrentIndex(2)
'''

import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QTabWidget,
    QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        tabs = QTabWidget()
        # tabs.setTabPosition(QTabWidget.West)  有问题会报错
        tabs.setMovable(True)

        for n, color in enumerate(["red", "green", "blue", "yellow"]):
            tabs.addTab(Color(color), color)

        self.setCentralWidget(tabs)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
