from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def window(): 
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(500, 500, 500, 500)
    win.setWindowTitle("Music Player")

    label = QtWidgets.QLabel(win)
    label.setText("Choose your music!")
    label.move(100, 100)

    win.show()
    sys.exit(app.exec_())

window()