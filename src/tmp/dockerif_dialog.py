# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/dockerif_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dockerif_Dialog(object):
    def setupUi(self, dockerif_Dialog):
        dockerif_Dialog.setObjectName("dockerif_Dialog")
        dockerif_Dialog.resize(452, 249)
        self.verticalLayout = QtWidgets.QVBoxLayout(dockerif_Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_dialog_virt_disk_wizard = QtWidgets.QFrame(dockerif_Dialog)
        self.frame_dialog_virt_disk_wizard.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_dialog_virt_disk_wizard.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_dialog_virt_disk_wizard.setProperty("paintme01", True)
        self.frame_dialog_virt_disk_wizard.setObjectName("frame_dialog_virt_disk_wizard")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_dialog_virt_disk_wizard)
        self.gridLayout.setObjectName("gridLayout")
        self.label_6 = QtWidgets.QLabel(self.frame_dialog_virt_disk_wizard)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 0, 1, 1)
        self.lineEdit_dialog_dockerif_ext = QtWidgets.QLineEdit(self.frame_dialog_virt_disk_wizard)
        self.lineEdit_dialog_dockerif_ext.setEnabled(True)
        self.lineEdit_dialog_dockerif_ext.setClearButtonEnabled(True)
        self.lineEdit_dialog_dockerif_ext.setObjectName("lineEdit_dialog_dockerif_ext")
        self.gridLayout.addWidget(self.lineEdit_dialog_dockerif_ext, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame_dialog_virt_disk_wizard)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 5, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.frame_dialog_virt_disk_wizard)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 2, 0, 1, 1)
        self.lineEdit_dialog_dockerif_vlan = QtWidgets.QLineEdit(self.frame_dialog_virt_disk_wizard)
        self.lineEdit_dialog_dockerif_vlan.setEnabled(True)
        self.lineEdit_dialog_dockerif_vlan.setClearButtonEnabled(True)
        self.lineEdit_dialog_dockerif_vlan.setObjectName("lineEdit_dialog_dockerif_vlan")
        self.gridLayout.addWidget(self.lineEdit_dialog_dockerif_vlan, 2, 1, 1, 1)
        self.lineEdit_dialog_dockerif_int = QtWidgets.QLineEdit(self.frame_dialog_virt_disk_wizard)
        self.lineEdit_dialog_dockerif_int.setEnabled(True)
        self.lineEdit_dialog_dockerif_int.setClearButtonEnabled(True)
        self.lineEdit_dialog_dockerif_int.setObjectName("lineEdit_dialog_dockerif_int")
        self.gridLayout.addWidget(self.lineEdit_dialog_dockerif_int, 1, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.frame_dialog_virt_disk_wizard)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 3, 0, 1, 1)
        self.lineEdit_dialog_dockerif_mac = QtWidgets.QLineEdit(self.frame_dialog_virt_disk_wizard)
        self.lineEdit_dialog_dockerif_mac.setEnabled(True)
        self.lineEdit_dialog_dockerif_mac.setClearButtonEnabled(True)
        self.lineEdit_dialog_dockerif_mac.setObjectName("lineEdit_dialog_dockerif_mac")
        self.gridLayout.addWidget(self.lineEdit_dialog_dockerif_mac, 3, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.frame_dialog_virt_disk_wizard)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 4, 0, 1, 1)
        self.lineEdit_dialog_dockerif_of = QtWidgets.QLineEdit(self.frame_dialog_virt_disk_wizard)
        self.lineEdit_dialog_dockerif_of.setEnabled(True)
        self.lineEdit_dialog_dockerif_of.setClearButtonEnabled(True)
        self.lineEdit_dialog_dockerif_of.setObjectName("lineEdit_dialog_dockerif_of")
        self.gridLayout.addWidget(self.lineEdit_dialog_dockerif_of, 4, 1, 1, 1)
        self.verticalLayout.addWidget(self.frame_dialog_virt_disk_wizard)
        self.buttonBox = QtWidgets.QDialogButtonBox(dockerif_Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(dockerif_Dialog)
        self.buttonBox.accepted.connect(dockerif_Dialog.accept)
        self.buttonBox.rejected.connect(dockerif_Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(dockerif_Dialog)

    def retranslateUi(self, dockerif_Dialog):
        _translate = QtCore.QCoreApplication.translate
        dockerif_Dialog.setWindowTitle(_translate("dockerif_Dialog", "Docker interface editor"))
        self.label_6.setText(_translate("dockerif_Dialog", "container interface"))
        self.label_5.setText(_translate("dockerif_Dialog", "ovs port"))
        self.label_7.setText(_translate("dockerif_Dialog", "ovs vlan"))
        self.label_8.setText(_translate("dockerif_Dialog", "mac"))
        self.label_9.setText(_translate("dockerif_Dialog", "ovs ofport:"))

