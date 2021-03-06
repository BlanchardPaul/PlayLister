import urllib.request
from PyQt5 import QtGui, QtCore
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QTableWidgetItem, QTreeWidgetItem
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QRect
import Files
from Files import serial

class PlayListerViewerSerial():

    def __init__(self, mainWindow):
        self.ui = mainWindow
        self.ui.treeWidget.header().setStretchLastSection(False)
        self.ui.treeWidget.header().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.ui.treeWidget.header().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        self.ui.treeWidget.header().setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        self.ui.treeWidget.clicked.connect(
            lambda item: self.clickOnItemInSerialTree(item))
        self.ui.treeWidget.doubleClicked.connect(
            lambda item: self.doubleClickOnItemInSerialTree(item))
        self.ui.label_5.mousePressEvent = self.clickOnDescriptionLabel

    def populateSerialTable(self, builtDir = None):
        if(builtDir):
            self.builtDir = builtDir
        elif not(hasattr(self, 'builtDir')):
            return
        self.ui.treeWidget.clear()
        self.builtDir.ListSerialFiles = sorted(self.builtDir.ListSerialFiles, key=lambda serial: serial.name)
        self.ui.label_6.setPixmap(QPixmap())
        self.ui.label_5.setText("")
        for serial in self.builtDir.ListSerialFiles:
            Ser = QTreeWidgetItem(self.ui.treeWidget, [serial.name])
            for season in serial.ListSeasons:
                Sea = QTreeWidgetItem(Ser, ["Saison " + str(season.number)])
                for episode in season.ListEpisodes:
                    Ep = QTreeWidgetItem(Sea, ["Episode " + str(episode.episode),
                                               episode.quality, episode.language])
                

    def clickOnItemInSerialTree(self, item):
        while(item.parent().row() != -1):
            item = item.parent()
        self.activeSerial = self.builtDir.ListSerialFiles[item.row()]
        self.activeSerial.getInformationsFromAPI()
        if(self.activeSerial.description):
            self.ui.label_5.setText(self.activeSerial.description)
        else:
            self.ui.label_5.setText("No correspondence found in the database. Rename the serial to search for more matches ?")
        if(self.activeSerial.picture):
            with urllib.request.urlopen("http://image.tmdb.org/t/p/w500/" + self.activeSerial.picture) as url:
                data = url.read()
            pixmap = QPixmap()
            pixmap.loadFromData(data)
            pixmap = pixmap.scaled(self.ui.label_6.width(), self.ui.label_6.height())
            self.ui.label_6.setPixmap(pixmap)
        else:
            self.ui.label_6.setPixmap(QPixmap())

    def doubleClickOnItemInSerialTree(self, item):
        if(item.parent().parent().row() == -1):
            return
        self.builtDir.ListSerialFiles[item.parent().parent().row()].ListSeasons[item.parent().row()].ListEpisodes[item.row()].read()

    def clickOnDescriptionLabel(self, event):
        if (not(hasattr(self, 'activeSerial'))):
            return
        text, ok = QInputDialog.getText(None, 'Rename', 'Enter the new name of the serial :')
        if not (ok):
            return
        ListEpisodes = []
        for season in self.activeSerial.ListSeasons:
            for episode in season.ListEpisodes:
                episode.rename(text.lower())
                ListEpisodes.append(episode)
        self.builtDir.ListSerialFiles.remove(self.activeSerial)        
        for episode in ListEpisodes:
            self.builtDir.displayInsertionInSerialList(episode)
        self.populateSerialTable()