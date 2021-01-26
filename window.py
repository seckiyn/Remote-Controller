import sys
import kumanda
from PyQt5 import QtWidgets
from PyQt5  import QtCore
from PyQt5.QtCore import QPoint
 



class Program(QtWidgets.QWidget):

    def __init__(self):

        super().__init__()
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)
        self.tv=kumanda.Kumanda("192.168.1.102")
        self.init_ui()
        self.setStyleSheet("""
        background-color: #515251;
        
        """)
        
    
    def init_ui(self):
        
        self.yazı_alanı = QtWidgets.QLineEdit()
         
        self.btn=QtWidgets.QPushButton("KUMANDAYI KAPAT")
                
        self.güc=QtWidgets.QPushButton("KAPAT")
        
        self.sessiz=QtWidgets.QPushButton("Sessize Al")

        self.ses_artı=QtWidgets.QPushButton("Ses Arttır")

        self.ses_eksi=QtWidgets.QPushButton("Ses Azalt")

        self.kanal_artı=QtWidgets.QPushButton("İleri Kanal")

        self.kanal_eksi=QtWidgets.QPushButton("Geri Kanal")

        self.setWindowTitle("Grundig Akıllı Tv Kumandası")

        self.menü1=QtWidgets.QPushButton("Menu")

        self.exit1=QtWidgets.QPushButton("Exit")

        self.back1=QtWidgets.QPushButton("Back")

        self.left1=QtWidgets.QPushButton("←")

        self.right1=QtWidgets.QPushButton("→")

        self.up1=QtWidgets.QPushButton("↑")

        self.down1=QtWidgets.QPushButton("↓")
      
        self.ok1= QtWidgets.QPushButton("Ok")

        self.tools1=QtWidgets.QPushButton("Tools")

        self.source1=QtWidgets.QPushButton("Source")
        
        self.guide1=QtWidgets.QPushButton("Guide")

        self.fav1=QtWidgets.QPushButton("Fav")

        self.text1=QtWidgets.QPushButton("Txt")

        self.zero1=QtWidgets.QPushButton("0")
        self.zero2=QtWidgets.QPushButton("1")
        self.zero3=QtWidgets.QPushButton("2")
        self.zero4=QtWidgets.QPushButton("3")
        self.zero5=QtWidgets.QPushButton("4")
        self.zero6=QtWidgets.QPushButton("5")
        self.zero7=QtWidgets.QPushButton("6")
        self.zero8=QtWidgets.QPushButton("7")
        self.zero9=QtWidgets.QPushButton("8")
        self.zero10=QtWidgets.QPushButton("9")

        self.rec1=QtWidgets.QPushButton("Rec")
        self.play1=QtWidgets.QPushButton("Play")
        self.pause1=QtWidgets.QPushButton("Pause")
        self.stop1=QtWidgets.QPushButton("Stop")
        self.prev1=QtWidgets.QPushButton("Previus")
        self.forward1=QtWidgets.QPushButton("Forward")
        self.next1=QtWidgets.QPushButton("Next")
      
        self.language1= QtWidgets.QPushButton("Language")
        self.subtitle1=QtWidgets.QPushButton("Subtittle")
        self.red1=QtWidgets.QPushButton(u"\U0001F534")
        self.green1=QtWidgets.QPushButton(u"\U0001F7E2")
        self.yellow1=QtWidgets.QPushButton(u"\U0001F7E0")
        self.blue1= QtWidgets.QPushButton(u"\U0001F535")
         

        self.setFixedSize(400,800)

        h1_box=QtWidgets.QHBoxLayout()

        h1_box.addWidget(self.güc)
        h1_box.addWidget(self.sessiz)
        
        h2_box=QtWidgets.QHBoxLayout()

        h2_box.addWidget(self.zero1)
        h2_box.addWidget(self.zero2)
        h2_box.addWidget(self.zero3)

        

        h3_box=QtWidgets.QHBoxLayout()
        
        h3_box.addWidget(self.zero4)
        h3_box.addWidget(self.zero5)
        h3_box.addWidget(self.zero6)

        h4_box=QtWidgets.QHBoxLayout()
        
        h4_box.addWidget(self.zero7)
        h4_box.addWidget(self.zero8)
        h4_box.addWidget(self.zero9)
        h4_box.addWidget(self.zero10)

        h41_box=QtWidgets.QHBoxLayout() 

        h41_box.addWidget(self.ses_artı)
        h41_box.addWidget(self.ses_eksi)
        h41_box.addWidget(self.kanal_artı)
        h41_box.addWidget(self.kanal_eksi)

        h5_box=QtWidgets.QHBoxLayout()

        h5_box.addWidget(self.menü1)
        h5_box.addWidget(self.back1)
        h5_box.addWidget(self.exit1)


        h6_box=QtWidgets.QHBoxLayout()

        h6_box.addWidget(self.left1)
        h6_box.addWidget(self.right1)
        h6_box.addWidget(self.up1)
        h6_box.addWidget(self.down1)



        h7_box=QtWidgets.QHBoxLayout()

        h7_box.addWidget(self.ok1)
        h7_box.addWidget(self.tools1)
        h7_box.addWidget(self.source1)
        h7_box.addWidget(self.guide1)
        h7_box.addWidget(self.fav1)
        h7_box.addWidget(self.text1)

        
        h8_box=QtWidgets.QHBoxLayout()

        h8_box.addWidget(self.rec1)
        h8_box.addWidget(self.play1)
        h8_box.addWidget(self.pause1)
        h8_box.addWidget(self.stop1)
        h8_box.addWidget(self.forward1)
        h8_box.addWidget(self.next1)

        h9_box=QtWidgets.QHBoxLayout()

        h9_box.addWidget(self.language1)
        h9_box.addWidget(self.subtitle1)

        h10_box=QtWidgets.QHBoxLayout()

        h10_box.addWidget(self.red1)
        h10_box.addWidget(self.green1)
        h10_box.addWidget(self.yellow1)
        h10_box.addWidget(self.blue1)


        v_box = QtWidgets.QVBoxLayout()
        v_box.addLayout(h1_box)
        v_box.addLayout(h2_box)
        v_box.addLayout(h3_box)
        v_box.addLayout(h4_box)
        v_box.addLayout(h41_box)
        v_box.addLayout(h5_box)
        v_box.addLayout(h6_box)
        v_box.addLayout(h7_box)
        v_box.addLayout(h8_box)
        v_box.addLayout(h9_box)
        v_box.addLayout(h10_box)
        v_box.addWidget(self.btn)
         

        self.setLayout(v_box)

        
        self.güc.clicked.connect(self.tv.power_off)
	
        self.sessiz.clicked.connect(self.tv.toggle_mute)

        self.ses_artı.clicked.connect(self.tv.volume_up)

        self.ses_eksi.clicked.connect(self.tv.volume_down)

        self.kanal_artı.clicked.connect(self.tv.channel_up)

        self.kanal_eksi.clicked.connect(self.tv.channel_down)

        self.menü1.clicked.connect(self.tv.menu)

        self.exit1.clicked.connect(self.tv.exitt)

        self.back1.clicked.connect(self.tv.back)

        self.left1.clicked.connect(self.tv.left)

        self.right1.clicked.connect(self.tv.right)

        self.up1.clicked.connect(self.tv.top)

        self.down1.clicked.connect(self.tv.bottom)
      
        self.ok1.clicked.connect(self.tv.ok)

        self.tools1.clicked.connect(self.tv.tools)

        self.source1.clicked.connect(self.tv.source)
        
        self.guide1.clicked.connect(self.tv.guide)

        self.fav1.clicked.connect(self.tv.fav)

        self.text1.clicked.connect(self.tv.txt)

        self.zero1.clicked.connect(self.tv.zero)
        self.zero2.clicked.connect(self.tv.one)
        self.zero3.clicked.connect(self.tv.two)
        self.zero4.clicked.connect(self.tv.three)
        self.zero5.clicked.connect(self.tv.four)
        self.zero6.clicked.connect(self.tv.five)
        self.zero7.clicked.connect(self.tv.six)
        self.zero8.clicked.connect(self.tv.seven)
        self.zero9.clicked.connect(self.tv.eight)
        self.zero10.clicked.connect(self.tv.nine)

        self.rec1.clicked.connect(self.tv.rec)
        self.play1.clicked.connect(self.tv.play)
        self.pause1.clicked.connect(self.tv.pause)
        self.stop1.clicked.connect(self.tv.stop)
        self.prev1.clicked.connect(self.tv.prev)
        self.forward1.clicked.connect(self.tv.forward)
        self.next1.clicked.connect(self.tv.next)
      
        self.language1.clicked.connect(self.tv.language)
        self.subtitle1.clicked.connect(self.tv.subtitle)
        self.red1.clicked.connect(self.tv.red)
        self.green1.clicked.connect(self.tv.green)
        self.yellow1.clicked.connect(self.tv.yellow)
        self.blue1.clicked.connect(self.tv.blue)
        
        self.btn.clicked.connect(self.close)

        self.show()

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint (event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()



app = QtWidgets.QApplication(sys.argv)

app.setStyle("Breeze")

pencere = Program()

sys.exit(app.exec_())


