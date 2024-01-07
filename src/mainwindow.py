# PyQt5 modules
from PyQt5.QtWidgets import QMainWindow, QFileDialog

# Project modules
from src.ui.mainwindow import Ui_MainWindow
from src.Predict_U_Net import predictWithU_Net

# Other modules
import numpy as np
import scipy as sp
import os


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        # Members
        self.chosenNet = None
        self.chosenSongAdress = None

        self.songAddressList = []

        # Signals and Slots
        self.addSongPushButton.clicked.connect(self.addSong)
        self.processSongPushButton.clicked.connect(self.processSong)

    def addSong(self):
        """
        Load a song from the computer. It will be added to the list of songs.
        """
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog  # Optional, but can be used to disable native dialogs on some platforms
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, 'Open File', '', 'WAV Files (*.wav);; All Files (*)', options=options)
        filename = os.path.basename(file_path)

        self.songAddressList.append(file_path)

        self.songsListWidget.addItem(str(len(self.songAddressList) - 1) + ' - ' + filename)


    def processSong(self):
        """
        The uploaded song will be processed using the selected net and decomposed in its tracks.
        """
        self.chosenNet = self.chooseNetComboBox.currentIndex()
        numberOfSong = self.songsListWidget.currentRow()
        self.chosenSongAdress = self.songAddressList[numberOfSong]
        

        if self.chosenNet == 0:
            predictWithU_Net(self.chosenSongAdress)
        
        elif self.choseNet == 1:
            self.processWithOpen_Unmix()


    def processWithU_Net(self):
        """
        Process the chosen song with the trained U-Net architecture.
        It will produce 2 tracks:
            - Vocals
            - Drums
            - Others
        """
        return 0



    
    def processWithOpen_Unmix(self):
        """
        Process the chosen song with the trained U-Net architecture.
        It will produce 2 tracks:
            - Vocals
            - Drums
            - Others
        """
        return 0



    
