from PyQt4 import QtGui, QtCore
from Tabela import Tabela

class Listar(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(Listar, self).__init__(parent)
        tabela = Tabela(self)
        self.setCentralWidget(tabela)
        self.resize(556, 500)

