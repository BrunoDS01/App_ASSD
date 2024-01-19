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
        plt.pcolormesh(times, frequencies, 10 * np.log10(amplitudes), shading='auto', cmap='viridis')
        plt.ylabel('Frequency [Hz]')
        plt.xlabel('Time [sec]')
        plt.title('Spectrogram of Audio Signal')
        plt.colorbar(label='Intensity [dB]')
        plt.show()
