from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtGui
from PyQt5 import uic
from PyQt5.QtCore import Qt
from pytube import YouTube


class MainWindows(QMainWindow):
    file_list = []
    current_row = None
    yt = None

    def __init__(self):
        super(MainWindows, self).__init__()
        self.dlg = uic.loadUi("yt_download.ui", self)
        self.show()
        self.go_button.clicked.connect(self.go_button_click)
        self.pushButton.clicked.connect(self.clear_button)
        self.listWidget.clicked.connect(self.select_version)
        self.dl_Button.clicked.connect(self.download_button)

    def download_button(self):
        videos = self.yt.streams.all()
        dn_video = videos[self.current_row]
        dn_video.download()
        self.label_3.setText('Pobrałem!')

    def select_version(self):
        self.current_row = self.listWidget.currentRow()
        print(self.current_row)

    def clear_button(self):
        self.listWidget.clear()
        self.listWidget.setEnabled(False)
        self.dl_Button.setEnabled(False)
        self.label_3.setText('Wyczyściłem')

    def go_button_click(self):
        self.dl_Button.setEnabled(True)
        self.listWidget.clear()
        link = self.lineEdit.text()
        try:
            self.yt = YouTube(link)
        except:
            self.label_3.setText('Jakiś dziwny ten link, sprawdź go')
        else:
            try:
                videos = self.yt.streams.all()
            except:
                self.label_3.setText('Nie odnaleziono plików, sprawdz link')
            else:
                self.label_3.setText('Zobacz co znalazłem')
                video = list(enumerate(videos))
                self.listWidget.setEnabled(True)
                for i in video:
                    self.file_list.append(i)
                    self.listWidget.addItem(str(i[1]))


def main():
    app = QApplication([])
    window = MainWindows()
    app.exec_()


if __name__ == '__main__':

    main()
