from PySide6.QtWidgets import QWidget, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

class mplwidget(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.figure = Figure()
        self.axis = self.figure.add_subplot(111)
        self.axis.grid()
        
        self.canvas = FigureCanvasQTAgg(self.figure)
        self.layoutvertical = QVBoxLayout(self)
        self.layoutvertical.addWidget(self.canvas)

    def clear_canvas(self):
        self.axis.cla()

    def redraw_canvas(self, x, y):    
        self.clear_canvas()
        self.axis.plot(x,y)
        self.axis.grid()
        self.canvas.draw()
