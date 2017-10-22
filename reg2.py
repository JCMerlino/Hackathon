# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reg2.ui'
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
    def _translate(context, text, disambig):  # lint:ok
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_Reg_2(object):
    def setupUi(self, Reg_2):
        Reg_2.setObjectName(_fromUtf8("Reg_2"))
        Reg_2.resize(560, 720)
        Reg_2.setAutoFillBackground(False)
        Reg_2.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);"))
        self.centralwidget = QtGui.QWidget(Reg_2)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.age_lbl = QtGui.QLabel(self.centralwidget)
        self.age_lbl.setGeometry(QtCore.QRect(50, 220, 210, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.age_lbl.setFont(font)
        self.age_lbl.setStyleSheet(_fromUtf8("color:rgb(255,34,34)"))
        self.age_lbl.setObjectName(_fromUtf8("age_lbl"))
        self.email_lbl = QtGui.QLabel(self.centralwidget)
        self.email_lbl.setGeometry(QtCore.QRect(50, 330, 400, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.email_lbl.setFont(font)
        self.email_lbl.setStyleSheet(_fromUtf8("color:rgb(255,34,34)"))
        self.email_lbl.setObjectName(_fromUtf8("email_lbl"))
        self.name_lbl = QtGui.QLabel(self.centralwidget)
        self.name_lbl.setGeometry(QtCore.QRect(50, 110, 451, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.name_lbl.setFont(font)
        self.name_lbl.setStyleSheet(_fromUtf8("color:rgb(255,34,34)"))
        self.name_lbl.setObjectName(_fromUtf8("name_lbl"))
        self.btn_Confirm = QtGui.QPushButton(self.centralwidget)
        self.btn_Confirm.setGeometry(QtCore.QRect(660, 850, 112, 34))
        self.btn_Confirm.setObjectName(_fromUtf8("btn_Confirm"))
        self.name_input = QtGui.QLineEdit(self.centralwidget)
        self.name_input.setGeometry(QtCore.QRect(50, 150, 450, 55))
        self.name_input.setStyleSheet(_fromUtf8("background-color:rgb(255,34,34)"))
        self.name_input.setObjectName(_fromUtf8("name_input"))
        self.age_input = QtGui.QLineEdit(self.centralwidget)
        self.age_input.setGeometry(QtCore.QRect(50, 260, 215, 55))
        self.age_input.setStyleSheet(_fromUtf8("background-color:rgb(255,34,34)"))
        self.age_input.setObjectName(_fromUtf8("age_input"))
        self.email_input = QtGui.QLineEdit(self.centralwidget)
        self.email_input.setGeometry(QtCore.QRect(50, 370, 450, 55))
        self.email_input.setStyleSheet(_fromUtf8("background-color:rgb(255,34,34)"))
        self.email_input.setObjectName(_fromUtf8("email_input"))
        self.done_btn = QtGui.QPushButton(self.centralwidget)
        self.done_btn.setGeometry(QtCore.QRect(210, 640, 141, 61))
        self.done_btn.setStyleSheet(_fromUtf8("background-color:rgb(255,34,34)"))
        self.done_btn.setObjectName(_fromUtf8("done_btn"))
        ############################## Button done event ###################################
        self.done_btn.clicked.connect(self.getInfo)
        #######################################################################################
        self.reg2_lbl = QtGui.QLabel(self.centralwidget)
        self.reg2_lbl.setGeometry(QtCore.QRect(50, 20, 451, 81))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.reg2_lbl.setFont(font)
        self.reg2_lbl.setStyleSheet(_fromUtf8("color:rgb(255,34,34)"))
        self.reg2_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.reg2_lbl.setObjectName(_fromUtf8("reg2_lbl"))
        self.gender_lbl = QtGui.QLabel(self.centralwidget)
        self.gender_lbl.setGeometry(QtCore.QRect(280, 220, 210, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.gender_lbl.setFont(font)
        self.gender_lbl.setStyleSheet(_fromUtf8("color:rgb(255,34,34)"))
        self.gender_lbl.setObjectName(_fromUtf8("gender_lbl"))
        self.gender_input = QtGui.QLineEdit(self.centralwidget)
        self.gender_input.setGeometry(QtCore.QRect(280, 260, 215, 55))
        self.gender_input.setStyleSheet(_fromUtf8("background-color:rgb(255,34,34)"))
        self.gender_input.setObjectName(_fromUtf8("gender_input"))
        self.loc_input = QtGui.QLineEdit(self.centralwidget)
        self.loc_input.setGeometry(QtCore.QRect(50, 470, 450, 55))
        self.loc_input.setStyleSheet(_fromUtf8("background-color:rgb(255,34,34)"))
        self.loc_input.setObjectName(_fromUtf8("loc_input"))
        self.loc_lbl = QtGui.QLabel(self.centralwidget)
        self.loc_lbl.setGeometry(QtCore.QRect(50, 430, 400, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.loc_lbl.setFont(font)
        self.loc_lbl.setStyleSheet(_fromUtf8("color:rgb(255,34,34)"))
        self.loc_lbl.setObjectName(_fromUtf8("loc_lbl"))
        self.msg_lnk_lbl = QtGui.QLabel(self.centralwidget)
        self.msg_lnk_lbl.setGeometry(QtCore.QRect(50, 530, 400, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.msg_lnk_lbl.setFont(font)
        self.msg_lnk_lbl.setStyleSheet(_fromUtf8("color:rgb(255,34,34)"))
        self.msg_lnk_lbl.setObjectName(_fromUtf8("msg_lnk_lbl"))
        self.msg_lnk_input = QtGui.QLineEdit(self.centralwidget)
        self.msg_lnk_input.setGeometry(QtCore.QRect(50, 570, 450, 55))
        self.msg_lnk_input.setStyleSheet(_fromUtf8("background-color:rgb(255,34,34)"))
        self.msg_lnk_input.setObjectName(_fromUtf8("msg_lnk_input"))
        Reg_2.setCentralWidget(self.centralwidget)

        self.retranslateUi(Reg_2)
        QtCore.QMetaObject.connectSlotsByName(Reg_2)

    def retranslateUi(self, Reg_2):
        Reg_2.setWindowTitle(_translate("Reg_2", "MainWindow", None))
        self.age_lbl.setText(_translate("Reg_2", "Age", None))
        self.email_lbl.setText(_translate("Reg_2", "Email", None))
        self.name_lbl.setText(_translate("Reg_2", "Full Name", None))
        self.btn_Confirm.setText(_translate("Reg_2", "Sing Up", None))
        self.done_btn.setText(_translate("Reg_2", "Done", None))
        self.reg2_lbl.setText(_translate("Reg_2", "Please enter your following\n"
"personal details", None))
        self.gender_lbl.setText(_translate("Reg_2", "Gender (M or F)", None))
        self.loc_input.setPlaceholderText(_translate("Reg_2", "Help us find people near you", None))
        self.loc_lbl.setText(_translate("Reg_2", "Where are you now?", None))
        self.msg_lnk_lbl.setText(_translate("Reg_2", "Messenger link", None))
        self.msg_lnk_input.setPlaceholderText(_translate("Reg_2", "e.g. m.me/facebookUsername", None))

    def msgBox(self, title, msg):
        msgBox = QtGui.QMessageBox()
        msgBox.setIcon(QtGui.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(msg)
        msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
        msgBox.exec_()

    def getInfo(self):
        name = self.name_input.text()
        age = self.age_input.text()
        gender = self.gender_input.text()
        email = self.email_input.text()
        location = self.loc_input.text()
        msg_lnk = self.msg_lnk_input.text()
        if (name == "") or (age == "") or (gender == "") or (email == "") or (location == "") or (msg_lnk == ""):
            self.msgBox("Warning!", "Please fill in all of the fields.")
        else:
            dtbs = open("Database.txt", "a")
            dtbs.writelines([name + "\n", age + "\n", gender + "\n", email + "\n", location + "\n", msg_lnk])
            dtbs.close()
            print("Registration completed.")
            Reg_2.close()


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Reg_2 = QtGui.QMainWindow()
    ui = Ui_Reg_2()
    ui.setupUi(Reg_2)
    Reg_2.show()
    sys.exit(app.exec_())