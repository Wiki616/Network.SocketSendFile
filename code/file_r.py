# -*- coding: utf-8 -*-
from socket import *
from config import *
import struct

def file_rec(path):
    ADDR = (IP,Port2)
    BUFSIZE = 1024
    FILEINFO_SIZE=struct.calcsize('128s32sI8s')
    recvSock = socket(AF_INET,SOCK_STREAM)
    recvSock.bind(ADDR)
    recvSock.listen(True)

    print "waiting..."

    conn,addr = recvSock.accept()

    print "connect success--> ",addr

    fhead = conn.recv(FILEINFO_SIZE)

    filename,temp1,filesize,temp2=struct.unpack('128s32sI8s',fhead)

    #print filename,temp1,filesize,temp2

    print filename
    print type(filename)
    print filesize
    
    filename = filename.strip('\00') #...
    fp = open(path+filename,'wb')
    restsize = filesize
    print "receiving... ",

    while 1:
        if restsize > BUFSIZE:
            filedata = conn.recv(BUFSIZE)
        else:
            filedata = conn.recv(restsize)
        if not filedata: break
        fp.write(filedata)
        restsize = restsize-len(filedata)
        if restsize == 0:
            break

    print "receive completed"

    fp.close()
    conn.close()
    recvSock.close()
    print "disconnected..."

#file_rec("")
