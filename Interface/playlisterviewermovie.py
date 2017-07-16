import urllib.request
from PyQt5 import QtGui, QtCore
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QTableWidgetItem
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QRect
import Files
from Files import movie

class PlayListerViewerMovie():

    def __init__(self, mainWindow):
        self.ui = mainWindow
        self.ui.tableWidget.clicked.connect(
            lambda item: self.clickOnItemInMovieTable(item))
        self.ui.tableWidget.doubleClicked.connect(
            lambda item: self.doubleClickOnItemInMovieTable(item))
        
    def populateMovieTable(self, builtDir):
        self.builtDir = builtDir
        self.ui.label_3.setText("")
        self.ui.label_4.setPixmap(QPixmap())
        for i in reversed(range(self.ui.tableWidget.rowCount())):
            self.ui.tableWidget.removeRow(i)
        for i in range (len(self.builtDir.ListMovieFiles)):
            self.ui.tableWidget.insertRow(i)
            self.ui.tableWidget.setItem(i, 0, QTableWidgetItem(self.builtDir.ListMovieFiles[i].name))
            self.ui.tableWidget.setItem(i, 1, QTableWidgetItem(self.builtDir.ListMovieFiles[i].date))
            self.ui.tableWidget.setItem(i, 2, QTableWidgetItem(self.builtDir.ListMovieFiles[i].language))
            self.ui.tableWidget.setItem(i, 3, QTableWidgetItem(self.builtDir.ListMovieFiles[i].quality))

    def getMovie(self, item):
        movie = self.builtDir.ListMovieFiles[item.row()]
        movie.getInformationsFromAPI()
        if(movie.description):
            self.ui.label_3.setText(movie.description)
        else:
            self.ui.label_3.setText("")
        if(movie.picture):
            with urllib.request.urlopen("http://image.tmdb.org/t/p/w500/" + movie.picture) as url:
                data = url.read()
            pixmap = QPixmap()
            pixmap.loadFromData(data)
            pixmap = pixmap.scaled(self.ui.label_4.width(), self.ui.label_4.height())
            self.ui.label_4.setPixmap(pixmap)
        else:
            self.ui.label_4.setPixmap(QPixmap())
            
        return movie
    
    def clickOnItemInMovieTable(self, item):
        self.getMovie(item)

    def doubleClickOnItemInMovieTable(self, item):
        movie = self.getMovie(item)
        movie.read()
