import paramiko
import threading
class MyThread(threading.Thread):
    def __init__(self,ip,port,username,password,cmd):
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        super(MyThread,self).__init__()
        self.ip = ip
        self.port = port
        self.username = username
        self.password = password
        self.cmd = cmd
    def run(self):
        port = int(self.port)
        self.ssh.connect(hostname=self.ip, port=port, username=self.username, password=self.password)
        stdin, stdout, stderr = self.ssh.exec_command(self.cmd)
        res, err = stdout.read(), stderr.read()
        result = res if res else err
        print(self.ip.rjust(50,'='),"command result:".ljust(50,'='))
        print(result.decode())
        self.ssh.close()
