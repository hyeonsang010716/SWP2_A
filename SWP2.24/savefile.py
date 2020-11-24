
from PyQt5.QtWidgets import *
import sys
import cv2
import os
import PIL

class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        ex = QLabel('사진을 드래그하세요!')

        self.label = QLabel(self)

        layout = QVBoxLayout()
        layout.addWidget(ex)
        layout.addWidget(self.label)

        self.setLayout(layout)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        event.acceptProposedAction()

    def dragMoveEvent(self, event):
        event.acceptProposedAction()

    def dropEvent(self, event):
        if (event.mimeData().hasUrls()):
            fname = event.mimeData().urls()[0].toLocalFile()
            img_color = cv2.imread(fname, cv2.IMREAD_COLOR)
            cv2.imwrite('../SWP2.24/savedimage{}.jpg'.format(len(os.listdir('/home/user/PycharmProjects/FirstUnittest/SWP2.24/'))-2), img_color)
            sys.exit(app.exec_())


        event.acceptProposedAction()

    def dragLeaveEvent(self, event):
        event.accept()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(320, 240)
    window.show()
    sys.exit(app.exec_())




