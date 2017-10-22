# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'profile_editor.ui'
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
        MainWindow.resize(1111, 937)
        MainWindow.setLayoutDirection(QtCore.Qt.RightToLeft)
        MainWindow.setStyleSheet(_fromUtf8("color: rgb(255, 34, 34);\n"
"background-color: rgb(0, 0, 0);"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.Banner = QtGui.QLabel(self.centralwidget)
        self.Banner.setGeometry(QtCore.QRect(0, 0, 1281, 141))
        self.Banner.setText(_fromUtf8(""))
        self.Banner.setPixmap(QtGui.QPixmap(_fromUtf8("banner.png")))
        self.Banner.setObjectName(_fromUtf8("Banner"))
        self.Date_of_Birth_ID = QtGui.QDateEdit(self.centralwidget)
        self.Date_of_Birth_ID.setGeometry(QtCore.QRect(430, 210, 341, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Date_of_Birth_ID.setFont(font)
        self.Date_of_Birth_ID.setWhatsThis(_fromUtf8(""))
        self.Date_of_Birth_ID.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Date_of_Birth_ID.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.Date_of_Birth_ID.setMaximumDateTime(QtCore.QDateTime(QtCore.QDate(2015, 12, 31), QtCore.QTime(23, 59, 59)))
        self.Date_of_Birth_ID.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(1950, 9, 14), QtCore.QTime(0, 0, 0)))
        self.Date_of_Birth_ID.setObjectName(_fromUtf8("Date_of_Birth_ID"))
        self.Date_of_Birth_Label = QtGui.QLabel(self.centralwidget)
        self.Date_of_Birth_Label.setGeometry(QtCore.QRect(180, 210, 240, 90))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Date_of_Birth_Label.setFont(font)
        self.Date_of_Birth_Label.setObjectName(_fromUtf8("Date_of_Birth_Label"))
        self.Location_Label = QtGui.QLabel(self.centralwidget)
        self.Location_Label.setGeometry(QtCore.QRect(270, 330, 151, 90))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Location_Label.setFont(font)
        self.Location_Label.setObjectName(_fromUtf8("Location_Label"))
        self.Locaion_ID = QtGui.QLineEdit(self.centralwidget)
        self.Locaion_ID.setGeometry(QtCore.QRect(430, 330, 340, 90))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Locaion_ID.setFont(font)
        self.Locaion_ID.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.Locaion_ID.setObjectName(_fromUtf8("Locaion_ID"))
        self.First_Name_Label = QtGui.QLabel(self.centralwidget)
        self.First_Name_Label.setGeometry(QtCore.QRect(220, 450, 200, 90))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.First_Name_Label.setFont(font)
        self.First_Name_Label.setObjectName(_fromUtf8("First_Name_Label"))
        self.First_Name_ID = QtGui.QLineEdit(self.centralwidget)
        self.First_Name_ID.setGeometry(QtCore.QRect(430, 450, 340, 90))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.First_Name_ID.setFont(font)
        self.First_Name_ID.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.First_Name_ID.setObjectName(_fromUtf8("First_Name_ID"))
        self.Last_Name_Label = QtGui.QLabel(self.centralwidget)
        self.Last_Name_Label.setGeometry(QtCore.QRect(220, 570, 200, 90))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Last_Name_Label.setFont(font)
        self.Last_Name_Label.setObjectName(_fromUtf8("Last_Name_Label"))
        self.Last_Name_ID = QtGui.QLineEdit(self.centralwidget)
        self.Last_Name_ID.setGeometry(QtCore.QRect(430, 570, 340, 90))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Last_Name_ID.setFont(font)
        self.Last_Name_ID.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.Last_Name_ID.setObjectName(_fromUtf8("Last_Name_ID"))
        self.Messenger_Link_Label = QtGui.QLabel(self.centralwidget)
        self.Messenger_Link_Label.setGeometry(QtCore.QRect(270, 690, 151, 90))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Messenger_Link_Label.setFont(font)
        self.Messenger_Link_Label.setObjectName(_fromUtf8("Messenger_Link_Label"))
        self.Messenger_Link_ID = QtGui.QLineEdit(self.centralwidget)
        self.Messenger_Link_ID.setGeometry(QtCore.QRect(430, 690, 340, 90))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Messenger_Link_ID.setFont(font)
        self.Messenger_Link_ID.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.Messenger_Link_ID.setObjectName(_fromUtf8("Messenger_Link_ID"))
        self.Update_All_Button = QtGui.QCommandLinkButton(self.centralwidget)
        self.Update_All_Button.setGeometry(QtCore.QRect(790, 690, 168, 90))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.Update_All_Button.setFont(font)
        self.Update_All_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Update_All_Button.setStyleSheet(_fromUtf8("background-color: rgb(255, 34, 34);\n"
"color: rgb(255, 255, 255);"))
        self.Update_All_Button.setObjectName(_fromUtf8("Update_All_Button"))
        self.Update_All_Button.clicked.connect(self.Update_All_Fun)
        self.Return_Profile_ID = QtGui.QPushButton(self.centralwidget)
        self.Return_Profile_ID.setGeometry(QtCore.QRect(270, 810, 500, 80))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Return_Profile_ID.setFont(font)
        self.Return_Profile_ID.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 34, 34);"))
        self.Return_Profile_ID.setObjectName(_fromUtf8("Return_Profile_ID"))
        self.Return_Profile_ID.clicked.connect(self.Return_Profile_Fun)
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
        self.menuProfile.addAction(self.actionView_your_profile)
        self.menuProfile.addAction(self.actionSettings)
        self.menuProfile.addAction(self.actionLog_out)
        self.menubar.addAction(self.menuProfile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.Date_of_Birth_ID.setDisplayFormat(_translate("MainWindow", "dd/MM/yyyy", None))
        self.Date_of_Birth_Label.setText(_translate("MainWindow", "Date of Birth", None))
        self.Location_Label.setText(_translate("MainWindow", "Location", None))
        self.First_Name_Label.setText(_translate("MainWindow", "First Name", None))
        self.Last_Name_Label.setText(_translate("MainWindow", "Last Name", None))
        self.Messenger_Link_Label.setText(_translate("MainWindow", "Messenger Link", None))
        self.Update_All_Button.setText(_translate("MainWindow", "Update All", None))
        self.Return_Profile_ID.setText(_translate("MainWindow", "Return to Profile", None))
        self.menuProfile.setTitle(_translate("MainWindow", "Profile", None))
        self.actionView_your_profile.setText(_translate("MainWindow", "View your profile", None))
        self.actionSettings.setText(_translate("MainWindow", "Settings", None))
        self.actionLog_out.setText(_translate("MainWindow", "Log out", None))


    def Return_Profile_Fun(self):
        MainWindow.close()
        import os
        os.system("python profile_manager.py")
        
    def Update_All_Fun(self):
        MainWindow.close()

        File = open("Current_Username.txt","r")
        username = File.readline()
        

        Name = ""
        FirstName = self.First_Name_ID.text()
        LastName = self.Last_Name_ID.text()
        Location = self.Locaion_ID.text()
        Link = self.Messenger_Link_ID.text()


        if FirstName != "" and LastName != "":
            Name = (str(FirstName) + " " + str(LastName))                            



        dtbs = open("Database.txt","r")
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
                break
            else:
                list2.append(line)
            pos += 1
        dtbs.close()
        
        if Name != "":
            list1[2] = Name
        if Location != "":
            list1[6] = Location
        if Link != "":
            list1[7] = Link

        dtbs = open("Database.txt", "w")

        dtbs.writelines(list2)
        
        for i in range(8):
            if i == 0:
                dtbs.write("@" + list1[i] + "\n")
            else:
                dtbs.write(list1[i] + "\n")
        dtbs.close()

        MainWindow.close()
        import os
        os.system("python profile_manager.py")



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

