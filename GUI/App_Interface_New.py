# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'App_InterfacerMuIAQ.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoginInterface.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


#from curses import ERR
#from pickle import TRUE
#from tkinter import Button



from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import *
import sys
import os
import subprocess
from os import *




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(700, 900)
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(40, 20, 581, 929))
        self.widget.setStyleSheet(u"QPushButton#pushButton{\n"
"	background-color: qlinegradient(spread:pad, x1:0, y1:0,505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
"	color:rgba(255, 255, 255, 210);\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton#pushButton:hover{\n"
"	background-color: qlinegradient(spread:pad, x1:0, y1:0,505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
"}\n"
"QPushButton#pushButton:pressed{\n"
"	padding-left:5px;\n"
"	padding:top;\n"
"	background-color:rgba(105, 118, 132, 200);\n"
"}\n"
"QPushButton#pushButton_2, #pushButton_3, #pushButton_4, #pushButton_6, #pushButton_7{\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"	color:rgba(85, 98, 112, 255);\n"
"}\n"
"QPushButton#pushButton_2:hover, #pushButton_3:hover, #pushButton_4:hover, #pushButton_6:hover, #pushButton_7:hover{\n"
"	color: rgba(155, 168, 182, 200);\n"
"}\n"
"QPushButton#pushButton_2:pressed, #pushButton_3:pressed, #pushButton_4:pressed, #pushButton_6:pressed, #pushButton_7:pressed{\n"
""
                        "	padding-left:5px;\n"
"	padding:top;\n"
"	background-color:rgba(115, 128, 142, 255);\n"
"}")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 40, 500, 780))
        self.label.setStyleSheet(u"border-image: url(7f631e577ed5e5ffbbce726f8ec03489.jpg);\n"
"border-radius:20px;\n"
"")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 20, 530, 820))
        self.label_2.setStyleSheet(u"background-color: qlinegradient(spread:pad, x1:0, y1:0, x2:0, y2:0.715909, stop:0rgba(0, 0, 0, 9), stop:0.375 rgba(0, 0, 0, 50), stop:0.835227 rgba(0, 0, 0, 75));\n"
"border-radius:20px;\n"
"")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(70, 70, 440, 720))
        self.label_3.setStyleSheet(u"background: rgba(0,0,0,100);\n"
"border-radius : 15px")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(175, 85, 241, 51))
        font = QFont()
        font.setFamily(u"Corbel")
        font.setPointSize(27)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"border-image: url(Screenshot_2023-09-28_at_7.44.17_PM-removebg.png);\n"
"border-radius:20px;\n"
"")
        self.label_4.setTextFormat(Qt.PlainText)
        self.label_4.setScaledContents(False)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(150, 310, 288, 32))
        font1 = QFont()
        font1.setFamily(u"Corbel")
        font1.setPointSize(15)
        font1.setBold(True)
        font1.setWeight(75)
        self.pushButton.setFont(font1)
        self.pushButton.setStyleSheet(u"QPushButton#pushButton{\n"
"	background-color: qlineargradient(spread:pad, x1:0.364, y1:1, x2:1, y2:1, stop:0 rgba(0, 71, 120, 255), stop:1 rgba(0, 41, 69, 255));\n"
"	color:rgba(255, 255, 255, 210);\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton#pushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0.364, y1:1, x2:1, y2:1, stop:0 rgba(0, 91, 140, 255), stop:1 rgba(0, 61, 89, 255));\n"
"}\n"
"QPushButton#pushButton:pressed{\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	background-color:rgba(65, 75, 116, 200);\n"
"}\n"   
"")
        self.pushButton_5 = QPushButton(self.widget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(150, 570, 288, 32))
        self.pushButton_5.setFont(font1)
        self.pushButton_5.setStyleSheet(u"QPushButton#pushButton_5{\n"
"	background-color: qlineargradient(spread:pad, x1:0.364, y1:1, x2:1, y2:1, stop:0 rgba(0, 71, 120, 255), stop:1 rgba(0, 41, 69, 255));\n"
"	color:rgba(255, 255, 255, 210);\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton#pushButton_5:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0.364, y1:1, x2:1, y2:1, stop:0 rgba(0, 91, 140, 255), stop:1 rgba(0, 61, 89, 255));\n"
"}\n"
"QPushButton#pushButton_5:pressed{\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	background-color:rgba(0, 56, 94, 200);\n"
"}\n"
"")
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(170, 390, 251, 40))
        font2 = QFont()
        font2.setFamily(u"Corbel")
        font2.setPointSize(14)
        self.label_5.setFont(font2)
        self.label_5.setStyleSheet(u"color:rgba(255, 255, 255, 210);\n"
"")
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(80, 440, 421, 40))
        self.label_6.setFont(font2)
        self.label_6.setStyleSheet(u"color:rgba(255, 255, 255, 210);\n"
"")
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(70, 480, 441, 40))
        self.label_7.setFont(font2)
        self.label_7.setStyleSheet(u"color:rgba(255, 255, 255, 210);\n"
"")
        self.label_7.setAlignment(Qt.AlignCenter)
        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(80, 90, 61, 51))
        self.pushButton_3 = QPushButton(self.widget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(470, 95, 31, 40))
        font3 = QFont()
        font3.setFamily(u"Corbel")
        font3.setPointSize(26)
        font3.setBold(True)
        font3.setWeight(75)
        self.pushButton_3.setFont(font3)
        self.pushButton_4 = QPushButton(self.widget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(100, 700, 381, 23))
        font4 = QFont()
        font4.setFamily(u"Corbel")
        font4.setPointSize(15)
        self.pushButton_4.setFont(font4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 700, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        #self.pushButton_2.setIconSize(10,10)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.label_2.setText("")
        self.label_3.setText("")
        self.label_4.setText("")
        #self.label_4.setWindowIcon(QIcon('Screenshot_2023-09-28_at_7.44.17_PM-removebg.png'))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Air Quality Index", None))
        self.pushButton.clicked.connect(self.con_aqi)
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Water Quality Index", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\"There is divinity in the clouds\"", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\"Climate is what we expect, weather is what we get\"", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\"To walk into nature is to witness a thousand miracles\"", None))
        #self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_2.setIcon(QIcon('588a64fed06f6719692a2d14.png'))
        self.pushButton_2.setIconSize(QSize(30,30))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"HYPERLINK ", None))
        self.pushButton_3.clicked.connect(QCoreApplication.instance().quit)
        self.pushButton_5.clicked.connect(self.con_wqi)
        #self.pushButton.clicked.connect(subprocess.call("AQI_Interface_Part1", shell = True))
        #self.pushButton.clicked.connect(self.con_aqi())
        #self.pushButton.clicked.connect(QCoreApplication.instance().quit)
        
    def con_aqi(self):
        p = subprocess.call("python AQI_Interface_Part1.py 1", shell = True)
        #sys.exit(app.exec_())

    def con_wqi(self):
        p = subprocess.call("python WQI_Interface.py 1", shell = True)



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

