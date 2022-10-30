import sys

from PyQt6.QtWidgets import QApplication, QDialog, QMainWindow, QPushButton, QDialogButtonBox, QVBoxLayout, QLabel, \
    QMessageBox

'''
class CustomDialog(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)

        self.setWindowTitle("HELLO!")

        QBtn = QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        # 创建两个按钮，确认和取消，| 符号可以并排显示多个按钮

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout() # 创建布局，垂直
        message = QLabel("Something happened, is that OK?")
        self.layout.addWidget(message) # 添加提示信息
        self.layout.addWidget(self.buttonBox) # 添加按钮
        self.setLayout(self.layout) # 应用布局


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Press me for a dialog!")
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)

    def button_clicked(self, s):
        print("click", s)

        # dlg = QDialog(self)  # 创建对象，传入父类QMainWindow作为参数，这样会显示弹窗
        # dlg.setWindowTitle("HELLO!")
        # dlg.exec()  # 开始循环，在这期间父窗口不可用！

        dlg = CustomDialog(self)
        if dlg.exec(): # 点击OK触发
            print('Sussess!')
        else:
            print('Cancel!')
'''

# Simple message dialogs with QMessageBox

'''
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Press me for a dialog!")
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)


    def button_clicked(self, s):
        dlg = QMessageBox(self)
        dlg.setWindowTitle("I have a question!")
        dlg.setText("This is a simple dialog")
        dlg.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.No) # 没有设置时默认有一个OK
        dlg.setIcon(QMessageBox.Icon.Critical) # 设置图标
        button = dlg.exec()

        if button == QMessageBox.StandardButton.Ok: # 如果选择了OK：
            print("OK!")
'''

# Built in QMessageBox dialogs

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Press me for a dialog!")
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)

    # def button_clicked(self, s):
    #
    #     button = QMessageBox.question(self, "Question dialog", "The longer message")
    #
    #     if button == QMessageBox.StandardButton.Yes:
    #         print("Yes!")
    #     else:
    #         print("No!")

    def button_clicked(self, s):

        button = QMessageBox.critical(
            self,
            "Oh dear!",
            "Something went very wrong.",
            buttons=QMessageBox.StandardButton.Discard | QMessageBox.StandardButton.NoToAll | QMessageBox.StandardButton.Ignore,
            defaultButton=QMessageBox.StandardButton.Discard,
        )

        if button == QMessageBox.StandardButton.Discard:
            print("Discard!")
        elif button == QMessageBox.StandardButton.NoToAll:
            print("No to all!")
        else:
            print("Ignore!")
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
