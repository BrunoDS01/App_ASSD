"""
    Qué falta:
        - Ver el tema de espectrogramas del mismo tamaño

        - Ver si podemos hacer que arranque más rápido

        - Quedarme sólo con las funciones que uso de las librerías
        - Hacer el ejecutable

    Qué anda mal:
        - Bass no anda (el entrenamiento y la red son malosss)
"""

# PyQt5 modules
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QInputDialog

# Project modules
from src.ui.mainwindow import Ui_MainWindow
from src.Predict_U_Net import Predict_U_Net
from src.Predict_Open_Unmix import Predict_Open_Unmix
from src.AudioPlayer import AudioPlayer
from src.Song import Song
from src.MPLClasses import SpectogramPlot

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
        self.newSongToProcess = False
        self.volumesWereChanged = False
        self.paused = False
        self.muteTracks = [False, False, False, False]

        self.songAddressList = []
        self.songIsYoutube = []

        self.currentTotalAudio = None

        self.currentSong = Song()

        self.audio_player = AudioPlayer(callback=self.updateCurrentTime)

        self.u_net_obj = Predict_U_Net()
        self.open_unmix_obj = Predict_Open_Unmix()

        self.vocalsSpectogramPlot = SpectogramPlot()
        self.drumsSpectogramPlot = SpectogramPlot()
        self.bassSpectogramPlot = SpectogramPlot()
        self.othersSpectogramPlot = SpectogramPlot()

        self.specVerticalLayout.addWidget(self.vocalsSpectogramPlot.navigationToolBar)
        self.specVerticalLayout.addWidget(self.vocalsSpectogramPlot)

        self.specVerticalLayout.addWidget(self.drumsSpectogramPlot.navigationToolBar)
        self.specVerticalLayout.addWidget(self.drumsSpectogramPlot)

        self.specVerticalLayout.addWidget(self.bassSpectogramPlot.navigationToolBar)
        self.specVerticalLayout.addWidget(self.bassSpectogramPlot)

        self.specVerticalLayout.addWidget(self.othersSpectogramPlot.navigationToolBar)
        self.specVerticalLayout.addWidget(self.othersSpectogramPlot)


        #############################################################################
        # Signals and Slots
        #############################################################################
        self.addSongPushButton.clicked.connect(self.addSong)
        #self.addSongYoutubePushButton.clicked.connect(self.addSongYoutube)

        self.processSongPushButton.clicked.connect(self.processSong)

        # Buttons to show spectograms
        self.vocalsCheckBox.clicked.connect(self.updateShowSpectograms)
        self.drumsCheckBox.clicked.connect(self.updateShowSpectograms)
        self.bassCheckBox.clicked.connect(self.updateShowSpectograms)
        self.othersCheckBox.clicked.connect(self.updateShowSpectograms)

        # Buttons related to reproduce the music
        self.changeVolumePushButton.clicked.connect(self.changeVolume)
        self.muteVocalsPushButton.clicked.connect(self.muteVocals)
        self.muteDrumsPushButton.clicked.connect(self.muteDrums)
        self.muteBassPushButton.clicked.connect(self.muteBass)
        self.muteOtherPushButton.clicked.connect(self.muteOther)

        self.musicScrollerHorizontalSlider.sliderMoved.connect(self.timeChanged)
        self.musicScrollerHorizontalSlider.sliderReleased.connect(self.changeAudioTime)

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
        file_path, _ = file_dialog.getOpenFileName(self, 'Open File', '', 'Audio Files (*.mp3 *.wav);; All Files (*)', options=options)
        if file_path == '':
            return
        
        filename = os.path.basename(file_path)

        if file_path not in self.songAddressList:
            self.songAddressList.append(file_path)
            self.songIsYoutube.append(False)
            self.songsListWidget.addItem(str(len(self.songAddressList) - 1) + ' - ' + filename)

    def addSongYoutube(self):
        """
        Load a song from the computer. It will be added to the list of songs.
        """
        inputDialog = QInputDialog()
        link, ok_pressed = inputDialog.getText(self, 'Enter Link', 'Link:')

        if not ok_pressed:
            return

        if link not in self.songAddressList:
            self.songAddressList.append(link)
            self.songIsYoutube.append(True)
            self.songsListWidget.addItem(str(len(self.songAddressList) - 1) + ' - ' + link)


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

        filename = self.chosenSongAdress
        
        # Show that the song will be processed
        if not self.songIsYoutube[numberOfSong]:
            filename = os.path.basename(self.chosenSongAdress)
        

        result = self.showMessageBox("Procesar canción", "Está seguro de procesar " + filename)
        
        if result != QMessageBox.Yes:
            return

        self.show_popup("A procesar " + filename)

        # U-Net case
        if self.chosenNet == 0:
            currentTotalAudio, currentVocalsAudio, currentDrumsAudio, currentBassAudio, currentOtherAudio\
                = self.u_net_obj.predictWithU_Net(self.chosenSongAdress, self.songIsYoutube[numberOfSong])
            sample_rate = 8192
        
        # OPEN-UNMIX case
        elif self.chosenNet == 1:
            currentTotalAudio, currentVocalsAudio, currentDrumsAudio, currentBassAudio, currentOtherAudio\
                  = self.open_unmix_obj.predictWithOpenUnmix(self.chosenSongAdress, self.songIsYoutube[numberOfSong])
            
        self.currentSong.setSongTracksData(sample_rate = sample_rate,
                                           totalAudio=currentTotalAudio,
                                               vocalsAudio=currentVocalsAudio,
                                               drumsAudio=currentDrumsAudio,
                                               bassAudio=currentBassAudio,
                                               otherAudio=currentOtherAudio)

        self.processingLabel.setText(filename)

        # Show that the song was processed
        self.show_popup("Procesado! " + filename)

        self.showSpectograms();

        self.newSongToProcess = True


    def changeVolume(self):
        """
        Change the volume of each track, depending on the sliders values.
        """
        if self.chosenSongAdress is None:
            self.show_warning_popup("No ha procesado ningún audio")
            return

        self.currentSong.setTracksVolumes(totalVolume=self.globalVolumeHorizontalSlider.value(),
                                          vocalsVolume=self.vocalsVolumeHorizontalSlider.value(),
                                                drumsVolume=self.drumsVolumeHorizontalSlider.value(),
                                                bassVolume=self.bassVolumeHorizontalSlider.value(),
                                                otherVolume=self.otherVolumeHorizontalSlider.value())
            
        self.currentTotalAudio = self.currentSong.getAudio()

        self.volumesWereChanged = True

        filename = os.path.basename(self.chosenSongAdress)

        if not self.newSongToProcess:
            self.audio_player.change_audio(self.currentTotalAudio, sample_rate=44100)

        else:
            self.chosenSongLabel.setText(filename)

        self.show_popup("Volúmenes cambiados " + filename)


    def playSong(self):
        """
        Plays or pauses the resulting song
        """
        if self.currentTotalAudio is None:
            self.show_warning_popup("No ha procesado ningún audio")
            return
        
        # If the new song is loaded and processed:
        if self.newSongToProcess and self.volumesWereChanged:
            self.newSongToProcess = False
            self.volumesWereChanged = False

            filename = os.path.basename(self.chosenSongAdress)
            self.chosenSongLabel.setText(filename)

            self.audio_player.stop_audio()
            self.audio_player.play_audio(self.currentTotalAudio, sample_rate=44100)
            self.changeAudioTotalDurationLabel()

        # If a new song was loaded, but not processed
        # Or         
        # If the song is the same as the previous one
        else:
            if self.paused:
                self.paused = False
                self.playSongPushButton.setStyleSheet("image: url(:/button_images/assets/pause_simb.png);")
                self.audio_player.resume_audio()

            else:
                self.paused = True
                self.playSongPushButton.setStyleSheet("image: url(:/button_images/assets/play_simb.png);")
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
        file_path, _ = QFileDialog.getSaveFileName(None, "Save File", default_file_name, "WAV Files (*.wav);;All Files (*)", options=options)
        
        if file_path == '':
            return
        
        scaled_audio_data = (self.currentTotalAudio * 32767).astype(np.int16)
        write(file_path, 44100, scaled_audio_data)


    def timeChanged(self, number):
        totalTime = self.audio_player.getAudioTotalTime()

        time = number / 3600 * totalTime
        seconds = int(time % 60)
        minutes = int(time // 60)

        text = str(minutes) + ":" + str(seconds).zfill(2)

        self.currentSongMinuteLabel.setText(text)

    def changeAudioTotalDurationLabel(self):
        time = self.audio_player.getAudioTotalTime()

        seconds = int(time % 60)
        minutes = int(time // 60)

        text = str(minutes) + ":" + str(seconds).zfill(2)

        self.totalSongDurationLabel.setText(text)


    def updateCurrentTime(self, time):
        if not self.musicScrollerHorizontalSlider.isSliderDown():
            seconds = int(time % 60)
            minutes = int(time // 60)

            text = str(minutes) + ":" + str(seconds).zfill(2)

            position = int(time / self.audio_player.getAudioTotalTime() * 3600)

            self.currentSongMinuteLabel.setText(text)
            self.musicScrollerHorizontalSlider.setValue(position)


    def changeAudioTime(self):
        self.audio_player.setAudioPlayedPercentage(self.musicScrollerHorizontalSlider.value() * 100 / 3600)


    #############################################################################
    # Spectograms Methods
    #############################################################################
    def updateShowSpectograms(self):
        if self.vocalsCheckBox.isChecked():
            self.vocalsSpectogramPlot.showPlot()
        else:
            self.vocalsSpectogramPlot.hidePlot()

        if self.drumsCheckBox.isChecked():
            self.drumsSpectogramPlot.showPlot()
        else:
            self.drumsSpectogramPlot.hidePlot()
        
        if self.bassCheckBox.isChecked():
            self.bassSpectogramPlot.showPlot()
        else:
            self.bassSpectogramPlot.hidePlot()
        
        if self.othersCheckBox.isChecked():
            self.othersSpectogramPlot.showPlot()
        else:
            self.othersSpectogramPlot.hidePlot()


    def showSpectograms(self):
        self.vocalsSpectogramPlot.plot(self.currentSong.vocalsAudio, sample_rate = 44100, title="Vocals")
        self.drumsSpectogramPlot.plot(self.currentSong.drumsAudio, sample_rate = 44100, title="Drums")
        self.bassSpectogramPlot.plot(self.currentSong.bassAudio, sample_rate = 44100, title="Bass")
        self.othersSpectogramPlot.plot(self.currentSong.otherAudio, sample_rate = 44100, title="Others")


    #############################################################################
    # Pop ups
    #############################################################################
    def show_warning_popup(self, text):
        """
        Warning PopUp
        """
        warning = QMessageBox()
        warning.setIcon(QMessageBox.Warning)
        warning.setWindowTitle("Warning")
        warning.setText(text)
        warning.setStandardButtons(QMessageBox.Ok)
        warning.exec_()


    def show_popup(self, text):
        """
        Warning PopUp
        """
        warning = QMessageBox()
        warning.setWindowTitle("Atención")
        warning.setText(text)
        warning.setStandardButtons(QMessageBox.Ok)
        warning.exec_()


    def showMessageBox(self, title, message):
        """
        Accept/Cancel pop up
        """
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Question)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        msg_box.setDefaultButton(QMessageBox.Cancel)

        return msg_box.exec_()        
    
    #############################################################################
    # Shut Down
    #############################################################################
    def shutDown(self):
        self.audio_player.stop_audio()