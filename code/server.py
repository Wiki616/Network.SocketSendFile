# -*- coding:utf-8 -*-
from socket import *
from config import *
from file_tra import *
import os
from file_s import *
from file_r import *
import time

def SocketServer():
    try:
        #建立socket对象
        print 'Server start:%s'%ServerUrl
        sockobj = socket(AF_INET, SOCK_STREAM)
        sockobj.setsockopt(SOL_SOCKET,SO_REUSEADDR, 1)

        #绑定IP端口号
        sockobj.bind((IP, Port))
        #监听，允许5个连结
        sockobj.listen(5)
        #直到进程结束时才结束循环
        while True:
            #等待client连结
            connection, address = sockobj.accept()
            print 'Server connected by client:', address
            while True:
                #读取Client消息包内容
                data = connection.recv(1024)
                #如果没有data，跳出循环
                if not data: break
                #发送回复至Client
                RES1='200 query OK'
                RES2='201 put OK'
                RES3='202 get OK'
                RES4='400 Code WA'
                RES5='401 No File'
                print 'Receive MSG:%s'%data.strip()
                val = data.split('_')
                if len(val) == 1:
                    if val[0] == 'query':
                        print 'RES:200 query OK'
                        connection.send(RES1)
                        file_tra("D:\\network")
                    else:
                        connection.send(RES4)
                        print 'RES:400 WA'
                else:
                    if len(val) == 3:
                        if val[0] == 'get' or val[0] =='put':
                            if val[0] == 'put':
                                path = val[2]
                                filename = val[1]
                                newpath = os.path.join("D:\\network\\",path)
                                if not os.path.isdir(newpath):
                                    os.mkdir(newpath)
                                connection.send(RES2)
                                print 'RES:%s\r\n'%RES2
                                file_rec("D:\\network\\" + path + '\\')
                            else:
                                path = val[2]
                                filename = val[1]
                                newpath = "D:\\network\\" + path + "\\" + filename
                                print newpath
                                if not os.path.exists(newpath):
                                    connection.send(RES5)
                                    print 'RES:%s\r\n'%RES5
                                else:
                                    connection.send(RES3)
                                    print 'RES:%s\r\n'%RES3
                                    time.sleep(5)
                                    #connection.recv(1024)
                                    file_send("D:\\network\\" + path + "\\",filename)
                        else:
                            connection.send(RES4)
                            print 'RES:400 Code WA'
                    else:
                        connection.send(RES4)
                        print 'RES:400 Code WA'
            #关闭Socket
            connection.close()

    except Exception,ex:
        print ex

SocketServer()
