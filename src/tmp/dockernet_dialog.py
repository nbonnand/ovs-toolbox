# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/dockernet_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dockernet_Dialog(object):
    def setupUi(self, dockernet_Dialog):
        dockernet_Dialog.setObjectName("dockernet_Dialog")
        dockernet_Dialog.resize(439, 218)
        self.verticalLayout = QtWidgets.QVBoxLayout(dockernet_Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_dialog_virt_disk_wizard = QtWidgets.QFrame(dockernet_Dialog)
        self.frame_dialog_virt_disk_wizard.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_dialog_virt_disk_wizard.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_dialog_virt_disk_wizard.setProperty("paintme01", True)
        self.frame_dialog_virt_disk_wizard.setObjectName("frame_dialog_virt_disk_wizard")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_dialog_virt_disk_wizard)
        self.gridLayout.setObjectName("gridLayout")
        self.label_7 = QtWidgets.QLabel(self.frame_dialog_virt_disk_wizard)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)
        self.lineEdit_dialog_dockernet_net = QtWidgets.QLineEdit(self.frame_dialog_virt_disk_wizard)
        self.lineEdit_dialog_dockernet_net.setEnabled(True)
        self.lineEdit_dialog_dockernet_net.setClearButtonEnabled(True)
        self.lineEdit_dialog_dockernet_net.setObjectName("lineEdit_dialog_dockernet_net")
        self.gridLayout.addWidget(self.lineEdit_dialog_dockernet_net, 2, 1, 1, 1)
        self.comboBox_dockernet = QtWidgets.QComboBox(self.frame_dialog_virt_disk_wizard)
        self.comboBox_dockernet.setObjectName("comboBox_dockernet")
        self.comboBox_dockernet.addItem("")
        self.comboBox_dockernet.setItemText(0, "")
        self.comboBox_dockernet.addItem("")
        self.comboBox_dockernet.addItem("")
        self.comboBox_dockernet.addItem("")
        self.gridLayout.addWidget(self.comboBox_dockernet, 0, 1, 1, 1)
        self.lineEdit_dialog_dockernet_ip = QtWidgets.QLineEdit(self.frame_dialog_virt_disk_wizard)
        self.lineEdit_dialog_dockernet_ip.setEnabled(True)
        self.lineEdit_dialog_dockernet_ip.setClearButtonEnabled(True)
        self.lineEdit_dialog_dockernet_ip.setObjectName("lineEdit_dialog_dockernet_ip")
        self.gridLayout.addWidget(self.lineEdit_dialog_dockernet_ip, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame_dialog_virt_disk_wizard)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.frame_dialog_virt_disk_wizard)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)
        self.lineEdit_dialog_dockernet_gw = QtWidgets.QLineEdit(self.frame_dialog_virt_disk_wizard)
        self.lineEdit_dialog_dockernet_gw.setEnabled(True)
        self.lineEdit_dialog_dockernet_gw.setClearButtonEnabled(True)
        self.lineEdit_dialog_dockernet_gw.setObjectName("lineEdit_dialog_dockernet_gw")
        self.gridLayout.addWidget(self.lineEdit_dialog_dockernet_gw, 3, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame_dialog_virt_disk_wizard)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame_dialog_virt_disk_wizard)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.buttonBox = QtWidgets.QDialogButtonBox(dockernet_Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(dockernet_Dialog)
        self.buttonBox.accepted.connect(dockernet_Dialog.accept)
        self.buttonBox.rejected.connect(dockernet_Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(dockernet_Dialog)

    def retranslateUi(self, dockernet_Dialog):
        _translate = QtCore.QCoreApplication.translate
        dockernet_Dialog.setWindowTitle(_translate("dockernet_Dialog", "Docker net editor"))
        self.label_7.setText(_translate("dockernet_Dialog", "gateway:"))
        self.comboBox_dockernet.setItemText(1, _translate("dockernet_Dialog", "addr"))
        self.comboBox_dockernet.setItemText(2, _translate("dockernet_Dialog", "route"))
        self.comboBox_dockernet.setItemText(3, _translate("dockernet_Dialog", "default route"))
        self.label_5.setText(_translate("dockernet_Dialog", "ip/mask:"))
        self.label_6.setText(_translate("dockernet_Dialog", "network/mask:"))
        self.label_4.setText(_translate("dockernet_Dialog", "type:"))

