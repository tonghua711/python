#！/usr/bin/env python3
# coding:utf-8

import time

from pip._internal.utils import logging


def ip():
    try:
        from IPy import IP  #加载模块
        ip_s = input('请输入IP地址或者网段地址：') #输入一个IP地址或者网段
        ips = IP(ip_s) #定义元素
        if len(ips) > 1: #如果len出来的数字大于1，那么就是一个网段
            print('网络地址：%s' % ips.net())
            print('子网掩码：%s' % ips.netmask())
            print('网络广播地址：' % ips.reverseNames()[0])
            print('网络子网数：%s' % len(ips))
        else:   ##否则就是一个地址
            print('IP反向解析：%s' % ips.reverseNames()[0])
            print('十六进制地址：%s' % ips.strHex())
            print('二进制地址：%s' % ips.strBin())
            print('地址类型 %s' % ips.iptype())
        print(time.strftime('%Y-%m-%d %H:%M:%S'))
        #code
    except Exception as e:
        # logging.info("error:" + str(e) + "\n" + traceback.format_exc())
        # print(traceback.format_exc())
        pass
    finally:
        pass