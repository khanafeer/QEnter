# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uis/home.ui'
#
# Created: Tue Jul 03 18:17:02 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(952, 579)
        Form.setMinimumSize(QtCore.QSize(0, 0))
        Form.setMaximumSize(QtCore.QSize(16777215, 16777215))
        Form.setStyleSheet(".QWidget{\n"
"background:#2F4858;}\n"
"\n"
".QToolButton{\n"
"background:#F6AE2D;}")
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stackedWidget = QtGui.QStackedWidget(Form)
        self.stackedWidget.setObjectName("stackedWidget")
        self.login_w = QtGui.QWidget()
        self.login_w.setObjectName("login_w")
        self.gridLayout = QtGui.QGridLayout(self.login_w)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtGui.QWidget(self.login_w)
        self.widget.setStyleSheet("QLineEdit{\n"
"padding:10px;\n"
"}\n"
"")
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtGui.QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pass_edt = QtGui.QLineEdit(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pass_edt.sizePolicy().hasHeightForWidth())
        self.pass_edt.setSizePolicy(sizePolicy)
        self.pass_edt.setMinimumSize(QtCore.QSize(300, 0))
        self.pass_edt.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pass_edt.setEchoMode(QtGui.QLineEdit.Password)
        self.pass_edt.setAlignment(QtCore.Qt.AlignCenter)
        self.pass_edt.setObjectName("pass_edt")
        self.gridLayout_2.addWidget(self.pass_edt, 2, 0, 1, 2)
        self.user_edt = QtGui.QLineEdit(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.user_edt.sizePolicy().hasHeightForWidth())
        self.user_edt.setSizePolicy(sizePolicy)
        self.user_edt.setMinimumSize(QtCore.QSize(300, 0))
        self.user_edt.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.user_edt.setAlignment(QtCore.Qt.AlignCenter)
        self.user_edt.setObjectName("user_edt")
        self.gridLayout_2.addWidget(self.user_edt, 1, 0, 1, 2)
        self.login_btn = QtGui.QPushButton(self.widget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/n/imgs/Checkmark-512 (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.login_btn.setIcon(icon)
        self.login_btn.setIconSize(QtCore.QSize(30, 30))
        self.login_btn.setObjectName("login_btn")
        self.gridLayout_2.addWidget(self.login_btn, 3, 1, 1, 1)
        self.exit_btn = QtGui.QPushButton(self.widget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/n/imgs/Cancel-500.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit_btn.setIcon(icon1)
        self.exit_btn.setIconSize(QtCore.QSize(30, 30))
        self.exit_btn.setObjectName("exit_btn")
        self.gridLayout_2.addWidget(self.exit_btn, 3, 0, 1, 1)
        self.label = QtGui.QLabel(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 2)
        self.gridLayout.addWidget(self.widget, 1, 1, 1, 1)
        self.widget_4 = QtGui.QWidget(self.login_w)
        self.widget_4.setObjectName("widget_4")
        self.gridLayout.addWidget(self.widget_4, 1, 2, 1, 1)
        self.widget_3 = QtGui.QWidget(self.login_w)
        self.widget_3.setObjectName("widget_3")
        self.gridLayout.addWidget(self.widget_3, 0, 1, 1, 1)
        self.widget_6 = QtGui.QWidget(self.login_w)
        self.widget_6.setObjectName("widget_6")
        self.gridLayout.addWidget(self.widget_6, 1, 0, 1, 1)
        self.widget_5 = QtGui.QWidget(self.login_w)
        self.widget_5.setObjectName("widget_5")
        self.gridLayout.addWidget(self.widget_5, 2, 1, 1, 1)
        self.stackedWidget.addWidget(self.login_w)
        self.home_w = QtGui.QWidget()
        self.home_w.setObjectName("home_w")
        self.gridLayout_3 = QtGui.QGridLayout(self.home_w)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_2 = QtGui.QLabel(self.home_w)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Alarabiya Font")
        font.setWeight(75)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background:#F6AE2D;\n"
"color:#fff;")
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)
        self.widget_2 = QtGui.QWidget(self.home_w)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(304, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.serv_w = QtGui.QWidget(self.widget_2)
        self.serv_w.setStyleSheet(".QWidget{\n"
"border:2px solid;\n"
"}")
        self.serv_w.setObjectName("serv_w")
        self.gridLayout_4 = QtGui.QGridLayout(self.serv_w)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalLayout.addWidget(self.serv_w)
        spacerItem1 = QtGui.QSpacerItem(304, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout_3.addWidget(self.widget_2, 4, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.home_w)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setStyleSheet("color:#fff;")
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 2, 0, 1, 1)
        self.line = QtGui.QFrame(self.home_w)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_3.addWidget(self.line, 1, 0, 1, 1)
        self.line_2 = QtGui.QFrame(self.home_w)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_3.addWidget(self.line_2, 3, 0, 1, 1)
        self.stackedWidget.addWidget(self.home_w)
        self.verticalLayout.addWidget(self.stackedWidget)

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.user_edt, self.pass_edt)
        Form.setTabOrder(self.pass_edt, self.login_btn)
        Form.setTabOrder(self.login_btn, self.exit_btn)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "QBAT - BATCODERS", None, QtGui.QApplication.UnicodeUTF8))
        self.login_btn.setText(QtGui.QApplication.translate("Form", "دخول", None, QtGui.QApplication.UnicodeUTF8))
        self.exit_btn.setText(QtGui.QApplication.translate("Form", "اغلاق", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "تسجيل الدخول", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600;\">شركة مياة الشرب والصرف الصحي بكفرالشيخ</span></p><p align=\"center\"><span style=\" font-size:24pt; font-weight:600;\">ترحب بكم</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">قم باختيار الخدمة المطلوبة</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

import source_rc
