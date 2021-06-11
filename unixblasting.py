#!/usr/bin/env python2
# coding=utf-8
import crypt
import re
import linecache
#输出可用账户
def users(f):
    line = f.readline()
    if len(line) == 0:
        return 0
    line = re.split(r'\:',line)
    # print line
    if line[1] == '!' or line[1] == '*':
        return 1
    print "用户名：",line[0]
    return line[1]
# 截取密码和盐部分
def salts_pass(strp):
        list =[]
        str_l = re.split(r'\$',strp)
        pass_str = '$' + str_l[3]
        salt_str = '$' + str_l[1] + '$' + str_l[2]
        list.append(pass_str)
        list.append(salt_str)
        return list
#对比
def crypts(p,s,new_f):
    p = s + p
    while True:
        i = new_f.readline()
        if len(i) == 0:
            break
        i = i.rstrip()
        cryptword = crypt.crypt(i,s)
        if p == cryptword:
            print "[+] 密码:",
            new_f.seek(0, 0)
            return i
    # print "[-] 未找到"
if __name__=='__main__':
    while True:
        passwd_dic = raw_input("输入字典路径(输入exit退出):")
        if passwd_dic == 'exit':
            exit()
        try:
            new_f = open(passwd_dic,'r')
            file_shadow = "/etc/shadow"
            f = open(file_shadow,'r')
            break
        except:
            print "没有这个文件或输入错误,请重新输入！"
    while True:
        strp = users(f)
        if strp == 0:
            break
        if strp == 1:
            continue
        list = salts_pass(strp)
        flag_file = crypts(list[0],list[1],new_f)
        if flag_file == None:
            print "[-] 没有匹配"
        else:
            print flag_file
    f.close()
    new_f.close()
