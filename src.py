import sys
from PyQt4 import QtGui, QtCore

from Login import Login
from Window import Window

app = QtGui.QApplication(sys.argv)
login = Login()

if login.exec_() == QtGui.QDialog.Accepted:
    current_user = login.getUser()
    window = Window(current_user)
    window.show()
    sys.exit(app.exec_())