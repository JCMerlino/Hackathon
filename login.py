# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
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


class Ui_login(object):

    def setupUi(self, login):
        global username
        login.setObjectName(_fromUtf8("login"))
        login.resize(560, 720)
        font = QtGui.QFont()
        font.setPointSize(16)
        login.setFont(font)
        login.setLayoutDirection(QtCore.Qt.LeftToRight)
        login.setAutoFillBackground(False)
        login.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);"))
        login.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedKingdom))
        self.centralwidget = QtGui.QWidget(login)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.btn_login = QtGui.QPushButton(self.centralwidget)
        self.btn_login.setGeometry(QtCore.QRect(80, 550, 400, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_login.setFont(font)
        self.btn_login.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 34, 34);"))
        self.btn_login.setObjectName(_fromUtf8("btn_login"))
        ############################## Button login event ###################################
        self.btn_login.clicked.connect(self.loginCheck)
        #####################################################################################
        self.usr_lbl = QtGui.QLabel(self.centralwidget)
        self.usr_lbl.setGeometry(QtCore.QRect(80, 300, 401, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.usr_lbl.setFont(font)
        self.usr_lbl.setStyleSheet(_fromUtf8("color: rgb(255, 34, 34);"))
        self.usr_lbl.setObjectName(_fromUtf8("usr_lbl"))
        self.pass_lbl = QtGui.QLabel(self.centralwidget)
        self.pass_lbl.setGeometry(QtCore.QRect(80, 430, 401, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pass_lbl.setFont(font)
        self.pass_lbl.setStyleSheet(_fromUtf8("color: rgb(255, 34, 34);"))
        self.pass_lbl.setObjectName(_fromUtf8("pass_lbl"))
        self.logo = QtGui.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(80, 10, 401, 271))
        self.logo.setSizeIncrement(QtCore.QSize(5, 5))
        self.logo.setStyleSheet(_fromUtf8("color: rgb(255, 34, 34);"))
        self.logo.setObjectName(_fromUtf8("logo"))
        self.u_name_input = QtGui.QLineEdit(self.centralwidget)
        self.u_name_input.setGeometry(QtCore.QRect(80, 360, 400, 60))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.u_name_input.setFont(font)
        self.u_name_input.setStyleSheet(_fromUtf8("background-color: rgb(255, 34, 34);"))
        self.u_name_input.setCursorPosition(0)
        self.u_name_input.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.u_name_input.setObjectName(_fromUtf8("u_name_input"))
        self.pass_input = QtGui.QLineEdit(self.centralwidget)
        self.pass_input.setGeometry(QtCore.QRect(80, 480, 400, 60))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pass_input.setFont(font)
        self.pass_input.setMouseTracking(True)
        self.pass_input.setStyleSheet(_fromUtf8("background-color: rgb(255, 34, 34);"))
        self.pass_input.setEchoMode(QtGui.QLineEdit.Password)
        self.pass_input.setPlaceholderText(_fromUtf8(""))
        self.pass_input.setObjectName(_fromUtf8("pass_input"))
        self.signup_lbl = QtGui.QLabel(self.centralwidget)
        self.signup_lbl.setGeometry(QtCore.QRect(100, 620, 191, 21))
        self.signup_lbl.setStyleSheet(_fromUtf8("color: rgb(255, 34, 34);"))
        self.signup_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.signup_lbl.setObjectName(_fromUtf8("signup_lbl"))
        self.btn_sign_up = QtGui.QPushButton(self.centralwidget)
        self.btn_sign_up.setGeometry(QtCore.QRect(310, 614, 151, 32))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.btn_sign_up.setFont(font)
        self.btn_sign_up.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 34, 34);"))
        self.btn_sign_up.setObjectName(_fromUtf8("btn_sign_up"))
        ############################## Button sign up event ###################################
        self.btn_sign_up.clicked.connect(self.signUpPrompt)
        #######################################################################################
        login.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(login)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 560, 31))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        login.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(login)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        login.setStatusBar(self.statusbar)

        self.retranslateUi(login)
        QtCore.QMetaObject.connectSlotsByName(login)

    def retranslateUi(self, login):
        login.setWindowTitle(_translate("login", "MainWindow", None))
        self.btn_login.setText(_translate("login", "Login", None))
        self.usr_lbl.setText(_translate("login", "Username", None))
        self.pass_lbl.setText(_translate("login", "Password", None))
        self.logo.setText(_translate("login", "<html><head/><body><p><img src=\":./Logo.png\"/></p></body></html>", None))
        self.signup_lbl.setText(_translate("login", "Don\'t have an account?", None))
        self.btn_sign_up.setText(_translate("login", "Sign up", None))

    def msgBox(self, title, msg):
        msgBox = QtGui.QMessageBox()
        msgBox.setIcon(QtGui.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(msg)
        msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
        msgBox.exec_()

    def loginCheck(self):
        username = self.u_name_input.text()
        password = self.pass_input.text()
        dtbs = open("Database.txt", "r")
        found = False
        while not found:
            line = dtbs.readline()
            if line == ("@" + username + "\n"):
                found = True
            elif line == "":
                self.msgBox("Warning!", "Username not found.")
                break
        line = dtbs.readline()
        dtbs.close()
        if found and ((encrypt(password) + "\n") == line):
            File = open("Current_Username.txt", "w")
            File.write(username)
            File.close()
            login.close()
            import os
            os.system("python listings_page.py")
        elif found and encrypt(password) != line:
            self.msgBox("Warning!", "Password incorrect.")

    def signUpPrompt(self):
        login.close()
        import os
        os.system("python reg.py")

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    login = QtGui.QMainWindow()
    ui = Ui_login()
    ui.setupUi(login)
    login.show()
    sys.exit(app.exec_())
