
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
import os

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        scrollArea = QScrollArea()
        self.resize(1000,1000)
        self.setWindowTitle("너의 코디는")
        cloth_type = ['Outer','Top(long)','Top(short)','Pants','Skirt','Ops']
        for i in range(len(cloth_type)):
            cloth_type[i] = QLabel(cloth_type[i], self)
            cloth_type[i].setFont(QFont('Arial', 20))
            cloth_type[i].move(40 + 170 * i, 30)

        list = ['Outer','Top(long)','Top(short)','Pants','Skirt','Ops']
        listA = [['padding','coat','jacket','zipup'],['tee','mtm','hood','shirt','knit'],['tee','shirt'],['long','short'],['long','short'],['long','short']]
        listB = [['Outer_padding','Outer_coat','Outer_jacket','Outer_zipup'],['Top(long)_tee','Top(long)_mtm','Top(long)_hood','Top(long)_shirt','Top(long)_knit'],['Top(short)_tee','Top(short)_shirt'],['Pants_long','Pants_short'],['Skirt_long','Skirt_short'],['Ops_long','Ops_short']]
        cloth_list = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        num = 0
        num2 = 0
        for i in range(len(list)):
            for k in range(len(listA[i])):
                cloth_list[num] = []
                cnt = 0
                cnt += len(os.listdir('/home/user/PycharmProjects/FirstUnittest/SWP2.24/{}/{}'.format(list[i],listA[i][k])))
                for t in range(cnt):
                    cloth_list[num].append(QLabel(self))
                    pixmap_rec = QPixmap('{}/{}/{}{}.jpg'.format(list[i],listA[i][k],listB[i][k],t))
                    pixmap_rec = pixmap_rec.scaledToWidth(100)
                    cloth_list[num][t].setPixmap(pixmap_rec)
                    cloth_list[num][t].move(20 + i * 170, 70 + 170 * num2)
                    num2 += 1
                num += 1
            num2 = 0




class Picture_closet(QWidget):
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
        #추천 옷 세트 1
        label_rec1 = []
        cnt = 0
        cnt += len(os.listdir('/home/user/PycharmProjects/FirstUnittest/SWP2.24/Outer/padding'))
        for i in range(cnt):
            label_rec1.append(QLabel(self))
            pixmap_rec = QPixmap('Outer/padding/Outer_padding{}.jpg'.format(i))
            pixmap_rec = pixmap_rec.scaledToWidth(100)
            label_rec1[i].setPixmap(pixmap_rec)
            rec_layout1.addWidget(label_rec1[i])

        cnt = 0
        cnt += len(os.listdir('/home/user/PycharmProjects/FirstUnittest/SWP2.24/Outer/coat'))
        for i in range(cnt):
            label_rec1.append(QLabel(self))
            pixmap_rec = QPixmap('Outer/coat/Outer_coat{}.jpg'.format(i))
            pixmap_rec = pixmap_rec.scaledToWidth(100)
            label_rec1[i].setPixmap(pixmap_rec)
            rec_layout1.addWidget(label_rec1[i])
        # 추천 옷 세트 2
        label_rec2 = []
        label_rec2.append(QLabel(self))
        pixmap_rec = QPixmap('savedata/doop.jpg')
        pixmap_rec = pixmap_rec.scaledToWidth(100)
        label_rec2[0].setPixmap(pixmap_rec)
        rec_layout2.addWidget(label_rec2[0])

        label_rec2.append(QLabel(self))
        pixmap_rec = QPixmap('savedata/hood.jpg')
        pixmap_rec = pixmap_rec.scaledToWidth(100)
        label_rec2[1].setPixmap(pixmap_rec)
        rec_layout2.addWidget(label_rec2[1])

        label_rec2.append(QLabel(self))
        pixmap_rec = QPixmap('savedata/pants2.jpg')
        pixmap_rec = pixmap_rec.scaledToWidth(100)
        label_rec2[2].setPixmap(pixmap_rec)
        rec_layout2.addWidget(label_rec2[2])

        # 추천 옷 세트 3
        label_rec3 = []
        label_rec3.append(QLabel(self))
        pixmap_rec = QPixmap('savedata/doop.jpg')
        pixmap_rec = pixmap_rec.scaledToWidth(100)
        label_rec3[0].setPixmap(pixmap_rec)
        rec_layout3.addWidget(label_rec3[0])

        label_rec3.append(QLabel(self))
        pixmap_rec = QPixmap('savedata/knit.jpg')
        pixmap_rec = pixmap_rec.scaledToWidth(100)
        label_rec3[1].setPixmap(pixmap_rec)
        rec_layout3.addWidget(label_rec3[1])

        label_rec3.append(QLabel(self))
        pixmap_rec = QPixmap('savedata/pants2.jpg')
        pixmap_rec = pixmap_rec.scaledToWidth(100)
        label_rec3[2].setPixmap(pixmap_rec)
        rec_layout3.addWidget(label_rec3[2])

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