'''
import sys

from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Widgets App")

        layout = QVBoxLayout()
        widgets = [
            QCheckBox,
             QComboBox,
            QDateEdit,
            QDateTimeEdit,
            QDial,
            QDoubleSpinBox,
            QFontComboBox,
            QLCDNumber,
            QLabel,
            QLineEdit,
            QProgressBar,
            QPushButton,
            QRadioButton,
            QSlider,
            QSpinBox,
            QTimeEdit,
        ]

        for w in widgets:
            layout.addWidget(w())

        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()
'''

import sys
from PyQt6.QtWidgets import (
    QMainWindow, QApplication,
    QLabel, QCheckBox, QComboBox, QListWidget, QLineEdit,
    QLineEdit, QSpinBox, QDoubleSpinBox, QSlider, QDial
)
from PyQt6.QtCore import Qt

# QLabel

'''
class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        widget = QLabel("Hello")
        font = widget.font()  # 选定字体模块
        font.setPointSize(30)  # 更改字体大小
        widget.setFont(font)  # 应用字体
        widget.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        # 设置对齐样式（垂直居中水平居中）

        self.setCentralWidget(widget)
'''

# QCheckBox
'''
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        widget = QCheckBox('this is a checkbox')
        widget.setCheckState(Qt.CheckState.Checked)  # 设置初始状态，打勾

        # 如果想要使box有三种状态：widget.setCheckState(Qt.PartiallyChecked)
        # 或者 widget.setTriState(True)
        widget.stateChanged.connect(self.show_state)

        self.setCentralWidget(widget)

    def show_state(self, s):
        print(s == Qt.CheckState.Checked)
        print(s)  # s: 打勾时值为2， 空时值为0
'''

# QComboBox
'''
class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        widget = QComboBox()
        widget.addItems(["One", "Two", "Three"])  # 下拉菜单添加元素

        widget.currentIndexChanged.connect(self.index_changed)  # 当选择不同项时传出选择项的索引

        widget.currentTextChanged.connect(self.text_changed)  # 当选择不同项时传出选择项的内容

        self.setCentralWidget(widget)

    def index_changed(self, i):
        print(i)

    def text_changed(self, s):
        print(s)
'''

# QListWidget

'''
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        widget = QListWidget()
        widget.addItems(["One", "Two", "Three"])

        widget.currentItemChanged.connect(self.index_changed)
        widget.currentTextChanged.connect(self.text_changed)

        self.setCentralWidget(widget)


    def index_changed(self, i): # Not an index, i is a QListItem
        print(i.text())

    def text_changed(self, s): # s is a str
        print(s)
'''

# QLineEdit
'''
class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        widget = QLineEdit()
        widget.setMaxLength(10)  # 设置文本最大长度
        widget.setPlaceholderText("Enter your text")  # 文本框默认显示的灰色文字

        # widget.setReadOnly(True)  # 设置为只读

        widget.returnPressed.connect(self.return_pressed)
        widget.selectionChanged.connect(self.selection_changed)
        widget.textChanged.connect(self.text_changed)
        widget.textEdited.connect(self.text_edited)

        widget.setInputMask('000.000.000.000;_')

        self.setCentralWidget(widget)

    def return_pressed(self):  # 按回车键触发
        print("Return pressed!")
        self.centralWidget().setText("BOOM!")  # 将输入框内的文本前面加上前缀

    def selection_changed(self):  # 鼠标划动取词触发
        print("Selection changed")
        print(self.centralWidget().selectedText())

    def text_changed(self, s):  # 文本更改后触发，每次更改一个字母都会触发
        print("Text changed...")
        print(s)

    def text_edited(self, s):  # 文本编辑后触发
        print("Text edited...")
        print(s)
'''

# QSpinBox and QDoubleSpinBox

'''
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        widget = QSpinBox()
        # Or: widget = QDoubleSpinBox()

        widget.setMinimum(-10)  # 设置数字的边界
        widget.setMaximum(3)
        # Or: widget.setRange(-10,3)

        widget.setPrefix("$")  # 设置前缀
        widget.setSuffix("c")  # 设置后缀
        widget.setSingleStep(3)  # 每按一次箭头数值变化的大小，spinbox只能是整数
        widget.valueChanged.connect(self.value_changed)
        widget.textChanged.connect(self.value_changed_str)

        self.setCentralWidget(widget)

    def value_changed(self, i):  # i 包括前后缀
        print("valueChanged")
        print(i)

    def value_changed_str(self, s): # s不包括前后缀，为int(float)
        print("text changed")
        print(s)
'''

# QSlider

'''
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        widget = QSlider(Qt.Orientation.Horizontal)

        widget.setMinimum(-10)
        widget.setMaximum(30)

        # Or: widget.setRange(-10,3)

        widget.setSingleStep(5)  # 这行好像没作用。。。

        widget.valueChanged.connect(self.value_changed)
        widget.sliderMoved.connect(self.slider_position)
        widget.sliderPressed.connect(self.slider_pressed)
        widget.sliderReleased.connect(self.slider_released)

        self.setCentralWidget(widget)

    def value_changed(self, i):  # 数值改变时触发，返回数值
        print(i)

    def slider_position(self, p): # 返回滑块的位置，p为数值
        print("position", p)

    def slider_pressed(self):  # 鼠标点击时触发
        print("Pressed!")

    def slider_released(self): # 鼠标松开时触发
        print("Released")
'''


# QDial

'''
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        widget = QDial()
        widget.setRange(-10, 100)
        widget.setSingleStep(1)

        widget.valueChanged.connect(self.value_changed)
        widget.sliderMoved.connect(self.slider_position)
        widget.sliderPressed.connect(self.slider_pressed)
        widget.sliderReleased.connect(self.slider_released)

        self.setCentralWidget(widget)

    def value_changed(self, i):
        print(i)

    def slider_position(self, p):
        print("position", p)

    def slider_pressed(self):
        print("Pressed!")

    def slider_released(self):
        print("Released")
'''


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
