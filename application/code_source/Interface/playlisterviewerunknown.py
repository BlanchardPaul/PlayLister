import urllib.request
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QTableWidgetItem
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QRect
import Files
import Interface
from Interface.moviedialog import *
from Interface.serialdialog import *

class PlayListerViewerUnknown():

    def __init__(self, playListerViewer):
        self.playListerViewer = playListerViewer
        self.ui = playListerViewer.ui
        self.ui.label_8.hide()
        self.ui.label_9.hide()
        self.ui.tableWidget_2.clicked.connect(
            lambda item: self.clickOnItemInUnknownTable(item))
        self.ui.tableWidget_2.doubleClicked.connect(
            lambda item: self.doubleClickOnItemInUnknownTable(item))
        self.ui.label_9.mousePressEvent = self.clickOnCreateMovie
        self.ui.label_8.mousePressEvent = self.clickOnCreateSerial
        
    def populateUnknownTable(self, builtDir = None):
        if(builtDir):
            self.builtDir = builtDir
        elif not(hasattr(self, 'builtDir')):
            return
        self.ui.label_8.hide()
        self.ui.label_9.hide()
        self.ui.label_7.setText("")
        for i in reversed(range(self.ui.tableWidget_2.rowCount())):
            self.ui.tableWidget_2.removeRow(i)
        for i in range(len(self.builtDir.ListUnknownFiles)):
            self.ui.tableWidget_2.insertRow(i)
            self.ui.tableWidget_2.setItem(i, 0, QTableWidgetItem(self.builtDir.ListUnknownFiles[i].name))
    
    def clickOnItemInUnknownTable(self, item):
        self.activeUnknown = self.builtDir.ListUnknownFiles[item.row()]
        self.index = item.row()
        self.ui.label_7.setText("Selected file : " + self.activeUnknown.name)
        self.ui.label_8.show()
        self.ui.label_9.show()
        
    def doubleClickOnItemInUnknownTable(self, item):
        self.activeUnknown = self.builtDir.ListUnknownFiles[item.row()]
        self.activeUnknown.read()
        self.index = item.row()
        self.ui.label_7.setText("Selected file : " + self.activeUnknown.name)
        self.ui.label_8.show()
        self.ui.label_9.show()
        
    def clickOnCreateMovie(self, event):
        form = MovieDialog()
        form.setupUi(form)
        if(form.exec_() == 0):
            return
        if(form.lineEdit.text() == ""):
            self.warningFieldNotTyped("The name should be precised.")
            return
        elif(form.lineEdit_2.text() == ""):
            self.warningFieldNotTyped("The quality should be precised.")
            return
        elif(form.lineEdit_3.text() == ""):
            self.warningFieldNotTyped("The language should be precised.")
            return
        self.activeUnknown.rename(form.lineEdit.text() + " " + form.dateEdit.date().toString('yyyy') 
                                  + " " + form.lineEdit_2.text() + " " + form.lineEdit_3.text() + " ")
        self.builtDir.ListFiles.append(self.activeUnknown.path)
        self.builtDir.displayFilesIntoMediaLists()
        self.playListerViewer.movieWindow.populateMovieTable()
        del self.builtDir.ListUnknownFiles[self.index]
        self.populateUnknownTable()
        
    def clickOnCreateSerial(self, event):
        form = SerialDialog()
        form.setupUi(form)
        if(form.exec_() == 0):
            return
        if(form.lineEdit.text() == ""):
            self.warningFieldNotTyped("The name should be precised.")
            return
        elif(form.lineEdit_4.text() == ""):
            self.warningFieldNotTyped("The season should be precised.")
            return
        elif(not self.checkDigit(form.lineEdit_4.text(), 2, "season")):
            return
        elif(form.lineEdit_5.text() == ""):
            self.warningFieldNotTyped("The episode should be precised.")
            return
        elif(not self.checkDigit(form.lineEdit_5.text(), None, "episode")):
            return
        elif(form.lineEdit_2.text() == ""):
            self.warningFieldNotTyped("The quality should be precised.")
            return
        elif(form.lineEdit_3.text() == ""):
            self.warningFieldNotTyped("The language should be precised.")
            return
        self.activeUnknown.rename(form.lineEdit.text() + " S" + form.lineEdit_4.text() + "E" +
                                 form.lineEdit_5.text() + " " + form.lineEdit_2.text() + " " + form.lineEdit_3.text() + " ")
        self.builtDir.ListFiles.append(self.activeUnknown.path)
        self.builtDir.displayFilesIntoMediaLists()
        self.playListerViewer.serialWindow.populateSerialTable()
        del self.builtDir.ListUnknownFiles[self.index]
        self.populateUnknownTable()

    def checkDigit(self, field, exceptedDigit, mediaType):
        try:
            int(field)
        except ValueError:
            self.warningFieldNotTyped("The field for " + mediaType + " should only comport numbers.")
            return False
        if(exceptedDigit != None and len(field) != exceptedDigit):
            self.warningFieldNotTyped("The field for " + mediaType + " does not comport enought or comport too much numbers (excepted = " + str(exceptedDigit) + " ).")
            return False
        return True
    
    def warningFieldNotTyped(self, txt):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText(txt)
        msg.setWindowTitle("Error during parsing")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()