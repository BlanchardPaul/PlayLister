# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1173, 800)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setStyleSheet("")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalWidget = QtWidgets.QWidget(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalWidget.sizePolicy().hasHeightForWidth())
        self.horizontalWidget.setSizePolicy(sizePolicy)
        self.horizontalWidget.setMaximumSize(QtCore.QSize(100000, 150))
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalWidget)
        font = QtGui.QFont()
        font.setFamily("Bernard MT Condensed")
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.gridFrame = QtWidgets.QFrame(self.horizontalWidget)
        self.gridFrame.setMinimumSize(QtCore.QSize(900, 0))
        self.gridFrame.setObjectName("gridFrame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.gridFrame)
        self.horizontalLayout_4.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.gridFrame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setText("")
        self.label_2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.pushButton = QtWidgets.QPushButton(self.gridFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(200, 0))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_4.addWidget(self.pushButton, 0, QtCore.Qt.AlignBottom)
        self.horizontalLayout.addWidget(self.gridFrame)
        self.verticalLayout.addWidget(self.horizontalWidget)
        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("background-color: black;")
        self.tabWidget.setObjectName("tabWidget")
        self.movies = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.movies.sizePolicy().hasHeightForWidth())
        self.movies.setSizePolicy(sizePolicy)
        self.movies.setMinimumSize(QtCore.QSize(100, 100))
        self.movies.setObjectName("movies")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.movies)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalWidget1 = QtWidgets.QWidget(self.movies)
        self.horizontalWidget1.setAutoFillBackground(False)
        self.horizontalWidget1.setStyleSheet("background-color: black;")
        self.horizontalWidget1.setObjectName("horizontalWidget1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalWidget1)
        self.horizontalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tableWidget = QtWidgets.QTableWidget(self.horizontalWidget1)
        self.tableWidget.setMinimumSize(QtCore.QSize(800, 0))
        self.tableWidget.setMaximumSize(QtCore.QSize(800, 16777215))
        self.tableWidget.setAutoFillBackground(True)
        self.tableWidget.setStyleSheet("background-color: grey;\n"
"color: black;")
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(170)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget.verticalHeader().setSortIndicatorShown(True)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.horizontalLayout_3.addWidget(self.tableWidget)
        self.label_4 = QtWidgets.QLabel(self.horizontalWidget1)
        self.label_4.setMinimumSize(QtCore.QSize(300, 0))
        self.label_4.setMaximumSize(QtCore.QSize(300, 16777215))
        self.label_4.setAutoFillBackground(False)
        self.label_4.setStyleSheet("background-color: black;")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.verticalLayout_2.addWidget(self.horizontalWidget1)
        self.label_3 = QtWidgets.QLabel(self.movies)
        self.label_3.setMinimumSize(QtCore.QSize(0, 90))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setStyleSheet("background-color: black;\n"
"color: white;")
        self.label_3.setText("")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.tabWidget.addTab(self.movies, "")
        self.serials = QtWidgets.QWidget()
        self.serials.setObjectName("serials")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.serials)
        self.verticalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.treeWidget = QtWidgets.QTreeWidget(self.serials)
        self.treeWidget.setMinimumSize(QtCore.QSize(800, 0))
        self.treeWidget.setMaximumSize(QtCore.QSize(800, 16777215))
        self.treeWidget.setStyleSheet("background-color: grey;\n"
"color: black;")
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.header().setDefaultSectionSize(300)
        self.horizontalLayout_6.addWidget(self.treeWidget)
        self.label_6 = QtWidgets.QLabel(self.serials)
        self.label_6.setMinimumSize(QtCore.QSize(300, 0))
        self.label_6.setMaximumSize(QtCore.QSize(300, 16777215))
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.label_5 = QtWidgets.QLabel(self.serials)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QtCore.QSize(0, 90))
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 90))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: white")
        self.label_5.setText("")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.tabWidget.addTab(self.serials, "")
        self.unknowns = QtWidgets.QWidget()
        self.unknowns.setObjectName("unknowns")
        self.tabWidget.addTab(self.unknowns, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "PlayLister"))
        self.pushButton.setText(_translate("MainWindow", "Choose directory"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Year"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Language"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Quality"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.movies), _translate("MainWindow", "Movies"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "Serial"))
        self.treeWidget.headerItem().setText(1, _translate("MainWindow", "Quality"))
        self.treeWidget.headerItem().setText(2, _translate("MainWindow", "Language"))
        self.label_6.setText(_translate("MainWindow", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.serials), _translate("MainWindow", "Serials"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.unknowns), _translate("MainWindow", "Unknowns"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

