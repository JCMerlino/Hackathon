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
        MainWindow.resize(1280, 860)
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
        self.Edit_profile_Button = QtGui.QPushButton(self.centralwidget)
        self.Edit_profile_Button.setGeometry(QtCore.QRect(430, 210, 390, 101))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("OCR A Std"))
        font.setBold(True)
        font.setWeight(75)
        self.Edit_profile_Button.setFont(font)
        self.Edit_profile_Button.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.Edit_profile_Button.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.Edit_profile_Button.setObjectName(_fromUtf8("Edit_profile_Button"))
        self.Your_Listings_Button = QtGui.QPushButton(self.centralwidget)
        self.Your_Listings_Button.setGeometry(QtCore.QRect(120, 390, 381, 101))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("OCR A Std"))
        font.setBold(True)
        font.setWeight(75)
        self.Your_Listings_Button.setFont(font)
        self.Your_Listings_Button.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.Your_Listings_Button.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.Your_Listings_Button.setObjectName(_fromUtf8("Your_Listings_Button"))
        self.Post_Listing_Button = QtGui.QPushButton(self.centralwidget)
        self.Post_Listing_Button.setGeometry(QtCore.QRect(720, 390, 381, 101))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("OCR A Std"))
        font.setBold(True)
        font.setWeight(75)
        self.Post_Listing_Button.setFont(font)
        self.Post_Listing_Button.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.Post_Listing_Button.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.Post_Listing_Button.setObjectName(_fromUtf8("Post_Listing_Button"))
        self.View_Events_Button = QtGui.QPushButton(self.centralwidget)
        self.View_Events_Button.setGeometry(QtCore.QRect(720, 530, 381, 101))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("OCR A Std"))
        font.setBold(True)
        font.setWeight(75)
        self.View_Events_Button.setFont(font)
        self.View_Events_Button.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.View_Events_Button.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.View_Events_Button.setObjectName(_fromUtf8("View_Events_Button"))
        self.Manage_Listings_Button = QtGui.QPushButton(self.centralwidget)
        self.Manage_Listings_Button.setGeometry(QtCore.QRect(120, 530, 381, 101))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("OCR A Std"))
        font.setBold(True)
        font.setWeight(75)
        self.Manage_Listings_Button.setFont(font)
        self.Manage_Listings_Button.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.Manage_Listings_Button.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.Manage_Listings_Button.setObjectName(_fromUtf8("Manage_Listings_Button"))
        self.Listings_Button = QtGui.QPushButton(self.centralwidget)
        self.Listings_Button.setGeometry(QtCore.QRect(120, 680, 990, 100))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("OCR A Std"))
        font.setBold(True)
        font.setWeight(75)
        self.Listings_Button.setFont(font)
        self.Listings_Button.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.Listings_Button.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.Listings_Button.setObjectName(_fromUtf8("Listings_Button"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 31))
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
        self.menuProfile.addAction(self.actionView_your_profile)
        self.menuProfile.addAction(self.actionSettings)
        self.menuProfile.addAction(self.actionLog_out)
        self.menubar.addAction(self.menuProfile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.Edit_profile_Button.setText(_translate("MainWindow", "EDIT PROFILE", None))
        self.Your_Listings_Button.setText(_translate("MainWindow", "YOUR LISTINGS", None))
        self.Post_Listing_Button.setText(_translate("MainWindow", "POST A LISTING", None))
        self.View_Events_Button.setText(_translate("MainWindow", "VIEW YOUR EVENTS", None))
        self.Manage_Listings_Button.setText(_translate("MainWindow", "MANAGE LISTINGS", None))
        self.Listings_Button.setText(_translate("MainWindow", "BACK TO LISTINGS", None))
        self.menuProfile.setTitle(_translate("MainWindow", "Profile", None))
        self.actionView_your_profile.setText(_translate("MainWindow", "View your profile", None))
        self.actionSettings.setText(_translate("MainWindow", "Settings", None))
        self.actionLog_out.setText(_translate("MainWindow", "Log out", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

