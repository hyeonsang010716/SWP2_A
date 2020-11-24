from PyQt5.QtWidgets import *
import sys
class ScoreDB(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        AddButton = QPushButton("자신의 옷 저장하기")
        hbox2 = QHBoxLayout()
        hbox2.addWidget(AddButton)

        Add2Button = QPushButton("자신의 옷장 보기")
        hbox2.addWidget(Add2Button)
        self.setLayout(hbox2)

        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('assignment6')
        self.show()

        AddButton.clicked.connect(self.buttonClicked)
        Add2Button.clicked.connect(self.buttonClicked)

    def buttonClicked(self):
        button = self.sender()
        key = button.text()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())