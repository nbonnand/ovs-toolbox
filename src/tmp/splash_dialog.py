# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/splash_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_splash_Dialog(object):
    def setupUi(self, splash_Dialog):
        splash_Dialog.setObjectName("splash_Dialog")
        splash_Dialog.resize(484, 276)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(splash_Dialog)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(splash_Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet("background: black;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(9, -1, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_release = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_release.sizePolicy().hasHeightForWidth())
        self.label_release.setSizePolicy(sizePolicy)
        self.label_release.setStyleSheet("color: rgb(200,200,240); background: black;")
        self.label_release.setObjectName("label_release")
        self.verticalLayout.addWidget(self.label_release)
        self.label_splashscreen = myClickableLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_splashscreen.sizePolicy().hasHeightForWidth())
        self.label_splashscreen.setSizePolicy(sizePolicy)
        self.label_splashscreen.setStyleSheet("")
        self.label_splashscreen.setText("")
        self.label_splashscreen.setObjectName("label_splashscreen")
        self.verticalLayout.addWidget(self.label_splashscreen)
        self.verticalLayout_2.addWidget(self.frame)

        self.retranslateUi(splash_Dialog)
        QtCore.QMetaObject.connectSlotsByName(splash_Dialog)

    def retranslateUi(self, splash_Dialog):
        _translate = QtCore.QCoreApplication.translate
        splash_Dialog.setWindowTitle(_translate("splash_Dialog", "OvS-ToolBox"))
        self.label_release.setText(_translate("splash_Dialog", "label_release"))

from myclickablelabel import myClickableLabel
