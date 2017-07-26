import urllib.request
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QTableWidgetItem
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QRect
import Files
import Interface
from Files import movie

class PlayListerViewerMovie():

    def __init__(self, mainWindow):
        self.ui = mainWindow
        self.ui.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        self.ui.tableWidget.clicked.connect(
            lambda item: self.clickOnItemInMovieTable(item))
        self.ui.tableWidget.doubleClicked.connect(
            lambda item: self.doubleClickOnItemInMovieTable(item))
        self.ui.label_3.mousePressEvent = self.clickOnDescriptionLabel
        
    def populateMovieTable(self, builtDir = None):
        if(builtDir):
            self.builtDir = builtDir
        elif not(hasattr(self, 'builtDir')):
            return
        self.ui.label_3.setText("")
        self.ui.label_4.setPixmap(QPixmap())
        for i in reversed(range(self.ui.tableWidget.rowCount())):
            self.ui.tableWidget.removeRow(i)
        self.builtDir.ListMovieFiles = sorted(self.builtDir.ListMovieFiles, key=lambda mov: mov.name)
        for i in range (len(self.builtDir.ListMovieFiles)):
            self.ui.tableWidget.insertRow(i)
            self.ui.tableWidget.setItem(i, 0, QTableWidgetItem(self.builtDir.ListMovieFiles[i].name))
            self.ui.tableWidget.setItem(i, 1, QTableWidgetItem(self.builtDir.ListMovieFiles[i].date))
            self.ui.tableWidget.setItem(i, 2, QTableWidgetItem(self.builtDir.ListMovieFiles[i].language))
            self.ui.tableWidget.setItem(i, 3, QTableWidgetItem(self.builtDir.ListMovieFiles[i].quality))

    def initMovie(self, item, read = False):
        self.activeMovie = self.builtDir.ListMovieFiles[item.row()]
        if(read):
            self.activeMovie.read()
        self.activeMovie.getInformationsFromAPI()
        if(self.activeMovie.description):
            self.ui.label_3.setText(self.activeMovie.description)
        else:
            self.ui.label_3.setText("No correspondence for \"" + self.activeMovie.name + "\" in the database. Click here to rename the movie.")
            
        if(self.activeMovie.picture):
            with urllib.request.urlopen("http://image.tmdb.org/t/p/w500/" + self.activeMovie.picture) as url:
                data = url.read()
            pixmap = QPixmap()
            pixmap.loadFromData(data)
            pixmap = pixmap.scaled(self.ui.label_4.width(), self.ui.label_4.height())
            self.ui.label_4.setPixmap(pixmap)
        else:
            self.ui.label_4.setPixmap(QPixmap())
    
    def clickOnItemInMovieTable(self, item):
        self.initMovie(item)

    def doubleClickOnItemInMovieTable(self, item):
        self.initMovie(item, True)

    def clickOnDescriptionLabel(self, event):
        if (not(hasattr(self, 'activeMovie'))):
            return
        text, ok = QInputDialog.getText(None, 'Rename', 'Enter the new name of the movie :')
        if not (ok):
            return
        self.activeMovie.rename(text.lower())
        self.populateMovieTable()
        