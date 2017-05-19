import paramiko
import threading
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
        src = self.cmd[1]
        des = self.cmd[2]
        self.sftp.put(src, des)
        self.transport.close()