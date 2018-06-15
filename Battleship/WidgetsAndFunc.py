#WindowWidgets - Responsive
# Simphiwe Mchunu
# 25 April 2016


import sys
from PyQt4 import QtGui, QtCore

class BattleshipPrototype(QtGui.QWidget):
    '''Constructor that initialises variables'''
    def __init__(self,parent= None):
        QtGui.QWidget.__init__(self,parent)
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
        self.setPalette(QtGui.QPalette(QtGui.QColor('Indigo')))
        self.setAutoFillBackground(True) 
        self.pixmap1 = QtGui.QPixmap('Grid_6x6.gif')
        self.pic_label1 = QtGui.QLabel(self)
        self.pic_label1.setPixmap(self.pixmap1)        
                
        self.role_holder = QtGui.QLabel('',self) # places holder to hold the participants role in line edit
        
        '''Game line edits, placeholders and buttons'''
        '''Server'''
        self.server_line_edit = QtGui.QLineEdit()
        self.connect_button = QtGui.QPushButton('Connect')
        self.connect_button.clicked.connect(self.connect)
        #self.connect_button.clicked.connect(self.return_guess)
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
        self.grid.addWidget(self.pic_label1,3,0,6,1)
        self.grid.addWidget(self.server_message,2,1)
        self.grid.addWidget(self.servermessage_text_edit,3,1,6,1)
        self.grid.addWidget(self.score,10,0)
        self.grid.addWidget(self.captain,11,0)
        self.grid.addWidget(self.captain_score_holder,11,1)
        self.grid.addWidget(self.general,12,0)
        self.grid.addWidget(self.general_score_holder,12,1)
        self.grid.addWidget(self.disconnect_button,11,2)
        self.grid.addWidget(self.abort_game_button,12,2)
        self.setLayout(self.grid)
        
    
 
        
    def connect(self):
        self.setWindowTitle('Connect button clicked!')
        
    def disconnect(self):
        self.setWindowTitle('Disconnect button clicked!!! game disconnected!')      
        
    def abort_game(self):
        sys.exit()
        
def main():
    app= QtGui.QApplication(sys.argv)
    widget= BattleshipPrototype()
    widget.show()
    sys.exit(app.exec_())
main()
