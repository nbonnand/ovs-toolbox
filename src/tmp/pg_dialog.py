# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/pg_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_pg_Dialog(object):
    def setupUi(self, pg_Dialog):
        pg_Dialog.setObjectName("pg_Dialog")
        pg_Dialog.resize(346, 240)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(pg_Dialog.sizePolicy().hasHeightForWidth())
        pg_Dialog.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(pg_Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_dialog_virt_disk_wizard = QtWidgets.QFrame(pg_Dialog)
        self.frame_dialog_virt_disk_wizard.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_dialog_virt_disk_wizard.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_dialog_virt_disk_wizard.setProperty("paintme01", True)
        self.frame_dialog_virt_disk_wizard.setObjectName("frame_dialog_virt_disk_wizard")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_dialog_virt_disk_wizard)
        self.gridLayout.setObjectName("gridLayout")
        self.label_5 = QtWidgets.QLabel(self.frame_dialog_virt_disk_wizard)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame_dialog_virt_disk_wizard)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.comboBox_dialog_kvm_pg_mode = QtWidgets.QComboBox(self.frame_dialog_virt_disk_wizard)
        self.comboBox_dialog_kvm_pg_mode.setObjectName("comboBox_dialog_kvm_pg_mode")
        self.comboBox_dialog_kvm_pg_mode.addItem("")
        self.comboBox_dialog_kvm_pg_mode.addItem("")
        self.gridLayout.addWidget(self.comboBox_dialog_kvm_pg_mode, 3, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.frame_dialog_virt_disk_wizard)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)
        self.lineEdit_dialog_kvm_pg_name = QtWidgets.QLineEdit(self.frame_dialog_virt_disk_wizard)
        self.lineEdit_dialog_kvm_pg_name.setClearButtonEnabled(True)
        self.lineEdit_dialog_kvm_pg_name.setObjectName("lineEdit_dialog_kvm_pg_name")
        self.gridLayout.addWidget(self.lineEdit_dialog_kvm_pg_name, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 5, 1, 1, 1)
        self.lineEdit_kvm_pg_tags = QtWidgets.QLineEdit(self.frame_dialog_virt_disk_wizard)
        self.lineEdit_kvm_pg_tags.setClearButtonEnabled(True)
        self.lineEdit_kvm_pg_tags.setObjectName("lineEdit_kvm_pg_tags")
        self.gridLayout.addWidget(self.lineEdit_kvm_pg_tags, 4, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame_dialog_virt_disk_wizard)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.checkBox_kvm_pg = QtWidgets.QCheckBox(self.frame_dialog_virt_disk_wizard)
        self.checkBox_kvm_pg.setText("")
        self.checkBox_kvm_pg.setObjectName("checkBox_kvm_pg")
        self.gridLayout.addWidget(self.checkBox_kvm_pg, 2, 1, 1, 1)
        self.verticalLayout.addWidget(self.frame_dialog_virt_disk_wizard)
        self.buttonBox = QtWidgets.QDialogButtonBox(pg_Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(pg_Dialog)
        self.buttonBox.accepted.connect(pg_Dialog.accept)
        self.buttonBox.rejected.connect(pg_Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(pg_Dialog)

    def retranslateUi(self, pg_Dialog):
        _translate = QtCore.QCoreApplication.translate
        pg_Dialog.setWindowTitle(_translate("pg_Dialog", "Dialog"))
        self.label_5.setText(_translate("pg_Dialog", "Default:"))
        self.label_2.setText(_translate("pg_Dialog", "Portgroup:"))
        self.comboBox_dialog_kvm_pg_mode.setItemText(0, _translate("pg_Dialog", "vlan"))
        self.comboBox_dialog_kvm_pg_mode.setItemText(1, _translate("pg_Dialog", "trunk"))
        self.label_6.setText(_translate("pg_Dialog", "Mode:"))
        self.label_3.setText(_translate("pg_Dialog", "Tags:"))

