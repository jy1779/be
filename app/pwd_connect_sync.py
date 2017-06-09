import sys
from app.ssh_be_sync import MyThread
from conf.config import  account
def pwd_con(host):
    ip = account[host]["ip"]
    port = account[host]["port"]
    username = account[host]["username"]
    password = account[host]["password"]
    cmd=sys.argv[0:100]
    M = MyThread(ip, port, username, password, cmd)
    M.start()
def connect():
    for host in account.keys():
        pwd_con(host)