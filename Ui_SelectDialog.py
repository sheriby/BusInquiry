# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/sher/Code/python/learnQT/BusInquiry/SelectDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 600)
        Dialog.setMinimumSize(QtCore.QSize(800, 600))
        Dialog.setMaximumSize(QtCore.QSize(800, 600))
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.lb1 = QtWidgets.QLabel(Dialog)
        self.lb1.setStyleSheet("font: 57 30pt \"WenQuanYi Zen Hei Sharp\";\n"
"")
        self.lb1.setObjectName("lb1")
        self.horizontalLayout.addWidget(self.lb1)
        self.lbFrom = QtWidgets.QLabel(Dialog)
        self.lbFrom.setStyleSheet("font: 57 30pt \"WenQuanYi Zen Hei Sharp\";\n"
"color: rgb(239, 41, 41);")
        self.lbFrom.setObjectName("lbFrom")
        self.horizontalLayout.addWidget(self.lbFrom)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.lb2 = QtWidgets.QLabel(Dialog)
        self.lb2.setStyleSheet("font: 57 30pt \"WenQuanYi Zen Hei Sharp\";\n"
"")
        self.lb2.setObjectName("lb2")
        self.horizontalLayout.addWidget(self.lb2)
        self.lbTo = QtWidgets.QLabel(Dialog)
        self.lbTo.setStyleSheet("font: 57 30pt \"WenQuanYi Zen Hei Sharp\";\n"
"color: rgb(239, 41, 41);")
        self.lbTo.setObjectName("lbTo")
        self.horizontalLayout.addWidget(self.lbTo)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setStyleSheet("font: 75 24pt \"WenQuanYi Zen Hei Sharp\";\n"
"color: rgb(255, 0, 255);")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.lbMinBus = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbMinBus.sizePolicy().hasHeightForWidth())
        self.lbMinBus.setSizePolicy(sizePolicy)
        self.lbMinBus.setStyleSheet("font: 57 14pt \"WenQuanYi Zen Hei Sharp\";\n"
"background-color: rgba(211, 215, 207, 0.85);")
        self.lbMinBus.setWordWrap(True)
        self.lbMinBus.setObjectName("lbMinBus")
        self.horizontalLayout_2.addWidget(self.lbMinBus)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setStyleSheet("font: 75 24pt \"WenQuanYi Zen Hei Sharp\";\n"
"color: rgb(255, 0, 255);")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.lbMinDistance = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbMinDistance.sizePolicy().hasHeightForWidth())
        self.lbMinDistance.setSizePolicy(sizePolicy)
        self.lbMinDistance.setStyleSheet("font: 57 14pt \"WenQuanYi Zen Hei Sharp\";\n"
"background-color: rgba(211, 215, 207, 0.85);")
        self.lbMinDistance.setWordWrap(True)
        self.lbMinDistance.setObjectName("lbMinDistance")
        self.horizontalLayout_3.addWidget(self.lbMinDistance)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem5)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem6 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem6)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_5.addWidget(self.pushButton)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem7)
        self.horizontalLayout_5.setStretch(0, 2)
        self.horizontalLayout_5.setStretch(1, 1)
        self.horizontalLayout_5.setStretch(2, 2)
        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.retranslateUi(Dialog)
        self.pushButton.clicked['bool'].connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lb1.setText(_translate("Dialog", "From "))
        self.lbFrom.setText(_translate("Dialog", "XXX"))
        self.lb2.setText(_translate("Dialog", "To "))
        self.lbTo.setText(_translate("Dialog", "XXX"))
        self.label_3.setText(_translate("Dialog", "最少换乘： "))
        self.lbMinBus.setText(_translate("Dialog", "\'审计局站\', \'工学院站\', \'劳动局站\', \'交通局站\', \'五金市场\'审计局站\', \'工学院站\', \'劳动局站\', \'交通局站\', \'五金市场\'审计局站\', \'工学院站\', \'劳动局站\', \'交通局站\', \'五金市场\'审计局站\', \'工学院站\', \'劳动局站\', \'交通局站\', \'五金市场"))
        self.label_4.setText(_translate("Dialog", "最短距离： "))
        self.lbMinDistance.setText(_translate("Dialog", "\'审计局站\', \'工学院站\', \'劳动局站\', \'交通局站\', \'五金市场\'审计局站\', \'工学院站\', \'劳动局站\', \'交通局站\', \'五金市场"))
        self.pushButton.setText(_translate("Dialog", "确定"))