from PyQt5 import QtCore, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import numpy as np

class MplCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        super(MplCanvas, self).__init__(self.fig)
        self.navigationToolBar = NavigationToolbar(self, parent)


class SpectogramPlot(MplCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        super().__init__(parent=None, width=5, height=4, dpi=100)

    def plot(self, audio_data, sample_rate = 44100, title = ''):
        _ = self.axes.specgram(audio_data, Fs=sample_rate, cmap='viridis')

        # Adjust the plot settings for better visualization
        self.axes.set_xlabel('Time (s)')
        self.axes.set_ylabel('Frequency (Hz)')
        self.axes.set_title(title + ' ' + 'Spectrogram')
        # self.fig.colorbar(label='Amplitude (dB)')
        self.show()
        self.navigationToolBar.show()

    def showPlot(self):
        self.show()
        self.navigationToolBar.show()

    def hidePlot(self):
        self.hide()
        self.navigationToolBar.hide()

