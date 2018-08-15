import sys, datetime
from PyQt4 import QtGui, QtCore
from pymongo import MongoClient

client = MongoClient('mongodb://admin:admin123@localhost:27017/')
db = client.test_database
collection = db.compras_collection
compras = db.compras

class Registrar(QtGui.QWidget):
    def __init__(self, current_user=None, parent=None):
        super(Registrar, self).__init__(parent)
        layout = QtGui.QVBoxLayout()
        self.current_user = current_user
        self.l1 = QtGui.QLabel('CPF: ')
        self.l2 = QtGui.QLabel('Valor: ')
        self.cpf = QtGui.QLineEdit(self)
        self.valor = QtGui.QLineEdit(self)
        self.button1 = QtGui.QPushButton('Submeter')
        self.button2 = QtGui.QPushButton('Voltar')
        layout.addWidget(self.l1)
        layout.addWidget(self.cpf)
        layout.addWidget(self.l2)
        layout.addWidget(self.valor)
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        self.setLayout(layout)

    def gravar(self):
        if (len(str(self.cpf.text())) == 11) and (len(str(self.cpf.text())) or len(str(self.valor.text())) != 0):
            compra = {
            'operador': self.current_user,
            'data':datetime.datetime.now().isoformat(),
            'cpf':str(self.cpf.text()),
            'valor':str(self.valor.text())
            }
            compras.insert_one(compra)
            self.cpf.clear()
            self.valor.clear()
            QtGui.QMessageBox.information(
                self, 'Registrado', 'Registrado com sucesso')
            print(compra)
        else:
            QtGui.QMessageBox.warning(
                self, 'Erro', 'Valores invalidos')