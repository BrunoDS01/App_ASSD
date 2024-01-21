# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(728, 553)
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
        self.songsListWidget = QtWidgets.QListWidget(self.frame)
        self.songsListWidget.setObjectName("songsListWidget")
        self.verticalLayout.addWidget(self.songsListWidget)
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
        self.tabWidget_2.setMinimumSize(QtCore.QSize(500, 0))
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tabWidget_2Page1 = QtWidgets.QWidget()
        self.tabWidget_2Page1.setObjectName("tabWidget_2Page1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tabWidget_2Page1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.widget_3 = QtWidgets.QWidget(self.tabWidget_2Page1)
        self.widget_3.setObjectName("widget_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.currentSongMiniteLabel = QtWidgets.QLabel(self.widget_3)
        self.currentSongMiniteLabel.setObjectName("currentSongMiniteLabel")
        self.gridLayout_4.addWidget(self.currentSongMiniteLabel, 2, 0, 1, 1)
        self.musicScrollerHorizontalSlider = QtWidgets.QSlider(self.widget_3)
        self.musicScrollerHorizontalSlider.setMaximum(3600)
        self.musicScrollerHorizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.musicScrollerHorizontalSlider.setObjectName("musicScrollerHorizontalSlider")
        self.gridLayout_4.addWidget(self.musicScrollerHorizontalSlider, 2, 1, 1, 1)
        self.totalSongDurationLabel = QtWidgets.QLabel(self.widget_3)
        self.totalSongDurationLabel.setObjectName("totalSongDurationLabel")
        self.gridLayout_4.addWidget(self.totalSongDurationLabel, 2, 3, 1, 1)
        self.playSongPushButton = QtWidgets.QPushButton(self.widget_3)
        self.playSongPushButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.playSongPushButton.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.playSongPushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.playSongPushButton.setStyleSheet("image: url(:/button_images/assets/play_simb.png);")
        self.playSongPushButton.setText("")
        self.playSongPushButton.setObjectName("playSongPushButton")
        self.gridLayout_4.addWidget(self.playSongPushButton, 0, 1, 1, 1)
        self.chosenSongLabel = QtWidgets.QLabel(self.widget_3)
        self.chosenSongLabel.setText("")
        self.chosenSongLabel.setObjectName("chosenSongLabel")
        self.gridLayout_4.addWidget(self.chosenSongLabel, 3, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.widget_3)
        self.label_7.setObjectName("label_7")
        self.gridLayout_4.addWidget(self.label_7, 3, 0, 1, 1)
        self.gridLayout_2.addWidget(self.widget_3, 2, 0, 1, 1)
        self.saveSongPushButton = QtWidgets.QPushButton(self.tabWidget_2Page1)
        self.saveSongPushButton.setObjectName("saveSongPushButton")
        self.gridLayout_2.addWidget(self.saveSongPushButton, 3, 0, 1, 1)
        self.stackedWidget = QtWidgets.QStackedWidget(self.tabWidget_2Page1)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.vocalsVolumeHorizontalSlider = QtWidgets.QSlider(self.page)
        self.vocalsVolumeHorizontalSlider.setMaximum(100)
        self.vocalsVolumeHorizontalSlider.setProperty("value", 100)
        self.vocalsVolumeHorizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.vocalsVolumeHorizontalSlider.setObjectName("vocalsVolumeHorizontalSlider")
        self.gridLayout_3.addWidget(self.vocalsVolumeHorizontalSlider, 0, 2, 1, 1)
        self.otherVolumeHorizontalSlider = QtWidgets.QSlider(self.page)
        self.otherVolumeHorizontalSlider.setMaximum(100)
        self.otherVolumeHorizontalSlider.setProperty("value", 100)
        self.otherVolumeHorizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.otherVolumeHorizontalSlider.setObjectName("otherVolumeHorizontalSlider")
        self.gridLayout_3.addWidget(self.otherVolumeHorizontalSlider, 3, 2, 1, 1)
        self.drumsVolumeHorizontalSlider = QtWidgets.QSlider(self.page)
        self.drumsVolumeHorizontalSlider.setMaximum(100)
        self.drumsVolumeHorizontalSlider.setProperty("value", 100)
        self.drumsVolumeHorizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.drumsVolumeHorizontalSlider.setObjectName("drumsVolumeHorizontalSlider")
        self.gridLayout_3.addWidget(self.drumsVolumeHorizontalSlider, 1, 2, 1, 1)
        self.changeVolumePushButton = QtWidgets.QPushButton(self.page)
        self.changeVolumePushButton.setObjectName("changeVolumePushButton")
        self.gridLayout_3.addWidget(self.changeVolumePushButton, 6, 0, 1, 3)
        self.label_4 = QtWidgets.QLabel(self.page)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 1, 0, 1, 1)
        self.bassVolumeHorizontalSlider = QtWidgets.QSlider(self.page)
        self.bassVolumeHorizontalSlider.setMaximum(100)
        self.bassVolumeHorizontalSlider.setProperty("value", 100)
        self.bassVolumeHorizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.bassVolumeHorizontalSlider.setObjectName("bassVolumeHorizontalSlider")
        self.gridLayout_3.addWidget(self.bassVolumeHorizontalSlider, 2, 2, 1, 1)
        self.muteDrumsPushButton = QtWidgets.QPushButton(self.page)
        self.muteDrumsPushButton.setStyleSheet("image: url(:/button_images/assets/mute.png);")
        self.muteDrumsPushButton.setText("")
        self.muteDrumsPushButton.setObjectName("muteDrumsPushButton")
        self.gridLayout_3.addWidget(self.muteDrumsPushButton, 1, 1, 1, 1)
        self.muteOtherPushButton = QtWidgets.QPushButton(self.page)
        self.muteOtherPushButton.setStyleSheet("image: url(:/button_images/assets/mute.png);")
        self.muteOtherPushButton.setText("")
        self.muteOtherPushButton.setObjectName("muteOtherPushButton")
        self.gridLayout_3.addWidget(self.muteOtherPushButton, 3, 1, 1, 1)
        self.muteBassPushButton = QtWidgets.QPushButton(self.page)
        self.muteBassPushButton.setStyleSheet("image: url(:/button_images/assets/mute.png);")
        self.muteBassPushButton.setText("")
        self.muteBassPushButton.setObjectName("muteBassPushButton")
        self.gridLayout_3.addWidget(self.muteBassPushButton, 2, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.page)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.page)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 3, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.page)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 2, 0, 1, 1)
        self.muteVocalsPushButton = QtWidgets.QPushButton(self.page)
        self.muteVocalsPushButton.setStyleSheet("image: url(:/button_images/assets/mute.png);")
        self.muteVocalsPushButton.setText("")
        self.muteVocalsPushButton.setObjectName("muteVocalsPushButton")
        self.gridLayout_3.addWidget(self.muteVocalsPushButton, 0, 1, 1, 1)
        self.globalVolumeHorizontalSlider = QtWidgets.QSlider(self.page)
        self.globalVolumeHorizontalSlider.setProperty("value", 99)
        self.globalVolumeHorizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.globalVolumeHorizontalSlider.setObjectName("globalVolumeHorizontalSlider")
        self.gridLayout_3.addWidget(self.globalVolumeHorizontalSlider, 5, 1, 1, 2)
        self.label_8 = QtWidgets.QLabel(self.page)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 5, 0, 1, 1)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.gridLayout_2.addWidget(self.stackedWidget, 0, 0, 1, 1)
        self.tabWidget_2.addTab(self.tabWidget_2Page1, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_4 = QtWidgets.QWidget(self.tab)
        self.widget_4.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.vocalsCheckBox = QtWidgets.QCheckBox(self.widget_4)
        self.vocalsCheckBox.setChecked(True)
        self.vocalsCheckBox.setObjectName("vocalsCheckBox")
        self.horizontalLayout_3.addWidget(self.vocalsCheckBox)
        self.drumsCheckBox = QtWidgets.QCheckBox(self.widget_4)
        self.drumsCheckBox.setChecked(True)
        self.drumsCheckBox.setObjectName("drumsCheckBox")
        self.horizontalLayout_3.addWidget(self.drumsCheckBox)
        self.bassCheckBox = QtWidgets.QCheckBox(self.widget_4)
        self.bassCheckBox.setChecked(True)
        self.bassCheckBox.setObjectName("bassCheckBox")
        self.horizontalLayout_3.addWidget(self.bassCheckBox)
        self.othersCheckBox = QtWidgets.QCheckBox(self.widget_4)
        self.othersCheckBox.setChecked(True)
        self.othersCheckBox.setObjectName("othersCheckBox")
        self.horizontalLayout_3.addWidget(self.othersCheckBox)
        self.verticalLayout_2.addWidget(self.widget_4)
        self.widget_5 = QtWidgets.QWidget(self.tab)
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.vocalsSpecVerticalLayout = QtWidgets.QVBoxLayout()
        self.vocalsSpecVerticalLayout.setObjectName("vocalsSpecVerticalLayout")
        self.verticalLayout_3.addLayout(self.vocalsSpecVerticalLayout)
        self.drumsSpecVerticalLayout = QtWidgets.QVBoxLayout()
        self.drumsSpecVerticalLayout.setObjectName("drumsSpecVerticalLayout")
        self.verticalLayout_3.addLayout(self.drumsSpecVerticalLayout)
        self.bassSpecVerticalLayout = QtWidgets.QVBoxLayout()
        self.bassSpecVerticalLayout.setObjectName("bassSpecVerticalLayout")
        self.verticalLayout_3.addLayout(self.bassSpecVerticalLayout)
        self.othersSpecVerticalLayout = QtWidgets.QVBoxLayout()
        self.othersSpecVerticalLayout.setObjectName("othersSpecVerticalLayout")
        self.verticalLayout_3.addLayout(self.othersSpecVerticalLayout)
        self.verticalLayout_2.addWidget(self.widget_5)
        self.tabWidget_2.addTab(self.tab, "")
        self.horizontalLayout.addWidget(self.tabWidget_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 728, 21))
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
        self.tabWidget_2.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Music Source Separation - Test App"))
        self.label.setText(_translate("MainWindow", "Agregar canción"))
        self.label_2.setText(_translate("MainWindow", "Red a utilizar:"))
        self.chooseNetComboBox.setItemText(0, _translate("MainWindow", "U-Net (simple)"))
        self.chooseNetComboBox.setItemText(1, _translate("MainWindow", "OPEN-UNMIX"))
        self.processSongPushButton.setText(_translate("MainWindow", "Procesar canción"))
        self.currentSongMiniteLabel.setText(_translate("MainWindow", "00:00"))
        self.totalSongDurationLabel.setText(_translate("MainWindow", "--:--"))
        self.label_7.setText(_translate("MainWindow", "Canción:"))
        self.saveSongPushButton.setText(_translate("MainWindow", "Guardar canción procesada"))
        self.changeVolumePushButton.setText(_translate("MainWindow", "Procesar cambio de volúmenes"))
        self.label_4.setText(_translate("MainWindow", "Drums"))
        self.label_3.setText(_translate("MainWindow", "Vocals"))
        self.label_5.setText(_translate("MainWindow", "Other"))
        self.label_6.setText(_translate("MainWindow", "Bass"))
        self.label_8.setText(_translate("MainWindow", "Master"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tabWidget_2Page1), _translate("MainWindow", "Tracks"))
        self.vocalsCheckBox.setText(_translate("MainWindow", "Vocals"))
        self.drumsCheckBox.setText(_translate("MainWindow", "Drums"))
        self.bassCheckBox.setText(_translate("MainWindow", "Bass"))
        self.othersCheckBox.setText(_translate("MainWindow", "Others"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab), _translate("MainWindow", "Espectrogramas"))
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
