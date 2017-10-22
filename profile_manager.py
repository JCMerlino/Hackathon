# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'profile_manager.ui'
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
        MainWindow.resize(1111, 860)
        MainWindow.setLayoutDirection(QtCore.Qt.RightToLeft)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 34, 34);"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.Banner = QtGui.QLabel(self.centralwidget)
        self.Banner.setGeometry(QtCore.QRect(0, 0, 1281, 141))
        self.Banner.setText(_fromUtf8(""))
        self.Banner.setPixmap(QtGui.QPixmap(_fromUtf8("banner.png")))
        self.Banner.setObjectName(_fromUtf8("Banner"))
        self.Listings_Button = QtGui.QPushButton(self.centralwidget)
        self.Listings_Button.setGeometry(QtCore.QRect(70, 680, 990, 100))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("OCR A Std"))
        font.setBold(True)
        font.setWeight(75)
        self.Listings_Button.setFont(font)
        self.Listings_Button.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.Listings_Button.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.Listings_Button.setObjectName(_fromUtf8("Listings_Button"))
        self.Listings_Button.clicked.connect(self.go_to_listings)
        self.profile_info_lbl = QtGui.QLabel(self.centralwidget)
        self.profile_info_lbl.setGeometry(QtCore.QRect(70, 250, 981, 401))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.profile_info_lbl.setFont(font)
        dtbs = open("Database.txt", "r")
        File = open("Current_Username.txt", "r")
        username = File.readline()
        File.close()
        found = False
        list1 = []
        list2 = []
        pos = 0
        while not found:
            line = dtbs.readline()
            if line == ("@" + username + "\n"):
                found = True
                line = line.strip("@")
                list1.append(line.strip("\n"))
                for i in range(7):
                    line = dtbs.readline()
                    list1.append(line.strip("\n"))
            else:
                list2.append(line)
            pos += 1
        dtbs.close()
        list1.pop(1)
        list1[0] = "Username: " + list1[0]
        list1[1] = "Name: " + list1[1]
        list1[2] = "Age: " + list1[2]
        list1[3] = "Gender: " + list1[3]
        list1[4] = "Email: " + list1[4]
        list1[5] = "Location: " + list1[5]
        list1[6] = "Messenger link: " + list1[6]
        self.profile_info_lbl.setText(_fromUtf8("\n".join(list1)))
        self.profile_info_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.profile_info_lbl.setObjectName(_fromUtf8("profile_info_lbl"))
        self.profile_lbl = QtGui.QLabel(self.centralwidget)
        self.profile_lbl.setGeometry(QtCore.QRect(450, 160, 231, 71))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.profile_lbl.setFont(font)
        self.profile_lbl.setObjectName(_fromUtf8("profile_lbl"))
        self.edit_btn = QtGui.QPushButton(self.centralwidget)
        self.edit_btn.setGeometry(QtCore.QRect(790, 170, 181, 61))
        self.edit_btn.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 34, 34);"))
        self.edit_btn.setObjectName(_fromUtf8("edit_btn"))
        self.edit_btn.clicked.connect(self.edit_profile)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1111, 31))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuProfile = QtGui.QMenu(self.menubar)
        self.menuProfile.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.menuProfile.setObjectName(_fromUtf8("menuProfile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionView_your_profile = QtGui.QAction(MainWindow)
        self.actionView_your_profile.setObjectName(_fromUtf8("actionView_your_profile"))
        self.actionSettings = QtGui.QAction(MainWindow)
        self.actionSettings.setObjectName(_fromUtf8("actionSettings"))
        self.actionLog_out = QtGui.QAction(MainWindow)
        self.actionLog_out.setObjectName(_fromUtf8("actionLog_out"))
        self.menubar.addAction(self.menuProfile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.Listings_Button.setText(_translate("MainWindow", "BACK TO LISTINGS", None))
        self.profile_lbl.setText(_translate("MainWindow", "Profile", None))
        self.edit_btn.setText(_translate("MainWindow", "Edit Profile", None))
        self.menuProfile.setTitle(_translate("MainWindow", "Profile", None))
        self.actionView_your_profile.setText(_translate("MainWindow", "View your profile", None))
        self.actionSettings.setText(_translate("MainWindow", "Settings", None))
        self.actionLog_out.setText(_translate("MainWindow", "Log out", None))

    def edit_profile(self):
        MainWindow.close()
        import os
        os.system("python profile_editor.py")

    def go_to_listings(self):
        MainWindow.close()
        import os
        os.system("python listings_page.py")

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

