"""
    Qué anda:
        - Reproducir y pausar
    Qué falta:
        - Hacer que, al cambiar el volumen, siga desde donde arrancó
        - bOTÓN DE MUTE
        - El botón de stop
        - Mostrar qué segundo de canción está
        - Modificar qué lugar de la canción está

        - Guardar el audio elegido
        - Mostrar los espectrogramas

        - Corregir error de, si no se elige una canción y se la intenta procesar.

        - Hacer toda la parte de OPEN-UNMIX: PRÁCTICAMENTE ESTÁ

    Qué anda mal:
        - Bass no anda (el entrenamiento y la red son malosss)
"""

# PyQt5 modules
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QBuffer, QByteArray, QIODevice
from PyQt5.QtCore import QUrl

# Project modules
from src.ui.mainwindow import Ui_MainWindow
from src.Predict_U_Net import Predict_U_Net
from src.Predict_Open_Unmix import Predict_Open_Unmix
from src.AudioPlayer import AudioPlayer
from src.Song import Song

# External modules
import numpy as np
from scipy.io import wavfile
import os

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        #############################################################################
        # Members
        #############################################################################
        self.chosenNet = None
        self.chosenSongAdress = None
        self.playing = False
        self.paused = False

        self.songAddressList = []

        self.currentTotalAudio = None

        self.currentSong = Song()

        # self.player = QMediaPlayer()
        self.audio_player = AudioPlayer()

        self.u_net_obj = Predict_U_Net()
        self.open_unmix_obj = Predict_Open_Unmix()

        #############################################################################
        # Signals and Slots
        #############################################################################
        self.addSongPushButton.clicked.connect(self.addSong)
        self.processSongPushButton.clicked.connect(self.processSong)

        # Buttons related to reproduce the music
        self.changeVolumePushButton.clicked.connect(self.changeVolume)
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

        currentTotalAudio, currentVocalsAudio, currentDrumsAudio, currentBassAudio, currentOtherAudio = None, None, None, None, None

        sample_rate = 44100

        # U-Net case
        if self.chosenNet == 0:
            currentTotalAudio, currentVocalsAudio, currentDrumsAudio, currentBassAudio, currentOtherAudio\
                = self.u_net_obj.predictWithU_Net(self.chosenSongAdress)
            sample_rate = 8192
        
        # OPEN-UNMIX case
        elif self.chosenNet == 1:
            currentTotalAudio, currentVocalsAudio, currentDrumsAudio, currentBassAudio, currentOtherAudio\
                  = self.open_unmix_obj.predictWithOpenUnmix(self.chosenSongAdress)
            
        self.currentSong.setSongTracksData(sample_rate = sample_rate,
                                           totalAudio=currentTotalAudio,
                                               vocalsAudio=currentVocalsAudio,
                                               drumsAudio=currentDrumsAudio,
                                               bassAudio=currentBassAudio,
                                               otherAudio=currentOtherAudio)


    def changeVolume(self):
        """
        Change the volume of each track, depending on the sliders values.
        """
        self.currentSong.setTracksVolumes(vocalsVolume=self.vocalsVolumeHorizontalSlider.value(),
                                                drumsVolume=self.drumsVolumeHorizontalSlider.value(),
                                                bassVolume=self.bassVolumeHorizontalSlider.value(),
                                                otherVolume=self.otherVolumeHorizontalSlider.value())
            
        self.currentTotalAudio = self.currentSong.getAudio()

        self.playing = False

        # Convert the NumPy array to bytes
        #audio_bytes = (self.currentTotalAudio * np.iinfo(np.int16).max).astype(np.int16).tobytes()

        #sd.play(audioFinal, samplerate=44100)

        # # Create a QBuffer and set the audio data
        # buffer = QBuffer()
        # buffer.setData(QByteArray(audio_bytes))
        # buffer.open(QIODevice.ReadOnly)

        # self.player.setMedia(QMediaContent(), buffer)

        # # Set the sample rate for the player
        # self.player.setPlaybackRate(44100)

        # # Play the audio
        # self.player.play()


    def playSong(self):
        """
        Plays or pauses the resulting song
        """
        if not self.playing:
            self.playing = True
            self.audio_player.play_audio(self.currentTotalAudio, sample_rate=44100)
        
        else:
            if self.paused:
                self.paused = False
                self.audio_player.resume_audio()

            else:
                self.paused = True
                self.audio_player.pause_audio()



    
