# -*- coding: utf-8 -*-
from PySide.QtGui import *
from PySide.QtCore import *
from view.home import Ui_Form as home
from model.model import Server
import sys
from math import ceil
def get_footer():
    try:
        f = open("footer")
        x = f.read()
        if not x: x = ''
        return x
    except:
        return ''
class Home(QWidget,home):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.login_btn.clicked.connect(self.login_f)
        self.db = Server()
        self.stackedWidget.setCurrentIndex(0)
        for i in self.findChildren(QWidget):
            i.setAttribute(Qt.WA_StyledBackground)
        self.exit_btn.clicked.connect(QApplication.exit)
        self.serv_w.setContentsMargins(10,10,10,10)
    def ord_service(self):
        serice_id = int(self.sender().objectName().split("_")[1])
        service_name = self.sender().text()
        st = self.db.order_service(service_name)
        if st:
            printer = QPrinter(QPrinter.HighResolution)
            txt = u'''<html><head><meta charset="UTF-8">
            </head><body>
            <center><img width='50' height='40' src='logo.png'></center>
            <center><h7>شركة مياة الشرب والصرف الصحى</h7><center><hr>'''
            txt += u'<h7>%s</h7>' %(st.get('date'))
            txt += u'<center><h7>الخدمة</h7></center>'
            txt += u'''<center><h7>%s</h7></center>''' %(service_name)
            txt += u'<center><h7>رقم العميل</h7></center>'
            txt += u'<center><h7>%s</h7></center><hr>' %(str(st.get('num')))
            txt += u'''<center><h7>%s</h7></center>''' % (get_footer())
            doc = QTextDocument()
            op = QTextOption()
            doc.setDocumentMargin(0)
            printer.setPageMargins(0,0,0,0,QPrinter.Millimeter)
            op.setTextDirection(Qt.RightToLeft)
            doc.setDefaultTextOption(op)
            doc.setHtml(txt)
            doc.print_(printer)
    def color_btn(self,btn):
        for i in self.findChildren(QToolButton):
            i.setStyleSheet("")
        btn.setStyleSheet("background:#CE7800")
        self.stackedWidget_3.setCurrentIndex(0)
    def log_out(self):
        self.stackedWidget.setCurrentIndex(0)
        self.user_edt.setFocus()
    def login_f(self):
        '''login function'''
        uname= self.user_edt.text()
        passw = self.pass_edt.text()
        if self.db.login(uname,passw):
            self.user_edt.clear()
            self.pass_edt.clear()
            self.stackedWidget.setCurrentIndex(1)
            self.show_items()
        else:
            QSound('fault.wav').play()
    def show_items(self):
        list = self.db.get_services()
        print list
        pos = self.create_grid_pos(list)
        self.empty_layout()
        x = 0
        for i in list:
            self.itm = QPushButton(i['name'])
            self.itm.setStyleSheet("background:#%s" %(i['color']))
            self.itm.setObjectName("btn_" + str(i['id']))
            self.itm.clicked.connect(self.ord_service)
            sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
            self.itm.setSizePolicy(sizePolicy)
            self.serv_w.layout().addWidget(self.itm, pos[x][0], pos[x][1])
            x += 1
    def create_grid_pos(self, list):
        """create the position of grid items"""
        pos = []
        mul = self.get_multiply(len(list))
        i = int(mul[0])
        j = int(mul[1])
        for x in range(j):
            for y in range(i):
                pos.append((x, y))
        return pos
    def get_multiply(self, count, i=1):
        """return the two multiplies"""
        sys.setrecursionlimit(8000)
        res = count / i
        if res > 5:
            i += 1
            return self.get_multiply(count, i)
        else:
            if ceil(res) * i < count:
                return (ceil(res) + 1, i)
            else:
                return (ceil(res), i)
    def empty_layout(self):
        for bt in self.serv_w.findChildren(QPushButton):
            bt.deleteLater()