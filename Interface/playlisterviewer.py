#!/usr/bin/python
 
import sys
import urllib.request
from PyQt5 import QtGui, QtCore
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QTableWidgetItem
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QRect
import Interface
import Files
from Interface import playlister, playlisterviewermovie, playlisterviewerserial
from Files import directory

class PlayListerViewer(QtWidgets.QMainWindow):
    
    def __init__(self, parent=None):
        try:
            QtWidgets.QMainWindow.__init__(self, parent)
            self.ui = playlister.Ui_MainWindow()
            self.ui.setupUi(self)
            self.ui.label_2.setText("")
            self.ui.pushButton.clicked.connect(self.selectDirButton)
            self.movieWindow = playlisterviewermovie.PlayListerViewerMovie(self.ui)
            self.serialWindow = playlisterviewerserial.PlayListerViewerSerial(self.ui)
        except Exception as e:
            print(e)
    
    def selectDirButton(self):
        dir_path = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select a directory')
        if(dir_path):
            self.ui.label_2.setText("Active directory : " + dir_path)
            self.builtDir = directory.Directory(dir_path)
            self.builtDir.initListFiles()
            self.builtDir.displayFilesIntoMediaLists()
            self.movieWindow.populateMovieTable(self.builtDir)
            self.serialWindow.populateSerialTable(self.builtDir)
