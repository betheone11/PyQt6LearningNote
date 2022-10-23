## signals & slots
signals: 当事件发生时部件发出的提醒  
slots: signals的接收者
### QpushButton Signals
    button = QPushButton("Press Me!")
    button.setCheckable(True) # 设置按钮可以被点击并发出信号
    button.clicked.connect(self.the_button_was_clicked) # 设置点击信号的slots为函数

    def the_button_was_clicked(self):
        print("Clicked!")

### Receiving data
    button.clicked.connect(self.the_button_was_clicked)
    button.clicked.connect(self.the_button_was_toggled)
    # 一个signals 可以有多个slots，并且都可以接收到信号
### Storing data
存储点击信号

    self.button_is_checked = True # 设置变量存储信号，设置初始值
    button.setCheckable(True)  
    button.clicked.connect(self.the_button_was_toggled) 
    button.setChecked(self.button_is_checked) # 设置部件的初始状态，当状态发生变化时可以接收信号并更改变量值

    def the_button_was_toggled(self, checked):
        self.button_is_checked = checked  当发生变化时，函数接受变化并更改变量值

        print(self.button_is_checked)
> False
  True
  False
  True

存储长按后释放的信号

    self.button_is_checked = True
    self.button.setCheckable(True)  
    self.button.released.connect(self.the_button_was_released) # 设置鼠标点击后的释放信号连接函数
    self.button.setChecked(self.button_is_checked)  # 设置部件的初始状态

    def the_button_was_released(self):
        self.button_is_checked = self.button.isChecked()  # 设置.isChecked()函数，鼠标点击完成后改变状态

        print(self.button_is_checked)

### Changing the interface
更改slots函数，让他接收信号后更改界面

    def the_button_was_clicked(self):
        self.button.setText("You already clicked me.")  # 更改显示的文字
        self.button.setEnabled(False)  # 让按钮不在能被点击

        # Also change the window title.
        self.setWindowTitle("My Oneshot App")
更多例子查看app_1.py
slots 并不关心signals的来源,接收到信号就行动。

    self.windowTitleChanged.connect(self.the_window_title_changed)  # 当窗口标题更改时(只有更改为与当前不同的标题时)signals接受的slots
    new_window_title = random.choice(window_titles) # 随机选取一个标题
    self.setWindowTitle(new_window_title)  # 更改标题
    self.button.setDisabled(True) 设置按钮不可点击的另一种方法

### Connecting widgets together directly
slots除了python函数外还可以是其他的Qt widgets.
[关于QLabel类](https://doc.qt.io/qt-5/qlabel.html#public-slots[QLabel])

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
## Events
Event: 用户与Qt应用的所有交互都是事件。

|Event handler|Event type moved|
|:---|:---|
|mouseMoveEvent|鼠标划动|
|mousePressEvent|按住鼠标|
|mouseReleaseEvent|松开鼠标|
|mouseDoubleClickEvent|双击鼠标|

下列例子中e是接受事件的变量

    class MainWindow(QMainWindow):
        def __init__(self):
            super().__init__()
            self.label = QLabel("Click in this window")
            self.setCentralWidget(self.label)
        
        #todo: 为什么没有设置信号的slots下面的函数就能自动调用？

        def mouseMoveEvent(self, e):
            self.label.setText("mouseMoveEvent")

        def mousePressEvent(self, e):
            self.label.setText("mousePressEvent")

        def mouseReleaseEvent(self, e):
            self.label.setText("mouseReleaseEvent")

        def mouseDoubleClickEvent(self, e):
            self.label.setText("mouseDoubleClickEvent")

鼠标移动事件只有在鼠标按下时移动才会触发，你可以调用self.setMouseTracking(True)来更改。
press与DoubleClick只在鼠标按住时触发，松开后变为release。
### Mouse events
QMouseEvent类包含了所有的鼠标相关的事件
下列方法返回鼠标对按钮的状态

|Method|Returns|
|:---|:---|
|.button()|触发此事件的特定按钮|
|.buttons()|所有鼠标按钮的状态|
|.position()|与小部件相对位置(QPoint对象)|

    def mousePressEvent(self, e):  # 函数名代表了相应的操作
        # 按下左键触发这个
        if e.button() == Qt.MouseButton.LeftButton:
            self.label.setText("mousePressEvent LEFT")

     def mouseReleaseEvent(self, e):
        # 按下中键后释放触发这个
        if e.button() == Qt.MouseButton.MiddleButton:
            self.label.setText("mouseReleaseEvent MIDDLE")

    def mouseDoubleClickEvent(self, e):
        # 右键双击触发这个
        if e.button() == Qt.MouseButton.RightButton:
            self.label.setText("mouseDoubleClickEvent RIGHT")
### Context menus(右键菜单)
    def contextMenuEvent(self, e):  # 重写父类的同名方法

    context = QMenu(self)  # 创建QMenu对象
    context.addAction(QAction("test 1", self))
    context.addAction(QAction("test 2", self))
    context.addAction(QAction("test 3", self))
    context.exec(e.globalPos()) # 让菜单在鼠标处出现
另一种方法：

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
## Event hierarchy
在PyQt中有两种绝对等级制度，python对象等级制度以及Qt布局等级制度
### Python inheritance forwarding
### Layout forwaeding  
signals是会沿着部件的嵌套顺序传递，如果子部件未响应signals，会传递给父部件，知道被处理或传递到主窗口。  
    class CustomButton(QPushButton)
            def mousePressEvent(self, e):
                e.accept()  # 你可以调用.accept()方法来标记为已处理。

     class CustomButton(QPushButton)
        def event(self, e):
            e.ignore()  # 调用.ignore() 来使其忽略并往外层传递。