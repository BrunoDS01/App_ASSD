from PyQt5 import QtCore, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

class MplCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)
        self.navigationToolBar = NavigationToolbar(self, parent)

class SpectogramPlot(MplCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        super(parent=None, width=5, height=4, dpi=100, self).__init__(*args, **kwargs)