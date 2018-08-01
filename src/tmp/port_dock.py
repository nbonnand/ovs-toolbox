# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/port_dock.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_port_dock_Dialog(object):
    def setupUi(self, port_dock_Dialog):
        port_dock_Dialog.setObjectName("port_dock_Dialog")
        port_dock_Dialog.resize(400, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(port_dock_Dialog.sizePolicy().hasHeightForWidth())
        port_dock_Dialog.setSizePolicy(sizePolicy)
        self.verticalLayout_for_dock = QtWidgets.QVBoxLayout(port_dock_Dialog)
        self.verticalLayout_for_dock.setObjectName("verticalLayout_for_dock")

        self.retranslateUi(port_dock_Dialog)
        QtCore.QMetaObject.connectSlotsByName(port_dock_Dialog)

    def retranslateUi(self, port_dock_Dialog):
        _translate = QtCore.QCoreApplication.translate
        port_dock_Dialog.setWindowTitle(_translate("port_dock_Dialog", "Ports"))

