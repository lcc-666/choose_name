#encoding=utf-8

import sys
import random
from PyQt5.QtWidgets import QApplication,QDialog,QFileDialog
from name import *
from init import *
from choose import *
from success import *
from read import *
from sql import *
from have import *
from get_sucess import *
from please import *
#请选择班级
class p_clase(QDialog,Ui_PDialog):
    def __init__(self,parent=None):
        super(p_clase, self).__init__()
        self.setupUi(self)
        self.exit.clicked.connect(self.close)

#班级信息获取成功
class get_suce(QDialog,Ui_SDialog):
    def __init__(self,parent=None):
        super(get_suce, self).__init__()
        self.setupUi(self)
        self.exit.clicked.connect(self.close)

#信息已存在
class h_Dialog(QDialog,Ui_QDialog):
    def __init__(self,parent=None):
        super(h_Dialog, self).__init__()
        self.setupUi(self)
        self.exit.clicked.connect(self.close)

#导入成功界面
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
        self.file_2.clicked.connect(self.msg_1)
        self.pushButton.clicked.connect(self.choose)

    def msg(self):
        directory = QFileDialog.getOpenFileName()
        self.file=str(directory[0]).split(",")[0]
        if self.file=="":
            pass
        else:
            dialogB = init_Dialog()
            dialogB.exec()
            if classes(self.file)==0:
                dialogB = h_Dialog()
                dialogB.exec()
            else:
                dialogB=success()
                dialogB.exec()
    def msg_1(self):
        directory = QFileDialog.getOpenFileName()
        self.file=str(directory[0]).split(",")[0]
        if self.file=="":
            pass
        else:
            dialogB = init_Dialog()
            dialogB.exec()
            getdata(self.file)
            dialogB = success()
            dialogB.exec()

    def choose(self):
        self.close()
        dialog=csDialog()
        dialog.exec()

#选择班级界面
class csDialog(QDialog,Ui_choose):
    ls_name=[]
    name=''
    class_id=''
    def __init__(self,parent=None):
        super(csDialog, self).__init__()
        self.setupUi(self)
        self.comboBox.addItems(get_class())
        self.cscs.clicked.connect(self.choose_class)
        self.exit.clicked.connect(self.close)
        self.suiji.clicked.connect(self.choose_name)
        self.arrived.clicked.connect(self.arrive)
        self.lack.clicked.connect(self.lackkkk)

    def choose_class(self):
        self.class_id=self.comboBox.currentText()
        self.ls_name=tongxue(self.class_id)
        dialog = get_suce()
        dialog.exec()

    def choose_name(self):
        if len(self.ls_name)!=0:
            self.name=random.choice(self.ls_name)
            self.ls_name.remove(self.name)
            self.textB.setText("此次的幸运儿是:"+self.name)
        else:
            dialog = p_clase()
            dialog.exec()

    def arrive(self):
        self.textB.setText("欢迎%s来上课"%self.name)

    def lackkkk(self):
        data=update(self.class_id, self.name)
        self.textB.setText(self.name+"无故不到,缺课共%s次"%data)


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

