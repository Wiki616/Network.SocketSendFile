# -*- coding: utf-8 -*-
from socket import *
from config import *
import os
import struct

def file_send(path,filename):
    ADDR = (IP,Port2)
    BUFSIZE = 1024

    FILEINFO_SIZE=struct.calcsize('128s32sI8s')
    sendSock = socket(AF_INET,SOCK_STREAM)
    sendSock.connect(ADDR)
    fhead=struct.pack('128s11I',filename,0,0,0,0,0,0,0,0,os.stat(path+filename).st_size,0,0)
    sendSock.send(fhead)
    fp = open(path+filename,'rb')
    while 1:
        filedata = fp.read(BUFSIZE)
        if not filedata: break
        sendSock.send(filedata)
    print "sending , disconnecting..."

    fp.close()
    sendSock.close()
    print "disconnected..."

#file_send('D:\\network\\BBB\\','b.txt')

