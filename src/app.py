# PyQt5 modules
from PyQt5 import QtWidgets

# Python modules
import sys
from functools import partial

# Main window ui import
from src.mainwindow import MainWindow


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.aboutToQuit.connect(partial(on_close, window))
    sys.exit(app.exec())

def on_close(window):
    window.shutDown()
    
