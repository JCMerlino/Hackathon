# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'listings_page.ui'
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
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1281, 141))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("banner.png")))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(360, 220, 341, 41))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.dateEdit = QtGui.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(30, 230, 131, 31))
        self.dateEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.dateEdit.setCalendarPopup(False)
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 290, 101, 91))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 410, 101, 91))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 530, 101, 91))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 650, 101, 91))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.plainTextEdit = QtGui.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(183, 290, 521, 91))
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.plainTextEdit_2 = QtGui.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(180, 410, 521, 91))
        self.plainTextEdit_2.setObjectName(_fromUtf8("plainTextEdit_2"))
        self.plainTextEdit_3 = QtGui.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_3.setGeometry(QtCore.QRect(180, 530, 521, 91))
        self.plainTextEdit_3.setObjectName(_fromUtf8("plainTextEdit_3"))
        self.plainTextEdit_4 = QtGui.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_4.setGeometry(QtCore.QRect(180, 640, 521, 91))
        self.plainTextEdit_4.setObjectName(_fromUtf8("plainTextEdit_4"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1111, 26))
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
        self.pushButton.setText(_translate("MainWindow", "Post Listing", None))
        self.dateEdit.setDisplayFormat(_translate("MainWindow", "yyyy/M/d", None))
        self.label_2.setText(_translate("MainWindow", "picture1", None))
        self.label_3.setText(_translate("MainWindow", "picture2", None))
        self.label_4.setText(_translate("MainWindow", "picture3", None))
        self.label_5.setText(_translate("MainWindow", "picture4", None))
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