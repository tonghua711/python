# coding: utf-8
"""
1.通过dns.resolver.query()方法获取业务域名A记录信息，查询出所有的IP地址列表
2.使用httplib模块的request()方法已GET方式请求监控页面，监控业务所有服务的iP是否服务正常

Version:0.1
Author: 钟增辉
Date:2019-06-02
"""

import dns.resolver
import os
import httplib2
#定义域名IP列表变量
iplist = []
#定义业务域名
appdomain = "www.baidu.com"
#域名解析函数，解析成功IP将被追加到iplist
def get_iplist(domain=""):
    try:
        #解析A记录类型
        A = dns.resolver.query(domain, 'A')
    except(Exception,e):
        print("dns resolver error:"+str(e))
        return
    for i in A.response.answer:
        for j in i.items:
            #追加到iplist
            iplist.append(j.address)
    return True

def checkip(ip):
    checkurl = ip + ":80"
    getcontent = ""
    #定义http连接超时时间（5秒）
    httplib2.socket.setdefaulttimeout(5)
    #创建http连接对象
    conn = httplib2.HTTPConnectionWithTimeout(checkurl)

    try:
        #发起URL请求，添加到主机
        conn.request("GET", "/", headers ="Host")
        r = conn.getresponse()
        #获取URL页面前15个字符，以便做可用性效验
        getcontent = r.read(15)
    finally:
        #监控URL页的内容一般是实现定义好的，比如“HTTP200”等
        if getcontent == "<!doctype html>":
            print(ip + "[OK]")
        else:
            #此处可放告警程序，可以是邮件、短信通知
            print(ip + "[Error]")

if __name__=="__main__":
#条件：域名解析正确至少返回一个IP
    if get_iplist(appdomain) and len(iplist) > 0:
        for ip in iplist:
            checkip(ip)
    else:
        print("dns resolver error.")