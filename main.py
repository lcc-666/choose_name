#encoding=utf-8

import sys
from PyQt5.QtWidgets import QApplication,QDialog,QFileDialog
from name import *
from init import *
from choose import *
from success import *
from read import *

#导入成功
class success(QDialog,Ui_suDialog):
    def __init__(self,parent=None):
        super(success, self).__init__()
        self.setupUi(self)
        self.start.clicked.connect(self.choose)
        self.coun.clicked.connect(self.close)

    def choose(self):
        self.close()
        dialog=csDialog()
        dialog.exec()

    def countinue(self):
        self.close()
        dialog=CDialog()
        dialog.exec()


#导入界面
class CDialog(QDialog,Ui_Dialog):
    def __init__(self,parent=None):
        super(CDialog,self).__init__(parent)
        self.setupUi(self)
        self.file.clicked.connect(self.msg)
        self.pushButton.clicked.connect(self.choose)

    def msg(self):
        directory = QFileDialog.getOpenFileName()
        file=str(directory[0]).split(",")[0]
        if file=="":
            pass
        else:
            dialogB = init_Dialog()
            dialogB.exec()
            getdata(file)
            dialogB=success()
            dialogB.exec()

    def choose(self):
        self.close()
        dialog=csDialog()
        dialog.exec()

#选择界面
class csDialog(QDialog,Ui_choose):
    def __init__(self,parent=None):
        super(csDialog, self).__init__()
        self.setupUi(self)
        self.comboBox.addItems(get_class())
    def choose_class(self):
        pass


#初始化等待界面
class init_Dialog(QDialog,Ui_initDialog):
    def __init__(self,parent=None):
        super(init_Dialog, self).__init__()
        self.setupUi(self)
        self.ok.clicked.connect(self.close)










if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    Widget=CDialog()
    Widget.show()
    sys.exit(app.exec_())

