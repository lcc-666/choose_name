import sys
from PyQt5.QtWidgets import QApplication,QDialog,QFileDialog
from name import *
from read import getdata


class CDialog(QDialog,Ui_Dialog):
    def __init__(self,parent=None):
        super(CDialog,self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.msg)

    def msg(self):
        directory = QFileDialog.getOpenFileName()
        file=str(directory[0]).split(",")[0]
        getdata(file)
if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    Widget=CDialog()
    Widget.show()
    sys.exit(app.exec_())
