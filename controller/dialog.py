from PySide.QtGui import QMessageBox

def showdialog(x, y):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setText(x)
    msg.setInformativeText(y)
    msg.setWindowTitle("Alert")
    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    return msg.exec_()