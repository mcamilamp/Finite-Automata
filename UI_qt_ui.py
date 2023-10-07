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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QSlider, QStatusBar,
    QWidget)
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
        self.frame_title.setStyleSheet(u"background-color: rgb(225, 225, 225);\n"
"border-radius:8px;")
        self.frame_title.setFrameShape(QFrame.StyledPanel)
        self.frame_title.setFrameShadow(QFrame.Raised)
        self.title = QLabel(self.frame_title)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(440, 10, 131, 21))
        self.title.setStyleSheet(u"color: rgb(98, 98, 98);\n"
"font: 700 12pt \"Segoe UI\";\n"
"color: rgb(74, 74, 74);\n"
"font: 700 16pt \"Segoe UI\";")
        self.frame_show_automata = QFrame(self.centralwidget)
        self.frame_show_automata.setObjectName(u"frame_show_automata")
        self.frame_show_automata.setGeometry(QRect(10, 60, 741, 331))
        self.frame_show_automata.setStyleSheet(u"background-color: rgb(225, 225, 225);\n"
"border-radius:8px;")
        self.frame_show_automata.setFrameShape(QFrame.StyledPanel)
        self.frame_show_automata.setFrameShadow(QFrame.Raised)
        self.horizontalSlider = QSlider(self.frame_show_automata)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setGeometry(QRect(20, 280, 261, 31))
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.frame_options = QFrame(self.centralwidget)
        self.frame_options.setObjectName(u"frame_options")
        self.frame_options.setGeometry(QRect(760, 60, 221, 331))
        self.frame_options.setStyleSheet(u"background-color: rgb(225, 225, 225);\n"
"border-radius:8px;")
        self.frame_options.setFrameShape(QFrame.StyledPanel)
        self.frame_options.setFrameShadow(QFrame.Raised)
        self.button_play = QPushButton(self.frame_options)
        self.button_play.setObjectName(u"button_play")
        self.button_play.setGeometry(QRect(70, 40, 75, 61))
        self.button_play.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u"img/play-circle-regular-24 (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_play.setIcon(icon)
        self.button_play.setIconSize(QSize(100, 100))
        self.button_voice = QPushButton(self.frame_options)
        self.button_voice.setObjectName(u"button_voice")
        self.button_voice.setGeometry(QRect(80, 130, 41, 41))
        self.button_voice.setStyleSheet(u"border-radius: 4px;")
        icon1 = QIcon()
        icon1.addFile(u"../../../Downloads/user-voice-regular-24.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_voice.setIcon(icon1)
        self.button_voice.setIconSize(QSize(55, 55))
        self.button_language = QPushButton(self.frame_options)
        self.button_language.setObjectName(u"button_language")
        self.button_language.setGeometry(QRect(70, 210, 75, 61))
        self.button_language.setStyleSheet(u"border-radius: 4px;")
        icon2 = QIcon()
        icon2.addFile(u"../../../Downloads/message-rounded-dots-regular-24.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_language.setIcon(icon2)
        self.button_language.setIconSize(QSize(89, 89))
        self.frame_input = QFrame(self.centralwidget)
        self.frame_input.setObjectName(u"frame_input")
        self.frame_input.setGeometry(QRect(10, 400, 431, 151))
        self.frame_input.setStyleSheet(u"background-color: rgb(225, 225, 225);\n"
"border-radius:8px;")
        self.frame_input.setFrameShape(QFrame.StyledPanel)
        self.frame_input.setFrameShadow(QFrame.Raised)
        self.frame_words = QFrame(self.centralwidget)
        self.frame_words.setObjectName(u"frame_words")
        self.frame_words.setGeometry(QRect(450, 400, 531, 151))
        self.frame_words.setStyleSheet(u"background-color: rgb(225, 225, 225);\n"
"border-radius:8px;")
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
#if QT_CONFIG(tooltip)
        self.title.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700; color:#646464;\">Automata</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.title.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700; color:#636363;\">Automata</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.title.setText(QCoreApplication.translate("MainWindow", u"Automata", None))
        self.button_play.setText("")
        self.button_voice.setText("")
        self.button_language.setText("")
    # retranslateUi

def create_and_show_ui():
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()

    ui = Ui_MainWindow()

    ui.setupUi(MainWindow)

    MainWindow.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    create_and_show_ui()