# -*- coding: UTF-8 -*-
# Copyright July 2017 Ramon Vila Ferreres <ramonvilafer@gmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import math
import sys
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui, uic
from PyQt4.QtGui import QListWidget, QListWidgetItem, QApplication, QDialog

#GUI generated from UI file with pyuic4

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
        MainWindow.setObjectName(_fromUtf8("Lineally"))
        MainWindow.resize(831, 460)
        MainWindow.setFixedSize(831, 460)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 811, 421))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        font.setPointSize(28)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.buttonClean = QtGui.QPushButton(self.groupBox)
        self.buttonClean.setGeometry(QtCore.QRect(700, 380, 91, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(14)
        self.buttonClean.setFont(font)
        self.buttonClean.setObjectName(_fromUtf8("buttonClean"))
        self.buttonGenerate = QtGui.QPushButton(self.groupBox)
        self.buttonGenerate.setGeometry(QtCore.QRect(600, 380, 91, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(14)
        self.buttonGenerate.setFont(font)
        self.buttonGenerate.setObjectName(_fromUtf8("buttonGenerate"))
        self.groupBox_2 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 40, 281, 361))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.groupBox_4 = QtGui.QGroupBox(self.groupBox_2)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 40, 261, 141))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.label = QtGui.QLabel(self.groupBox_4)
        self.label.setGeometry(QtCore.QRect(20, 40, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.groupBox_4)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pointX = QtGui.QTextEdit(self.groupBox_4)
        self.pointX.setGeometry(QtCore.QRect(140, 30, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setKerning(True)
        self.pointX.setFont(font)
        self.pointX.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.pointX.setAcceptDrops(True)
        self.pointX.setFrameShape(QtGui.QFrame.NoFrame)
        self.pointX.setObjectName(_fromUtf8("pointX"))
        self.pointY = QtGui.QTextEdit(self.groupBox_4)
        self.pointY.setGeometry(QtCore.QRect(140, 80, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setKerning(True)
        self.pointY.setFont(font)
        self.pointY.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.pointY.setAcceptDrops(True)
        self.pointY.setFrameShape(QtGui.QFrame.NoFrame)
        self.pointY.setObjectName(_fromUtf8("pointY"))
        self.groupBox_5 = QtGui.QGroupBox(self.groupBox_2)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 190, 261, 141))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.label_3 = QtGui.QLabel(self.groupBox_5)
        self.label_3.setGeometry(QtCore.QRect(20, 40, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.groupBox_5)
        self.label_4.setGeometry(QtCore.QRect(20, 90, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.vectorX = QtGui.QTextEdit(self.groupBox_5)
        self.vectorX.setGeometry(QtCore.QRect(140, 30, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setKerning(True)
        self.vectorX.setFont(font)
        self.vectorX.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.vectorX.setAcceptDrops(True)
        self.vectorX.setFrameShape(QtGui.QFrame.NoFrame)
        self.vectorX.setObjectName(_fromUtf8("vectorX"))
        self.vectorY = QtGui.QTextEdit(self.groupBox_5)
        self.vectorY.setGeometry(QtCore.QRect(140, 80, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setKerning(True)
        self.vectorY.setFont(font)
        self.vectorY.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.vectorY.setAcceptDrops(True)
        self.vectorY.setFrameShape(QtGui.QFrame.NoFrame)
        self.vectorY.setObjectName(_fromUtf8("vectorY"))
        self.groupBox_3 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_3.setGeometry(QtCore.QRect(300, 40, 501, 331))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.label_6 = QtGui.QLabel(self.groupBox_3)
        self.label_6.setGeometry(QtCore.QRect(10, 80, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.groupBox_3)
        self.label_7.setGeometry(QtCore.QRect(10, 30, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.groupBox_3)
        self.label_8.setGeometry(QtCore.QRect(10, 130, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(self.groupBox_3)
        self.label_9.setGeometry(QtCore.QRect(10, 180, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(self.groupBox_3)
        self.label_10.setGeometry(QtCore.QRect(10, 230, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_5 = QtGui.QLabel(self.groupBox_3)
        self.label_5.setGeometry(QtCore.QRect(10, 280, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.ptopte = QtGui.QTextEdit(self.groupBox_3)
        self.ptopte.setGeometry(QtCore.QRect(80, 30, 411, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setKerning(True)
        self.ptopte.setFont(font)
        self.ptopte.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.ptopte.setAcceptDrops(True)
        self.ptopte.setFrameShape(QtGui.QFrame.NoFrame)
        self.ptopte.setObjectName(_fromUtf8("ptopte"))
        self.vectorial = QtGui.QTextEdit(self.groupBox_3)
        self.vectorial.setGeometry(QtCore.QRect(80, 80, 411, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setKerning(True)
        self.vectorial.setFont(font)
        self.vectorial.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.vectorial.setAcceptDrops(True)
        self.vectorial.setFrameShape(QtGui.QFrame.NoFrame)
        self.vectorial.setObjectName(_fromUtf8("vectorial"))
        self.cont = QtGui.QTextEdit(self.groupBox_3)
        self.cont.setGeometry(QtCore.QRect(80, 130, 411, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setKerning(True)
        self.cont.setFont(font)
        self.cont.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.cont.setAcceptDrops(True)
        self.cont.setFrameShape(QtGui.QFrame.NoFrame)
        self.cont.setObjectName(_fromUtf8("cont"))
        self.expl = QtGui.QTextEdit(self.groupBox_3)
        self.expl.setGeometry(QtCore.QRect(80, 180, 411, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setKerning(True)
        self.expl.setFont(font)
        self.expl.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.expl.setAcceptDrops(True)
        self.expl.setFrameShape(QtGui.QFrame.NoFrame)
        self.expl.setObjectName(_fromUtf8("expl"))
        self.general = QtGui.QTextEdit(self.groupBox_3)
        self.general.setGeometry(QtCore.QRect(80, 230, 411, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setKerning(True)
        self.general.setFont(font)
        self.general.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.general.setAcceptDrops(True)
        self.general.setFrameShape(QtGui.QFrame.NoFrame)
        self.general.setObjectName(_fromUtf8("general"))
        self.paramX = QtGui.QTextEdit(self.groupBox_3)
        self.paramX.setGeometry(QtCore.QRect(100, 280, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setKerning(True)
        self.paramX.setFont(font)
        self.paramX.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.paramX.setAcceptDrops(True)
        self.paramX.setFrameShape(QtGui.QFrame.NoFrame)
        self.paramX.setObjectName(_fromUtf8("paramX"))
        self.label_11 = QtGui.QLabel(self.groupBox_3)
        self.label_11.setGeometry(QtCore.QRect(80, 280, 21, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_11.setFont(font)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.paramY = QtGui.QTextEdit(self.groupBox_3)
        self.paramY.setGeometry(QtCore.QRect(310, 280, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setKerning(True)
        self.paramY.setFont(font)
        self.paramY.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.paramY.setAcceptDrops(True)
        self.paramY.setFrameShape(QtGui.QFrame.NoFrame)
        self.paramY.setObjectName(_fromUtf8("paramY"))
        self.label_12 = QtGui.QLabel(self.groupBox_3)
        self.label_12.setGeometry(QtCore.QRect(290, 280, 21, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_12.setFont(font)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.buttonExit = QtGui.QPushButton(self.groupBox)
        self.buttonExit.setGeometry(QtCore.QRect(500, 380, 91, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(14)
        self.buttonExit.setFont(font)
        self.buttonExit.setObjectName(_fromUtf8("buttonExit"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 831, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Lineally", None))
        self.groupBox.setTitle(_translate("MainWindow", "Straight Line Equations", None))
        self.buttonClean.setText(_translate("MainWindow", "Clean", None))
        self.buttonGenerate.setText(_translate("MainWindow", "Generate!", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Point & Vector", None))
        self.groupBox_4.setTitle(_translate("MainWindow", "Point", None))
        self.label.setText(_translate("MainWindow", "X Coordinate", None))
        self.label_2.setText(_translate("MainWindow", "Y Coordinate", None))
        self.pointX.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial Narrow\'; font-size:17pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.pointY.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial Narrow\'; font-size:17pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.groupBox_5.setTitle(_translate("MainWindow", "Vector", None))
        self.label_3.setText(_translate("MainWindow", "X Coordinate", None))
        self.label_4.setText(_translate("MainWindow", "Y Coordinate", None))
        self.vectorX.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial Narrow\'; font-size:17pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.vectorY.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial Narrow\'; font-size:17pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "Equations", None))
        self.label_6.setText(_translate("MainWindow", "Vectorial", None))
        self.label_7.setText(_translate("MainWindow", "Pt - Slpe", None))
        self.label_8.setText(_translate("MainWindow", "Continue", None))
        self.label_9.setText(_translate("MainWindow", "Explicit", None))
        self.label_10.setText(_translate("MainWindow", "General", None))
        self.label_5.setText(_translate("MainWindow", "Param.", None))
        self.ptopte.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial Narrow\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.vectorial.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial Narrow\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.cont.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial Narrow\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.expl.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial Narrow\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.general.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial Narrow\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.paramX.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial Narrow\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_11.setText(_translate("MainWindow", "X", None))
        self.paramY.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial Narrow\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_12.setText(_translate("MainWindow", "Y", None))
        self.buttonExit.setText(_translate("MainWindow", "Salir", None))

#--------------------------------------------------------------------------

class MainWindow(QtGui.QMainWindow, Ui_MainWindow, object):

 def __init__(self, parent = None):

  #---------------------------EXECUTED-AT-START----------------------------------

  QtGui.QMainWindow.__init__(self, parent) #Creates the main window

  self.setupUi(self) # Starts main GUI
  # Widget interactions

  self.buttonExit.clicked.connect(self.exit)
  self.buttonGenerate.clicked.connect(self.getData)
  self.buttonClean.clicked.connect(self.clean)

 def exit(self):
    self.close()

 def clean(self):
    self.vectorial.clear()
    self.paramX.clear()
    self.paramY.clear()
    self.cont.clear()
    self.ptopte.clear()
    self.expl.clear()
    self.general.clear()
    self.pointX.clear()
    self.pointY.clear()
    self.vectorX.clear()
    self.vectorY.clear()

 def cleanTextEditOnly(self):
    self.vectorial.clear()
    self.paramX.clear()
    self.paramY.clear()
    self.cont.clear()
    self.ptopte.clear()
    self.expl.clear()
    self.general.clear()

 def getData(self): #Extracts data from QtTextEdit
    self.ptoX = int(self.pointX.toPlainText())
    self.ptoY = int(self.pointY.toPlainText())
    self.vctX = int(self.vectorX.toPlainText())
    self.vctY = int(self.vectorY.toPlainText())
    print (self.ptoX,self.ptoY,self.vctX,self.vctY)
    self.computeEquations(self.ptoX,self.ptoY,self.vctX,self.vctY)


 def computeEquations(self,poitX,poitY,vectrX,vectrY):
    self.results = [] #Every generated equation will be stored here

    #String version of data, to be used in the TextEdit to show the final equations
    self.vectorYstr = str(vectrY)
    self.vectorXstr = str(vectrX)
    self.pointXstr = str(poitX)
    self.pointYstr = str(poitY)

    #Ugly stuff, needed to make some calculations
    self.z = int((vectrY * poitX))
    self.d = int((self.z * -1))
    self.dstr = str(self.d)
    self.k = int(self.z/vectrX)
    self.n = str(poitY - self.k)

    #Magic happens here, all the calculations are perfomed here
    self.results.append("(x,y)=(" + self.pointXstr + self.pointYstr + ")+t *(" + self.vectorXstr + "," + self.vectorYstr + ")")               #Ecuacion vectorial
    self.results.append([(self.pointXstr + " +" + self.vectorXstr + "t"),(self.pointYstr + " +" + self.vectorYstr + "t")])                    #Ecuacion parametrica
    self.results.append("(x-" + self.pointXstr + ")" + "/" + self.vectorXstr + " = " + "(y-" + self.pointYstr + ")" + "/" + self.vectorYstr)  #Ecuacion continua
    self.results.append("y-" + self.pointYstr + " = " + self.vectorYstr + "/" + self.vectorXstr + "(x-" + self.pointXstr + ")")               #Ecuacion punto-pendiente
    self.results.append("y = " + self.vectorYstr + "/" + self.vectorXstr + "x +" + self.n)                           #Ecuacion explicita
    self.results.append(-1 * self.vectorYstr + "x" + "+" + self.vectorXstr + "y" + "+" + self.dstr + "=0")           #Ecuacion general
    self.showData(self.results)

 def showData(self,listOfData): #Just shows the computed equations in the QtTextEdit

    self.cleanTextEditOnly()
    self.vectorial.insertPlainText(str(listOfData[0]))
    self.paramX.insertPlainText(str(listOfData[1][0]))
    self.paramY.insertPlainText(str(listOfData[1][1]))
    self.cont.insertPlainText(str(listOfData[2]))
    self.ptopte.insertPlainText(str(listOfData[3]))
    self.expl.insertPlainText(str(listOfData[4]))
    self.general.insertPlainText(str(listOfData[5]))


app = QtGui.QApplication(sys.argv)
eq = MainWindow()
eq.show()
app.exec_()






