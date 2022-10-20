
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget,QMenu
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
        button.setCheckable(True)   # ���ð�ť���Ա�����������ź�
        button.clicked.connect(self.the_button_was_clicked)  # ���õ���źŵ�slotsΪ����

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
        
        # һ��signals �����ж��slots�����Ҷ����Խ��յ��ź�

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

        self.button_is_checked = True  # ���ñ����洢�źţ����ó�ʼֵ

        self.setWindowTitle("My App")

        button = QPushButton("Press Me!")
        button.setCheckable(True)  
        button.clicked.connect(self.the_button_was_toggled)
        button.setChecked(self.button_is_checked)  # ���ò����ĳ�ʼ״̬����״̬�����仯ʱ���Խ����źŲ����ı���ֵ

        self.setCentralWidget(button)

    def the_button_was_toggled(self, checked):
        self.button_is_checked = checked  # �������仯ʱ���������ܱ仯�����ı���ֵ

        print(self.button_is_checked)
'''
'''
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.button_is_checked = True

        self.setWindowTitle("My App")

        self.button = QPushButton("Press Me!")
        self.button.setCheckable(True)  # ���ð�ť���ܱ�����
        self.button.released.connect(self.the_button_was_released) # �������������ͷ��ź����Ӻ���
        self.button.setChecked(self.button_is_checked)  # ���ò����ĳ�ʼ״̬

        self.setCentralWidget(self.button)

    def the_button_was_released(self):
        self.button_is_checked = self.button.isChecked()  # ����.isChecked()�������������ɺ�ı�״̬

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
        self.button.setText("You already clicked me.")  # ������ʾ������
        self.button.setEnabled(False)  # �ð�ť�����ܱ����

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

        self.windowTitleChanged.connect(self.the_window_title_changed)  # �����ڱ������ʱsignals���ܵ�slots

        # Set the central widget of the Window.
        self.setCentralWidget(self.button)

    def the_button_was_clicked(self):
        print("Clicked.")
        new_window_title = random.choice(window_titles) # ���ѡȡһ������
        print("Setting title:  %s" % new_window_title) 
        self.setWindowTitle(new_window_title)  # ���ı���

    def the_window_title_changed(self, window_title):
        print("Window title changed: %s" % window_title)

        if window_title == 'Something went wrong':  # ������Ϊ%s ʱ��ֹ��ť�ɵ��
            self.button.setDisabled(True)
'''

# Connecting widgets together directly

'''
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        self.label = QLabel()  # Ϊ�˽�input��label����label���붨��

        self.input = QLineEdit()  # ����һ�����������û�����
        self.input.textChanged.connect(self.label.setText)  # ���û������¼���QLabel��������

        layout = QVBoxLayout()  # ����һ������
        layout.addWidget(self.input) # ��<QLineEdit>���벼��
        layout.addWidget(self.label)  # ��<QLabel>���벼��

        container = QWidget()  # ��������
        container.setLayout(layout) # �����ڷ��벼��

        # Set the central widget of the Window.
        self.setCentralWidget(container)
'''

# Events
'''
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel("Click in this window")
        self.setCentralWidget(self.label)
#todo: Ϊʲôû�������źŵ�slots����ĺ��������Զ����ã�
    def mouseMoveEvent(self, e):
        self.label.setText("mouseMoveEvent")

    def mousePressEvent(self, e):
        self.label.setText("mousePressEvent")

    def mouseReleaseEvent(self, e):
        self.label.setText("mouseReleaseEvent")

    def mouseDoubleClickEvent(self, e):
        self.label.setText("mouseDoubleClickEvent")
'''

# Mouse events

'''
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel("Click in this window")
        self.setCentralWidget(self.label)

    def mousePressEvent(self, e): # �����¼�
        if e.button() == Qt.MouseButton.LeftButton:
            # ����������
            self.label.setText("mousePressEvent LEFT")

        elif e.button() == Qt.MouseButton.MiddleButton:
            # �н��������
            self.label.setText("mousePressEvent MIDDLE")

        elif e.button() == Qt.MouseButton.RightButton:
            # �Ҽ��������
            self.label.setText("mousePressEvent RIGHT")

    def mouseReleaseEvent(self, e): #�ͷ��¼�
        if e.button() == Qt.MouseButton.LeftButton:
            self.label.setText("mouseReleaseEvent LEFT")

        elif e.button() == Qt.MouseButton.MiddleButton:
            self.label.setText("mouseReleaseEvent MIDDLE")

        elif e.button() == Qt.MouseButton.RightButton:
            self.label.setText("mouseReleaseEvent RIGHT")

    def mouseDoubleClickEvent(self, e):  # ˫���¼�
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

    def contextMenuEvent(self, e):  # ��д�����ͬ������
        context = QMenu(self)  # ����QMenu����
        context.addAction(QAction("test 1", self))
        context.addAction(QAction("test 2", self))
        context.addAction(QAction("test 3", self))
        context.exec(e.globalPos()) # �ò˵�����괦����
'''
'''
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.show() # ?

        self.setContextMenuPolicy(Qt.CustomContextMenu) # ���ô������ͣ���ʼ��
        self.customContextMenuRequested.connect(self.on_context_menu) # ���û����Ҽ��˵���slots

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
