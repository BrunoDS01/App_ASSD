# PyQt5 modules
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QBuffer, QByteArray, QIODevice
from PyQt5.QtCore import QUrl

# Project modules
from src.ui.mainwindow import Ui_MainWindow
from src.Predict_U_Net import Predict_U_Net
from src.AudioPlayer import AudioPlayer

# External modules
import numpy as np
from scipy.io import wavfile
import os
from librosa import resample
import sounddevice as sd

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        #############################################################################
        # Members
        #############################################################################
        self.chosenNet = None
        self.chosenSongAdress = None

        self.songAddressList = []

        self.currentVocalsAudio = None
        self.currentDrumsAudio = None
        self.currentTotalAudio = None

        # self.player = QMediaPlayer()
        self.audio_player = AudioPlayer()

        self.u_net_obj = Predict_U_Net()

        #############################################################################
        # Signals and Slots
        #############################################################################
        self.addSongPushButton.clicked.connect(self.addSong)
        self.processSongPushButton.clicked.connect(self.processSong)

        # Buttons related to reproduce the music
        self.playSongPushButton.clicked.connect(self.playSong)

    #############################################################################
    # Main Window Methods
    #############################################################################
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

        # U-Net case
        if self.chosenNet == 0:
            self.currentVocalsAudio, self.currentDrumsAudio = \
                self.u_net_obj.predictWithU_Net(self.chosenSongAdress)
        
        # OPEN-UNMIX case
        elif self.choseNet == 1:
            self.processWithOpen_Unmix()


    def playSong(self):
        """
        Plays or pauses the resulting song
        """
        self.currentTotalAudio = self.currentVocalsAudio * 1 + self.currentDrumsAudio * 1

        self.currentTotalAudio = self.currentTotalAudio / np.max(np.abs(self.currentTotalAudio))

        audioFinal = resample(self.currentTotalAudio, orig_sr = self.u_net_obj.getSampleRate(), target_sr=22050)
        # Convert the NumPy array to bytes
        #audio_bytes = (self.currentTotalAudio * np.iinfo(np.int16).max).astype(np.int16).tobytes()

        #sd.play(audioFinal, samplerate=22050)

        self.audio_player.play_audio(audioFinal, sample_rate=22050)

        # # Create a QBuffer and set the audio data
        # buffer = QBuffer()
        # buffer.setData(QByteArray(audio_bytes))
        # buffer.open(QIODevice.ReadOnly)

        # self.player.setMedia(QMediaContent(), buffer)

        # # Set the sample rate for the player
        # self.player.setPlaybackRate(22050)

        # # Play the audio
        # self.player.play()


    
    def processWithOpen_Unmix(self):
        """
        Process the chosen song with the trained U-Net architecture.
        It will produce 2 tracks:
            - Vocals
            - Drums
            - Others
        """
        print('Unmix not developed yet')



    
