from PySide6 import QtWidgets, QtCore, QtGui


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Hello World")
        self.resize(800, 600)

        self.label = QtWidgets.QLabel("Hello World", self)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setFont(QtGui.QFont("Arial", 20))

        self.setCentralWidget(self.label)

        self.show()


app = QtWidgets.QApplication([])
window = MainWindow()
app.exec()
