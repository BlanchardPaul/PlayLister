import Interface
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from Interface.playlisterviewer import *

try:
    app = QtWidgets.QApplication(sys.argv)
    untitled = PlayListerViewer()
    untitled.show()
    sys.exit(app.exec_())
except Exception as e:
    print(e)

if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)
    untitled = PlayListerViewer()
    untitled.show()
    sys.exit(app.exec_())
