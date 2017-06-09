import paramiko
import threading
import datetime
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
        f = open("/root/be/logs/becmd.log",'a')
        f.write(str(datetime.datetime.now())+" ")
        f.write(self.ip+" ")
        f.write(self.username+ " ")
        f.write(self.cmd+ "\n")
        f.close()
        print("\033[1;32;40m" + self.ip.rjust(33,'=')+ "\033[0m","\033[1;32;40m" + "Command result: ".ljust(37,'=')+ "\033[0m")
        print(result.decode())
        self.ssh.close()

