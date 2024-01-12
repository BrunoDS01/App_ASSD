"""
    Qué anda:
        - Reproducir y pausar

    Qué falta:
        - Hacer que, al cambiar el volumen, siga desde donde arrancó
        - El botón de stop
        - Mostrar qué segundo de canción está
        - Modificar qué lugar de la canción está
        - Arreglar el tema del puntero y que se pase de la canción (o le falte)

        - Mostrar los espectrogramas

        - Ver si podemos hacer que arranque más rápido

        - Quedarme sólo con las funciones que uso de las librerías
        - Hacer el ejecutable

    Qué anda mal:
        - Bass no anda (el entrenamiento y la red son malosss)
"""

# PyQt5 modules
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox

# Project modules
from src.ui.mainwindow import Ui_MainWindow
from src.Predict_U_Net import Predict_U_Net
from src.Predict_Open_Unmix import Predict_Open_Unmix
from src.AudioPlayer import AudioPlayer
from src.Song import Song

# External modules
import os
from scipy.io.wavfile import write
import numpy as np

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
        self.muteTracks = [False, False, False, False]

        self.songAddressList = []

        self.currentTotalAudio = None

        self.currentSong = Song()

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
        self.muteVocalsPushButton.clicked.connect(self.muteVocals)
        self.muteDrumsPushButton.clicked.connect(self.muteDrums)
        self.muteBassPushButton.clicked.connect(self.muteBass)
        self.muteOtherPushButton.clicked.connect(self.muteOther)

        self.playSongPushButton.clicked.connect(self.playSong)

        self.saveSongPushButton.clicked.connect(self.saveSong)

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
        if file_path == '':
            return
        
        filename = os.path.basename(file_path)

        if file_path not in self.songAddressList:
            self.songAddressList.append(file_path)
            self.songsListWidget.addItem(str(len(self.songAddressList) - 1) + ' - ' + filename)


    def processSong(self):
        """
        The uploaded song will be processed using the selected net and decomposed in its tracks.
        """
        self.chosenNet = self.chooseNetComboBox.currentIndex()
        numberOfSong = self.songsListWidget.currentRow()
        
        if numberOfSong == -1:
            self.show_warning_popup("No ha seleccionado una canción de la lista.")
            return

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
        
        filename = os.path.basename(self.chosenSongAdress)
        self.chosenSongLabel.setText(filename)


    def changeVolume(self):
        """
        Change the volume of each track, depending on the sliders values.
        """
        if self.chosenSongAdress is None:
            self.show_warning_popup("No ha procesado ningún audio")
            return

        self.currentSong.setTracksVolumes(vocalsVolume=self.vocalsVolumeHorizontalSlider.value(),
                                                drumsVolume=self.drumsVolumeHorizontalSlider.value(),
                                                bassVolume=self.bassVolumeHorizontalSlider.value(),
                                                otherVolume=self.otherVolumeHorizontalSlider.value())
            
        self.currentTotalAudio = self.currentSong.getAudio()

        self.playing = False


    def playSong(self):
        """
        Plays or pauses the resulting song
        """
        if self.currentTotalAudio is None:
            self.show_warning_popup("No ha procesado ningún audio")
            return
        
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


    def muteVocals(self):
        self.currentSong.muteUnmuteTrack(0)

        if not self.muteTracks[0]:
            self.muteVocalsPushButton.setStyleSheet("image: url(:/button_images/assets/mute.png);\n"
"background-color: rgb(255, 0, 0);")
            self.muteTracks[0] = True
        else:
            self.muteVocalsPushButton.setStyleSheet("image: url(:/button_images/assets/mute.png);\n")
            self.muteTracks[0] = False

    def muteDrums(self):
        self.currentSong.muteUnmuteTrack(1)

        if not self.muteTracks[1]:
            self.muteDrumsPushButton.setStyleSheet("image: url(:/button_images/assets/mute.png);\n"
"background-color: rgb(255, 0, 0);")
            self.muteTracks[1] = True
        else:
            self.muteDrumsPushButton.setStyleSheet("image: url(:/button_images/assets/mute.png);\n")
            self.muteTracks[1] = False


    def muteBass(self):
        self.currentSong.muteUnmuteTrack(2)

        if not self.muteTracks[2]:
            self.muteBassPushButton.setStyleSheet("image: url(:/button_images/assets/mute.png);\n"
"background-color: rgb(255, 0, 0);")
            self.muteTracks[2] = True
        else:
            self.muteBassPushButton.setStyleSheet("image: url(:/button_images/assets/mute.png);\n")
            self.muteTracks[2] = False


    def muteOther(self):
        self.currentSong.muteUnmuteTrack(3)

        if not self.muteTracks[3]:
            self.muteOtherPushButton.setStyleSheet("image: url(:/button_images/assets/mute.png);\n"
"background-color: rgb(255, 0, 0);")
            self.muteTracks[3] = True
        else:
            self.muteOtherPushButton.setStyleSheet("image: url(:/button_images/assets/mute.png);\n")
            self.muteTracks[3] = False


    def saveSong(self):
        """
        Saves the song in the computer
        """
        if self.currentTotalAudio is None:
            self.show_warning_popup("No ha procesado ningún audio")
            return
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog  # Optional, but can be used to disable native dialogs on some platforms
        file_dialog = QFileDialog()

        default_file_name = "output.wav"
        file_path, selected_filter = QFileDialog.getSaveFileName(None, "Save File", default_file_name, "WAV Files (*.wav);;All Files (*)", options=options)
        
        if file_path == '':
            return
        
        scaled_audio_data = (self.currentTotalAudio * 32767).astype(np.int16)
        write(file_path, 44100, scaled_audio_data)


    def show_warning_popup(self, text):
        warning = QMessageBox()
        warning.setIcon(QMessageBox.Warning)
        warning.setWindowTitle("Warning")
        warning.setText(text)
        warning.setStandardButtons(QMessageBox.Ok)
        warning.exec_()