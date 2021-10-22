from time import sleep
#https://www.youtube.com/watch?v=hWrFEU_605g&ab_channel=LinusTechTips
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread, QObject, pyqtSignal, QRunnable, QThreadPool
from pytube import YouTube


class Runnable(QRunnable):


    def __init__(self, n):
        super().__init__()
        self.n = n


    def run(self):
        global console, URL, PATH, progress, radio1, radio2, radio3

        try:
            if radio1.isChecked():
                print('downloading 1080p')
                yt = YouTube(URL)
                itag = 137
                console.append('<fetching_media>')
                console.append('<.mp4 1080p>')
                ys = yt.streams.get_by_itag(itag)
            elif radio2.isChecked():
                print('downloading 720p')
                yt = YouTube(URL)
                itag = 136
                console.append('<fetching_media>')
                console.append('<.mp4 720p>')
                ys = yt.streams.get_by_itag(itag)
            elif radio3.isChecked():
                print('downloading .webm 50kbps')
                yt = YouTube(URL)
                itag = 249
                console.append('<fetching_media>')
                console.append('<.webm 50kbps>')
                ys = yt.streams.get_by_itag(itag)
            else:
                print('error')
                console.append('<ERROR>')
                console.append('<Please_select_file_type>')




        except:

            print('error')
            console.append('<ERROR>')
            console.append('<Please_enter_valid_url>')
        else:
            Ui_MainWindow.fifty(Ui_MainWindow())
            console.append('<connected_to_server>')
            ys.download(PATH)
            Ui_MainWindow.hundred(Ui_MainWindow())
            self.finished.emit()



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(472, 305)
        font = QtGui.QFont()
        font.setFamily("Small Fonts")
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color:    qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(160, 245, 190, 255), stop:1 rgba(83, 44, 255, 255))")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 10, 271, 51))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 190, 431, 31))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 70, 431, 21))
        self.lineEdit.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(171, 160, 245, 255), stop:1 rgba(255, 255, 255, 255))")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 90, 431, 21))
        self.lineEdit_2.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(171, 160, 245, 255), stop:1 rgba(255, 255, 255, 255))")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(280, 120, 171, 16))
        self.label_4.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(171, 160, 245, 255), stop:1 rgba(255, 255, 255, 255))")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(280, 160, 171, 16))
        self.label_5.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(171, 160, 245, 255), stop:1 rgba(255, 255, 255, 255))")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(280, 140, 171, 16))
        self.label_6.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(171, 160, 245, 255), stop:1 rgba(255, 255, 255, 255))")
        self.label_6.setObjectName("label_6")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(120, 120, 151, 58))
        self.textBrowser.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.textBrowser.setObjectName("textBrowser")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(20, 230, 431, 16))
        self.progressBar.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(171, 160, 245, 255), stop:1 rgba(255, 255, 255, 255))")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setChecked(True)
        self.radioButton.setGeometry(QtCore.QRect(20, 160, 91, 16))
        self.radioButton.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(171, 160, 245, 255), stop:1 rgba(255, 255, 255, 255))")
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 140, 91, 16))
        self.radioButton_2.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(171, 160, 245, 255), stop:1 rgba(255, 255, 255, 255))")
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(20, 120, 91, 16))
        self.radioButton_3.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(171, 160, 245, 255), stop:1 rgba(255, 255, 255, 255))")
        self.radioButton_3.setObjectName("radioButton_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 472, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)




        global title, console, progress, radio1, radio2, radio3, button, length, views
        views = self.label_5
        length = self.label_6
        button = self.pushButton
        radio1 = self.radioButton
        radio2 = self.radioButton_2
        radio3 = self.radioButton_3
        progress = self.progressBar
        title = self.label_4
        console = self.textBrowser

        button.clicked.connect(self.start_threading)


    def fifty(self):
        global progress, title, length, views
        print('test')
        progress.setProperty("value", 50)

    def hundred(self):
        global progress, button
        button.setText('<DONE>')
        print('test2')
        progress.setProperty("value", 100)


    def start_threading(self):
        global console, URL, PATH, radio1


        PATH = self.lineEdit_2.text()
        URL = self.lineEdit.text()

        console.clear()

        pool = QThreadPool.globalInstance()
        for i in range(1):
            runnable = Runnable(i)

        pool.start(runnable)
        print('1')


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "downy v0.01"))
        self.pushButton.setText(_translate("MainWindow", "download"))
        self.lineEdit.setText(
            _translate("MainWindow", "Enter URL"))
        self.lineEdit_2.setText(
            _translate("MainWindow", "c:/videos"))
        self.label_4.setText(_translate("MainWindow", " TITLE:"))
        self.label_5.setText(_translate("MainWindow", " VIEWS:"))
        self.label_6.setText(_translate("MainWindow", " LENGTH:"))
        self.textBrowser.setHtml(_translate("MainWindow",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt;console&gt;</p></body></html>"))
        self.radioButton.setText(_translate("MainWindow", "1080p mp4"))
        self.radioButton_2.setText(_translate("MainWindow", "720p mp4"))
        self.radioButton_3.setText(_translate("MainWindow", "mp3 50kbps"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
