import sys
from PyQt4 import QtGui, QtCore
from pymongo import MongoClient
import hashlib

client = MongoClient('mongodb://admin:admin123@localhost:27017/')
db = client.test_database
collection = db.test_collection
users = db.users

class Login(QtGui.QDialog):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.l1 = QtGui.QLabel('Usuario: ')
        self.l2 = QtGui.QLabel('Senha: ')
        self.textName = QtGui.QLineEdit(self)
        self.textPass = QtGui.QLineEdit(self)
        self.buttonLogin = QtGui.QPushButton('Login', self)
        self.buttonLogin.clicked.connect(self.handleLogin)
        self.current = None
        self.move(100, 100)
        layout = QtGui.QVBoxLayout(self)
        layout.addWidget(self.l1)
        layout.addWidget(self.textName)
        layout.addWidget(self.l2)
        layout.addWidget(self.textPass)
        layout.addWidget(self.buttonLogin)

    def handleLogin(self):
        user = str(self.textName.text())
        self.current = user
        if users.find_one({'user':user}) != None:
            password = users.find_one({'user':user})['pass'].encode('ascii')
            if (hashlib.sha224(str(self.textPass.text())).hexdigest() == password):
                self.accept()
            else:
                QtGui.QMessageBox.warning(
                    self, 'Erro', 'Usuario ou senha invalidos.')
        else:
            QtGui.QMessageBox.warning(
                self, 'Erro', 'Usuario ou senha invalidos.')

    def getUser(self):
        return self.current