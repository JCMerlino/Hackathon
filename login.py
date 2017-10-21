# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(560, 720)
        font = QtGui.QFont()
        font.setPointSize(16)
        MainWindow.setFont(font)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);"))
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedKingdom))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.btn_login = QtGui.QPushButton(self.centralwidget)
        self.btn_login.setGeometry(QtCore.QRect(80, 550, 400, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_login.setFont(font)
        self.btn_login.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 34, 34);"))
        self.btn_login.setObjectName(_fromUtf8("btn_login"))
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
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 10, 401, 271))
        self.label.setSizeIncrement(QtCore.QSize(5, 5))
        self.label.setStyleSheet(_fromUtf8("color: rgb(255, 34, 34);"))
        self.label.setObjectName(_fromUtf8("label"))
        self.u_name_input = QtGui.QLineEdit(self.centralwidget)
        self.u_name_input.setGeometry(QtCore.QRect(80, 360, 400, 60))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.u_name_input.setFont(font)
        self.u_name_input.setStyleSheet(_fromUtf8("background-color: rgb(255, 34, 34);"))
        self.u_name_input.setCursorPosition(0)
        self.u_name_input.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
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
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 620, 191, 21))
        self.label_2.setStyleSheet(_fromUtf8("color: rgb(255, 34, 34);"))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.btn_login_sign_up = QtGui.QPushButton(self.centralwidget)
        self.btn_login_sign_up.setGeometry(QtCore.QRect(310, 614, 151, 32))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.btn_login_sign_up.setFont(font)
        self.btn_login_sign_up.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 34, 34);"))
        self.btn_login_sign_up.setObjectName(_fromUtf8("btn_login_sign_up"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 560, 31))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.btn_login.setText(_translate("MainWindow", "Login", None))
        self.usr_lbl.setText(_translate("MainWindow", "Username", None))
        self.pass_lbl.setText(_translate("MainWindow", "Password", None))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":./Logo.png\"/></p></body></html>", None))
        self.label_2.setText(_translate("MainWindow", "Don\'t have an account?", None))
        self.btn_login_sign_up.setText(_translate("MainWindow", "Sign up", None))

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

