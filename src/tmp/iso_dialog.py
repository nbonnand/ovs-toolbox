# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/iso_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_iso_Dialog(object):
    def setupUi(self, iso_Dialog):
        iso_Dialog.setObjectName("iso_Dialog")
        iso_Dialog.resize(440, 146)
        self.verticalLayout = QtWidgets.QVBoxLayout(iso_Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_dialog_virt_disk_wizard = QtWidgets.QFrame(iso_Dialog)
        self.frame_dialog_virt_disk_wizard.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_dialog_virt_disk_wizard.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_dialog_virt_disk_wizard.setProperty("paintme01", True)
        self.frame_dialog_virt_disk_wizard.setObjectName("frame_dialog_virt_disk_wizard")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_dialog_virt_disk_wizard)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_dialog_kvm_iso_dstfile = QtWidgets.QLineEdit(self.frame_dialog_virt_disk_wizard)
        self.lineEdit_dialog_kvm_iso_dstfile.setEnabled(True)
        self.lineEdit_dialog_kvm_iso_dstfile.setClearButtonEnabled(True)
        self.lineEdit_dialog_kvm_iso_dstfile.setObjectName("lineEdit_dialog_kvm_iso_dstfile")
        self.gridLayout.addWidget(self.lineEdit_dialog_kvm_iso_dstfile, 2, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame_dialog_virt_disk_wizard)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.frame_dialog_virt_disk_wizard)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 1, 1, 1)
        self.lineEdit_dialog_kvm_iso_srcdir = QtWidgets.QLineEdit(self.frame_dialog_virt_disk_wizard)
        self.lineEdit_dialog_kvm_iso_srcdir.setEnabled(True)
        self.lineEdit_dialog_kvm_iso_srcdir.setClearButtonEnabled(True)
        self.lineEdit_dialog_kvm_iso_srcdir.setObjectName("lineEdit_dialog_kvm_iso_srcdir")
        self.gridLayout.addWidget(self.lineEdit_dialog_kvm_iso_srcdir, 1, 2, 1, 1)
        self.verticalLayout.addWidget(self.frame_dialog_virt_disk_wizard)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.buttonBox = QtWidgets.QDialogButtonBox(iso_Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(iso_Dialog)
        self.buttonBox.accepted.connect(iso_Dialog.accept)
        self.buttonBox.rejected.connect(iso_Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(iso_Dialog)

    def retranslateUi(self, iso_Dialog):
        _translate = QtCore.QCoreApplication.translate
        iso_Dialog.setWindowTitle(_translate("iso_Dialog", "ISO file generator"))
        self.lineEdit_dialog_kvm_iso_dstfile.setToolTip(_translate("iso_Dialog", "2 digit number example: 11 "))
        self.label_5.setText(_translate("iso_Dialog", "Source directory:"))
        self.label_6.setText(_translate("iso_Dialog", "destination iso file:"))
        self.lineEdit_dialog_kvm_iso_srcdir.setToolTip(_translate("iso_Dialog", "2 digit number example: 05 "))

