import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog

from UI.Ui_main_window import Ui_MainWindow

class NewWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("新窗口")
        # 在这里添加新窗口的UI元素

class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        
        # 加载UI内容
        self.ui.setupUi(self)
        
        self.init_ui()
        
    def init_ui(self):
        # 创建一个按钮
        self.open_window_button = QPushButton("打开新窗口", self)
        self.open_window_button.clicked.connect(self.open_new_window)
        self.open_window_button.move(50, 50)  # 设置按钮的位置
        
    def open_new_window(self):
        self.new_window = NewWindow()
        self.new_window.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec_())
