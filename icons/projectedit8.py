# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'projectedit.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 410)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(600, 400))
        self.centralwidget.setMaximumSize(QtCore.QSize(600, 400))
        self.centralwidget.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 81, 401))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_home = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_home.setStyleSheet("background-color: rgb(255, 170, 255);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/69524.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_home.setIcon(icon)
        self.btn_home.setObjectName("btn_home")
        self.verticalLayout.addWidget(self.btn_home)
        self.btn_calendar_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_calendar_2.setStyleSheet("background-color: rgb(255, 170, 255);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/calendar-icon-marketing-image.webp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_calendar_2.setIcon(icon1)
        self.btn_calendar_2.setObjectName("btn_calendar_2")
        self.verticalLayout.addWidget(self.btn_calendar_2)
        self.btn_how_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_how_2.setStyleSheet("background-color: rgb(255, 170, 255);")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/d66f27ddc6cea33a948e4cafefc9038e.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_how_2.setIcon(icon2)
        self.btn_how_2.setObjectName("btn_how_2")
        self.verticalLayout.addWidget(self.btn_how_2)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(80, 0, 521, 401))
        self.stackedWidget.setObjectName("stackedWidget")
        self.today_page = QtWidgets.QWidget()
        self.today_page.setStyleSheet("")
        self.today_page.setObjectName("today_page")
        self.label_9 = QtWidgets.QLabel(self.today_page)
        self.label_9.setGeometry(QtCore.QRect(-40, 0, 561, 401))
        self.label_9.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("inout.jpg"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.todaydateEdit_2 = QtWidgets.QDateEdit(self.today_page)
        self.todaydateEdit_2.setGeometry(QtCore.QRect(130, 80, 71, 20))
        self.todaydateEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.todaydateEdit_2.setObjectName("todaydateEdit_2")
        self.btn_save_2 = QtWidgets.QPushButton(self.today_page)
        self.btn_save_2.setGeometry(QtCore.QRect(80, 260, 75, 23))
        self.btn_save_2.setObjectName("btn_save_2")
        self.income = QtWidgets.QPlainTextEdit(self.today_page)
        self.income.setGeometry(QtCore.QRect(130, 140, 71, 31))
        self.income.setObjectName("income")
        self.outcome = QtWidgets.QPlainTextEdit(self.today_page)
        self.outcome.setGeometry(QtCore.QRect(130, 200, 71, 31))
        self.outcome.setObjectName("outcome")
        self.stackedWidget.addWidget(self.today_page)
        self.calendar_page = QtWidgets.QWidget()
        self.calendar_page.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.calendar_page.setObjectName("calendar_page")
        self.label_10 = QtWidgets.QLabel(self.calendar_page)
        self.label_10.setGeometry(QtCore.QRect(0, 0, 521, 401))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("calendar.jpg"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.totalmoney = QtWidgets.QLabel(self.calendar_page)
        self.totalmoney.setGeometry(QtCore.QRect(90, 300, 309, 41))
        self.totalmoney.setObjectName("totalmoney")
        self.dateEdit = QtWidgets.QDateEdit(self.calendar_page)
        self.dateEdit.setGeometry(QtCore.QRect(90, 30, 110, 22))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        self.btn_get = QtWidgets.QPushButton(self.calendar_page)
        self.btn_get.setGeometry(QtCore.QRect(180, 270, 75, 23))
        self.btn_get.setObjectName("btn_get")
        self.stackedWidget.addWidget(self.calendar_page)
        self.home_page = QtWidgets.QWidget()
        self.home_page.setObjectName("home_page")
        self.username = QtWidgets.QTextEdit(self.home_page)
        self.username.setGeometry(QtCore.QRect(220, 200, 104, 31))
        self.username.setObjectName("username")
        self.savingpercent = QtWidgets.QSpinBox(self.home_page)
        self.savingpercent.setGeometry(QtCore.QRect(280, 250, 41, 21))
        self.savingpercent.setObjectName("savingpercent")
        self.label_2 = QtWidgets.QLabel(self.home_page)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 521, 401))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("home.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.btn_save = QtWidgets.QPushButton(self.home_page)
        self.btn_save.setGeometry(QtCore.QRect(240, 300, 75, 23))
        self.btn_save.setObjectName("btn_save")
        self.label_2.raise_()
        self.savingpercent.raise_()
        self.username.raise_()
        self.btn_save.raise_()
        self.stackedWidget.addWidget(self.home_page)
        self.howmuch_page = QtWidgets.QWidget()
        self.howmuch_page.setStyleSheet("")
        self.howmuch_page.setObjectName("howmuch_page")
        self.label_13 = QtWidgets.QLabel(self.howmuch_page)
        self.label_13.setGeometry(QtCore.QRect(0, -10, 521, 411))
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap("howmuch.jpg"))
        self.label_13.setScaledContents(True)
        self.label_13.setObjectName("label_13")
        self.verticalLayoutWidget_7 = QtWidgets.QWidget(self.howmuch_page)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(230, 140, 121, 151))
        self.verticalLayoutWidget_7.setObjectName("verticalLayoutWidget_7")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.progressBar_3 = QtWidgets.QProgressBar(self.verticalLayoutWidget_7)
        self.progressBar_3.setMaximum(31)
        self.progressBar_3.setProperty("value", 0)
        self.progressBar_3.setObjectName("progressBar_3")
        self.verticalLayout_7.addWidget(self.progressBar_3)
        self.progressBar_4 = QtWidgets.QProgressBar(self.verticalLayoutWidget_7)
        self.progressBar_4.setMaximum(31)
        self.progressBar_4.setProperty("value", 0)
        self.progressBar_4.setObjectName("progressBar_4")
        self.verticalLayout_7.addWidget(self.progressBar_4)
        self.howmuch_label = QtWidgets.QLabel(self.howmuch_page)
        self.howmuch_label.setGeometry(QtCore.QRect(330, 310, 141, 31))
        self.howmuch_label.setText("")
        self.howmuch_label.setObjectName("howmuch_label")
        self.label_3 = QtWidgets.QLabel(self.howmuch_page)
        self.label_3.setGeometry(QtCore.QRect(50, 310, 91, 31))
        self.label_3.setObjectName("label_3")
        self.name_label = QtWidgets.QLabel(self.howmuch_page)
        self.name_label.setGeometry(QtCore.QRect(140, 310, 91, 31))
        self.name_label.setText("")
        self.name_label.setObjectName("name_label")
        self.label_4 = QtWidgets.QLabel(self.howmuch_page)
        self.label_4.setGeometry(QtCore.QRect(226, 310, 111, 31))
        self.label_4.setObjectName("label_4")
        self.stackedWidget.addWidget(self.howmuch_page)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

#assighn 
        self.ondate = '1/1/2000'
        self.getdate = '1/1/2000'

#set click
        self.btn_save.clicked.connect(self.savingusername)
        self.btn_home.clicked.connect(self.gohome)
        self.btn_calendar_2.clicked.connect(self.gocalendar)
        self.btn_how_2.clicked.connect(self.gohow)
        self.btn_save_2.clicked.connect(self.totaltoday)
        self.btn_get.clicked.connect(self.getdata)

#get date
        self.todaydateEdit_2.dateChanged.connect(self.onDateChanged)
        self.dateEdit.dateChanged.connect(self.getdatedata)
        
    
        
    
#get date from wicalendon
    def onDateChanged(self, qDate):
        self.ondate = ('{0}/{1}/{2}'.format(qDate.month(), qDate.day(), qDate.year()))
        
        self.ondatesplit = self.ondate.split('/')
        
    
    def getdatedata(self, qDate):
        self.getdate = ('{0}/{1}/{2}'.format(qDate.month(), qDate.day(), qDate.year()))
        return self.getdate 
        
#create storage

    def totaltoday(self, qDate):
        self.ondate = '1/1/2000'
        self.getdate = '1/1/2000'
        
        self.storage={}
        self.totalvalue=0
        income = self.income.toPlainText() #get income
        income=int(income)
        outcome = self.outcome.toPlainText()
        outcome=int(outcome)
        self.ondatesplit = self.ondate.split('/')
        print('test')
        self.storage[self.ondate]=income-outcome
        print('test2')
        print(str(self.ondatesplit[1]))
        self.progressBar_3.setValue(int(self.ondatesplit[1]))
    
        for k,v in self.storage.items():
            v=int(v)
            
            self.totalvalue +=v
            
        self.progressBar_4.setValue(int(self.totalvalue))    
        

    
        
#get data from date
    def getdata(self):
        
        if self.getdate not in self.storage:
            self.totalmoney.setText(str(0))

        else:
            print('testbefore')
            self.totalthatday = self.storage.get(self.getdate)
            print(self.totalthatday)
            self.totalmoney.setText(str(self.totalthatday))
            print('test2')

#set go to next page
    def gohome(self):
        self.stackedWidget.setCurrentIndex(0)

    def gocalendar(self):
        self.stackedWidget.setCurrentIndex(1)

    def gohow(self):
        self.stackedWidget.setCurrentIndex(3)

#save user name
    def savingusername(self):
        self.usernamee= self.username.toPlainText()
        self.savingper= self.savingpercent.value()
        self.name_label.setText(str(self.usernamee))
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_home.setText(_translate("MainWindow", "Home"))
        self.btn_calendar_2.setText(_translate("MainWindow", "calendar"))
        self.btn_how_2.setText(_translate("MainWindow", "how much"))
        self.btn_save_2.setText(_translate("MainWindow", "save"))
        self.totalmoney.setText(_translate("MainWindow", "total money"))
        self.btn_get.setText(_translate("MainWindow", "GET"))
        self.btn_save.setText(_translate("MainWindow", "save"))
        self.label_3.setText(_translate("MainWindow", "how much money "))
        self.label_4.setText(_translate("MainWindow", "should spend for day?"))

if __name__=="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

        
