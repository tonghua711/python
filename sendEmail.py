# coding:utf-8

"""
邮件smtplib模块 常用方法如下
smtp.connect([host[,port]])  连接远程smtp主机方法，host为远程主机地址，port为端口默认25 （host:port ）
smtp.login(user,password) 远程smtp主机的效验方法，参数名为用户和密码
smtp.sendmail(from_addr,to_addrs,msg[,mail_options,rcpt_options]) 实现邮件的发送功能，参数依次为
发件人，收件人，邮件内容，
smtp.starttls([keyfile[,certfile]]) 启用TLS模式，所有smtp指令都将加密
smtp.quit() 断开smtp服务器的连接

Version:0.1
Author:钟增辉
Date:2019-06-04

"""

import smtplib
import string

#定义smtp主机
HOST = 'smtp.163.com'
#定义邮件主题
SUBJECT = "Test email from Python"
#定义邮件收件人
TO = "tonghua711@163.com"
#定义邮件发件人
FROM = "tonghua711@163.com"
#邮件内容
text = "Python rules them all!"
#组装sendmail 方法的邮件主题内容，各段以“\r\n”进行分隔
BODY = "\r\n".join((
        "From: %s" % FROM,
        "To: %s" % TO,
        "Subject: %s" % SUBJECT,
        "",
        text
        ))
#创建一个SMTP()对象
server = smtplib.SMTP()
#通过connect 方法连接smtp主机
server.connect(HOST,"25")
# server.starttls()
server.login("tonghua711@163.com","********")
#邮件发送
server.sendmail(FROM, [TO],BODY)
#断开smtp连接
server.quit()