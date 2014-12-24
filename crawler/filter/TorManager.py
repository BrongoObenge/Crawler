__author__ = 'j'

import socket
import os

class TorManager:

    def __init__(self):
        pass

    def newId(self):
        print ">>>GETTING NEW IDENTITY"
        self.forceNewId()
        success = False
        s = socket.socket()
        s.connect(('localhost', 9050))
        s.send('AUTHENTICATE "hello"\r\n')
        resp = s.recv(1024)
        if resp.startswith('250'):
            s.send("signal NEWNYM\r\n")
            s.recv(1024)
        if resp.startswith('250'):
            success = True
        return success

    def forceNewId(self):
        os.system("killall -HUP tor")