# BattleShipTextClient
# Simphiwe Mchunu
# 18 April 2016

from GameClient import *

class BattleShipTextClient(GameClient):

    def __init__(self):
        GameClient.__init__(self)
        self.board = [x[:] for x in [[' ']*6]*6] # creates 6x6 game board
        self.role = None # role C (for captain) or G (for general)
        
    def clear_board(self):
        self.board = [x[:] for x in [[' ']*6]*6]
        
    def input_server(self):
        #return self.text
        return input('enter server:')
     
    def input_move(self):
        return input('enter move(0-5,0-5):')
     
    def input_play_again(self):
        return input('play again(y/n):')

    def display_board(self):
        for i in self.board:
            print('-----------------')
            for j in i:
                print(j,end ="| ")
            print()
        print('-----------------')       
    
    def handle_message(self,msg):
        if msg=="your move":
            print(msg)
            move=self.input_move()
            self.send_message(move)                   
        elif msg[:-10]=='valid move': # valid move message handled
            print(msg)
            row = int(msg[13]) # takes the row position
            col = int(msg[15]) # takes column position
            self.board[row][col]=  msg[11] # replaces played postision by participants' role on the board
            self.display_board() # calls an updated board for display
        else:
            if msg=='play again': # play again message handled
                choice_option= self.input_play_again() # allows users input
                if choice_option=='y':
                    self.clear_board() # clears the board if the option chosen is y by calling the clear_board method
                self.send_message(choice_option) # sends choice chosen server
                ####print the winner###
            else: 
                print(msg)   # prints any message except for play again  
    
    def play_loop(self):
        while True:
            msg = self.receive_message()
            if len(msg):
                print(msg)
                self.handle_message(msg)
            else: 
                break
            
def main():
    bstc = BattleShipTextClient()
    while True:
        try:
            bstc.connect_to_server(bstc.input_server())
            break
        except:
            print('Error connecting to server!')
    bstc.play_loop()
    input('Press enter to exit.')  
main()
