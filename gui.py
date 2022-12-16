from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QLineEdit
from pytube import YouTube
import requests


class UiYourTube(object):
    lineEdit: QLineEdit
    centralwidget: QWidget
    file_list = []
    current_row = None
    yt = None

    def setupUi(self, yourtube):
        yourtube.setObjectName("YourTube")
        yourtube.resize(864, 502)
        self.centralwidget = QtWidgets.QWidget(yourtube)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 30, 601, 31))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.returnPressed.connect(self.go_button_click)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 71, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 420, 55, 16))
        self.label_2.setObjectName("label_2")
        self.go_button = QtWidgets.QPushButton(self.centralwidget)
        self.go_button.clicked.connect(self.go_button_click)
        self.go_button.setGeometry(QtCore.QRect(630, 30, 221, 31))
        self.go_button.setObjectName("go_button")
        self.dl_Button = QtWidgets.QPushButton(self.centralwidget)
        self.dl_Button.setEnabled(False)
        self.dl_Button.setGeometry(QtCore.QRect(560, 420, 291, 31))
        self.dl_Button.setObjectName("dl_Button")
        self.dl_Button.clicked.connect(self.download_button)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setEnabled(False)
        self.listWidget.setGeometry(QtCore.QRect(20, 130, 831, 281))
        self.listWidget.setObjectName("listWidget")
        self.listWidget.clicked.connect(self.select_version)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 70, 341, 51))
        self.groupBox.setObjectName("groupBox")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setEnabled(False)
        self.radioButton_2.setGeometry(QtCore.QRect(10, 20, 95, 20))
        self.radioButton_2.setChecked(True)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_3.setEnabled(False)
        self.radioButton_3.setGeometry(QtCore.QRect(110, 20, 95, 20))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setEnabled(False)
        self.radioButton.setGeometry(QtCore.QRect(230, 20, 95, 20))
        self.radioButton.setObjectName("radioButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 420, 261, 16))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(412, 420, 131, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.clear_button)
        yourtube.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(yourtube)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 864, 26))
        self.menubar.setObjectName("menubar")
        yourtube.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(yourtube)
        self.statusbar.setObjectName("statusbar")
        yourtube.setStatusBar(self.statusbar)
        self.retranslateUi(yourtube)
        QtCore.QMetaObject.connectSlotsByName(yourtube)

    def check_net(self):
        timeout = 1
        try:
            requests.head("http://www.google.com/", timeout=timeout)
            self.statusbar.showMessage('Internet works')
            return True
        except requests.ConnectionError:
            self.statusbar.showMessage('Internet connections problem.')
            return False

    def select_version(self):
        self.current_row = self.listWidget.currentRow()
        self.dl_Button.setEnabled(True)

    def download_button(self):
        if self.check_net():
            videos = self.yt.streams.all()
            dn_video = videos[self.current_row]
            dn_str = str(dn_video)
            dn_video.download()
            self.label_3.setText('Done and done')

    def clear_button(self):
        self.listWidget.clear()
        self.listWidget.setEnabled(False)
        self.dl_Button.setEnabled(False)
        self.lineEdit.setText("")
        self.label_3.setText('Its clear!')

    def go_button_click(self):
        if self.check_net():
            self.listWidget.clear()
            link = self.lineEdit.text()
            try:
                self.yt = YouTube(link)
            except:
                self.label_3.setText('Weird link...')
            else:
                try:
                    videos = self.yt.streams.all()
                except:
                    self.label_3.setText('I found nothing.')
                else:
                    self.label_3.setText('Look what i found, ' + str(len(videos)) + ' files')
                    video = list(enumerate(videos))
                    self.listWidget.setEnabled(True)
                    for i in video:
                        self.file_list.append(i)
                        self.listWidget.addItem(str(i[1]))

    def retranslateUi(self, yourtube):
        _translate = QtCore.QCoreApplication.translate
        yourtube.setWindowTitle(_translate("YourTube", "YourTube"))
        self.label.setText(_translate("YourTube", "Enter URL:"))
        self.label_2.setText(_translate("YourTube", "Status:"))
        self.go_button.setText(_translate("YourTube", "Go!"))
        self.dl_Button.setText(_translate("YourTube", "Download"))
        self.groupBox.setTitle(_translate("YourTube", "Filters"))
        self.radioButton_2.setText(_translate("YourTube", "All"))
        self.radioButton_3.setText(_translate("YourTube", "Video"))
        self.radioButton.setText(_translate("YourTube", "Audio"))
        self.label_3.setText(_translate("YourTube", "I am waiting..."))
        self.pushButton.setText(_translate("YourTube", "Clear"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon(r'img/icon.PNG'))
    YourTube = QtWidgets.QMainWindow()
    ui = UiYourTube()
    ui.setupUi(YourTube)
    YourTube.show()
    sys.exit(app.exec())
