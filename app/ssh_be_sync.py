import paramiko
import threading
import datetime,time
import os
from os.path import getsize
class MyThread(threading.Thread):
    def __init__(self,ip,port,username,password,cmd):
        super(MyThread,self).__init__()
        self.ip = ip
        self.port = port
        self.username = username
        self.password = password
        self.cmd = cmd
    def run(self):
        port = int(self.port)
        self.transport = paramiko.Transport((self.ip, port))
        self.transport.connect(username=self.username, password=self.password)
        self.sftp = paramiko.SFTPClient.from_transport(self.transport)
        help="""
                -f send file to remote host.
                   %s -f <source address> <destination address>
                -d send dir to remote host.
                   %s -d <source address> <destination address>
                --help show help.
                   %s --help
            """%(self.cmd[0],self.cmd[0],self.cmd[0])
        def create_remote_dir(dir):
            for item in dir:
                try:
                    self.sftp.stat(item)
                    pass
                except FileNotFoundError:
                    print("Create a new directory: ", item)
                    self.sftp.mkdir(item)
        def besync_log():
            f = open("../logs/besync.log",'a')
            for i in str(datetime.datetime.now())+" ",self.ip+" ",self.username+ " ",self.cmd[0]+" ",self.cmd[1]+" ",src+" ",des+ "\n":
                f.write(i)
            f.close()
        if len(self.cmd) == 4 and self.cmd[1] == "-f":
            src = self.cmd[2]
            des = self.cmd[3]
            besync_log()
            time_start = time.time()
            if os.path.isfile(src):
                des_list = des.split("/")
                des_dir = des_list[1:-1]
                b=""
                c=[]
                for item in des_dir:
                    b+="/"+item
                    c.append(b)
                create_remote_dir(c)
                self.sftp.put(src, des)
                total_time = time.time() - time_start
                print("\033[1;32;40mSend Successful.\033[0m")
                print("total size: " + str(getsize(src)) + " bytes")
                print("total time: " + str(total_time))
                self.transport.close()
        elif len(self.cmd) == 4 and self.cmd[1] == "-d":
            def for_dir():
                for res in path:
                    if os.path.isdir(res):
                        local_dir_path.append(res)
                remote_dir_path.append(des)
            def for_zdir():
                des_src_dir.append(remote_dir_path[1])
                des_src_dir_list = des_src_dir[0].split("/")
                des_dir_list = des_src_dir_list[1:]
                c = ""
                remote_des_src_path = []
                for item in des_dir_list:
                    c += "/" + item
                    remote_des_src_path.append(c)
                create_remote_dir(remote_des_src_path)
                create_remote_dir(remote_dir_path)
                for res in path:
                    if os.path.isfile(res):
                        local_file_path.append(res)
            src = self.cmd[2]
            des = self.cmd[3]
            besync_log()
            sep = "/"
            path = []
            local_dir_path = []
            local_file_path = []
            remote_dir_path = []
            remote_file_path = []
            des_src_dir = []
            for i in os.listdir(src):
                path.append(src + sep + i)
            for n in path:
                if os.path.isdir(n) and os.listdir(n):
                    for i in os.listdir(n):
                        path.append(n + sep + i)
            local_dir_path.append(src)
            local_dir = src.split("/")
            local_dir_first = local_dir[0:-1]
            global a
            if len(local_dir_first) == 0:
                for_dir()
                for res in local_dir_path:
                    remote_dir_path.append(des + "/" + res)
                for_zdir()
                for res in local_file_path:
                        remote_file_path.append(des + "/" + res)
            else:
                if len(local_dir_first) ==1:
                    dir_join="/".join(local_dir_first)
                    a=dir_join
                else:
                    dir_join="/".join(local_dir_first)
                    a=dir_join+"/"
                for res in path:
                    if os.path.isdir(res):
                        local_dir_path.append(res)
                remote_dir_path.append(des)
                b=[item.split(a)[-1] for item in local_dir_path]
                for res in b:
                    if len(local_dir_first) ==1:
                        remote_dir_path.append(des + res)
                    else:
                        remote_dir_path.append(des + "/" + res)
                for_zdir()
                d = [item.split(a)[-1] for item in local_file_path]
                for res in d:
                    if len(local_dir_first) ==1:
                        remote_file_path.append(des + res)
                    else:
                        remote_file_path.append(des + "/" + res)
            time_start = time.time()
            local_file_num = len(local_file_path)
            for i in range(local_file_num):
                self.sftp.put(local_file_path[i],remote_file_path[i])
            total_time = time.time() - time_start
            print("\033[1;32;40mSend Successful.\033[0m")
            print("total time: " + str(total_time))
            self.transport.close()
        else:
            print(help)