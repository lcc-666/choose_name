#encoding=utf-8

import sys
import random
from PyQt5.QtWidgets import QApplication,QDialog,QFileDialog
from conf.name import *
from conf.init import *
from conf.choose import *
from conf.success import *
from conf.have import *
from conf.get_sucess import *
from conf.please import *
from conf.no_mate import *
from hint import *
from read import *

#导入界面
class name_Dialog(QDialog,Ui_name):
    def __init__(self,parent=None):
        super(name_Dialog, self).__init__()
        self.setupUi(self)
        self.file.clicked.connect(self.msg)
        self.file_2.clicked.connect(self.msg_1)
        self.pushButton.clicked.connect(self.choose)
        self.exit.clicked.connect(self.close)
        self.view.clicked.connect(self.hint)

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
                init_calss(self.file)
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
            init_calss(self.file)
            dialogB = success()
            dialogB.exec()

    def choose(self):
        self.close()
        dialog=csDialog()
        dialog.exec()

    def hint(self):
        dialog = hint()
        dialog.exec()

#提示界面
class hint(QDialog,Ui_Hi_Dialog):
    def __init__(self,parent=None):
        super(hint, self).__init__()
        self.setupUi(self)
        self.exit.clicked.connect(self.close)

#请选择同学
class no_mate(QDialog,Ui_no_Dialog):
    def __init__(self,parent=None):
        super(no_mate, self).__init__()
        self.setupUi(self)
        self.exit.clicked.connect(self.close)

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
        dialog=name_Dialog()
        dialog.exec()


#选择班级界面
class csDialog(QDialog,Ui_choose):
    ls_name=[]
    ls_name_index=[]
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
        self.ls_name_index=tongxue(self.class_id)
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
        if self.name=="":
            dialog=no_mate()
            dialog.exec()
        else:
            self.textB.setText("欢迎%s来上课" % self.name)
    def lackkkk(self):
        if self.name=="":
            dialog=no_mate()
            dialog.exec()
        else:
            id=self.ls_name_index.index(self.name)+2
            data=update(self.class_id, id)
            self.textB.setText(self.name+"无故不到,缺课共%s次"%data)





#初始化等待界面
class init_Dialog(QDialog,Ui_initDialog):
    def __init__(self,parent=None):
        super(init_Dialog, self).__init__()
        self.setupUi(self)
        self.ok.clicked.connect(self.close)

if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    Widget=name_Dialog()
    Widget.show()
    sys.exit(app.exec_())
