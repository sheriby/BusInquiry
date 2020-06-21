# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/sher/Code/python/learnQT/BusInquiry/ManageLogin.ui'
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
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setStyleSheet("color: rgb(239, 41, 41);\n"
"font: 57 30pt \"WenQuanYi Zen Hei Sharp\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setStyleSheet("font: 75 20pt \"WenQuanYi Zen Hei Sharp\";\n"
"color: rgb(248, 0, 216);")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.leAccount = QtWidgets.QLineEdit(Dialog)
        self.leAccount.setStyleSheet("font: 57 18pt \"WenQuanYi Zen Hei Sharp\";")
        self.leAccount.setClearButtonEnabled(True)
        self.leAccount.setObjectName("leAccount")
        self.horizontalLayout_2.addWidget(self.leAccount)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setStyleSheet("font: 75 20pt \"WenQuanYi Zen Hei Sharp\";\n"
"color: rgb(248, 0, 216);")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.lePasswd = QtWidgets.QLineEdit(Dialog)
        self.lePasswd.setStyleSheet("font: 57 18pt \"WenQuanYi Zen Hei Sharp\";")
        self.lePasswd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lePasswd.setObjectName("lePasswd")
        self.horizontalLayout.addWidget(self.lePasswd)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem3)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.btnLogin = QtWidgets.QPushButton(Dialog)
        self.btnLogin.setStyleSheet("font: 57 18pt \"WenQuanYi Zen Hei Sharp\";")
        self.btnLogin.setObjectName("btnLogin")
        self.horizontalLayout_3.addWidget(self.btnLogin)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setStyleSheet("font: 57 18pt \"WenQuanYi Zen Hei Sharp\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem7)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem8)

        self.retranslateUi(Dialog)
        self.pushButton_2.clicked['bool'].connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "管理员登录"))
        self.label_2.setText(_translate("Dialog", "账号： "))
        self.leAccount.setPlaceholderText(_translate("Dialog", "请输入账号"))
        self.label_3.setText(_translate("Dialog", "密码： "))
        self.lePasswd.setPlaceholderText(_translate("Dialog", "请输入密码"))
        self.btnLogin.setText(_translate("Dialog", "登录"))
        self.pushButton_2.setText(_translate("Dialog", "取消"))