# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/qos_queue_link.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_qos_queue_link_Dialog(object):
    def setupUi(self, qos_queue_link_Dialog):
        qos_queue_link_Dialog.setObjectName("qos_queue_link_Dialog")
        qos_queue_link_Dialog.resize(402, 200)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(qos_queue_link_Dialog.sizePolicy().hasHeightForWidth())
        qos_queue_link_Dialog.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(qos_queue_link_Dialog)
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_dialog_virt_disk_wizard = QtWidgets.QFrame(qos_queue_link_Dialog)
        self.frame_dialog_virt_disk_wizard.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_dialog_virt_disk_wizard.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_dialog_virt_disk_wizard.setProperty("paintme01", True)
        self.frame_dialog_virt_disk_wizard.setObjectName("frame_dialog_virt_disk_wizard")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_dialog_virt_disk_wizard)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.frame_dialog_virt_disk_wizard)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.lineEdit_dialog_qos_queue = QtWidgets.QLineEdit(self.frame_dialog_virt_disk_wizard)
        self.lineEdit_dialog_qos_queue.setReadOnly(True)
        self.lineEdit_dialog_qos_queue.setClearButtonEnabled(True)
        self.lineEdit_dialog_qos_queue.setObjectName("lineEdit_dialog_qos_queue")
        self.gridLayout.addWidget(self.lineEdit_dialog_qos_queue, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame_dialog_virt_disk_wizard)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.lineEdit_dialog_queue_mapid = QtWidgets.QLineEdit(self.frame_dialog_virt_disk_wizard)
        self.lineEdit_dialog_queue_mapid.setClearButtonEnabled(True)
        self.lineEdit_dialog_queue_mapid.setObjectName("lineEdit_dialog_queue_mapid")
        self.gridLayout.addWidget(self.lineEdit_dialog_queue_mapid, 2, 1, 1, 1)
        self.lineEdit_dialog_qos_qos = QtWidgets.QLineEdit(self.frame_dialog_virt_disk_wizard)
        self.lineEdit_dialog_qos_qos.setReadOnly(True)
        self.lineEdit_dialog_qos_qos.setClearButtonEnabled(True)
        self.lineEdit_dialog_qos_qos.setObjectName("lineEdit_dialog_qos_qos")
        self.gridLayout.addWidget(self.lineEdit_dialog_qos_qos, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 3, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.frame_dialog_virt_disk_wizard)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame_dialog_virt_disk_wizard)
        self.buttonBox = QtWidgets.QDialogButtonBox(qos_queue_link_Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(qos_queue_link_Dialog)
        self.buttonBox.accepted.connect(qos_queue_link_Dialog.accept)
        self.buttonBox.rejected.connect(qos_queue_link_Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(qos_queue_link_Dialog)

    def retranslateUi(self, qos_queue_link_Dialog):
        _translate = QtCore.QCoreApplication.translate
        qos_queue_link_Dialog.setWindowTitle(_translate("qos_queue_link_Dialog", "Add queue in QOS"))
        self.label_2.setText(_translate("qos_queue_link_Dialog", "queue:"))
        self.label_5.setText(_translate("qos_queue_link_Dialog", "qos:"))
        self.label_6.setText(_translate("qos_queue_link_Dialog", "map id:"))

