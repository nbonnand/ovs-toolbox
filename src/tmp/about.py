# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/about.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_about_Dialog(object):
    def setupUi(self, about_Dialog):
        about_Dialog.setObjectName("about_Dialog")
        about_Dialog.resize(703, 659)
        about_Dialog.setProperty("paintme01", True)
        self.verticalLayout = QtWidgets.QVBoxLayout(about_Dialog)
        self.verticalLayout.setContentsMargins(10, 10, 10, 5)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.plainTextEdit_about = QtWidgets.QPlainTextEdit(about_Dialog)
        self.plainTextEdit_about.setReadOnly(True)
        self.plainTextEdit_about.setObjectName("plainTextEdit_about")
        self.verticalLayout.addWidget(self.plainTextEdit_about)
        self.buttonBox = QtWidgets.QDialogButtonBox(about_Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(about_Dialog)
        self.buttonBox.accepted.connect(about_Dialog.accept)
        self.buttonBox.rejected.connect(about_Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(about_Dialog)

    def retranslateUi(self, about_Dialog):
        _translate = QtCore.QCoreApplication.translate
        about_Dialog.setWindowTitle(_translate("about_Dialog", "About"))

