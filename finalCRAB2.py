
from CRABUI import Ui_CRAB
from PyQt5 import QtCore ,QtGui,QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt , QTimer , QTime , QDate
from PyQt5.uic import loadUiType
import MAIN
import os
import webbrowser as web
import sys

class MainThread(QThread):


    
    def __init__(self):
        
        super(MainThread,self).__init__()

    def run(self):
        MAIN.tasks()

startExe=MainThread()

class Gui_start(QMainWindow):

    def __init__(self):
        super().__init__()

        self.gui = Ui_CRAB()
        self.gui.setupUi(self)

        self.gui.START_button.clicked.connect(self.startTask)
        self.gui.EXIT_button.clicked.connect(self.close)
        self.gui.chrome_button.clicked.connect(self.chrome_app)
        self.gui.YouTube_button.clicked.connect(self.yt_app)

    def chrome_app(self):
        os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
      
    def yt_app(self):
        web.open("https://www.youtube.com/")
    
    def startTask(self):

        self.gui.label1 = QtGui.QMovie("gui CRAB//VoiceReg//Siri_1.gif")
        self.gui.gif1.setMovie(self.gui.label1)
        self.gui.label1.start()

        timer=QTimer(self)
        timer.timeout.connect(self.showTimeLive)
        timer.start(9)
        
        startExe.start()
   
    def showTimeLive(self):
        t_ime=QTime.currentTime()
        time=t_ime.toString()
        d_ate=QDate.currentDate()
        date=d_ate.toString()
        label_time="Time: "+ time
        label_date="Date: "+ date
        self.gui.Time.setText(label_time)
        self.gui.date.setText(label_date)
        



GuiApp = QApplication(sys.argv)
crab_gui = Gui_start()
crab_gui.show()
exit(GuiApp.exec_())

