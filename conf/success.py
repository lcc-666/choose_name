# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'success.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_suDialog(object):
    def setupUi(self, suDialog):
        suDialog.setObjectName("suDialog")
        suDialog.resize(423, 241)
        self.label = QtWidgets.QLabel(suDialog)
        self.label.setGeometry(QtCore.QRect(120, 40, 201, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.start = QtWidgets.QPushButton(suDialog)
        self.start.setGeometry(QtCore.QRect(30, 140, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.start.setFont(font)
        self.start.setObjectName("start")
        self.coun = QtWidgets.QPushButton(suDialog)
        self.coun.setGeometry(QtCore.QRect(220, 140, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.coun.setFont(font)
        self.coun.setObjectName("coun")

        self.retranslateUi(suDialog)
        QtCore.QMetaObject.connectSlotsByName(suDialog)

    def retranslateUi(self, suDialog):
        _translate = QtCore.QCoreApplication.translate
        suDialog.setWindowTitle(_translate("suDialog", "Dialog"))
        self.label.setText(_translate("suDialog", "班级信息导入成功"))
        self.start.setText(_translate("suDialog", "开始点名"))
        self.coun.setText(_translate("suDialog", "继续导入"))
