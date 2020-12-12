import sys
import pickle
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
'''from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication, QLabel,
    QComboBox, QTextEdit, QLineEdit, QRadioButton, QDialog)
from PyQt5.QtCore import Qt'''


class FistWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.dbfilename = 'user.dat'
        self.user = []
        self.readDB()


    def initUI(self):
        self.setGeometry(300, 300, 400, 200)
        self.setWindowTitle('너의 코디는')

        # QHBoxLayout 만들기
        self.hbox0 = QHBoxLayout()  # '너의 코디는'
        self.hbox1 = QHBoxLayout()  # 사용자 이름
        self.hbox2 = QHBoxLayout()  # 비밀번호
        self.hbox3 = QHBoxLayout()  # 지역명
        self.hbox4 = QHBoxLayout()  # 성별
        self.hbox5 = QHBoxLayout()  # go 버


        # hbox0 구성
        label1 = QLabel('너의 코디는', self)
        label1.setAlignment(Qt.AlignCenter)

        font1 = label1.font()
        font1.setPointSize(20)

        label1.setFont(font1)

        self.hbox0.addWidget(label1)


        # hbox1 구성
        self.hbox1.addWidget(QLabel('사용자 이름 : '))
        self.username_input = QLineEdit()
        self.hbox1.addWidget(self.username_input)

        # hbox2 구성
        self.hbox2.addWidget(QLabel('    비밀번호 : '))
        self.usercode_input = QLineEdit()
        self.hbox2.addWidget(self.usercode_input)


        # hbox3 구성
        self.hbox3.addWidget(QLabel('  지역명(동) : '))
        self.loc_input = QLineEdit()
        self.hbox3.addWidget(self.loc_input)


        #hbox4 구성
        self.man = QRadioButton('남자')
        self.woman = QRadioButton('여자')

        self.hbox4.addWidget(QLabel('성별:'))
        self.hbox4.addWidget(self.man)
        self.hbox4.addWidget(self.woman)


        #hbox5 구성
        self.goButton = QPushButton("GO")
        self.hbox5.addWidget(self.goButton)
        self.goButton.clicked.connect(self.mb)

        # QVBoxLayout 만들기
        self.vbox = QVBoxLayout()
        self.vbox.addLayout(self.hbox0)
        self.vbox.addLayout(self.hbox1)
        self.vbox.addLayout(self.hbox2)
        self.vbox.addLayout(self.hbox3)
        self.vbox.addLayout(self.hbox4)
        self.vbox.addLayout(self.hbox5)

        self.setLayout(self.vbox)

        self.dialog = QDialog()


    def closeEvent(self, event):
        self.writeDB()

    def readDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.user = []
            return
        try:
            self.user = pickle.load(fH)
        except:
            pass
        fH.close()


    def writeDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.user, fH)
        fH.close()



    def mb(self , event):
        iusname = str(self.username_input)
        iuscode = str(self.usercode_input)
        ilocation = str(self.loc_input.text())

        if self.username_input.text() == '' or iusname.isdigit() == True:
            reply = QMessageBox.question(self, '알림창', '지역명을 바르게 입력하세요.',
                                         QMessageBox.Yes)
        elif self.loc_input.text() == '' or ilocation.isdigit() == True:
            reply = QMessageBox.question(self, '알림창', '지역명과 성별을 입력하세요.',
                                     QMessageBox.Yes)

        else:
            self.dialog_open()
        '''if self.loc_input.text().isdigit() == False:
            reply = QMessageBox.question(self, '알림창', '지역명과 성별을 입력하세요.',
                                         QMessageBox.Yes)'''



    def dialog_open(self):
        if self.man.isChecked():
            name = self.username_input.text()
            pw = self.usercode_input.text()
            location = self.loc_input.text()
            sex = 'man'
            record = dict(Name=name, Pw=pw, Location=location, Sex=sex)
            self.user += [record]

            self.dialog.setWindowTitle('남자')
            self.dialog.setWindowModality(Qt.ApplicationModal)
            self.dialog.resize(200, 200)
            self.dialog.show()



        if self.woman.isChecked():
            name = self.username_input
            pw = self.usercode_input
            location = self.loc_input.text()
            sex = 'woman'
            record = dict(Name=name, Pw=pw, Location=location, Sex=sex)
            self.user += [record]

            self.dialog.setWindowTitle('여자')
            self.dialog.setWindowModality(Qt.ApplicationModal)
            self.dialog.resize(200, 200)
            self.dialog.show()


    def dialog_close(self):
        self.dialog.close()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FistWindow()
    ex.show()
    sys.exit(app.exec_())