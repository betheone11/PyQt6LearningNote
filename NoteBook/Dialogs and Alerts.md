<h1 align = 'center'>Dialogs and Alerts</h1>

## Dialogs

在Qt中dialog boxes 由QDialog类创建。

    dlg = QDialog(self)  # 创建对象，传入父类QMainWindow作为参数，这样会显示弹窗
    dlg.setWindowTitle("HELLO!")
    dlg.exec()  # 开始循环，在这期间父窗口不可用！

### 创建 QDialog 子类

    class CustomDialog(QDialog):
        def __init__(self):
            super().__init__()

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

除了确认和取消，还有更多的按钮可以添加：

* QDialogButtonBox.StandardButton.Ok
* QDialogButtonBox.StandardButton.Open
* QDialogButtonBox.StandardButton.Save
* QDialogButtonBox.StandardButton.Cancel
* QDialogButtonBox.StandardButton.Close
* QDialogButtonBox.StandardButton.Discard
* QDialogButtonBox.StandardButton.Apply
* QDialogButtonBox.StandardButton.Reset
* QDialogButtonBox.StandardButton.RestoreDefaults
* QDialogButtonBox.StandardButton.Help
* QDialogButtonBox.StandardButton.SaveAll
* QDialogButtonBox.StandardButton.Yes
* QDialogButtonBox.StandardButton.YesToAll
* QDialogButtonBox.StandardButton.No
* QDialogButtonBox.StandardButton.Abort
* QDialogButtonBox.StandardButton.Retry
* QDialogButtonBox.StandardButton.Ignore
* QDialogButtonBox.StandardButton.NoButton

### 调整子窗口出现的位置

    class CustomDialog(QDialog):
        def __init__(self,parent=None):
            super().__init__(parent)
    在创建子类时，super指定窗口，在创建示例时传入父窗口实现。

## Simple message dialogs with QMessageBox

    def button_clicked(self, s):
        dlg = QMessageBox(self)
        dlg.setWindowTitle("I have a question!")
        dlg.setText("This is a simple dialog")
        button = dlg.exec()

        if button == QMessageBox.StandardButton.Ok: # 如果选择了OK：
            print("OK!")

### 设置更多的按钮

    dlg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
    # 不设置时，默认有一个OK按钮！

### 设置图标

    dlg.setIcon(QMessageBox.Icon.Question)

| Icon state                   | Description  |
| :--------------------------- | :----------: |
| QMessageBox.Icon.NoIcon      |   没有图标   |
| QMessageBox.Icon.Question    |   提问图标   |
| QMessageBox.Icon.Information |   通知图标   |
| QMessageBox.Icon.Warning     |   警告图标   |
| QMessageBox.Icon.Critical    | 严重问题图标 |

## Built in QMessageBox dialogs

QMessageBox 封装了一系列设置好的提示框可供使用。
parent传入父窗口(如self)，title：标题，message：提示信息
创建的窗口默认有Yes与No两个按钮。

> QMessageBox.about(parent, title, message)
> QMessageBox.critical(parent, title, message)
> QMessageBox.information(parent, title, message)
> QMessageBox.question(parent, title, message)
> QMessageBox.warning(parent, title, message)

    button = QMessageBox.question(self, "Question dialog", "The longer message")

你可以自定义他们的 按钮 或 默认按钮：

    button = QMessageBox.critical(
                self,
                "Oh dear!",
                "Something went very wrong.",
                buttons=QMessageBox.StandardButton.Discard | QMessageBox.StandardButton.NoToAll | QMessageBox.StandardButton.Ignore,
                defaultButton=QMessageBox.StandardButton.Discard,
            )
