# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/qos_queue_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_qqueue_Dialog(object):
    def setupUi(self, qqueue_Dialog):
        qqueue_Dialog.setObjectName("qqueue_Dialog")
        qqueue_Dialog.resize(465, 282)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(qqueue_Dialog.sizePolicy().hasHeightForWidth())
        qqueue_Dialog.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(qqueue_Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_dialog_virt_disk_wizard = QtWidgets.QFrame(qqueue_Dialog)
        self.frame_dialog_virt_disk_wizard.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_dialog_virt_disk_wizard.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_dialog_virt_disk_wizard.setProperty("paintme01", True)
        self.frame_dialog_virt_disk_wizard.setObjectName("frame_dialog_virt_disk_wizard")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_dialog_virt_disk_wizard)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_dialog_qos_queue_dscp = QtWidgets.QLineEdit(self.frame_dialog_virt_disk_wizard)
        self.lineEdit_dialog_qos_queue_dscp.setClearButtonEnabled(True)
        self.lineEdit_dialog_qos_queue_dscp.setObjectName("lineEdit_dialog_qos_queue_dscp")
        self.gridLayout.addWidget(self.lineEdit_dialog_qos_queue_dscp, 4, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame_dialog_virt_disk_wizard)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.frame_dialog_virt_disk_wizard)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.frame_dialog_virt_disk_wizard)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 4, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 5, 1, 1, 1)
        self.lineEdit_dialog_qos_queue_maxrate = QtWidgets.QLineEdit(self.frame_dialog_virt_disk_wizard)
        self.lineEdit_dialog_qos_queue_maxrate.setClearButtonEnabled(True)
        self.lineEdit_dialog_qos_queue_maxrate.setObjectName("lineEdit_dialog_qos_queue_maxrate")
        self.gridLayout.addWidget(self.lineEdit_dialog_qos_queue_maxrate, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame_dialog_virt_disk_wizard)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.frame_dialog_virt_disk_wizard)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)
        self.lineEdit_dialog_qos_queue_minrate = QtWidgets.QLineEdit(self.frame_dialog_virt_disk_wizard)
        self.lineEdit_dialog_qos_queue_minrate.setClearButtonEnabled(True)
        self.lineEdit_dialog_qos_queue_minrate.setObjectName("lineEdit_dialog_qos_queue_minrate")
        self.gridLayout.addWidget(self.lineEdit_dialog_qos_queue_minrate, 0, 1, 1, 1)
        self.lineEdit_dialog_qos_queue_burst = QtWidgets.QLineEdit(self.frame_dialog_virt_disk_wizard)
        self.lineEdit_dialog_qos_queue_burst.setClearButtonEnabled(True)
        self.lineEdit_dialog_qos_queue_burst.setObjectName("lineEdit_dialog_qos_queue_burst")
        self.gridLayout.addWidget(self.lineEdit_dialog_qos_queue_burst, 2, 1, 1, 1)
        self.lineEdit_dialog_qos_queue_priority = QtWidgets.QLineEdit(self.frame_dialog_virt_disk_wizard)
        self.lineEdit_dialog_qos_queue_priority.setClearButtonEnabled(True)
        self.lineEdit_dialog_qos_queue_priority.setObjectName("lineEdit_dialog_qos_queue_priority")
        self.gridLayout.addWidget(self.lineEdit_dialog_qos_queue_priority, 3, 1, 1, 1)
        self.verticalLayout.addWidget(self.frame_dialog_virt_disk_wizard)
        self.buttonBox = QtWidgets.QDialogButtonBox(qqueue_Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(qqueue_Dialog)
        self.buttonBox.accepted.connect(qqueue_Dialog.accept)
        self.buttonBox.rejected.connect(qqueue_Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(qqueue_Dialog)

    def retranslateUi(self, qqueue_Dialog):
        _translate = QtCore.QCoreApplication.translate
        qqueue_Dialog.setWindowTitle(_translate("qqueue_Dialog", "New Queue"))
        self.label_5.setText(_translate("qqueue_Dialog", "max-rate:"))
        self.label_7.setText(_translate("qqueue_Dialog", "priority:"))
        self.label_8.setText(_translate("qqueue_Dialog", "dscp:"))
        self.label_2.setText(_translate("qqueue_Dialog", "min-rate:"))
        self.label_6.setText(_translate("qqueue_Dialog", "burst:"))

