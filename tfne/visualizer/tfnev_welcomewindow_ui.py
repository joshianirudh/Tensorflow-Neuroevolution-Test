# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tfnev_welcomewindow_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WelcomeWindow(object):
    def setupUi(self, WelcomeWindow):
        WelcomeWindow.setObjectName("WelcomeWindow")
        WelcomeWindow.resize(220, 250)
        self.centralwidget = QtWidgets.QWidget(WelcomeWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button_open_backup_dir = QtWidgets.QPushButton(self.centralwidget)
        self.button_open_backup_dir.setGeometry(QtCore.QRect(10, 210, 200, 25))
        self.button_open_backup_dir.setObjectName("button_open_backup_dir")
        WelcomeWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(WelcomeWindow)
        QtCore.QMetaObject.connectSlotsByName(WelcomeWindow)

    def retranslateUi(self, WelcomeWindow):
        _translate = QtCore.QCoreApplication.translate
        WelcomeWindow.setWindowTitle(_translate("WelcomeWindow", "WelcomeWindow"))
        self.button_open_backup_dir.setText(_translate("WelcomeWindow", "Open TFNE State Backup"))
