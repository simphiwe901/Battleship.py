# BattleshipGameClient - Prototype
# Simphiwe Mchunu
# 25 April 2016

import sys
from PyQt4 import QtGui, QtCore
from LoopThread import*
from GameClient import *

class Guessgame(QtGui.QWidget, GameClient):
    '''Constructor that initialises variables'''
    def __init__(self,parent= None):
        QtGui.QWidget.__init__(self)
        GameClient.__init__(self)
        #self.board = self.game_board()
        self.setWindowTitle('BattleshipGameClient')
        self.setGeometry(500,200,460,350)
        self.server = QtGui.QLabel('Enter Server:')
        self.role = QtGui.QLabel("Participants' role:")
        self.board_message = QtGui.QLabel('Game Board')
        self.server_message = QtGui.QLabel('Server Message')
        self.server_message.setFont(QtGui.QFont('Arial Black',11,1))
        self.board_message.setFont(QtGui.QFont('Arial Black',11,1))
        self.score = QtGui.QLabel('Score')
        self.score.setFont(QtGui.QFont('Arial Black',10,1))
        self.captain = QtGui.QLabel('Captain:')
        self.general = QtGui.QLabel('General:') 
        self.setPalette(QtGui.QPalette(QtGui.QColor('lightblue')))
        #self.setAutoFillBackground(True)
        #self.setStyleSheet("background-image: url(1.png);")

        
        self.gamelayout= QtGui.QGridLayout()
        win = QtGui.QWidget()
        self.pixmap1 = QtGui.QPixmap('2.jpg')
        self.pic_label1= QtGui.QLabel(self)
        self.pic_label1.setPixmap(self.pixmap1)
        
        vbox = QtGui.QGridLayout()
        vbox.addWidget(self.pic_label1)
        win.setLayout(vbox)
        
        self.position00= QtGui.QPushButton('')
        self.position00.setFixedWidth(80)
        self.position00.setFixedHeight(80)
        self.position00.setStyleSheet('background-color:darkMagenta;')
        
        self.position01= QtGui.QPushButton('')
        self.position01.setFixedWidth(80)
        self.position01.setFixedHeight(80)
        self.position01.setStyleSheet('background-color:darkMagenta;')
        
        self.position02= QtGui.QPushButton('')
        self.position02.setFixedWidth(80)
        self.position02.setFixedHeight(80)
        self.position02.setStyleSheet('background-color:darkMagenta;')
        
        self.position03= QtGui.QPushButton('')
        self.position03.setFixedWidth(80)
        self.position03.setFixedHeight(80)
        self.position03.setStyleSheet('background-color:darkMagenta;')
        
        self.position04= QtGui.QPushButton('')
        self.position04.setFixedWidth(80)
        self.position04.setFixedHeight(80) 
        self.position04.setStyleSheet('background-color:darkMagenta;')
        self.position05= QtGui.QPushButton('')
        self.position05.setFixedWidth(80)
        self.position05.setFixedHeight(80) 
        self.position05.setStyleSheet('background-color:darkMagenta;')
        
        self.position10= QtGui.QPushButton('')
        self.position10.setFixedWidth(80)
        self.position10.setFixedHeight(80)
        self.position10.setStyleSheet('background-color:darkMagenta;')
        
        self.position11= QtGui.QPushButton('')
        self.position11.setFixedWidth(80)
        self.position11.setFixedHeight(80)
        self.position11.setStyleSheet('background-color:lightblue;')
        
        self.position12= QtGui.QPushButton('')
        self.position12.setFixedWidth(80)
        self.position12.setFixedHeight(80)
        self.position12.setStyleSheet('background-color:lightblue;')
        
        self.position13= QtGui.QPushButton('')
        self.position13.setFixedWidth(80)
        self.position13.setFixedHeight(80)
        self.position13.setStyleSheet('background-color:lightblue;')
        
        
        self.position14= QtGui.QPushButton('')
        self.position14.setFixedWidth(80)
        self.position14.setFixedHeight(80)
        self.position14.setStyleSheet('background-color:lightblue;')
        
        self.position15= QtGui.QPushButton('')
        self.position15.setFixedWidth(80)
        self.position15.setFixedHeight(80)
        self.position15.setStyleSheet('background-color:darkMagenta;')
        
        self.position20= QtGui.QPushButton('')
        self.position20.setFixedWidth(80)
        self.position20.setFixedHeight(80)
        self.position20.setStyleSheet('background-color:darkMagenta;')
        
        self.position21= QtGui.QPushButton('')
        self.position21.setFixedWidth(80)
        self.position21.setFixedHeight(80)
        self.position21.setStyleSheet('background-color:lightblue;')
        
        
        self.position22= QtGui.QPushButton('')
        self.position22.setFixedWidth(80)
        self.position22.setFixedHeight(80)
        self.position22.setStyleSheet('background-color:magenta;')
        
        self.position23= QtGui.QPushButton('')
        self.position23.setFixedWidth(80)
        self.position23.setFixedHeight(80)
        self.position23.setStyleSheet('background-color:magenta;')
        
        self.position24= QtGui.QPushButton('')
        self.position24.setFixedWidth(80)
        self.position24.setFixedHeight(80)
        self.position24.setStyleSheet('background-color:lightblue;')
        
        self.position25= QtGui.QPushButton('')
        self.position25.setFixedWidth(80)
        self.position25.setFixedHeight(80)
        self.position25.setStyleSheet('background-color:darkMagenta;')
        
        self.position30= QtGui.QPushButton('')
        self.position30.setFixedWidth(80)
        self.position30.setFixedHeight(80)
        self.position30.setStyleSheet('background-color:darkMagenta;')
        
        self.position31= QtGui.QPushButton('')
        self.position31.setFixedWidth(80)
        self.position31.setFixedHeight(80)
        self.position31.setStyleSheet('background-color:lightblue;')
        
        self.position32= QtGui.QPushButton('')
        self.position32.setFixedWidth(80)
        self.position32.setFixedHeight(80)
        self.position32.setStyleSheet('background-color:magenta;')
        
        self.position33= QtGui.QPushButton('')
        self.position33.setFixedWidth(80)
        self.position33.setFixedHeight(80)
        self.position33.setStyleSheet('background-color:magenta;')
        
        
        self.position34= QtGui.QPushButton('')
        self.position34.setFixedWidth(80)
        self.position34.setFixedHeight(80)
        self.position34.setStyleSheet('background-color:lightblue;')
        
        
        self.position35= QtGui.QPushButton('')
        self.position35.setFixedWidth(80)
        self.position35.setFixedHeight(80)
        self.position35.setStyleSheet('background-color:darkMagenta;')
        
        
        self.position40= QtGui.QPushButton('')
        self.position40.setFixedWidth(80)
        self.position40.setFixedHeight(80)
        self.position40.setStyleSheet('background-color:darkMagenta;')
        
        self.position41= QtGui.QPushButton('')
        self.position41.setFixedWidth(80)
        self.position41.setFixedHeight(80)
        self.position41.setStyleSheet('background-color:lightblue;')
        
        self.position42= QtGui.QPushButton('')
        self.position42.setFixedWidth(80)
        self.position42.setFixedHeight(80)
        self.position42.setStyleSheet('background-color:lightblue;')
        
        self.position43= QtGui.QPushButton('')
        self.position43.setFixedWidth(80)
        self.position43.setFixedHeight(80)
        self.position43.setStyleSheet('background-color:lightblue;')
        
        self.position44= QtGui.QPushButton('')
        self.position44.setFixedWidth(80)
        self.position44.setFixedHeight(80)
        self.position44.setStyleSheet('background-color:lightblue;')
        
        self.position45= QtGui.QPushButton('')
        self.position45.setFixedWidth(80)
        self.position45.setFixedHeight(80)
        self.position45.setStyleSheet('background-color:darkMagenta;')
        
        self.position50= QtGui.QPushButton('')
        self.position50.setFixedWidth(80)
        self.position50.setFixedHeight(80)
        self.position50.setStyleSheet('background-color:darkMagenta;')
        
        self.position51= QtGui.QPushButton('')
        self.position51.setFixedWidth(80)
        self.position51.setFixedHeight(80)
        self.position51.setStyleSheet('background-color:darkMagenta;')
        
        self.position52= QtGui.QPushButton('')
        self.position52.setFixedWidth(80)
        self.position52.setFixedHeight(80)
        self.position52.setStyleSheet('background-color:darkMagenta;')
        
        self.position53= QtGui.QPushButton('')
        self.position53.setFixedWidth(80)
        self.position53.setFixedHeight(80)
        self.position53.setStyleSheet('background-color:darkMagenta;')
        
        self.position54= QtGui.QPushButton('')
        self.position54.setFixedWidth(80)
        self.position54.setFixedHeight(80)
        self.position54.setStyleSheet('background-color:darkMagenta;')
        
        self.position55= QtGui.QPushButton('')
        self.position55.setFixedWidth(80)
        self.position55.setFixedHeight(80)
        self.position55.setStyleSheet('background-color:darkMagenta;')
        
        self.gamelayout.addWidget(self.position00,0,0)
        self.gamelayout.addWidget(self.position01,0,1)
        self.gamelayout.addWidget(self.position02,0,2)
        self.gamelayout.addWidget(self.position03,0,3)
        self.gamelayout.addWidget(self.position04,0,4)
        self.gamelayout.addWidget(self.position05,0,5)
        self.gamelayout.addWidget(self.position10,1,0)
        self.gamelayout.addWidget(self.position11,1,1)
        self.gamelayout.addWidget(self.position12,1,2)
        self.gamelayout.addWidget(self.position13,1,3)
        self.gamelayout.addWidget(self.position14,1,4)
        self.gamelayout.addWidget(self.position15,1,5)
        self.gamelayout.addWidget(self.position20,2,0)
        self.gamelayout.addWidget(self.position21,2,1)
        self.gamelayout.addWidget(self.position22,2,2)
        self.gamelayout.addWidget(self.position23,2,3)
        self.gamelayout.addWidget(self.position24,2,4)
        self.gamelayout.addWidget(self.position25,2,5)
        self.gamelayout.addWidget(self.position30,3,0)
        self.gamelayout.addWidget(self.position31,3,1)
        self.gamelayout.addWidget(self.position32,3,2)
        self.gamelayout.addWidget(self.position33,3,3)
        self.gamelayout.addWidget(self.position34,3,4)
        self.gamelayout.addWidget(self.position35,3,5)
        self.gamelayout.addWidget(self.position40,4,0)
        self.gamelayout.addWidget(self.position41,4,1)
        self.gamelayout.addWidget(self.position42,4,2)
        self.gamelayout.addWidget(self.position43,4,3)
        self.gamelayout.addWidget(self.position44,4,4)
        self.gamelayout.addWidget(self.position45,4,5)
        self.gamelayout.addWidget(self.position50,5,0)
        self.gamelayout.addWidget(self.position51,5,1)
        self.gamelayout.addWidget(self.position52,5,2)
        self.gamelayout.addWidget(self.position53,5,3)
        self.gamelayout.addWidget(self.position54,5,4)
        self.gamelayout.addWidget(self.position55,5,5)

        grid_widget= QtGui.QWidget()
        grid_widget.setLayout(self.gamelayout)
                
        self.role_holder = QtGui.QLabel('',self) # places holder to hold the participants role in line edit
        
        '''Game line edits, placeholders and buttons'''
        '''Server'''
        self.server_line_edit = QtGui.QLineEdit()
        self.connect_button = QtGui.QPushButton('Connect')
        #self.connect_button.clicked.connect(self.connect)
        
        self.loop_thread = LoopThread()      # create thread
        ### connect signals to slots
        #self.loop_thread.update_label_signal.connect(self.handle_message) 
        
        '''Participants'''
        self.captain_score_holder =  QtGui.QLabel('',self)
        self.general_score_holder = QtGui.QLabel('',self)
        '''buttons'''
        self.disconnect_button = QtGui.QPushButton('Disconnect')
        self.disconnect_button.clicked.connect(self.disconnect)
        self.abort_game_button = QtGui.QPushButton('Abort Game')
        self.abort_game_button.clicked.connect(self.abort_game)
        '''general game edits'''
        '''Game board'''
        self.gameboard_text_edit = QtGui.QTextEdit()
        '''server message'''
              
        self.servermessage_text_edit = QtGui.QTextEdit()
        
        '''Grid layout'''
        self.grid = QtGui.QGridLayout()
        self.grid.addWidget(self.server,0,0)
        self.grid.addWidget(self.server_line_edit,0,1)
        self.grid.addWidget(self.connect_button,0,2)
        self.grid.addWidget(self.role,1,0)
        self.grid.addWidget(self.role_holder,1,1)
        self.grid.addWidget(self.board_message,2,0)
        self.grid.addWidget(grid_widget,3,0,6,1)
        self.grid.addWidget(self.server_message,2,1)
        self.grid.addWidget(self.servermessage_text_edit,3,1,6,6)
        self.grid.addWidget(self.score,10,0)
        self.grid.addWidget(self.captain,11,0)
        self.grid.addWidget(self.captain_score_holder,11,1)
        self.grid.addWidget(self.general,12,0)
        self.grid.addWidget(self.general_score_holder,12,1)
        self.grid.addWidget(self.disconnect_button,11,2)
        self.grid.addWidget(self.abort_game_button,12,2)
        self.setLayout(self.grid)
        
        self.dialogTextBrowser = MyDialog(self)
            
    def handle_message(self,msg):
        if msg[:3]=='new':
            if msg[-1]=='G':
                self.role_holder.setText('New game:\nYour role is General')
            else:
                self.role_holder.setText('New game:\nYour role is Captain')
        elif msg=='your move':
            self.servermessage_text_edit.setText('your move')
        elif msg== 'opponents move':
            self.servermessage_text_edit.setText('opponents move')
        elif msg[:5]=='valid':
            if msg[12]=='G':
                self.general_score_holder.setText(msg[-1])
            else:
                self.captain_score_holder.setText(msg[-2])
        
    def connect(self):
        self.ip_info=self.server_line_edit.displayText()
        print(self.ip_info)
        while True:
            try:
                self.connect_to_server(self.ip_info)
                break
            except:
                self.server_line_edit.setText("Error connection to server")        
        self.loop_thread.start()
        
    def disconnect(self):
        self.setWindowTitle('Disconnect button clicked!!! game disconnected!')
            
    def abort_game(self):
        sys.exit()
class MyDialog(QtGui.QDialog):
            def __init__(self, parent=None):
                super(MyDialog, self).__init__(parent)
                self.textBrowser = QtGui.QTextBrowser(self)
                self.textBrowser.append("1.The player waits for another player before he/she can play")
        
                self.verticalLayout = QtGui.QGridLayout()
                self.verticalLayout.addWidget(self.textBrowser,3,1,6,6)
                self.setLayout(self.verticalLayout)
        
def main():
    app= QtGui.QApplication(sys.argv)
    widget= Guessgame()
    widget.show()
    sys.exit(app.exec_())
main()
