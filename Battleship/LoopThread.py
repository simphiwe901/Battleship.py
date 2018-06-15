#LoopThread
# Simphiwe Mchunu
# 25 April 2016


from PyQt4 import QtCore
from time import *
import time 
from GameClient import*

class LoopThread(QtCore.QThread,GameClient):

    update_label_signal = QtCore.pyqtSignal(str)       
    
    def __init__(self,Parent=None):
        QtCore.QThread.__init__(self)
        self.access_server=GameClient()
        self.connection=None
                     
    def run(self):               
        while True:
            msg = self.access_server.receive_message()
            if len(msg):
                self.update_label_signal.emit(str(msg))         
            else:  
                break
               
        
       
          
        
        
        
    
