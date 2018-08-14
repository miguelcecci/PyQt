from PyQt4 import QtGui, QtCore

class Tabela(QtGui.QTableWidget):
    def __init__(self, parent=None):
        super(Tabela, self).__init__(parent)
        self.data = [{'user':'asd', 'data':'dasd', 'cpf':'120399', 'valor':'123'}, {'user':'eafsasd', 'data':'dassd', 'cpf':'1320399', 'valor':'12333'}]
        self.setRowCount(4)
        self.setColumnCount(4)
        self.set_data()
        self.resizeColumnsToContents()
        self.resizeRowsToContents()
 
    def set_data(self):
        horHeaders = ['user', 'data', 'cpf', 'valor']
        for n, key in enumerate(horHeaders):
            for m, values in enumerate(self.data):
                newitem = QtGui.QTableWidgetItem(values[key])
                self.setItem(m, n, newitem)
        self.setHorizontalHeaderLabels(horHeaders)

