# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/misc_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_misc_Dialog(object):
    def setupUi(self, misc_Dialog):
        misc_Dialog.setObjectName("misc_Dialog")
        misc_Dialog.resize(647, 236)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(misc_Dialog.sizePolicy().hasHeightForWidth())
        misc_Dialog.setSizePolicy(sizePolicy)
        misc_Dialog.setStatusTip("")
        misc_Dialog.setWhatsThis("")
        misc_Dialog.setAccessibleName("")
        misc_Dialog.setAccessibleDescription("")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(misc_Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(misc_Dialog)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.frame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 521, 170))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.scrollArea)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.frame)
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout.addWidget(self.buttonBox)
        self.verticalLayout_2.addWidget(self.frame)
        self.label_4 = QtWidgets.QLabel(misc_Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)

        self.retranslateUi(misc_Dialog)
        self.buttonBox.accepted.connect(misc_Dialog.accept)
        self.buttonBox.rejected.connect(misc_Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(misc_Dialog)

    def retranslateUi(self, misc_Dialog):
        _translate = QtCore.QCoreApplication.translate
        misc_Dialog.setWindowTitle(_translate("misc_Dialog", "Virt options wizzard"))
        self.label_2.setText(_translate("misc_Dialog", "Value"))
        self.label.setText(_translate("misc_Dialog", "Name"))
        self.label_3.setText(_translate("misc_Dialog", "Description"))
        self.label_4.setText(_translate("misc_Dialog", "Select options you want to add. You can fill their value now or later."))

