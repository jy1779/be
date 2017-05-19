import sys
from app.ssh_be_cmd import MyThread
from conf.config import account
def pwd_con(host):
    ip = account[host]["ip"]
    port = account[host]["port"]
    username = account[host]["username"]
    password = account[host]["password"]
    a=sys.argv[1:100]
    cmd = " ".join(a)
    if len(a) >=1:
        M = MyThread(ip,port,username,password,cmd)
        M.start()
    else:
        print("Reminder: The command does not exist")
        exit()
def connect():
    for host in account.keys():
        pwd_con(host)
