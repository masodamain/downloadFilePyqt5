import urllib.request
from os.path import splitext
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

class Myapp(QWidget):  
    def __init__(self): 
        super().__init__() 
        self.init_UI() 

    def init_UI(self):
        global en
        self.setGeometry(100, 100, 465, 300)
        self.setWindowTitle("download file from internet")
        self.setStyleSheet('background-color: rgb(133,144,219)')
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.buttone = QPushButton('X', self)
        self.buttone.setStyleSheet('color: white ;background-color:#e01f1a;border: 1px solid #f1e4e4; border-radius: 9px')
        self.buttone.resize(40,40)
        self.buttone.move(420, 11) 
        self.buttone.clicked.connect(self.exit) 
    
        self.en = QLineEdit(self)
        self.en.setPlaceholderText('Enter url ')
        self.en.setStyleSheet('color:#eee6e2 ;border: 1px solid #f1e4e4; border-radius: 10px')
        self.en.move(10,10)
        self.en.resize(400,50)
        
        self.button = QPushButton('download', self)
        self.button.setStyleSheet('color: white ;background-color:#fb6b2b;border: 1px solid #f1e4e4; border-radius: 9px')
        self.button.resize(400,40)
        self.button.move(10, 100) 
        self.button.clicked.connect(self.Download) 

        self.progressBar = QProgressBar(self)
        self.progressBar.setGeometry(25, 45, 210, 30)
        self.progressBar.resize(400,40)
        self.progressBar.move(10, 150)
        
        style = '''
        QProgressBar{
            border: 2px solid #f1e4e4;
            border-radius: 9px;
            text-align: center;
            }
        QProgressBar::chunk{
            background-color:#8f8f8f;
            color: #d9d9d9
            }
            '''        
        self.progressBar.setStyleSheet(style)
        self.show()

    def exit(self):
        window.close() 
   
    def Handle_Progress(self, blocknum, blocksize, totalsize):
        
        readed_data = blocknum * blocksize   
        if totalsize > 0: 
            download_percentage = readed_data * 101 / totalsize 
            self.progressBar.setValue(download_percentage) 
            QApplication.processEvents()
            
    def Download(self):   
        down = self.en.text() 
        c=splitext(down_url)[1]
        if c =='':
            QMessageBox.warning(self,'data vide','U cant download this file')
        else:
            loc = 'File dowwnload'+str(c)
            x = urllib.request.urlretrieve(down,loc, self.Handle_Progress)
  
if __name__ == '__main__': 
    App = QApplication(sys.argv) 
    window = Myapp() 
    sys.exit(App.exec()) 
