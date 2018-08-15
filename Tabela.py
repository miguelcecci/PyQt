from PyQt4 import QtGui, QtCore
from pymongo import MongoClient

client = MongoClient('mongodb://admin:admin123@localhost:27017/')
db = client.test_database
collection = db.compras_collection
compras = db.compras

class Tabela(QtGui.QTableWidget):
    def __init__(self, parent=None):
        super(Tabela, self).__init__(parent)
        self.dados = list(compras.find({}))
        self.setRowCount(len(self.dados))
        self.setColumnCount(4)
        self.set_data()
        self.resizeColumnsToContents()
        self.resizeRowsToContents()
 
    def set_data(self):
        horHeaders = ['operador', 'data', 'cpf', 'valor']
        for n, key in enumerate(horHeaders):
            for m, values in enumerate(self.dados):
                newitem = QtGui.QTableWidgetItem(values[key])
                self.setItem(m, n, newitem)
        self.setHorizontalHeaderLabels(horHeaders)

