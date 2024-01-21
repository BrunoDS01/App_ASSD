from PyQt5 import QtCore, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import numpy as np

class MplCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)
        self.navigationToolBar = NavigationToolbar(self, parent)


class SpectogramPlot(MplCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        super().__init__(parent=None, width=5, height=4, dpi=100)

    def plot(self, amplitudes, times, frequencies):
        self.axes.pcolormesh(times, frequencies, 10 * np.log10(amplitudes), shading='auto', cmap='viridis')
        self.axes.ylabel('Frequency [Hz]')
        self.axes.xlabel('Time [sec]')
        self.axes.title('Spectrogram of Audio Signal')
        self.axes.colorbar(label='Intensity [dB]')
        self.axes.show()

    def showPlot(self):
        self.show()
        self.navigationToolBar.show()

    def hidePlot(self):
        self.hide()
        self.navigationToolBar.hide()

