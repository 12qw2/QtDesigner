import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from ui.Ui_untitled import Ui_Form

class MyWidget(QWidget):
    
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        self.init_ui()
    
    # 获取的用户名
   
    # 获取的密码
    
    # 获取的性别
    
    # 获取的爱好
    
    # 获取的个性签名
    
    # 择偶要求
    
    
        
    def zuce(self):
        print("按钮点击!")
        print(self.ui.lineEdit_1.text())
        
    def init_ui(self):
        self.ui.pushButton.clicked.connect(self.zuce)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())


