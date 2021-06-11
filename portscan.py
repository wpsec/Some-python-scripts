#!/usr/bin/env python2
# coding=utf-8
import socket
import time
import multiprocessing.pool
import optparse
def scport(ports):
	socket.setdefaulttimeout(1)
	s = socket.socket()
	try:
		tu = s.connect_ex((ip,ports))
		if tu == 0:
			print ('\033[0;32;40m [+] \033[0m 开放端口: ' + str(ports))
		s.send("hello")
		banner = s.recv(1024)
		if banner != 'null':
			print (str(ports) + ' 端口banner信息: ' + 'banner:'+ banner)
		else:
			pass
		s.close()
	except:
		s.close()
		pass
		# print '[-] ' + str(ip) + ':' + str(ports)
def main():
	# 命令行解析获取ip 端口
	global ip
	parser = optparse.OptionParser()
	parser.add_option('-H','--host',dest='server',help='tag ip')
	parser.add_option('-p','--sport',dest='sport',type='int',help='start port')
	parser.add_option('-P','--eport',dest='eport',type='int',help='end port')
	(options, args) = parser.parse_args()
	if (options.server == None) and (options.sport == None) and (options.eport == None):
		print '参数错误'
		exit(0)
	else:
		ip = options.server
		sports = options.sport
		eports = options.eport
	try:
		# sports = int(raw_input("开始端口："))
		# eports = int(raw_input("结束端口："))
		if sports > eports:
			print ('开始端口不能大于结束端口')
		# return
	except:
		return
	# 计算扫描时间，实例化一个进程池对象
	start_time = time.time()
	tp = multiprocessing.pool.ThreadPool(processes=2)
	tp.map_async(scport,range(sports,eports))
	tp.close(),tp.join()
	end_time = time.time()
	print ('扫描完成 用时：{:.1s}'.format(str(end_time - start_time)) + ' 秒')
if __name__ == '__main__':
	main()





