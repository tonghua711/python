#coding:utf-8

from IPy import IP
#查看IP版本
print(IP("11.12.14.13").version())
print(IP("::1").version()) #ip v6
ip=IP("192.168.0.0/16")#网络子网的所有IP
print(ip.len())#长度
print(ip.iptype())#内网
print('-'*30)
print(ip.reverseNames())
print(ip.int(),ip.strBin(),ip.strHex()) #ip进制

for myip in ip:
    print(myip)