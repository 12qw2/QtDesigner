import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from ui22.Ui_untitled import Ui_Form

class MyWidget(QWidget):
    
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        self.init_ui()
    
    # 获取的用户名
    def get_username(self):
        return self.ui.lineEdit_1.text()
   
    # 获取的密码
    def get_password(self):
        return self.ui.lineEdit_2.text()
    
    # 获取的性别
    def get_gender(self):
        if self.ui.radioButton_1.isChecked():
            return "男"
        elif self.ui.radioButton_2.isChecked():
            return "女"
        
    # 获取的爱好
    def get_hobby(self):
        hobbies = []
        if self.ui.checkBox_1.isChecked():
            hobbies.append("抽烟")
        if self.ui.checkBox_2.isChecked():
            hobbies.append("喝酒")
        if self.ui.checkBox_3.isChecked():
            hobbies.append("烫头")
        
        # 格式化元组
        return  ",".join(hobbies)





    
    # 获取的个性签名
    def get_signature(self):
        return self.ui.lineEdit_3.text()
    
    # 择偶要求
    def get_sex_requirement(self):
        return self.ui.plainTextEdit_1.toPlainText()
        
    def zuce(self):
        print("用户名:", self.ui.lineEdit_1.text())
        print("密码:", self.ui.lineEdit_2.text())
        print("性别:", self.get_gender())
        print("爱好:", self.get_hobby())
        print("个性签名:", self.get_signature())
        print("择偶要求:", self.get_sex_requirement())
        
    def init_ui(self):
        self.ui.pushButton.clicked.connect(self.zuce)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())




