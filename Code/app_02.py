import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget, QMenu
import random
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction

# signals & slots
'''
class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
'''

# QpushButton Signals
'''
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Press Me!")
        button.setCheckable(True)   # 设置按钮可以被点击并发出信号
        button.clicked.connect(self.the_button_was_clicked)  # 设置点击信号的slots为函数

        # Set the central widget of the Window.
        self.setCentralWidget(button)

    def the_button_was_clicked(self):
        print("Clicked!")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
'''

# Receiving data
'''
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Press Me!")
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked)
        button.clicked.connect(self.the_button_was_toggled)
        
        # 一个signals 可以有多个slots，并且都可以接收到信号

        self.setCentralWidget(button)

    def the_button_was_clicked(self):
        print("Clicked!")

    def the_button_was_toggled(self, checked):
        print("Checked?", checked)
'''

# Storing data
'''
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.button_is_checked = True  # 设置变量存储信号，设置初始值

        self.setWindowTitle("My App")

        button = QPushButton("Press Me!")
        button.setCheckable(True)  
        button.clicked.connect(self.the_button_was_toggled)
        button.setChecked(self.button_is_checked)  # 设置部件的初始状态，当状态发生变化时可以接收信号并更改变量值

        self.setCentralWidget(button)

    def the_button_was_toggled(self, checked):
        self.button_is_checked = checked  # 当发生变化时，函数接受变化并更改变量值

        print(self.button_is_checked)
'''
'''
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.button_is_checked = True

        self.setWindowTitle("My App")

        self.button = QPushButton("Press Me!")
        self.button.setCheckable(True)  # 设置按钮是能被检查的
        self.button.released.connect(self.the_button_was_released) # 设置鼠标点击后的释放信号连接函数
        self.button.setChecked(self.button_is_checked)  # 设置部件的初始状态

        self.setCentralWidget(self.button)

    def the_button_was_released(self):
        self.button_is_checked = self.button.isChecked()  # 设置.isChecked()函数，鼠标点击完成后改变状态

        print(self.button_is_checked)
'''

# Changing the interface

"""
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        self.button = QPushButton("Press Me!")
        self.button.clicked.connect(self.the_button_was_clicked)

        self.setCentralWidget(self.button)

    def the_button_was_clicked(self):
        self.button.setText("You already clicked me.")  # 更改显示的文字
        self.button.setEnabled(False)  # 让按钮不在能被点击

        # Also change the window title.
        self.setWindowTitle("My Oneshot App")
"""

'''
window_titles = [
    'My App',
    'My App',
    'Still My App',
    'Still My App',
    'What on earth',
    'What on earth',
    'This is surprising',
    'This is surprising',
    'Something went wrong'
]


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.n_times_clicked = 0

        self.setWindowTitle("My App")

        self.button = QPushButton("Press Me!")
        self.button.clicked.connect(self.the_button_was_clicked)

        self.windowTitleChanged.connect(self.the_window_title_changed)  # 当窗口标题更改时signals接受的slots

        # Set the central widget of the Window.
        self.setCentralWidget(self.button)

    def the_button_was_clicked(self):
        print("Clicked.")
        new_window_title = random.choice(window_titles) # 随机选取一个标题
        print("Setting title:  %s" % new_window_title) 
        self.setWindowTitle(new_window_title)  # 更改标题

    def the_window_title_changed(self, window_title):
        print("Window title changed: %s" % window_title)

        if window_title == 'Something went wrong':  # 当标题为%s 时禁止按钮可点击
            self.button.setDisabled(True)
'''

# Connecting widgets together directly

'''
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        self.label = QLabel()  # 为了将input与label连接label必须定义

        self.input = QLineEdit()  # 创建一个输入框接收用户输入
        self.input.textChanged.connect(self.label.setText)  # 将用户输入事件与QLabel对象连接

        layout = QVBoxLayout()  # 创建一个布局
        layout.addWidget(self.input) # 将<QLineEdit>加入布局
        layout.addWidget(self.label)  # 将<QLabel>加入布局

        container = QWidget()  # 创建容器
        container.setLayout(layout) # 容器内放入布局

        # Set the central widget of the Window.
        self.setCentralWidget(container)
'''


# Events

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel("Click in this window")
        self.setCentralWidget(self.label)

    # todo: 为什么没有设置信号的slots下面的函数就能自动调用？
    def mouseMoveEvent(self, e):
        self.label.setText("mouseMoveEvent")

    def mousePressEvent(self, e):
        self.label.setText("mousePressEvent")

    def mouseReleaseEvent(self, e):
        self.label.setText("mouseReleaseEvent")

    def mouseDoubleClickEvent(self, e):
        self.label.setText("mouseDoubleClickEvent")


# Mouse events

'''
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel("Click in this window")
        self.setCentralWidget(self.label)

    def mousePressEvent(self, e): # 按下事件
        if e.button() == Qt.MouseButton.LeftButton:
            # 左键触发这个
            self.label.setText("mousePressEvent LEFT")

        elif e.button() == Qt.MouseButton.MiddleButton:
            # 中建触发这个
            self.label.setText("mousePressEvent MIDDLE")

        elif e.button() == Qt.MouseButton.RightButton:
            # 右键触发这个
            self.label.setText("mousePressEvent RIGHT")

    def mouseReleaseEvent(self, e): #释放事件
        if e.button() == Qt.MouseButton.LeftButton:
            self.label.setText("mouseReleaseEvent LEFT")

        elif e.button() == Qt.MouseButton.MiddleButton:
            self.label.setText("mouseReleaseEvent MIDDLE")

        elif e.button() == Qt.MouseButton.RightButton:
            self.label.setText("mouseReleaseEvent RIGHT")

    def mouseDoubleClickEvent(self, e):  # 双击事件
        if e.button() == Qt.MouseButton.LeftButton:
            self.label.setText("mouseDoubleClickEvent LEFT")

        elif e.button() == Qt.MouseButton.MiddleButton:
            self.label.setText("mouseDoubleClickEvent MIDDLE")

        elif e.button() == Qt.MouseButton.RightButton:
            self.label.setText("mouseDoubleClickEvent RIGHT")
'''

# Context menus

'''
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

    def contextMenuEvent(self, e):  # 重写父类的同名方法
        context = QMenu(self)  # 创建QMenu对象
        context.addAction(QAction("test 1", self))
        context.addAction(QAction("test 2", self))
        context.addAction(QAction("test 3", self))
        context.exec(e.globalPos()) # 让菜单在鼠标处出现
'''
'''
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.show() # ?

        self.setContextMenuPolicy(Qt.CustomContextMenu) # 设置窗口类型，初始化
        self.customContextMenuRequested.connect(self.on_context_menu) # 设置唤起右键菜单的slots

    def on_context_menu(self, pos): 
        context = QMenu(self)
        context.addAction(QAction("test 1", self))
        context.addAction(QAction("test 2", self))
        context.addAction(QAction("test 3", self))
        context.exec(self.mapToGlobal(pos))
'''

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
