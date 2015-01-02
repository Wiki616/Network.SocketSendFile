# -*- coding:utf-8 -*-
from socket import *
from config import *
from file_s import *
from file_r import *

def SocketClient():
    try:
        #输入指令
        msg = raw_input("input : ")
        #建立socket对象
        s=socket(AF_INET,SOCK_STREAM,0)

        #建立连接
        s.connect((IP,int(Port)))

        sdata=msg
        send = msg.split('_')
        
        print "Request:\r\n%s\r\n"%sdata
        s.send(sdata)
        sresult=s.recv(1024)
        print "Response:\r\n%s\r\n" %sresult
        val = sresult.split(' ')
        if val[0] == '201':
            print send[1]
            file_send('',send[1])
        if val[0] == '202':
            file_rec('')
            #s.send('OK')
        #关闭Socket
        s.close()
    except Exception,ex:
        print ex
while 1:
    SocketClient()
