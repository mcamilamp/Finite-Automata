# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_qt.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QMainWindow, QSizePolicy,
    QStatusBar, QWidget)
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(996, 569)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame_title = QFrame(self.centralwidget)
        self.frame_title.setObjectName(u"frame_title")
        self.frame_title.setGeometry(QRect(10, 10, 971, 41))
        self.frame_title.setStyleSheet(u"background-color: rgb(225, 225, 225);")
        self.frame_title.setFrameShape(QFrame.StyledPanel)
        self.frame_title.setFrameShadow(QFrame.Raised)
        self.frame_show_automata = QFrame(self.centralwidget)
        self.frame_show_automata.setObjectName(u"frame_show_automata")
        self.frame_show_automata.setGeometry(QRect(10, 60, 741, 331))
        self.frame_show_automata.setStyleSheet(u"background-color: rgb(225, 225, 225);")
        self.frame_show_automata.setFrameShape(QFrame.StyledPanel)
        self.frame_show_automata.setFrameShadow(QFrame.Raised)
        self.frame_options = QFrame(self.centralwidget)
        self.frame_options.setObjectName(u"frame_options")
        self.frame_options.setGeometry(QRect(760, 60, 221, 331))
        self.frame_options.setStyleSheet(u"background-color: rgb(225, 225, 225);")
        self.frame_options.setFrameShape(QFrame.StyledPanel)
        self.frame_options.setFrameShadow(QFrame.Raised)
        self.frame_input = QFrame(self.centralwidget)
        self.frame_input.setObjectName(u"frame_input")
        self.frame_input.setGeometry(QRect(10, 400, 431, 151))
        self.frame_input.setStyleSheet(u"background-color: rgb(225, 225, 225);")
        self.frame_input.setFrameShape(QFrame.StyledPanel)
        self.frame_input.setFrameShadow(QFrame.Raised)
        self.frame_words = QFrame(self.centralwidget)
        self.frame_words.setObjectName(u"frame_words")
        self.frame_words.setGeometry(QRect(450, 400, 531, 151))
        self.frame_words.setStyleSheet(u"background-color: rgb(225, 225, 225);")
        self.frame_words.setFrameShape(QFrame.StyledPanel)
        self.frame_words.setFrameShadow(QFrame.Raised)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
    # retranslateUi

def create_and_show_ui():
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()

    # Crea una instancia de Ui_MainWindow
    ui = Ui_MainWindow()

    # Configura la interfaz en la ventana principal
    ui.setupUi(MainWindow)

    # Muestra la ventana principal
    MainWindow.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    create_and_show_ui()