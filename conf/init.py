# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'init.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_initDialog(object):
    def setupUi(self, initDialog):
        initDialog.setObjectName("initDialog")
        initDialog.resize(362, 191)
        self.label = QtWidgets.QLabel(initDialog)
        self.label.setGeometry(QtCore.QRect(60, 20, 231, 71))
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.ok = QtWidgets.QPushButton(initDialog)
        self.ok.setGeometry(QtCore.QRect(90, 130, 171, 51))
        self.ok.setObjectName("ok")

        self.retranslateUi(initDialog)
        QtCore.QMetaObject.connectSlotsByName(initDialog)

    def retranslateUi(self, initDialog):
        _translate = QtCore.QCoreApplication.translate
        initDialog.setWindowTitle(_translate("initDialog", "Dialog"))
        self.label.setText(_translate("initDialog", "        第一次导入可能时间较长,请稍候,开始导入后无需操作,成功会自动跳转."))
        self.ok.setText(_translate("initDialog", "我知道了,开始导入"))
