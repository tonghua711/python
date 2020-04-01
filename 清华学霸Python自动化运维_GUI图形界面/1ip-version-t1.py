#coding:utf-8

from IPy import IP

ip=IP('192.168.0.0/28')
print(ip.len())
for x in ip:
    print(x)
print(ip.strNormal(0))
print(ip.strNormal(1))
print(ip.strNormal(2))
print(ip.strNormal(3))

