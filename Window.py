import sys,datetime
from PyQt4 import QtGui, QtCore

from Menu import Menu
from Registrar import Registrar
from Listar import Listar

class Window(QtGui.QMainWindow):
    def __init__(self, current_user=None, parent=None):
        super(Window, self).__init__()
        self.current_user = current_user
        self.central_widget = QtGui.QStackedWidget()
        self.setCentralWidget(self.central_widget)
        self.menu()

    def menu(self):
        menu_widget = Menu(self)
        menu_widget.button1.clicked.connect(self.registrar)
        menu_widget.button2.clicked.connect(self.listar)
        menu_widget.button3.clicked.connect(self.close_application)
        self.central_widget.addWidget(menu_widget)
        self.central_widget.setCurrentWidget(menu_widget)
        self.dialog = Listar(self)

    def registrar(self):
        reg_widget = Registrar(current_user=self.current_user)
        reg_widget.button1.clicked.connect(reg_widget.gravar)
        reg_widget.button2.clicked.connect(self.menu)
        self.central_widget.addWidget(reg_widget)
        self.central_widget.setCurrentWidget(reg_widget)

    def listar(self):
        self.dialog.show()


    def close_application(self):
        choice = QtGui.QMessageBox.question(self,'Sair', 
                                            'Tem certeza que quer sair?',
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            sys.exit()
