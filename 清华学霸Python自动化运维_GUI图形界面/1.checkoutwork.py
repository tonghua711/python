#coding:utf-8

import dns.resolver
import os
import httplib2

iplist=[]
appdomain="qq.com"

def get_iplist(domain=""):
    try:
        A=dns.resolver.query(domain,"A")
    except Exception as e:
        print(e)
        return
    for i in A.response.answer:
        for j in i.items:
            iplist.append(j.address)
    return iplist
# print(get_iplist(appdomain))
def checkip(ip: object) -> object:
    checkurl=ip + ":80"
    getcontent=""
    httplib2.socket.setdefaulttimeout(5)#超时
    conn=httplib2.HTTPConnectionWithTimeout(checkurl)
    try:
        conn.request("GET","/",headers={"host":appdomain})
        result=conn.getresponse()
        getcontent=result.read()
    finally:
        # if getcontent.find("<!doctype html")!=-1:
        if getcontent.find("<!doctype html") == 0:
                print("ipOK",checkurl)
        else:
            print("ipNO",checkurl)
iplist=get_iplist(domain=appdomain)
if iplist!= None and len(iplist)!=0:
    for ip in iplist:
        print(type(ip))
        checkip(ip)