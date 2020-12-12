
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
import os

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.resize(1000,1000)
        self.setWindowTitle("너의 코디는")
        self.hbox3 = QHBoxLayout()  # 추천조합
        cloth_type = ['Outer','Top(long)','Top(short)','Pants','Skirt','Ops']

        rec_layout1 = QVBoxLayout()
        rec_layout2 = QVBoxLayout()
        rec_layout3 = QVBoxLayout()
        rec_layout4 = QVBoxLayout()
        rec_layout5 = QVBoxLayout()
        rec_layout6 = QVBoxLayout()
        rec_layout1.addWidget(QLabel(cloth_type[0], self))
        rec_layout2.addWidget(QLabel(cloth_type[1], self))
        rec_layout3.addWidget(QLabel(cloth_type[2], self))
        rec_layout4.addWidget(QLabel(cloth_type[3], self))
        rec_layout5.addWidget(QLabel(cloth_type[4], self))
        rec_layout6.addWidget(QLabel(cloth_type[5], self))
        #Outer 모음
        label_outer1 = []
        cnt = 0
        cnt += len(os.listdir('/home/user/PycharmProjects/FirstUnittest/SWP2.24/Outer/padding'))
        for i in range(cnt):
            label_outer1.append(QLabel(self))
            pixmap_rec = QPixmap('Outer/padding/Outer_padding{}.jpg'.format(i))
            pixmap_rec = pixmap_rec.scaledToWidth(100)
            label_outer1[i].setPixmap(pixmap_rec)
            rec_layout1.addWidget(label_outer1[i])
        label_outer2 = []
        cnt = 0
        cnt += len(os.listdir('/home/user/PycharmProjects/FirstUnittest/SWP2.24/Outer/coat'))
        for i in range(cnt):
            label_outer2.append(QLabel(self))
            pixmap_rec = QPixmap('Outer/coat/Outer_coat{}.jpg'.format(i))
            pixmap_rec = pixmap_rec.scaledToWidth(100)
            label_outer2[i].setPixmap(pixmap_rec)
            rec_layout1.addWidget(label_outer2[i])
        label_outer3 = []
        cnt = 0
        cnt += len(os.listdir('/home/user/PycharmProjects/FirstUnittest/SWP2.24/Outer/jacket'))
        for i in range(cnt):
            label_outer3.append(QLabel(self))
            pixmap_rec = QPixmap('Outer/jacket/Outer_jacket{}.jpg'.format(i))
            pixmap_rec = pixmap_rec.scaledToWidth(100)
            label_outer3[i].setPixmap(pixmap_rec)
            rec_layout1.addWidget(label_outer3[i])
        label_outer4 = []
        cnt = 0
        cnt += len(os.listdir('/home/user/PycharmProjects/FirstUnittest/SWP2.24/Outer/zipup'))
        for i in range(cnt):
            label_outer4.append(QLabel(self))
            pixmap_rec = QPixmap('Outer/zipup/Outer_zipup{}.jpg'.format(i))
            pixmap_rec = pixmap_rec.scaledToWidth(100)
            label_outer4[i].setPixmap(pixmap_rec)
            rec_layout1.addWidget(label_outer4[i])

        # Top(long) 모음
        label_top_long1 = []
        cnt = 0
        cnt += len(os.listdir('/home/user/PycharmProjects/FirstUnittest/SWP2.24/Top(long)/tee'))
        for i in range(cnt):
            label_top_long1.append(QLabel(self))
            pixmap_rec = QPixmap('Top(long)/tee/Top(long)_tee{}.jpg'.format(i))
            pixmap_rec = pixmap_rec.scaledToWidth(100)
            label_top_long1[i].setPixmap(pixmap_rec)
            rec_layout2.addWidget(label_top_long1[i])

        label_top_long2 = []
        cnt = 0
        cnt += len(os.listdir('/home/user/PycharmProjects/FirstUnittest/SWP2.24/Top(long)/mtm'))
        for i in range(cnt):
            label_top_long2.append(QLabel(self))
            pixmap_rec = QPixmap('Top(long)/mtm/Top(long)_mtm{}.jpg'.format(i))
            pixmap_rec = pixmap_rec.scaledToWidth(100)
            label_top_long2[i].setPixmap(pixmap_rec)
            rec_layout2.addWidget(label_top_long2[i])

        label_top_long3 = []
        cnt = 0
        cnt += len(os.listdir('/home/user/PycharmProjects/FirstUnittest/SWP2.24/Top(long)/hood'))
        for i in range(cnt):
            label_top_long3.append(QLabel(self))
            pixmap_rec = QPixmap('Top(long)/hood/Top(long)_hood{}.jpg'.format(i))
            pixmap_rec = pixmap_rec.scaledToWidth(100)
            label_top_long3[i].setPixmap(pixmap_rec)
            rec_layout2.addWidget(label_top_long3[i])

        label_top_long4 = []
        cnt = 0
        cnt += len(os.listdir('/home/user/PycharmProjects/FirstUnittest/SWP2.24/Top(long)/shirt'))
        for i in range(cnt):
            label_top_long4.append(QLabel(self))
            pixmap_rec = QPixmap('Top(long)/shirt/Top(long)_shirt{}.jpg'.format(i))
            pixmap_rec = pixmap_rec.scaledToWidth(100)
            label_top_long4[i].setPixmap(pixmap_rec)
            rec_layout2.addWidget(label_top_long4[i])

        label_top_long5 = []
        cnt = 0
        cnt += len(os.listdir('/home/user/PycharmProjects/FirstUnittest/SWP2.24/Top(long)/knit'))
        for i in range(cnt):
            label_top_long5.append(QLabel(self))
            pixmap_rec = QPixmap('Top(long)/knit/Top(long)_knit{}.jpg'.format(i))
            pixmap_rec = pixmap_rec.scaledToWidth(100)
            label_top_long5[i].setPixmap(pixmap_rec)
            rec_layout2.addWidget(label_top_long5[i])

        # Top(short) 모음
        label_top_short1 = []
        cnt = 0
        cnt += len(os.listdir('/home/user/PycharmProjects/FirstUnittest/SWP2.24/Top(short)/tee'))
        for i in range(cnt):
            label_top_short1.append(QLabel(self))
            pixmap_rec = QPixmap('Top(short)/tee/Top(short)_tee{}.jpg'.format(i))
            pixmap_rec = pixmap_rec.scaledToWidth(100)
            label_top_short1[i].setPixmap(pixmap_rec)
            rec_layout3.addWidget(label_top_short1[i])

        label_top_short2 = []
        cnt = 0
        cnt += len(os.listdir('/home/user/PycharmProjects/FirstUnittest/SWP2.24/Top(short)/shirt'))
        for i in range(cnt):
            label_top_short2.append(QLabel(self))
            pixmap_rec = QPixmap('Top(short)/shirt/Top(short)_shirt{}.jpg'.format(i))
            pixmap_rec = pixmap_rec.scaledToWidth(100)
            label_top_short2[i].setPixmap(pixmap_rec)
            rec_layout3.addWidget(label_top_short2[i])
        # Pants 모음
        label_pants1 = []
        cnt = 0
        cnt += len(os.listdir('/home/user/PycharmProjects/FirstUnittest/SWP2.24/Pants/long'))
        for i in range(cnt):
            label_pants1.append(QLabel(self))
            pixmap_rec = QPixmap('Pants/long/Pants_long{}.jpg'.format(i))
            pixmap_rec = pixmap_rec.scaledToWidth(100)
            label_pants1[i].setPixmap(pixmap_rec)
            rec_layout4.addWidget(label_pants1[i])

        label_pants2 = []
        cnt = 0
        cnt += len(os.listdir('/home/user/PycharmProjects/FirstUnittest/SWP2.24/Pants/short'))
        for i in range(cnt):
            label_pants2.append(QLabel(self))
            pixmap_rec = QPixmap('Pants/short/Pants_short{}.jpg'.format(i))
            pixmap_rec = pixmap_rec.scaledToWidth(100)
            label_pants2[i].setPixmap(pixmap_rec)
            rec_layout4.addWidget(label_pants2[i])

        #Skirt 모음
        label_skirt1 = []
        cnt = 0
        cnt += len(os.listdir('/home/user/PycharmProjects/FirstUnittest/SWP2.24/Skirt/long'))
        for i in range(cnt):
            label_skirt1.append(QLabel(self))
            pixmap_rec = QPixmap('Skirt/long/Skirt_long{}.jpg'.format(i))
            pixmap_rec = pixmap_rec.scaledToWidth(100)
            label_skirt1[i].setPixmap(pixmap_rec)
            rec_layout5.addWidget(label_skirt1[i])

        label_skirt2 = []
        cnt = 0
        cnt += len(os.listdir('/home/user/PycharmProjects/FirstUnittest/SWP2.24/Skirt/short'))
        for i in range(cnt):
            label_skirt2.append(QLabel(self))
            pixmap_rec = QPixmap('Skirt/short/Skirt_short{}.jpg'.format(i))
            pixmap_rec = pixmap_rec.scaledToWidth(100)
            label_skirt2[i].setPixmap(pixmap_rec)
            rec_layout5.addWidget(label_skirt2[i])

        #Ops 모음
        label_ops1 = []
        cnt = 0
        cnt += len(os.listdir('/home/user/PycharmProjects/FirstUnittest/SWP2.24/Ops/long'))
        for i in range(cnt):
            label_ops1.append(QLabel(self))
            pixmap_rec = QPixmap('Ops/long/Ops_long{}.jpg'.format(i))
            pixmap_rec = pixmap_rec.scaledToWidth(100)
            label_ops1[i].setPixmap(pixmap_rec)
            rec_layout6.addWidget(label_ops1[i])

        label_ops2 = []
        cnt = 0
        cnt += len(os.listdir('/home/user/PycharmProjects/FirstUnittest/SWP2.24/Ops/short'))
        for i in range(cnt):
            label_ops2.append(QLabel(self))
            pixmap_rec = QPixmap('Ops/short/Ops_short{}.jpg'.format(i))
            pixmap_rec = pixmap_rec.scaledToWidth(100)
            label_ops2[i].setPixmap(pixmap_rec)
            rec_layout6.addWidget(label_ops2[i])



        self.hbox3.addLayout(rec_layout1)
        self.hbox3.addLayout(rec_layout2)
        self.hbox3.addLayout(rec_layout3)
        self.hbox3.addLayout(rec_layout4)
        self.hbox3.addLayout(rec_layout5)
        self.hbox3.addLayout(rec_layout6)


        # QVBoxLayout 만들기
        self.vbox = QVBoxLayout()
        self.vbox.addLayout(self.hbox3)

        self.setLayout(self.vbox)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

