# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cabledrivenparallerobot.ui'
#
# Created: Wed May 25 09:13:14 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from saveparam import *

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

class Ui_CableDrivenParalleRobot(object):
    def setupUi(self, CableDrivenParalleRobot):
        CableDrivenParalleRobot.setObjectName(_fromUtf8("CableDrivenParalleRobot"))
        CableDrivenParalleRobot.resize(904, 682)
        self.centralWidget = QtGui.QWidget(CableDrivenParalleRobot)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.pushButton = QtGui.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(730, 536, 91, 21))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.centralWidget)
        self.pushButton_2.setGeometry(QtCore.QRect(710, 600, 131, 21))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label_16 = QtGui.QLabel(self.centralWidget)
        self.label_16.setGeometry(QtCore.QRect(470, 10, 131, 16))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.layoutWidget = QtGui.QWidget(self.centralWidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 30, 359, 318))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.anchorpoint1 = QtGui.QLineEdit(self.layoutWidget)
        self.anchorpoint1.setObjectName(_fromUtf8("anchorpoint1"))
        self.gridLayout.addWidget(self.anchorpoint1, 1, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.layoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.anchorpoint2 = QtGui.QLineEdit(self.layoutWidget)
        self.anchorpoint2.setObjectName(_fromUtf8("anchorpoint2"))
        self.gridLayout.addWidget(self.anchorpoint2, 2, 1, 1, 1)
        self.exitpoint2 = QtGui.QLineEdit(self.layoutWidget)
        self.exitpoint2.setObjectName(_fromUtf8("exitpoint2"))
        self.gridLayout.addWidget(self.exitpoint2, 2, 2, 1, 1)
        self.label_5 = QtGui.QLabel(self.layoutWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.anchorpoint3 = QtGui.QLineEdit(self.layoutWidget)
        self.anchorpoint3.setObjectName(_fromUtf8("anchorpoint3"))
        self.gridLayout.addWidget(self.anchorpoint3, 3, 1, 1, 1)
        self.label_12 = QtGui.QLabel(self.layoutWidget)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout.addWidget(self.label_12, 0, 0, 1, 1)
        self.exitpoint3 = QtGui.QLineEdit(self.layoutWidget)
        self.exitpoint3.setObjectName(_fromUtf8("exitpoint3"))
        self.gridLayout.addWidget(self.exitpoint3, 3, 2, 1, 1)
        self.exitpoint1 = QtGui.QLineEdit(self.layoutWidget)
        self.exitpoint1.setObjectName(_fromUtf8("exitpoint1"))
        self.gridLayout.addWidget(self.exitpoint1, 1, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 3)
        self.label_7 = QtGui.QLabel(self.layoutWidget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_2.addWidget(self.label_7, 1, 0, 1, 1)
        self.anchorpoint4 = QtGui.QLineEdit(self.layoutWidget)
        self.anchorpoint4.setObjectName(_fromUtf8("anchorpoint4"))
        self.gridLayout_2.addWidget(self.anchorpoint4, 1, 1, 1, 1)
        self.exitpoint4 = QtGui.QLineEdit(self.layoutWidget)
        self.exitpoint4.setObjectName(_fromUtf8("exitpoint4"))
        self.gridLayout_2.addWidget(self.exitpoint4, 1, 2, 1, 1)
        self.label_8 = QtGui.QLabel(self.layoutWidget)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_2.addWidget(self.label_8, 2, 0, 1, 1)
        self.anchorpoint5 = QtGui.QLineEdit(self.layoutWidget)
        self.anchorpoint5.setObjectName(_fromUtf8("anchorpoint5"))
        self.gridLayout_2.addWidget(self.anchorpoint5, 2, 1, 1, 1)
        self.exitpoint5 = QtGui.QLineEdit(self.layoutWidget)
        self.exitpoint5.setObjectName(_fromUtf8("exitpoint5"))
        self.gridLayout_2.addWidget(self.exitpoint5, 2, 2, 1, 1)
        self.label_9 = QtGui.QLabel(self.layoutWidget)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_2.addWidget(self.label_9, 3, 0, 1, 1)
        self.anchorpoint6 = QtGui.QLineEdit(self.layoutWidget)
        self.anchorpoint6.setObjectName(_fromUtf8("anchorpoint6"))
        self.gridLayout_2.addWidget(self.anchorpoint6, 3, 1, 1, 1)
        self.label_10 = QtGui.QLabel(self.layoutWidget)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_2.addWidget(self.label_10, 4, 0, 1, 1)
        self.anchorpoint7 = QtGui.QLineEdit(self.layoutWidget)
        self.anchorpoint7.setObjectName(_fromUtf8("anchorpoint7"))
        self.gridLayout_2.addWidget(self.anchorpoint7, 4, 1, 1, 1)
        self.exitpoint7 = QtGui.QLineEdit(self.layoutWidget)
        self.exitpoint7.setObjectName(_fromUtf8("exitpoint7"))
        self.gridLayout_2.addWidget(self.exitpoint7, 4, 2, 1, 1)
        self.label_11 = QtGui.QLabel(self.layoutWidget)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout_2.addWidget(self.label_11, 5, 0, 1, 1)
        self.exitpoint8 = QtGui.QLineEdit(self.layoutWidget)
        self.exitpoint8.setObjectName(_fromUtf8("exitpoint8"))
        self.gridLayout_2.addWidget(self.exitpoint8, 5, 2, 1, 1)
        self.anchorpoint8 = QtGui.QLineEdit(self.layoutWidget)
        self.anchorpoint8.setObjectName(_fromUtf8("anchorpoint8"))
        self.gridLayout_2.addWidget(self.anchorpoint8, 5, 1, 1, 1)
        self.exitpoint6 = QtGui.QLineEdit(self.layoutWidget)
        self.exitpoint6.setObjectName(_fromUtf8("exitpoint6"))
        self.gridLayout_2.addWidget(self.exitpoint6, 3, 2, 1, 1)
        self.layoutWidget1 = QtGui.QWidget(self.centralWidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(470, 30, 189, 29))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_17 = QtGui.QLabel(self.layoutWidget1)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.horizontalLayout_3.addWidget(self.label_17)
        self.CableMass = QtGui.QLineEdit(self.layoutWidget1)
        self.CableMass.setObjectName(_fromUtf8("CableMass"))
        self.horizontalLayout_3.addWidget(self.CableMass)
        self.layoutWidget2 = QtGui.QWidget(self.centralWidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(470, 60, 200, 29))
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_18 = QtGui.QLabel(self.layoutWidget2)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.horizontalLayout_4.addWidget(self.label_18)
        self.CableRadius = QtGui.QLineEdit(self.layoutWidget2)
        self.CableRadius.setObjectName(_fromUtf8("CableRadius"))
        self.horizontalLayout_4.addWidget(self.CableRadius)
        self.pushButton_3 = QtGui.QPushButton(self.centralWidget)
        self.pushButton_3.setGeometry(QtCore.QRect(710, 570, 131, 21))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.label_19 = QtGui.QLabel(self.centralWidget)
        self.label_19.setGeometry(QtCore.QRect(30, 470, 121, 17))
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.label_29 = QtGui.QLabel(self.centralWidget)
        self.label_29.setGeometry(QtCore.QRect(60, 0, 191, 17))
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.CableMass_3 = QtGui.QLineEdit(self.centralWidget)
        self.CableMass_3.setGeometry(QtCore.QRect(575, 756, 81, 27))
        self.CableMass_3.setObjectName(_fromUtf8("CableMass_3"))
        self.layoutWidget3 = QtGui.QWidget(self.centralWidget)
        self.layoutWidget3.setGeometry(QtCore.QRect(10, 490, 332, 118))
        self.layoutWidget3.setObjectName(_fromUtf8("layoutWidget3"))
        self.gridLayout_3 = QtGui.QGridLayout(self.layoutWidget3)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_24 = QtGui.QLabel(self.layoutWidget3)
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.gridLayout_3.addWidget(self.label_24, 1, 2, 1, 1)
        self.Inertialyy = QtGui.QLineEdit(self.layoutWidget3)
        self.Inertialyy.setObjectName(_fromUtf8("Inertialyy"))
        self.gridLayout_3.addWidget(self.Inertialyy, 1, 3, 1, 1)
        self.label_26 = QtGui.QLabel(self.layoutWidget3)
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.gridLayout_3.addWidget(self.label_26, 2, 0, 1, 1)
        self.Inertialyz = QtGui.QLineEdit(self.layoutWidget3)
        self.Inertialyz.setObjectName(_fromUtf8("Inertialyz"))
        self.gridLayout_3.addWidget(self.Inertialyz, 1, 5, 1, 1)
        self.label_27 = QtGui.QLabel(self.layoutWidget3)
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.gridLayout_3.addWidget(self.label_27, 2, 2, 1, 1)
        self.Inertialyz_2 = QtGui.QLineEdit(self.layoutWidget3)
        self.Inertialyz_2.setObjectName(_fromUtf8("Inertialyz_2"))
        self.gridLayout_3.addWidget(self.Inertialyz_2, 2, 3, 1, 1)
        self.label_25 = QtGui.QLabel(self.layoutWidget3)
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.gridLayout_3.addWidget(self.label_25, 2, 4, 1, 1)
        self.Inertialxy = QtGui.QLineEdit(self.layoutWidget3)
        self.Inertialxy.setObjectName(_fromUtf8("Inertialxy"))
        self.gridLayout_3.addWidget(self.Inertialxy, 0, 3, 1, 1)
        self.label_6 = QtGui.QLabel(self.layoutWidget3)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_3.addWidget(self.label_6, 0, 0, 1, 1)
        self.Inertialxx = QtGui.QLineEdit(self.layoutWidget3)
        self.Inertialxx.setObjectName(_fromUtf8("Inertialxx"))
        self.gridLayout_3.addWidget(self.Inertialxx, 0, 1, 1, 1)
        self.label_20 = QtGui.QLabel(self.layoutWidget3)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.gridLayout_3.addWidget(self.label_20, 0, 2, 1, 1)
        self.Inertialxz = QtGui.QLineEdit(self.layoutWidget3)
        self.Inertialxz.setObjectName(_fromUtf8("Inertialxz"))
        self.gridLayout_3.addWidget(self.Inertialxz, 0, 5, 1, 1)
        self.Inertialxy_2 = QtGui.QLineEdit(self.layoutWidget3)
        self.Inertialxy_2.setObjectName(_fromUtf8("Inertialxy_2"))
        self.gridLayout_3.addWidget(self.Inertialxy_2, 1, 1, 1, 1)
        self.label_21 = QtGui.QLabel(self.layoutWidget3)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.gridLayout_3.addWidget(self.label_21, 0, 4, 1, 1)
        self.label_22 = QtGui.QLabel(self.layoutWidget3)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.gridLayout_3.addWidget(self.label_22, 1, 4, 1, 1)
        self.Inertialxz_2 = QtGui.QLineEdit(self.layoutWidget3)
        self.Inertialxz_2.setObjectName(_fromUtf8("Inertialxz_2"))
        self.gridLayout_3.addWidget(self.Inertialxz_2, 2, 1, 1, 1)
        self.label_23 = QtGui.QLabel(self.layoutWidget3)
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.gridLayout_3.addWidget(self.label_23, 1, 0, 1, 1)
        self.Inertialzz = QtGui.QLineEdit(self.layoutWidget3)
        self.Inertialzz.setObjectName(_fromUtf8("Inertialzz"))
        self.gridLayout_3.addWidget(self.Inertialzz, 2, 5, 1, 1)
        self.layoutWidget4 = QtGui.QWidget(self.centralWidget)
        self.layoutWidget4.setGeometry(QtCore.QRect(30, 370, 306, 89))
        self.layoutWidget4.setObjectName(_fromUtf8("layoutWidget4"))
        self.gridLayout_4 = QtGui.QGridLayout(self.layoutWidget4)
        self.gridLayout_4.setMargin(0)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.label_28 = QtGui.QLabel(self.layoutWidget4)
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.gridLayout_4.addWidget(self.label_28, 2, 1, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_13 = QtGui.QLabel(self.layoutWidget4)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.horizontalLayout.addWidget(self.label_13)
        self.endeffMass = QtGui.QLineEdit(self.layoutWidget4)
        self.endeffMass.setObjectName(_fromUtf8("endeffMass"))
        self.horizontalLayout.addWidget(self.endeffMass)
        self.gridLayout_4.addLayout(self.horizontalLayout, 1, 0, 1, 2)
        self.endEffShape_2 = QtGui.QComboBox(self.layoutWidget4)
        self.endEffShape_2.setObjectName(_fromUtf8("endEffShape_2"))
        self.endEffShape_2.addItem(_fromUtf8(""))
        self.endEffShape_2.addItem(_fromUtf8(""))
        self.endEffShape_2.addItem(_fromUtf8(""))
        self.endEffShape_2.addItem(_fromUtf8(""))
        self.endEffShape_2.addItem(_fromUtf8(""))
        self.endEffShape_2.addItem(_fromUtf8(""))
        self.endEffShape_2.addItem(_fromUtf8(""))
        self.endEffShape_2.addItem(_fromUtf8(""))
        self.gridLayout_4.addWidget(self.endEffShape_2, 2, 2, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_14 = QtGui.QLabel(self.layoutWidget4)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.horizontalLayout_2.addWidget(self.label_14)
        self.endEffShape = QtGui.QComboBox(self.layoutWidget4)
        self.endEffShape.setObjectName(_fromUtf8("endEffShape"))
        self.endEffShape.addItem(_fromUtf8(""))
        self.endEffShape.addItem(_fromUtf8(""))
        self.horizontalLayout_2.addWidget(self.endEffShape)
        self.gridLayout_4.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
        self.label_15 = QtGui.QLabel(self.layoutWidget4)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.gridLayout_4.addWidget(self.label_15, 0, 0, 1, 1)
        self.layoutWidget5 = QtGui.QWidget(self.centralWidget)
        self.layoutWidget5.setGeometry(QtCore.QRect(350, 370, 252, 85))
        self.layoutWidget5.setObjectName(_fromUtf8("layoutWidget5"))
        self.gridLayout_6 = QtGui.QGridLayout(self.layoutWidget5)
        self.gridLayout_6.setMargin(0)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.label_31 = QtGui.QLabel(self.layoutWidget5)
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.gridLayout_6.addWidget(self.label_31, 0, 0, 1, 2)
        self.label_37 = QtGui.QLabel(self.layoutWidget5)
        self.label_37.setObjectName(_fromUtf8("label_37"))
        self.gridLayout_6.addWidget(self.label_37, 1, 0, 1, 1)
        self.label_30 = QtGui.QLabel(self.layoutWidget5)
        self.label_30.setObjectName(_fromUtf8("label_30"))
        self.gridLayout_6.addWidget(self.label_30, 2, 0, 1, 1)
        self.endeffRPY = QtGui.QLineEdit(self.layoutWidget5)
        self.endeffRPY.setObjectName(_fromUtf8("endeffRPY"))
        self.gridLayout_6.addWidget(self.endeffRPY, 2, 1, 1, 1)
        self.endeffPosition = QtGui.QLineEdit(self.layoutWidget5)
        self.endeffPosition.setObjectName(_fromUtf8("endeffPosition"))
        self.gridLayout_6.addWidget(self.endeffPosition, 1, 1, 1, 1)
        self.layoutWidget6 = QtGui.QWidget(self.centralWidget)
        self.layoutWidget6.setGeometry(QtCore.QRect(420, 140, 332, 159))
        self.layoutWidget6.setObjectName(_fromUtf8("layoutWidget6"))
        self.gridLayout_9 = QtGui.QGridLayout(self.layoutWidget6)
        self.gridLayout_9.setMargin(0)
        self.gridLayout_9.setObjectName(_fromUtf8("gridLayout_9"))
        self.gridLayout_7 = QtGui.QGridLayout()
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.endEffShape_5 = QtGui.QComboBox(self.layoutWidget6)
        self.endEffShape_5.setObjectName(_fromUtf8("endEffShape_5"))
        self.endEffShape_5.addItem(_fromUtf8(""))
        self.endEffShape_5.addItem(_fromUtf8(""))
        self.endEffShape_5.addItem(_fromUtf8(""))
        self.endEffShape_5.addItem(_fromUtf8(""))
        self.endEffShape_5.addItem(_fromUtf8(""))
        self.endEffShape_5.addItem(_fromUtf8(""))
        self.endEffShape_5.addItem(_fromUtf8(""))
        self.endEffShape_5.addItem(_fromUtf8(""))
        self.gridLayout_7.addWidget(self.endEffShape_5, 2, 2, 1, 1)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label_40 = QtGui.QLabel(self.layoutWidget6)
        self.label_40.setObjectName(_fromUtf8("label_40"))
        self.horizontalLayout_8.addWidget(self.label_40)
        self.endEffShape_6 = QtGui.QComboBox(self.layoutWidget6)
        self.endEffShape_6.setObjectName(_fromUtf8("endEffShape_6"))
        self.endEffShape_6.addItem(_fromUtf8(""))
        self.horizontalLayout_8.addWidget(self.endEffShape_6)
        self.gridLayout_7.addLayout(self.horizontalLayout_8, 2, 0, 1, 1)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_39 = QtGui.QLabel(self.layoutWidget6)
        self.label_39.setObjectName(_fromUtf8("label_39"))
        self.horizontalLayout_7.addWidget(self.label_39)
        self.endeffMass_3 = QtGui.QLineEdit(self.layoutWidget6)
        self.endeffMass_3.setObjectName(_fromUtf8("endeffMass_3"))
        self.horizontalLayout_7.addWidget(self.endeffMass_3)
        self.gridLayout_7.addLayout(self.horizontalLayout_7, 1, 0, 1, 2)
        self.label_38 = QtGui.QLabel(self.layoutWidget6)
        self.label_38.setObjectName(_fromUtf8("label_38"))
        self.gridLayout_7.addWidget(self.label_38, 2, 1, 1, 1)
        self.label_41 = QtGui.QLabel(self.layoutWidget6)
        self.label_41.setObjectName(_fromUtf8("label_41"))
        self.gridLayout_7.addWidget(self.label_41, 0, 0, 1, 2)
        self.gridLayout_9.addLayout(self.gridLayout_7, 0, 0, 1, 1)
        self.gridLayout_8 = QtGui.QGridLayout()
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.lowerframe = QtGui.QLineEdit(self.layoutWidget6)
        self.lowerframe.setObjectName(_fromUtf8("lowerframe"))
        self.gridLayout_8.addWidget(self.lowerframe, 1, 1, 1, 1)
        self.upperframe = QtGui.QLineEdit(self.layoutWidget6)
        self.upperframe.setObjectName(_fromUtf8("upperframe"))
        self.gridLayout_8.addWidget(self.upperframe, 2, 1, 1, 1)
        self.label_43 = QtGui.QLabel(self.layoutWidget6)
        self.label_43.setObjectName(_fromUtf8("label_43"))
        self.gridLayout_8.addWidget(self.label_43, 1, 0, 1, 1)
        self.label_44 = QtGui.QLabel(self.layoutWidget6)
        self.label_44.setObjectName(_fromUtf8("label_44"))
        self.gridLayout_8.addWidget(self.label_44, 2, 0, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout_8, 1, 0, 1, 1)
        self.label_55 = QtGui.QLabel(self.centralWidget)
        self.label_55.setGeometry(QtCore.QRect(850, 1060, 41, 27))
        self.label_55.setObjectName(_fromUtf8("label_55"))
        self.widget = QtGui.QWidget(self.centralWidget)
        self.widget.setGeometry(QtCore.QRect(370, 480, 311, 91))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout_5 = QtGui.QGridLayout(self.widget)
        self.gridLayout_5.setMargin(0)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.label_34 = QtGui.QLabel(self.widget)
        self.label_34.setObjectName(_fromUtf8("label_34"))
        self.gridLayout_5.addWidget(self.label_34, 1, 1, 1, 1)
        self.label_35 = QtGui.QLabel(self.widget)
        self.label_35.setObjectName(_fromUtf8("label_35"))
        self.gridLayout_5.addWidget(self.label_35, 1, 5, 1, 1)
        self.fmax = QtGui.QLineEdit(self.widget)
        self.fmax.setObjectName(_fromUtf8("fmax"))
        self.gridLayout_5.addWidget(self.fmax, 1, 2, 1, 3)
        self.label_54 = QtGui.QLabel(self.widget)
        self.label_54.setObjectName(_fromUtf8("label_54"))
        self.gridLayout_5.addWidget(self.label_54, 2, 3, 1, 1)
        self.P = QtGui.QLineEdit(self.widget)
        self.P.setObjectName(_fromUtf8("P"))
        self.gridLayout_5.addWidget(self.P, 2, 1, 1, 2)
        self.fmin = QtGui.QLineEdit(self.widget)
        self.fmin.setObjectName(_fromUtf8("fmin"))
        self.gridLayout_5.addWidget(self.fmin, 1, 6, 1, 2)
        self.label_36 = QtGui.QLabel(self.widget)
        self.label_36.setObjectName(_fromUtf8("label_36"))
        self.gridLayout_5.addWidget(self.label_36, 2, 0, 1, 1)
        self.D = QtGui.QLineEdit(self.widget)
        self.D.setObjectName(_fromUtf8("D"))
        self.gridLayout_5.addWidget(self.D, 2, 7, 1, 1)
        self.I = QtGui.QLineEdit(self.widget)
        self.I.setObjectName(_fromUtf8("I"))
        self.gridLayout_5.addWidget(self.I, 2, 4, 1, 2)
        self.label_33 = QtGui.QLabel(self.widget)
        self.label_33.setObjectName(_fromUtf8("label_33"))
        self.gridLayout_5.addWidget(self.label_33, 2, 6, 1, 1)
        self.label_32 = QtGui.QLabel(self.widget)
        self.label_32.setObjectName(_fromUtf8("label_32"))
        self.gridLayout_5.addWidget(self.label_32, 0, 2, 1, 6)
        CableDrivenParalleRobot.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(CableDrivenParalleRobot)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 904, 25))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuCDPR_Parameters = QtGui.QMenu(self.menuBar)
        self.menuCDPR_Parameters.setObjectName(_fromUtf8("menuCDPR_Parameters"))
        self.menuImport = QtGui.QMenu(self.menuCDPR_Parameters)
        self.menuImport.setObjectName(_fromUtf8("menuImport"))
        self.menuEdit = QtGui.QMenu(self.menuBar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        CableDrivenParalleRobot.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(CableDrivenParalleRobot)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        CableDrivenParalleRobot.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(CableDrivenParalleRobot)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        CableDrivenParalleRobot.setStatusBar(self.statusBar)
        self.actionNew_Window = QtGui.QAction(CableDrivenParalleRobot)
        self.actionNew_Window.setObjectName(_fromUtf8("actionNew_Window"))
        self.actionClose = QtGui.QAction(CableDrivenParalleRobot)
        self.actionClose.setObjectName(_fromUtf8("actionClose"))
        self.actionFile = QtGui.QAction(CableDrivenParalleRobot)
        self.actionFile.setObjectName(_fromUtf8("actionFile"))
        self.actionRobot = QtGui.QAction(CableDrivenParalleRobot)
        self.actionRobot.setObjectName(_fromUtf8("actionRobot"))
        self.actionCopy = QtGui.QAction(CableDrivenParalleRobot)
        self.actionCopy.setObjectName(_fromUtf8("actionCopy"))
        self.actionPaste = QtGui.QAction(CableDrivenParalleRobot)
        self.actionPaste.setObjectName(_fromUtf8("actionPaste"))
        self.actionClear = QtGui.QAction(CableDrivenParalleRobot)
        self.actionClear.setObjectName(_fromUtf8("actionClear"))
        self.menuImport.addAction(self.actionFile)
        self.menuImport.addAction(self.actionRobot)
        self.menuCDPR_Parameters.addAction(self.actionNew_Window)
        self.menuCDPR_Parameters.addAction(self.actionClose)
        self.menuCDPR_Parameters.addAction(self.menuImport.menuAction())
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addAction(self.actionClear)
        self.menuBar.addAction(self.menuCDPR_Parameters.menuAction())
        self.menuBar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(CableDrivenParalleRobot)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), CableDrivenParalleRobot.close)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.pSaveParameter)
        QtCore.QMetaObject.connectSlotsByName(CableDrivenParalleRobot)

    def retranslateUi(self, CableDrivenParalleRobot):
        CableDrivenParalleRobot.setWindowTitle(_translate("CableDrivenParalleRobot", "CableDrivenParalleRobot", None))
        self.pushButton.setText(_translate("CableDrivenParalleRobot", "Close", None))
        self.pushButton_2.setText(_translate("CableDrivenParalleRobot", "Save Parameters", None))
        self.label_16.setText(_translate("CableDrivenParalleRobot", "Cable Paramters", None))
        self.label.setText(_translate("CableDrivenParalleRobot", "Anchor Points", None))
        self.label_2.setText(_translate("CableDrivenParalleRobot", "Exit  Points", None))
        self.label_3.setText(_translate("CableDrivenParalleRobot", "Cable 1", None))
        self.label_4.setText(_translate("CableDrivenParalleRobot", "Cable 2", None))
        self.label_5.setText(_translate("CableDrivenParalleRobot", "Cable 3", None))
        self.label_12.setText(_translate("CableDrivenParalleRobot", "Cable", None))
        self.label_7.setText(_translate("CableDrivenParalleRobot", "Cable 4", None))
        self.label_8.setText(_translate("CableDrivenParalleRobot", "Cable 5", None))
        self.label_9.setText(_translate("CableDrivenParalleRobot", "Cable 6", None))
        self.label_10.setText(_translate("CableDrivenParalleRobot", "Cable 7", None))
        self.label_11.setText(_translate("CableDrivenParalleRobot", "Cable 8", None))
        self.label_17.setText(_translate("CableDrivenParalleRobot", "Mass", None))
        self.label_18.setText(_translate("CableDrivenParalleRobot", "Radius", None))
        self.pushButton_3.setText(_translate("CableDrivenParalleRobot", "Load Parameters", None))
        self.label_19.setText(_translate("CableDrivenParalleRobot", "Inertial Paramters", None))
        self.label_29.setText(_translate("CableDrivenParalleRobot", "Enter Co-ordinates as  X,Y,Z", None))
        self.label_24.setText(_translate("CableDrivenParalleRobot", "Iyy", None))
        self.label_26.setText(_translate("CableDrivenParalleRobot", "Ixz", None))
        self.label_27.setText(_translate("CableDrivenParalleRobot", "Iyz", None))
        self.label_25.setText(_translate("CableDrivenParalleRobot", "Izz", None))
        self.label_6.setText(_translate("CableDrivenParalleRobot", "Ixx", None))
        self.label_20.setText(_translate("CableDrivenParalleRobot", "Ixy", None))
        self.label_21.setText(_translate("CableDrivenParalleRobot", "Ixz", None))
        self.label_22.setText(_translate("CableDrivenParalleRobot", "Iyz", None))
        self.label_23.setText(_translate("CableDrivenParalleRobot", "Ixy", None))
        self.label_28.setText(_translate("CableDrivenParalleRobot", "Color", None))
        self.label_13.setText(_translate("CableDrivenParalleRobot", "Mass", None))
        self.endEffShape_2.setItemText(0, _translate("CableDrivenParalleRobot", "Black", None))
        self.endEffShape_2.setItemText(1, _translate("CableDrivenParalleRobot", "Blue", None))
        self.endEffShape_2.setItemText(2, _translate("CableDrivenParalleRobot", "Grey", None))
        self.endEffShape_2.setItemText(3, _translate("CableDrivenParalleRobot", "Yellow", None))
        self.endEffShape_2.setItemText(4, _translate("CableDrivenParalleRobot", "Green", None))
        self.endEffShape_2.setItemText(5, _translate("CableDrivenParalleRobot", "White", None))
        self.endEffShape_2.setItemText(6, _translate("CableDrivenParalleRobot", "Orange", None))
        self.endEffShape_2.setItemText(7, _translate("CableDrivenParalleRobot", "Red", None))
        self.label_14.setText(_translate("CableDrivenParalleRobot", "Shape", None))
        self.endEffShape.setItemText(0, _translate("CableDrivenParalleRobot", "Sphere", None))
        self.endEffShape.setItemText(1, _translate("CableDrivenParalleRobot", "Box", None))
        self.label_15.setText(_translate("CableDrivenParalleRobot", "End-Effector Paramters", None))
        self.label_31.setText(_translate("CableDrivenParalleRobot", "Initial End-Effector Pose", None))
        self.label_37.setText(_translate("CableDrivenParalleRobot", "Position X,Y,Z", None))
        self.label_30.setText(_translate("CableDrivenParalleRobot", "Orientation R,P,Y", None))
        self.endEffShape_5.setItemText(0, _translate("CableDrivenParalleRobot", "Black", None))
        self.endEffShape_5.setItemText(1, _translate("CableDrivenParalleRobot", "Blue", None))
        self.endEffShape_5.setItemText(2, _translate("CableDrivenParalleRobot", "Grey", None))
        self.endEffShape_5.setItemText(3, _translate("CableDrivenParalleRobot", "Yellow", None))
        self.endEffShape_5.setItemText(4, _translate("CableDrivenParalleRobot", "Green", None))
        self.endEffShape_5.setItemText(5, _translate("CableDrivenParalleRobot", "White", None))
        self.endEffShape_5.setItemText(6, _translate("CableDrivenParalleRobot", "Orange", None))
        self.endEffShape_5.setItemText(7, _translate("CableDrivenParalleRobot", "Red", None))
        self.label_40.setText(_translate("CableDrivenParalleRobot", "Shape", None))
        self.endEffShape_6.setItemText(0, _translate("CableDrivenParalleRobot", "Box", None))
        self.label_39.setText(_translate("CableDrivenParalleRobot", "Mass", None))
        self.label_38.setText(_translate("CableDrivenParalleRobot", "Color", None))
        self.label_41.setText(_translate("CableDrivenParalleRobot", "Bounding Frame Paramters", None))
        self.label_43.setText(_translate("CableDrivenParalleRobot", "Lowest Edge co-ordinate", None))
        self.label_44.setText(_translate("CableDrivenParalleRobot", "Uppermost Edge co-ordinate", None))
        self.label_55.setText(_translate("CableDrivenParalleRobot", "Fmin", None))
        self.label_34.setText(_translate("CableDrivenParalleRobot", "Fmax", None))
        self.label_35.setText(_translate("CableDrivenParalleRobot", "Fmin", None))
        self.label_54.setText(_translate("CableDrivenParalleRobot", "I", None))
        self.label_36.setText(_translate("CableDrivenParalleRobot", "P", None))
        self.label_33.setText(_translate("CableDrivenParalleRobot", "D", None))
        self.label_32.setText(_translate("CableDrivenParalleRobot", "Control Paramters", None))
        self.menuCDPR_Parameters.setTitle(_translate("CableDrivenParalleRobot", "File", None))
        self.menuImport.setTitle(_translate("CableDrivenParalleRobot", "Import", None))
        self.menuEdit.setTitle(_translate("CableDrivenParalleRobot", "Edit", None))
        self.actionNew_Window.setText(_translate("CableDrivenParalleRobot", "Open", None))
        self.actionClose.setText(_translate("CableDrivenParalleRobot", "Close", None))
        self.actionFile.setText(_translate("CableDrivenParalleRobot", "File", None))
        self.actionRobot.setText(_translate("CableDrivenParalleRobot", "Robot", None))
        self.actionCopy.setText(_translate("CableDrivenParalleRobot", "Copy", None))
        self.actionPaste.setText(_translate("CableDrivenParalleRobot", "Paste", None))
        self.actionClear.setText(_translate("CableDrivenParalleRobot", "Clear", None))

    def pSaveParameter(self):
        SaveParameter(self)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    CableDrivenParalleRobot = QtGui.QMainWindow()
    ui = Ui_CableDrivenParalleRobot()
    ui.setupUi(CableDrivenParalleRobot)
    CableDrivenParalleRobot.show()
    app.exec_()
    #sys.exit(app.exec_())

