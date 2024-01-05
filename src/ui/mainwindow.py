# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(794, 604)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMaximumSize(QtCore.QSize(300, 16777215))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.addSongPushButton = QtWidgets.QPushButton(self.widget)
        self.addSongPushButton.setMaximumSize(QtCore.QSize(30, 16777215))
        self.addSongPushButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.addSongPushButton.setStyleSheet("image: url(:/button_images/assets/mas_simb.png);")
        self.addSongPushButton.setText("")
        self.addSongPushButton.setAutoDefault(False)
        self.addSongPushButton.setDefault(False)
        self.addSongPushButton.setObjectName("addSongPushButton")
        self.gridLayout.addWidget(self.addSongPushButton, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.widget)
        self.listWidget = QtWidgets.QListWidget(self.frame)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.widget_2 = QtWidgets.QWidget(self.frame)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.chooseNetComboBox = QtWidgets.QComboBox(self.widget_2)
        self.chooseNetComboBox.setObjectName("chooseNetComboBox")
        self.chooseNetComboBox.addItem("")
        self.chooseNetComboBox.addItem("")
        self.horizontalLayout_2.addWidget(self.chooseNetComboBox)
        self.verticalLayout.addWidget(self.widget_2)
        self.processSongPushButton = QtWidgets.QPushButton(self.frame)
        self.processSongPushButton.setObjectName("processSongPushButton")
        self.verticalLayout.addWidget(self.processSongPushButton)
        self.horizontalLayout.addWidget(self.frame)
        self.tabWidget_2 = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tabWidget_2Page1 = QtWidgets.QWidget()
        self.tabWidget_2Page1.setObjectName("tabWidget_2Page1")
        self.tabWidget_2.addTab(self.tabWidget_2Page1, "")
        self.horizontalLayout.addWidget(self.tabWidget_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 794, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuSave = QtWidgets.QMenu(self.menubar)
        self.menuSave.setObjectName("menuSave")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSave.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Music Source Separation - Test App"))
        self.label.setText(_translate("MainWindow", "Agregar canción"))
        self.label_2.setText(_translate("MainWindow", "Red a utilizar:"))
        self.chooseNetComboBox.setItemText(0, _translate("MainWindow", "U-Net (simple)"))
        self.chooseNetComboBox.setItemText(1, _translate("MainWindow", "OPEN-UNMIX"))
        self.processSongPushButton.setText(_translate("MainWindow", "Procesar canción"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tabWidget_2Page1), _translate("MainWindow", "Tracks"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuSave.setTitle(_translate("MainWindow", "Save"))

from src.resources import assd_resources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

