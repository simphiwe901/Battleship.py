#InterfaceShotsCuts
# Simphiwe Mchunu
# 25 April 2016


import sys
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):
    def __init__(self):
        super(Window,self).__init__()
        self.resize(400,500)
        #self.setWindowTitle("BattleshipGameClient Home!!")
        self.setWindowIcon(QtGui.QIcon("java.jpg"))
        #self.app = QApplication(sys.argv)
        #self.widget = QWidget() 
        
        mainAction1 = QtGui.QAction("&Exit",self)
        mainAction1.setShortcut("CTRL+Q")
        mainAction1.setStatusTip("Quit App!!")
        mainAction1.triggered.connect(self.quit)
        self.statusBar()
        mainmenu = self.menuBar()
        filemenu = mainmenu.addMenu("&File")
        filemenu.addAction(mainAction1)
        
        mainAction2 = QtGui.QAction("&Play",self)
        mainAction2.setShortcut("CTRL+P")
        self.statusBar()
        mainmenu = self.menuBar()
        filemenu.addAction(mainAction2)  
        
        mainAction3 = QtGui.QAction("&Synopsis",self)
        mainAction3.triggered.connect(self.handle_new_window)
        mainAction3.setShortcut("CTRL+A")
        self.statusBar()
        mainmenu = self.menuBar()
        filemenu.addAction(mainAction3)
        
        mainAction4 = QtGui.QAction("&Game Settings",self)
        mainAction4.setShortcut("CTRL+G")
        self.statusBar()
        mainmenu = self.menuBar()
        filemenu = mainmenu.addMenu("&Settings")
        filemenu.addAction(mainAction4) 
        
        
        '''PROGRESS BAR'''
        self.bar = QtGui.QProgressBar(self)
        self.bar.setGeometry(150,80,250,20)
        self.bar.move(300,650)       
        
        
        self.home()
        self.initUI()
    
    def home(self):
        quit_button = QtGui.QPushButton("QUIT",self)
        quit_button.clicked.connect(self.quit)
        quit_button.resize(100,80)
        quit_button.move(700,600)
        
        info_button = QtGui.QPushButton("SYNOPSIS",self)
        info_button.clicked.connect(self.handle_new_window)
        info_button.resize(100,80)
        info_button.move(700,500) 
        
        play_button = QtGui.QPushButton("PLAY",self)
        play_button.resize(100,80)
        play_button.move(700,400)
        self.show()
        
    def initUI(self):
                
    #Layout of window
            self.resize(800,700) #Maximizing main window
            self.setWindowTitle('BattleshipGameClient Home') #Setting window title
            #self.setStyleSheet("border-image: url(battleship2016.jpg);") # sets background image      
            self.show()    
        
    def quit(self):
        player_choice = QtGui.QMessageBox.question(self,"QUIT!!!","You are about to exit, Are sure you want to Quit?",QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if player_choice == QtGui.QMessageBox.No:
            pass
        else:
            sys.exit()
        
    def handle_new_window(self):
        window = QtGui.QMainWindow(self)
        window.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        window.resize(700,600)
        window.setWindowTitle(self.tr('GAME INSTRUCTIONS'))
        
        quit_button = QtGui.QPushButton("QUIT",self)
        quit_button.clicked.connect(self.quit)
        quit_button.resize(100,80)
        quit_button.move(700,200) 
        
        window.show()
        
    def progress_bar_1(self):
            self.done = 0
            while self.done < 100:
                self.done += 0.00001
                self.bar.setValue(self.done)
            time.sleep(2)
    def progress_bar_2(self):
            self.done = 0
            while self.done < 100:
                self.done += 0.00001
                self.bar.setValue(self.done)     
def main():
    app= QtGui.QApplication(sys.argv)
    widget= Window()
    widget.show()
    sys.exit(app.exec_())
    
main()
