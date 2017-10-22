# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reg.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from security import *

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):  # lint:ok
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_Reg_1(object):
    def setupUi(self, Reg_1):
        Reg_1.setObjectName(_fromUtf8("Reg_1"))
        Reg_1.resize(560, 720)
        Reg_1.setAutoFillBackground(False)
        Reg_1.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);"))
        self.centralwidget = QtGui.QWidget(Reg_1)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pass_lbl = QtGui.QLabel(self.centralwidget)
        self.pass_lbl.setGeometry(QtCore.QRect(50, 260, 400, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pass_lbl.setFont(font)
        self.pass_lbl.setStyleSheet(_fromUtf8("color:rgb(255,34,34)"))
        self.pass_lbl.setObjectName(_fromUtf8("pass_lbl"))
        self.conf_pass_lbl = QtGui.QLabel(self.centralwidget)
        self.conf_pass_lbl.setGeometry(QtCore.QRect(50, 370, 400, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.conf_pass_lbl.setFont(font)
        self.conf_pass_lbl.setStyleSheet(_fromUtf8("color:rgb(255,34,34)"))
        self.conf_pass_lbl.setObjectName(_fromUtf8("conf_pass_lbl"))
        self.usr_lbl = QtGui.QLabel(self.centralwidget)
        self.usr_lbl.setGeometry(QtCore.QRect(50, 150, 400, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.usr_lbl.setFont(font)
        self.usr_lbl.setStyleSheet(_fromUtf8("color:rgb(255,34,34)"))
        self.usr_lbl.setObjectName(_fromUtf8("usr_lbl"))
        self.btn_Confirm = QtGui.QPushButton(self.centralwidget)
        self.btn_Confirm.setGeometry(QtCore.QRect(660, 850, 112, 34))
        self.btn_Confirm.setObjectName(_fromUtf8("btn_Confirm"))
        self.usr_input = QtGui.QLineEdit(self.centralwidget)
        self.usr_input.setGeometry(QtCore.QRect(50, 190, 450, 55))
        self.usr_input.setStyleSheet(_fromUtf8("background-color:rgb(255,34,34)"))
        self.usr_input.setObjectName(_fromUtf8("usr_input"))
        self.pass_input = QtGui.QLineEdit(self.centralwidget)
        self.pass_input.setGeometry(QtCore.QRect(50, 300, 450, 55))
        self.pass_input.setEchoMode(QtGui.QLineEdit.Password)
        self.pass_input.setStyleSheet(_fromUtf8("background-color:rgb(255,34,34)"))
        self.pass_input.setObjectName(_fromUtf8("pass_input"))
        self.conf_pass_input = QtGui.QLineEdit(self.centralwidget)
        self.conf_pass_input.setGeometry(QtCore.QRect(50, 410, 450, 55))
        self.conf_pass_input.setEchoMode(QtGui.QLineEdit.Password)
        self.conf_pass_input.setStyleSheet(_fromUtf8("background-color:rgb(255,34,34)"))
        self.conf_pass_input.setObjectName(_fromUtf8("conf_pass_input"))
        self.next_btn = QtGui.QPushButton(self.centralwidget)
        self.next_btn.setGeometry(QtCore.QRect(200, 540, 141, 61))
        self.next_btn.setStyleSheet(_fromUtf8("background-color:rgb(255,34,34)"))
        self.next_btn.setObjectName(_fromUtf8("next_btn"))
        ############################## Button next event ###################################
        self.next_btn.clicked.connect(self.getInfo)
        #######################################################################################
        self.reg_lbl = QtGui.QLabel(self.centralwidget)
        self.reg_lbl.setGeometry(QtCore.QRect(50, 40, 451, 81))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.reg_lbl.setFont(font)
        self.reg_lbl.setStyleSheet(_fromUtf8("color:rgb(255,34,34)"))
        self.reg_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.reg_lbl.setObjectName(_fromUtf8("reg_lbl"))
        Reg_1.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Reg_1)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 560, 31))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        Reg_1.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Reg_1)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Reg_1.setStatusBar(self.statusbar)

        self.retranslateUi(Reg_1)
        QtCore.QMetaObject.connectSlotsByName(Reg_1)

    def retranslateUi(self, Reg_1):
        Reg_1.setWindowTitle(_translate("Reg_1", "MainWindow", None))
        self.pass_lbl.setText(_translate("Reg_1", "Password", None))
        self.conf_pass_lbl.setText(_translate("Reg_1", "Confirm password", None))
        self.usr_lbl.setText(_translate("Reg_1", "Username", None))
        self.btn_Confirm.setText(_translate("Reg_1", "Sing Up", None))
        self.next_btn.setText(_translate("Reg_1", "Next >", None))
        self.reg_lbl.setText(_translate("Reg_1", "Please fill all of\n""the fields below", None))

    def msgBox(self, title, msg):
        msgBox = QtGui.QMessageBox()
        msgBox.setIcon(QtGui.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(msg)
        msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
        msgBox.exec_()

    def reg2Prompt(self):
        Reg_1.close()
        import os
        os.system("python reg2.py")

    def getInfo(self):
        username = self.usr_input.text()
        password = self.pass_input.text()
        conf_password = self.conf_pass_input.text()
        if password != conf_password:
            self.msgBox("Warning!", "Both passwords do not match")
        else:
            dtbs = open("Database.txt", "a")
            dtbs.writelines(["@" + username + "\n", encrypt(password) + "\n"])
            #dtbs.write("@" + username)
            #dtbs.write(encrypt(password))
            dtbs.close()
            self.reg2Prompt()

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Reg_1 = QtGui.QMainWindow()
    ui = Ui_Reg_1()
    ui.setupUi(Reg_1)
    Reg_1.show()
    sys.exit(app.exec_())