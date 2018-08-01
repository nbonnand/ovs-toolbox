# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/of_delete_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_of_delete_Dialog(object):
    def setupUi(self, of_delete_Dialog):
        of_delete_Dialog.setObjectName("of_delete_Dialog")
        of_delete_Dialog.resize(346, 226)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(of_delete_Dialog.sizePolicy().hasHeightForWidth())
        of_delete_Dialog.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(of_delete_Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_dialog_virt_disk_wizard = QtWidgets.QFrame(of_delete_Dialog)
        self.frame_dialog_virt_disk_wizard.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_dialog_virt_disk_wizard.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_dialog_virt_disk_wizard.setObjectName("frame_dialog_virt_disk_wizard")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_dialog_virt_disk_wizard)
        self.gridLayout.setObjectName("gridLayout")
        self.radioButton_of_delete_all = QtWidgets.QRadioButton(self.frame_dialog_virt_disk_wizard)
        self.radioButton_of_delete_all.setObjectName("radioButton_of_delete_all")
        self.gridLayout.addWidget(self.radioButton_of_delete_all, 4, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 5, 1, 1, 1)
        self.radioButton_of_delete_cookie = QtWidgets.QRadioButton(self.frame_dialog_virt_disk_wizard)
        self.radioButton_of_delete_cookie.setObjectName("radioButton_of_delete_cookie")
        self.gridLayout.addWidget(self.radioButton_of_delete_cookie, 1, 0, 1, 1)
        self.radioButton_of_delete_table = QtWidgets.QRadioButton(self.frame_dialog_virt_disk_wizard)
        self.radioButton_of_delete_table.setObjectName("radioButton_of_delete_table")
        self.gridLayout.addWidget(self.radioButton_of_delete_table, 2, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.frame_dialog_virt_disk_wizard)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)
        self.radioButton_of_delete_table_and_cookie = QtWidgets.QRadioButton(self.frame_dialog_virt_disk_wizard)
        self.radioButton_of_delete_table_and_cookie.setObjectName("radioButton_of_delete_table_and_cookie")
        self.gridLayout.addWidget(self.radioButton_of_delete_table_and_cookie, 3, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame_dialog_virt_disk_wizard)
        self.buttonBox = QtWidgets.QDialogButtonBox(of_delete_Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(of_delete_Dialog)
        self.buttonBox.accepted.connect(of_delete_Dialog.accept)
        self.buttonBox.rejected.connect(of_delete_Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(of_delete_Dialog)

    def retranslateUi(self, of_delete_Dialog):
        _translate = QtCore.QCoreApplication.translate
        of_delete_Dialog.setWindowTitle(_translate("of_delete_Dialog", "Delete flows wizzard"))
        self.radioButton_of_delete_all.setText(_translate("of_delete_Dialog", "all flows"))
        self.radioButton_of_delete_cookie.setText(_translate("of_delete_Dialog", "flows wi&th filter cookie"))
        self.radioButton_of_delete_table.setText(_translate("of_delete_Dialog", "flows with filter table"))
        self.label_6.setText(_translate("of_delete_Dialog", "Delete:"))
        self.radioButton_of_delete_table_and_cookie.setText(_translate("of_delete_Dialog", "flows with filter table AN&D filter cookie"))

