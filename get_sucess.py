# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'get_sucess.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SDialog(object):
    def setupUi(self, SDialog):
        SDialog.setObjectName("SDialog")
        SDialog.resize(484, 299)
        self.label = QtWidgets.QLabel(SDialog)
        self.label.setGeometry(QtCore.QRect(100, 70, 281, 81))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.exit = QtWidgets.QPushButton(SDialog)
        self.exit.setGeometry(QtCore.QRect(150, 180, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.exit.setFont(font)
        self.exit.setObjectName("exit")

        self.retranslateUi(SDialog)
        QtCore.QMetaObject.connectSlotsByName(SDialog)

    def retranslateUi(self, SDialog):
        _translate = QtCore.QCoreApplication.translate
        SDialog.setWindowTitle(_translate("SDialog", "Dialog"))
        self.label.setText(_translate("SDialog", "班级信息获取成功,请开始点名"))
        self.exit.setText(_translate("SDialog", "确定"))