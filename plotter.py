from PySide6.QtWidgets import QMainWindow, QApplication, QDoubleSpinBox
from plotterWindow import Ui_MainWindow
import sys
import numpy as np
from MatPlotLibWidget import mplwidget

class mainWindow(QMainWindow, Ui_MainWindow, ):
    t = []
    c = 0
    w = 0
    ang = 0
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.t = np.linspace(0,10,1000)
        self.spin_exp.valueChanged.connect(self.fetch_value)
        self.spin_omega.valueChanged.connect(self.fetch_value)
        self.spin_phi.valueChanged.connect(self.fetch_value)
        self.config()
        self.plotWindow.axis.plot(self.t,(np.e**(self.c*self.t))*np.cos(self.w*self.t+self.ang))
    
    def fetch_value(self):
        self.c = self.spin_exp.value()
        self.w = self.spin_omega.value()
        self.ang = self.spin_phi.value()
        self.retranslateUi(self)
        self.redraw()

    def redraw(self):
        x = self.t
        y = (np.e**(self.c*self.t))*np.cos(self.w*self.t+self.ang)
        self.plotWindow.redraw_canvas(x,y)
        

    def config(self):
        self.spin_exp.setMinimum(-15.00)
        self.spin_exp.setMaximum(15.00)
        self.spin_exp.setSingleStep(0.1)
        
        self.spin_omega.setMaximum(189.00) #+- 30Hz
        
        self.spin_phi.setMinimum(-3.14) #-pi
        self.spin_phi.setMaximum(3.14) #+pi
        self.spin_phi.setSingleStep(0.01)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = mainWindow()
    w.show()
    sys.exit(app.exec())