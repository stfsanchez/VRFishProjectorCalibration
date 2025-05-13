# MIT License

# Copyright (c) 2023 Renaud Bastien

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import numpy
import threading
import time
import socket
import struct
import numpy as np
import uuid




class Controller:
    def connect(self):
        self.socketClient = socket.socket()
        self.socketClient.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        print('--- Connection Unity : ' +self.ip + "with port :"+str(self.port))


        while not self.connected :
            try:
                self.socketClient.connect((self.ip, self.port))
                self.connected = True
            except:
                pass
        print('--- Unity connected')
    
    def disconnect(self):
        self.socketClient.shutdown(socket.SHUT_RDWR)
        self.socketClient.close()

    def stopDisplay(self):
        code = 0
        data = struct.pack('i', int(code))
        self.socketClient.sendall(data)

    def calibrator(self):
        dataRec =[] 
        if self.calibration:
            code = 501
        else:
            code = 500
        data = struct.pack('i', int(code))
        self.socketClient.sendall(data)
        print('------ CalibrationMode : ' +mode)
        self.calibration = not self.calibration



    def calibrationPosition(self,x):

        code = 510
        data = struct.pack('i', int(code))
        self.socketClient.sendall(data)
        data = struct.pack('d', x)
        self.socketClient.sendall(data)
        return code
            
    def calibrationScale(self,x):

        code = 511
        data = struct.pack('i', int(code))
        self.socketClient.sendall(data)
        data = struct.pack('d', x)
        self.socketClient.sendall(data)
        return code
            
    def calibrationVertical(self,x):

        code = 512
        data = struct.pack('i', int(code))
        self.socketClient.sendall(data)
        data = struct.pack('i', x)
        self.socketClient.sendall(data)
        return code

    def calibrationScale3(self,x,y,z):

        code = 513
        data = struct.pack('i', int(code))
        self.socketClient.sendall(data)
        data = struct.pack('ddd', x,y,z)
        self.socketClient.sendall(data)
        return code

    def calibrationMesh(self,mesh):

        code = 523
        data = struct.pack('i', int(code))
        self.socketClient.sendall(data)
        data = struct.pack('i', mesh)
        self.socketClient.sendall(data)
        return code


    def calibrationColor(self,h,s,v,bg=True):
        if bg:
            code = 720
        else:
            code = 721
        data = struct.pack('i', int(code))
        self.socketClient.sendall(data)
        data = struct.pack('ddd', h,s,v)
        self.socketClient.sendall(data)
        return code



    def __init__(self):

        calibratorApp = "./calibratorApp/ProjectionMapping.exe"
        def startController():
        subprocess.Popen(pathUnity)
        
        self.ip = "127.0.0.1"
        self.port = 5500

        self.calibration = False


