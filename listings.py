# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'listings.ui'
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

class listings_cl(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1111, 860)
        MainWindow.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, -10, 1281, 141))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("banner.png")))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(420, 700, 211, 51))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 260, 1061, 141))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(12, 15, 101, 111))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lineEdit = QtGui.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(170, 20, 791, 101))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButton_2 = QtGui.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(970, 30, 81, 28))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(970, 70, 81, 28))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.frame_2 = QtGui.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(30, 470, 1061, 131))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.label_3 = QtGui.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(12, 15, 101, 101))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEdit_2 = QtGui.QLineEdit(self.frame_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(170, 21, 791, 91))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.pushButton_4 = QtGui.QPushButton(self.frame_2)
        self.pushButton_4.setGeometry(QtCore.QRect(970, 30, 81, 28))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_5 = QtGui.QPushButton(self.frame_2)
        self.pushButton_5.setGeometry(QtCore.QRect(970, 70, 81, 28))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(500, 160, 191, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_4.setTextFormat(QtCore.Qt.RichText)
        self.label_4.setObjectName(_fromUtf8("label_4"))
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
        self.pushButton.setText(_translate("MainWindow", "Back to the hub.", None))
        self.label_2.setText(_translate("MainWindow", "picture1", None))
        self.pushButton_2.setText(_translate("MainWindow", "Edit", None))
        self.pushButton_3.setText(_translate("MainWindow", "Delete", None))
        self.label_3.setText(_translate("MainWindow", "picture2", None))
        self.pushButton_4.setText(_translate("MainWindow", "Edit", None))
        self.pushButton_5.setText(_translate("MainWindow", "Delete", None))
        self.label_4.setText(_translate("MainWindow", "Your Listings", None))
        self.menuProfile.setTitle(_translate("MainWindow", "Profile", None))
        self.actionView_your_profile.setText(_translate("MainWindow", "View your profile", None))
        self.actionSettings.setText(_translate("MainWindow", "Settings", None))
        self.actionLog_out.setText(_translate("MainWindow", "Log out", None))

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = listings_cl()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
