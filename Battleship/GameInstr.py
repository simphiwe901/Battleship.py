#GameInstructions
# Simphiwe Mchunu
# 25 April 2016

import sys
from PyQt4 import QtGui, QtCore

class gamesynopsis(QtGui.QWidget):
    def __init__(self,parent= None):
            QtGui.QWidget.__init__(self,parent)
            self.setWindowTitle('GAME SYNOPSIS')
            self.resize(1000,600)
            self.instructions = QtGui.QLabel('Instructions on how the game is played') 
            self.instructions.setFont(QtGui.QFont('Arial Black',13,1))
            self.label1 = QtGui.QLabel('1. The player waits for another player before he/she can play')
            self.label1.setFont(QtGui.QFont('Georgia',12,2))
            self.label2 = QtGui.QLabel('2. Only one player can play in each turn')
            self.label2.setFont(QtGui.QFont('Georgia',12,2))
            self.label3 = QtGui.QLabel('3. One point is assigned to a player after he/she has chosen a position which hits a boat the first time and two points are assigned to a player if the same boat is hit again and is sunk')
            self.label3.setFont(QtGui.QFont('Georgia',12,2))
            self.label4 = QtGui.QLabel('4. The winner is the player to get the most hit-points after all five boats are sunk') 
            self.label4.setFont(QtGui.QFont('Georgia',12,2))
            
            vbox = QtGui.QVBoxLayout()
            vbox.addWidget(self.instructions)
            vbox.addWidget(self.label1)
            vbox.addWidget(self.label2)
            vbox.addWidget(self.label3)
            vbox.addWidget(self.label4)
            self.setLayout(vbox)
            self.show()
                    
        
    
def main():
    app= QtGui.QApplication(sys.argv)
    widget= gamesynopsis()
    widget.show()
    sys.exit(app.exec_())
main()

    




