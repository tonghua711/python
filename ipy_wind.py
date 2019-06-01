# coding: utf-8

"""
通过IPY
通过输入ip地址或者字网返回网络、掩码、广播、方向解析、字网数
IP类型等信息
"""

from IPy import IP

ip_s = input('Please input an IP or net-range:')
ips = IP(ip_s)
if len(ips) > 1:
    print('net: %s' % ips.net())
    print('netmask: %s' % ips.netmask())
    print('broadcast: %s' % ips.reverseNames())
    print('reverse address: %s' % ips.reverseNames()[0])
    print('subnet: %s' % len(ips))
else:
    print('reverse address: %s' % ips.reverseNames()[0])

print('hexadecimal: %s' % ips.strHex())
print('binary ip: %s' % ips.strBin())
print('iptype: %s' % ips.iptype())
