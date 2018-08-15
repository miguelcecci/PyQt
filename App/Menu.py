from PyQt4 import QtGui, QtCore

class Menu(QtGui.QWidget):
    def __init__(self, parent=None):
        super(Menu, self).__init__(parent)
        layout = QtGui.QVBoxLayout()
        self.button1 = QtGui.QPushButton('Registrar')
        self.button2 = QtGui.QPushButton('Listar')
        self.button3 = QtGui.QPushButton('Sair')
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)
        self.setLayout(layout)
 