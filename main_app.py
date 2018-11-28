# -*- coding: utf-8 -*-
from PySide.QtGui import *
from controller.home import Home
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    h = Home()
    h.show()
    h.user_edt.setFocus()
    app.exec_()