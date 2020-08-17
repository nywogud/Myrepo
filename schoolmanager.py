# with open('D:\\leejh\\PycharmProjects\\jump\\schoolmanager.txt', 'r', encoding = "utf-8") as f:
#     list = []
#     data = f.read() # 파일 읽어오기
#     list = data.split(',') # 문자열을 리스트로 변환
#     list_1 = []
#     for i in range(len(list)): # 2차원 리스트로 가공 [['손', 10, 20, 50], ['케인', 30, 40, 10]]
#        if i %4 == 0:
#            list_1.append([list[i],int(list[i+1]), int(list[i+2]), int(list[i+3])]) # list_1 = [['손', 10, 20, 50], ['케인', 30, 40, 10], ['알리', 20, 70, 30], [' 무리뉴', 50, 60, 70]]
#
#
#     temp = []
#     for j in range(len(list_1)):
#         temp.append(round((list_1[j][1]+ list_1[j][2] +list_1[j][3])/3,2)) #과목수 만큼 나누기
#
#         # temp = [26.67, 26.67, 40.0, 60.0]
#     for a in range(len(list_1)):
#         print("{}의 전과목 평균 점수 : {}".format(list_1[a][0], temp[a])) # 각 학생의 평균 점수 출력





# import sys
# from PyQt5.QtWidgets import *
#
#
# class MyApp(QWidget):
#
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#
#     def initUI(self):
#         self.setWindowTitle('Centering')
#         self.resize(800, 700)
#         self.center()
#         self.show()
#
#
#     def center(self):
#         qr = self.frameGeometry()
#         cp = QDesktopWidget().availableGeometry().center()
#         qr.moveCenter(cp)
#         self.move(qr.topLeft())
#
# if __name__ == '__main__':
#    app = QApplication(sys.argv)
#    ex = MyApp()
#    sys.exit(app.exec_())
#



#  파일 쓰기 TextEdit 검색 : [PyQt5]pyqt5로 파일 생성하는 프로그램 만들기

# import sys
# from PyQt5.QtWidgets import *
# import os
#
# class Main(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         lbl1 = QLabel('파일 경로')
#         self.qle1 = QLineEdit()
#
#         lbl2 = QLabel('파일 이름')
#         self.qle2 = QLineEdit()
#
#         lbl3 = QLabel('파일 내용')
#         self.te = QTextEdit()
#
#         btn = QPushButton('파일 생성')
#         btn.clicked.connect(self.makeFile_btn)
#
#         vbox = QVBoxLayout()
#         vbox.addWidget(lbl1)
#         vbox.addWidget(self.qle1)
#         vbox.addWidget(lbl2)
#         vbox.addWidget(self.qle2)
#         vbox.addWidget(lbl3)
#         vbox.addWidget(self.te)
#         vbox.addWidget(btn)
#
#         self.setLayout(vbox)
#
#         self.setWindowTitle('makeFile')
#         self.setGeometry(100, 100, 250, 300)
#         self.show()
#
#     def makeFile_btn(self):
#         if len(self.qle1.text()) == 0 or len(self.qle2.text()) == 0 or len(self.te.toPlainText()) == 0:
#             return
#         directory = self.qle1.text() + '/'
#         if os.path.isdir(directory):
#             print('its okay')
#         else:
#             print('다이렉토리가 존재하지 않습니다.')
#             return
#         name = self.qle2.text() + '.txt'
#         content = self.te.toPlainText()
#         filename = directory + name
#         mkfile = open(filename, 'w')
#         mkfile.write(content)
#         mkfile.close()
#
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Main()
#     sys.exit(app.exec_())





