# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'timer2.ui',
# licensing of 'timer2.ui' applies.
#
# Created: Fri May 17 11:00:32 2019
#      by: pyside2-uic  running on PySide2 5.12.3
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QApplication
from PySide2.QtCore import QTimer
from PySide2.QtCore import *
from PySide2.QtGui import *

import time

i=0
DURATION_INT=5
dest_casa=1
dest_bere=0
dest_both=0

class Ui_MainWindow(object):
    a=0
    form2 = []
    ui2 = []
    real_amount = "Your Money (€)"
    imaginary_amount = "Your Dream Money (€)"
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.sogni = QtWidgets.QToolButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sogni.sizePolicy().hasHeightForWidth())
        self.sogni.setSizePolicy(sizePolicy)
        self.sogni.setObjectName("sogni")
        self.gridLayout.addWidget(self.sogni, 3, 0, 1, 4)
        self.tempo = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tempo.setFont(font)
        self.tempo.setAlignment(QtCore.Qt.AlignCenter)
        self.tempo.setObjectName("tempo")
        self.gridLayout.addWidget(self.tempo, 7, 1, 1, 1)
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setObjectName("start")
        self.gridLayout.addWidget(self.start, 12, 0, 1, 4)
        self.stop = QtWidgets.QPushButton(self.centralwidget)
        self.stop.setObjectName("stop")
        self.gridLayout.addWidget(self.stop, 13, 0, 1, 4)
        self.Laureando = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Laureando.setFont(font)
        self.Laureando.setObjectName("Laureando")
        self.gridLayout.addWidget(self.Laureando, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 4)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 10, 0, 1, 4)
        self.Assegnista = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Assegnista.setFont(font)
        self.Assegnista.setObjectName("Assegnista")
        self.gridLayout.addWidget(self.Assegnista, 1, 2, 1, 1)
        self.lcd_tempo = QtWidgets.QLCDNumber(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcd_tempo.sizePolicy().hasHeightForWidth())
        self.lcd_tempo.setSizePolicy(sizePolicy)
        self.lcd_tempo.setObjectName("lcd_tempo")
        self.gridLayout.addWidget(self.lcd_tempo, 7, 2, 1, 2)
        self.lcd_tempo.setDigitCount(10)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 11, 0, 1, 4)
        self.altro = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.altro.setFont(font)
        self.altro.setObjectName("altro")
        self.gridLayout.addWidget(self.altro, 1, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 4)

        self.chi_vorresti = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.chi_vorresti.setFont(font)
        self.chi_vorresti.setObjectName("chi_vorresti")
        self.gridLayout.addWidget(self.chi_vorresti, 2, 2, 1, 1)

        self.dovevai = QtWidgets.QLabel(self.centralwidget)
        self.dovevai.setFont(font)
        self.dovevai.setObjectName("dovevai")
        self.dovevai.setText("Where do you go after work?")
        self.gridLayout.addWidget(self.dovevai, 4, 0, 1, 4)

        self.casa = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.casa.setFont(font)
        self.casa.setObjectName("casa")
        self.casa.setText("Home")
        self.gridLayout.addWidget(self.casa, 5, 0, 1, 2)

        self.bere = QtWidgets.QCheckBox(self.centralwidget)
        self.bere.setText("Drink")
        font = QtGui.QFont()
        font.setPointSize(14)
        self.bere.setFont(font)
        self.bere.setObjectName("bere")
        self.gridLayout.addWidget(self.bere, 5, 2, 1, 2)


        self.Dottorando = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Dottorando.setFont(font)
        self.Dottorando.setObjectName("Dottorando")
        self.gridLayout.addWidget(self.Dottorando, 1, 1, 1, 1)
        self.lcd_money = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_money.setObjectName("lcd_money")
        self.gridLayout.addWidget(self.lcd_money, 8, 2, 1, 2)
        self.lcd_money.setDigitCount(10)
        self.real = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.real.setFont(font)
        self.real.setAlignment(QtCore.Qt.AlignCenter)
        self.real.setObjectName("real")
        self.gridLayout.addWidget(self.real, 8, 1, 1, 1)
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setObjectName("lcdNumber")
        self.lcdNumber.setDigitCount(10)
        self.gridLayout.addWidget(self.lcdNumber, 9, 2, 1, 2)
        self.imag = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.imag.setFont(font)
        self.imag.setObjectName("imag")
        self.gridLayout.addWidget(self.imag, 9, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 583, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)


#####################STYLE##################

        self.stylesheet = """

        QPushButton{
                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(155, 155, 155, 255), stop:1 rgba(155, 155, 155, 128));
                color:  white;
                border: 2px solid grey;
                border-radius: 5px;
        }
        QPushButton:pressed{
                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(200, 200, 200, 255), stop:1 rgba(200, 200, 200, 128));
                color:  white;
                border: 2px solid grey;
                border-radius: 5px;
        }
        QToolButton{
                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(155, 155, 155, 255), stop:1 rgba(155, 155, 155, 128));
                color:  white;
                border: 2px solid grey;
                border-radius: 5px;
        }
        QToolButton:pressed{
                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(200, 200, 200, 255), stop:1 rgba(200, 200, 200, 128));
                color:  white;
                border: 2px solid grey;
                border-radius: 5px;
        }
        QMainWindow{
            background-color: rgba(70,70,70,255)

        }
        QProgressBar{
            background-color: black;
            color: white;
            border: 2px solid grey;
            border-radius: 5px;
            text-align: center
    }

    QProgressBar::chunk {
    background-color: grey;
    width: 5px;
    margin: 1px;
    }

    QLabel{
    color: white;
    }
    QCheckBox{
    color: white;
    }
    QLCDNumber{
    color: white;
    }

        """






#########################################


        self.bg = QtWidgets.QButtonGroup()
        self.bg.addButton(self.Laureando,1)
        self.bg.addButton(self.Dottorando,2)
        self.bg.addButton(self.Assegnista,3)
        self.bg.addButton(self.altro,4)


        self.time_left_int = DURATION_INT
        self.widget_counter_int = 0





        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)





#################################################################################
        if self.Laureando.isChecked():
            text_support="Ciao"


        self.pushButton.clicked.connect(self.support)
        self.sogni.clicked.connect(self.list)
        self.start.clicked.connect(self.timer_start)
        self.start.clicked.connect(self.change_a)
        self.stop.clicked.connect(self.timer_stop)
        real_amount = "Your Money (€)"
        imaginary_amount = "Your Dream Money ($)"




##################################################################################


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Wages calculator", None, -1))
        self.sogni.setText(QtWidgets.QApplication.translate("MainWindow", "...", None, -1))
        self.tempo.setText(QtWidgets.QApplication.translate("MainWindow", "Time (s)", None, -1))
        self.start.setText(QtWidgets.QApplication.translate("MainWindow", "Start", None, -1))
        self.stop.setText(QtWidgets.QApplication.translate("MainWindow", "Stop", None, -1))
        self.Laureando.setText(QtWidgets.QApplication.translate("MainWindow", "Master student", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "What are you?", None, -1))
        self.Assegnista.setText(QtWidgets.QApplication.translate("MainWindow", "PostDoc", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("MainWindow", "Show Support!", None, -1))
        self.altro.setText(QtWidgets.QApplication.translate("MainWindow", "Altro", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("MainWindow", "Who would you like to be?", None, -1))
        self.chi_vorresti.setText(QtWidgets.QApplication.translate("MainWindow", Ui_list.vorresti, None, -1))
        self.Dottorando.setText(QtWidgets.QApplication.translate("MainWindow", "PhD Student", None, -1))
        self.real.setText(QtWidgets.QApplication.translate("MainWindow", Ui_MainWindow.real_amount, None, -1))
        self.imag.setText(QtWidgets.QApplication.translate("MainWindow", Ui_MainWindow.imaginary_amount, None, -1))
        self.toolBar.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "toolBar", None, -1))



    def support(self):
        self.form = QtWidgets.QMainWindow()
        self.ui = Ui_support()
        self.ui.setupUi(self.form)
        self.form.show()

    def list(self):
        Ui_MainWindow.form2 = QtWidgets.QMainWindow()
        Ui_MainWindow.ui2 = Ui_list()
        Ui_MainWindow.ui2.setupUi(self.form2)
        Ui_MainWindow.form2.show()

    def close_list(self):

        self.close()

    def finish(self):
        self.form3 = QtWidgets.QMainWindow()
        self.ui3 = Ui_finish()
        self.ui3.setupUi(self.form3)
        self.form3.show()

    #################TIMER FUNCTION#################################################
    def increase(self):
        i=0
        self.lcd_money.display(i+1)
        while i <= 10:

            i+=1
            time.sleep(1)
    def change_a(self):
        Ui_MainWindow.a=1


    def timer_start(self):
        self.euro_real=0
        self.euro_img=0
        self.Laureando.setEnabled(False)
        self.Dottorando.setEnabled(False)
        self.Assegnista.setEnabled(False)
        self.altro.setEnabled(False)
        self.sogni.setEnabled(False)
        if self.casa.isChecked():
            print("CIOA")




        if Ui_MainWindow.a == 0:
            self.time_left_int = 0
        else:
            self.time_left_int = self.time_left_int
        #euro_img=0
        if self.Dottorando.isChecked():
            self.euro_real=0.001909722
        if self.Assegnista.isChecked():
            self.euro_real=0.002430556
        if self.Laureando.isChecked():
            self.euro_real=0

        if Ui_list.lst == 1:
            self.euro_img = 0.002777778
            Ui_MainWindow.imaginary_amount= "Researcher's Money (€)"
        if Ui_list.lst == 2:
            self.euro_img = 0.003993056
            Ui_MainWindow.imaginary_amount= "Associated Professors's Money (€)"
        if Ui_list.lst == 3:
            self.euro_img = 0.006944444
            Ui_MainWindow.imaginary_amount= "Full Professors's Money (€)"
        if Ui_list.lst == 4:
            self.euro_img = 0.007927448
            Ui_MainWindow.imaginary_amount= "Volleyball player's Money (€)"
        if Ui_list.lst == 5:
            self.euro_img = 0.015854896
            Ui_MainWindow.imaginary_amount= "Basketball player's Money (€)"
        if Ui_list.lst == 6:
            self.euro_img = 1.4
            Ui_MainWindow.imaginary_amount= "CR7's Money (€)"
        if Ui_list.lst == 7:
            self.euro_img = 0.001243024
            Ui_MainWindow.imaginary_amount= "Bezos's Money 0(M$)"
        if Ui_list.lst == 8:
            self.euro_img = 0.000190259
            Ui_MainWindow.imaginary_amount = "Musk's Money (M$)"
        if Ui_list.lst == 9:
            self.euro_img = 0.018042872
            Ui_MainWindow.imaginary_amount= "Trump's Money ($)"
        if Ui_list.lst == 10:
            self.euro_img = 1
            Ui_MainWindow.imaginary_amount= "The pope's Money (blessings)"
        if Ui_list.lst == 11:
            self.euro_img = float('inf')
            Ui_MainWindow.imaginary_amount= "Scrooge McDuck's money ($)"


        self.retranslateUi(Form)


        #self.time_left_int = DURATION_INT
        self.money_real = (self.time_left_int * self.euro_real)
        self.money_real = float(self.money_real)
        self.money_img = (self.time_left_int * self.euro_img)
        self.money_img = '{:.2f}'.format(float(self.money_img))

        self.my_qtimer = QtCore.QTimer()
        self.my_qtimer.timeout.connect(self.timer_timeout)
        self.my_qtimer.start(1000)

        self.update_gui()

    def timer_timeout(self):
        self.time_left_int += 1
        #print(self.money_real)


        if self.time_left_int == 6:
            self.my_qtimer.stop()
            time.sleep(3)
            Form.close()
            self.finish()

        self.update_gui()

    def timer_stop(self):
        self.my_qtimer.stop()
        self.Laureando.setEnabled(True)
        self.Dottorando.setEnabled(True)
        self.Assegnista.setEnabled(True)
        self.altro.setEnabled(True)
        self.sogni.setEnabled(True)




    def update_gui(self):

        self.lcd_tempo.display(format(self.time_left_int))
        self.lcd_money.display('{:.2f}'.format(self.time_left_int*self.euro_real))
        if Ui_list.lst == 11:
            self.lcdNumber.display('7oo grEa7')
        else:
            self.lcdNumber.display('{:.2f}'.format(self.time_left_int*self.euro_img))
        self.progressBar.setValue(self.time_left_int/5*100)
    '''
    def start_timer(self,interval):
        timer = QTimer()
        timer.timeout.connect(self.increase)
        timer.timeout.connect(self.lcd_money.display(i+1))
        timer.timeout.connect(print("ciao"))
        timer.setInterval(1000)
        timer.start()
    '''


    def start_funct(self):
        euro_real=0
        euro_img=0
        if self.Dottorando.isChecked():
            euro_real=7
        self.timer_start()



    ################################################################################

class Ui_support(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("support")
        MainWindow.resize(800, 674)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)






    def retranslateUi(self, MainWindow):
        text_support=""

        if ui.Laureando.isChecked():
            self.text_support="Putroppo sei l'ultima\nruota del carro"
        else:
            self.text_support="Pensa che c'è sempre un laureando\nche non viene pagato"


        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("support", ":)", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("support", self.text_support, None, -1))
######################################################################################################

class Ui_list(object):
    vorresti= ""
    lst = 0
    def setupUi(self, list):
        list.setObjectName("list")
        list.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(list)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.ricercatore = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ricercatore.setFont(font)
        self.ricercatore.setObjectName("ricercatore")
        self.gridLayout.addWidget(self.ricercatore, 0, 0, 1, 1)
        self.bezos = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.bezos.setFont(font)
        self.bezos.setObjectName("bezos")
        self.gridLayout.addWidget(self.bezos, 2, 0, 1, 1)
        self.CR7 = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.CR7.setFont(font)
        self.CR7.setObjectName("CR7")
        self.gridLayout.addWidget(self.CR7, 1, 2, 1, 1)
        self.musk = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.musk.setFont(font)
        self.musk.setObjectName("musk")
        self.gridLayout.addWidget(self.musk, 2, 1, 1, 1)
        self.checkBox_11 = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_11.setFont(font)
        self.checkBox_11.setObjectName("checkBox_11")
        self.gridLayout.addWidget(self.checkBox_11, 3, 1, 1, 1)
        self.pallavolo = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pallavolo.setFont(font)
        self.pallavolo.setObjectName("pallavolo")
        self.gridLayout.addWidget(self.pallavolo, 1, 0, 1, 1)
        self.cestista = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cestista.setFont(font)
        self.cestista.setObjectName("cestista")
        self.gridLayout.addWidget(self.cestista, 1, 1, 1, 1)
        self.papa = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.papa.setFont(font)
        self.papa.setObjectName("papa")
        self.gridLayout.addWidget(self.papa, 3, 0, 1, 1)
        self.trump = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.trump.setFont(font)
        self.trump.setObjectName("trump")
        self.gridLayout.addWidget(self.trump, 2, 2, 1, 1)
        self.ordinario = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ordinario.setFont(font)
        self.ordinario.setObjectName("ordinario")
        self.gridLayout.addWidget(self.ordinario, 0, 2, 1, 1)
        self.checkBox_12 = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_12.setFont(font)
        self.checkBox_12.setObjectName("checkBox_12")
        self.gridLayout.addWidget(self.checkBox_12, 3, 2, 1, 1)
        self.associato = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.associato.setFont(font)
        self.associato.setObjectName("associato")
        self.gridLayout.addWidget(self.associato, 0, 1, 1, 1)
        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setObjectName("pushButton2")
        self.gridLayout.addWidget(self.pushButton2, 4, 1, 1, 1)
        list.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(list)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        list.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(list)
        self.statusbar.setObjectName("statusbar")
        list.setStatusBar(self.statusbar)

        self.retranslateUi(list)
        QtCore.QMetaObject.connectSlotsByName(list)

        self.bg2=QtWidgets.QButtonGroup()
        self.bg2.addButton(self.ricercatore,1)
        self.bg2.addButton(self.bezos,2)
        self.bg2.addButton(self.CR7,3)
        self.bg2.addButton(self.musk,4)
        self.bg2.addButton(self.checkBox_11,5)
        self.bg2.addButton(self.pallavolo,6)
        self.bg2.addButton(self.cestista,7)
        self.bg2.addButton(self.papa,8)
        self.bg2.addButton(self.trump,9)
        self.bg2.addButton(self.ordinario,10)
        self.bg2.addButton(self.associato,11)
        self.bg2.addButton(self.checkBox_12,12)

        self.pushButton2.clicked.connect(self.param)
        self.pushButton2.clicked.connect(self.close)

    def retranslateUi(self, list):
        list.setWindowTitle(QtWidgets.QApplication.translate("list", "Dream Jobs", None, -1))
        self.ricercatore.setText(QtWidgets.QApplication.translate("list", "Researcher", None, -1))
        self.bezos.setText(QtWidgets.QApplication.translate("list", "Jeff Bezos", None, -1))
        self.CR7.setText(QtWidgets.QApplication.translate("list", "CR7", None, -1))
        self.musk.setText(QtWidgets.QApplication.translate("list", "Elon Musk", None, -1))
        self.checkBox_11.setText(QtWidgets.QApplication.translate("list", "Scrooge McDuck", None, -1))
        self.pallavolo.setText(QtWidgets.QApplication.translate("list", "Volleyball player", None, -1))
        self.cestista.setText(QtWidgets.QApplication.translate("list", "Basketball player", None, -1))
        self.papa.setText(QtWidgets.QApplication.translate("list", "The pope", None, -1))
        self.trump.setText(QtWidgets.QApplication.translate("list", "Donald Trump", None, -1))
        self.ordinario.setText(QtWidgets.QApplication.translate("list", "Full Professor", None, -1))
        self.checkBox_12.setText(QtWidgets.QApplication.translate("list", "Unemployed", None, -1))
        self.associato.setText(QtWidgets.QApplication.translate("list", "Associated Professor", None, -1))
        self.pushButton2.setText(QtWidgets.QApplication.translate("list", "OK", None, -1))



    def close(self):
        Ui_MainWindow.form2.close()




    def param(self):
        # parameter val is actually the same as self.myQListWidget.currentItem
        #self.listWidget.itemActivated.connect
        if self.ricercatore.isChecked():
            Ui_list.lst=1
            Ui_list.vorresti= "Researcher"
        if self.associato.isChecked():
            Ui_list.lst=2
            Ui_list.vorresti= "Associated professor"
        if self.ordinario.isChecked():
            Ui_list.lst=3
            Ui_list.vorresti= "Full professor"
        if self.pallavolo.isChecked():
            Ui_list.lst=4
            Ui_list.vorresti= "Volleyball player"
        if self.cestista.isChecked():
            Ui_list.lst=5
            Ui_list.vorresti= "Basketball player"
        if self.CR7.isChecked():
            Ui_list.lst=6
            Ui_list.vorresti= "CR7"
        if self.bezos.isChecked():
            Ui_list.lst=7
            Ui_list.vorresti= "Jeff Bezos"
        if self.musk.isChecked():
            Ui_list.lst=8
            Ui_list.vorresti= "Elon Musk"
        if self.trump.isChecked():
            Ui_list.lst=9
            Ui_list.vorresti= "Donald Trump"
        if self.papa.isChecked():
            Ui_list.lst=10
            Ui_list.vorresti= "The pope"
        if self.checkBox_11.isChecked():
            Ui_list.lst=11
            Ui_list.vorresti= "Scrooge McDuck"

'''
        self.form2 = QtWidgets.QMainWindow()
        self.ui2 = Ui_list()
        self.ui2.setupUi(self.form2)
        self.form2.close()
   '''



class Ui_finish(object):
    def setupUi(self, finish):
        finish.setObjectName("finish")
        finish.resize(800, 674)
        self.centralwidget = QtWidgets.QWidget(finish)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(50)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        finish.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(finish)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        finish.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(finish)
        self.statusbar.setObjectName("statusbar")
        finish.setStatusBar(self.statusbar)

        self.retranslateUi(finish)
        QtCore.QMetaObject.connectSlotsByName(finish)

    def retranslateUi(self, finish):
        self.bere=False
        if ui.bere.isChecked():
            self.bere=True
            if ui.casa.isChecked():
                finish.setWindowTitle(QtWidgets.QApplication.translate("finish", "MainWindow", None, -1))
                self.label.setText(QtWidgets.QApplication.translate("finish", "Si va a Casa a Bere!!!!!", None, -1))
            else:
                finish.setWindowTitle(QtWidgets.QApplication.translate("finish", "MainWindow", None, -1))
                self.label.setText(QtWidgets.QApplication.translate("finish", "Si va a Bere!!!!!", None, -1))
        if not self.bere:
            if ui.casa.isChecked():
                finish.setWindowTitle(QtWidgets.QApplication.translate("finish", "MainWindow", None, -1))
                self.label.setText(QtWidgets.QApplication.translate("finish", "Si va a Casa!!!!!", None, -1))
            else:
                finish.setWindowTitle(QtWidgets.QApplication.translate("finish", "MainWindow", None, -1))
                self.label.setText(QtWidgets.QApplication.translate("finish", "Error!!! \n\n Destination not Specified!!! \n\n ABORT", None, -1))














if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)


    Form = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(Form)
    app.setStyleSheet(ui.stylesheet)
    Form.setWindowIcon(QIcon('./money-bag.svg'))
    Form.show()
    sys.exit(app.exec_())
