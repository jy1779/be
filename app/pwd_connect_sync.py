import sys
from app.ssh_be_sync import MyThread
from conf.config import  account
def pwd_con(host):
    ip = account[host]["ip"]
    port = account[host]["port"]
    username = account[host]["username"]
    password = account[host]["password"]
    cmd=sys.argv[0:100]
    if len(cmd) == 3:
        M = MyThread(ip, port, username, password, cmd)
        M.start()
    elif len(cmd) == 2:
        print("Reminder: The destination address does not exist")
        print("Usage: %s %s <destination address>" %(cmd[0],cmd[1]))
        exit()
    elif len(cmd) == 1:
        print("Reminder: The source and destination addresses do not exist")
        print("Usage: %s <source address> <destination address>" %cmd[0])
        exit()
def connect():
    for host in account.keys():
        pwd_con(host)