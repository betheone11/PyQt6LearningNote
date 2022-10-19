## signals & slots
signals: ���¼�����ʱ��������������
slots: signals�Ľ�����
### QpushButton Signals
    button = QPushButton("Press Me!")
    button.setCheckable(True) # ���ð�ť���Ա�����������ź�
    button.clicked.connect(self.the_button_was_clicked) # ���õ���źŵ�slotsΪ����

    def the_button_was_clicked(self):
        print("Clicked!")

### Receiving data
    button.clicked.connect(self.the_button_was_clicked)
    button.clicked.connect(self.the_button_was_toggled)
    # һ��signals �����ж��slots�����Ҷ����Խ��յ��ź�
### Storing data
�洢����ź�

    self.button_is_checked = True # ���ñ����洢�źţ����ó�ʼֵ
    button.setCheckable(True)  
    button.clicked.connect(self.the_button_was_toggled) 
    button.setChecked(self.button_is_checked) # ���ò����ĳ�ʼ״̬����״̬�����仯ʱ���Խ����źŲ����ı���ֵ

    def the_button_was_toggled(self, checked):
        self.button_is_checked = checked  �������仯ʱ���������ܱ仯�����ı���ֵ

        print(self.button_is_checked)
> False
  True
  False
  True

�洢�������ͷŵ��ź�
    self.button_is_checked = True
    self.button.setCheckable(True)  
    self.button.released.connect(self.the_button_was_released) # �������������ͷ��ź����Ӻ���
    self.button.setChecked(self.button_is_checked)  # ���ò����ĳ�ʼ״̬

    def the_button_was_released(self):
        self.button_is_checked = self.button.isChecked()  # ����.isChecked()�������������ɺ�ı�״̬

        print(self.button_is_checked)

### Changing the interface
����slots���������������źź���Ľ���
    def the_button_was_clicked(self):
        self.button.setText("You already clicked me.")  # ������ʾ������
        self.button.setEnabled(False)  # �ð�ť�����ܱ����

        # Also change the window title.
        self.setWindowTitle("My Oneshot App")
�������Ӳ鿴app_1.py
slots ��������signals����Դ,���յ��źž��ж���
    self.windowTitleChanged.connect(self.the_window_title_changed)  # �����ڱ������ʱ(ֻ�и���Ϊ�뵱ǰ��ͬ�ı���ʱ)signals���ܵ�slots
    new_window_title = random.choice(window_titles) # ���ѡȡһ������
    self.setWindowTitle(new_window_title)  # ���ı���
    self.button.setDisabled(True) ���ð�ť���ɵ������һ�ַ���

### Connecting widgets together directly
slots����python�����⻹������������Qt widgets.
[����QLabel��](https://doc.qt.io/qt-5/qlabel.html#public-slots[QLabel])
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
## Events
Event: �û���QtӦ�õ����н��������¼���

|Event handler|Event type moved|
|:---|:---|
|mouseMoveEvent|��껮��|
|mousePressEvent|��ס���|
|mouseReleaseEvent|�ɿ����|
|mouseDoubleClickEvent|˫�����|
����������e�ǽ����¼��ı���
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

����ƶ��¼�ֻ������갴��ʱ�ƶ��Żᴥ��������Ե���self.setMouseTracking(True)�����ġ�
press��DoubleClickֻ����갴סʱ�������ɿ����Ϊrelease��
### Mouse events
QMouseEvent����������е������ص��¼�
���з����������԰�ť��״̬
|Method|Returns|
|:---|:---|
|.button()|�������¼����ض���ť|
|.buttons()|������갴ť��״̬|
|.position()|��С�������λ��(QPoint����)|
    def mousePressEvent(self, e):  # ��������������Ӧ�Ĳ���
        # ��������������
        if e.button() == Qt.MouseButton.LeftButton:
            self.label.setText("mousePressEvent LEFT")

     def mouseReleaseEvent(self, e):
        # �����м����ͷŴ������
        if e.button() == Qt.MouseButton.MiddleButton:
            self.label.setText("mouseReleaseEvent MIDDLE")

    def mouseDoubleClickEvent(self, e):
        # �Ҽ�˫���������
        if e.button() == Qt.MouseButton.RightButton:
            self.label.setText("mouseDoubleClickEvent RIGHT")
### Context menus(�Ҽ��˵�)
    def contextMenuEvent(self, e):  # ��д�����ͬ������

    context = QMenu(self)  # ����QMenu����
    context.addAction(QAction("test 1", self))
    context.addAction(QAction("test 2", self))
    context.addAction(QAction("test 3", self))
    context.exec(e.globalPos()) # �ò˵�����괦����
��һ�ַ�����
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
## Event hierarchy
��PyQt�������־��Եȼ��ƶȣ�python����ȼ��ƶ��Լ�Qt���ֵȼ��ƶ�
### Python inheritance forwarding