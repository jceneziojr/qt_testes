# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'plotterWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QHBoxLayout, QLabel,
    QMainWindow, QMenuBar, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

from MatPlotLibWidget import mplwidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(700, 600)
        MainWindow.setMinimumSize(QSize(700, 600))
        MainWindow.setMaximumSize(QSize(700, 600))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.plotWindow = mplwidget(self.centralwidget)
        self.plotWindow.setObjectName(u"plotWindow")
        self.plotWindow.setMinimumSize(QSize(683, 400))
        self.plotWindow.setMaximumSize(QSize(683, 400))

        self.verticalLayout_4.addWidget(self.plotWindow)

        self.label_equation = QLabel(self.centralwidget)
        self.label_equation.setObjectName(u"label_equation")

        self.verticalLayout_4.addWidget(self.label_equation)

        self.Slot_spins = QWidget(self.centralwidget)
        self.Slot_spins.setObjectName(u"Slot_spins")
        self.Slot_spins.setMinimumSize(QSize(683, 100))
        self.Slot_spins.setMaximumSize(QSize(683, 100))
        self.Slot_spins.setLayoutDirection(Qt.LeftToRight)
        self.horizontalLayout = QHBoxLayout(self.Slot_spins)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Box_expoente = QWidget(self.Slot_spins)
        self.Box_expoente.setObjectName(u"Box_expoente")
        self.Box_expoente.setMinimumSize(QSize(90, 70))
        self.Box_expoente.setMaximumSize(QSize(90, 70))
        self.verticalLayout = QVBoxLayout(self.Box_expoente)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_exp = QLabel(self.Box_expoente)
        self.label_exp.setObjectName(u"label_exp")

        self.verticalLayout.addWidget(self.label_exp)

        self.spin_exp = QDoubleSpinBox(self.Box_expoente)
        self.spin_exp.setObjectName(u"spin_exp")

        self.verticalLayout.addWidget(self.spin_exp)


        self.horizontalLayout.addWidget(self.Box_expoente)

        self.Box_omega = QWidget(self.Slot_spins)
        self.Box_omega.setObjectName(u"Box_omega")
        self.Box_omega.setMinimumSize(QSize(90, 70))
        self.Box_omega.setMaximumSize(QSize(90, 70))
        self.verticalLayout_2 = QVBoxLayout(self.Box_omega)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_omega = QLabel(self.Box_omega)
        self.label_omega.setObjectName(u"label_omega")

        self.verticalLayout_2.addWidget(self.label_omega)

        self.spin_omega = QDoubleSpinBox(self.Box_omega)
        self.spin_omega.setObjectName(u"spin_omega")

        self.verticalLayout_2.addWidget(self.spin_omega)


        self.horizontalLayout.addWidget(self.Box_omega)

        self.Box_phi = QWidget(self.Slot_spins)
        self.Box_phi.setObjectName(u"Box_phi")
        self.Box_phi.setMinimumSize(QSize(90, 70))
        self.Box_phi.setMaximumSize(QSize(90, 70))
        self.verticalLayout_3 = QVBoxLayout(self.Box_phi)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_phi = QLabel(self.Box_phi)
        self.label_phi.setObjectName(u"label_phi")

        self.verticalLayout_3.addWidget(self.label_phi)

        self.spin_phi = QDoubleSpinBox(self.Box_phi)
        self.spin_phi.setObjectName(u"spin_phi")

        self.verticalLayout_3.addWidget(self.spin_phi)


        self.horizontalLayout.addWidget(self.Box_phi)


        self.verticalLayout_4.addWidget(self.Slot_spins)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 700, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        string1="<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">e</span><span style=\" font-size:12pt; vertical-align:super;\">" + str(round(self.spin_exp.value(), 2)) +"t</span><span style=\" font-size:12pt;\">cos(" + str(round(self.spin_omega.value(), 2)) +"t+" + str(round(self.spin_phi.value(), 2)) +")</span></p></body></html>"
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_equation.setText(QCoreApplication.translate("MainWindow", string1, None))
        self.label_exp.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Expoente</span></p></body></html>", None))
        self.label_omega.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">\u03c9</span></p></body></html>", None))
        self.label_phi.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">\u03a6</span></p></body></html>", None))
    # retranslateUi

