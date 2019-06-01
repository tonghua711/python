# coding: utf-8

""""
Python 常用模块
-运行时服务相关模块：copy / pickle /sys/...
-数学相关模块：decimal / math / random /...
-字符串处理模块：codesc /re /...
-文件处理相关模块：shutil / gzip/...
-进程和线程相关模块： multiprocessing / threading /queue
-网络应用相关模块： ftplib / http / smtplib /urllib /...
-Web编程相关模块：cgi / webbrowser
-数据处理和编码模块: base64 / csv / html.parser /json/xml/...

Version:0.1
Author:钟增辉
Date:2019-05-31
"""

import time
import shutil
import os

seconds = time.time()
print(seconds)
localtime = time.localtime(seconds)
print(localtime)
print(localtime.tm_year)
print(localtime.tm_mon)
print(localtime.tm_mday)
asctime = time.asctime(localtime)
print(asctime)
strtime = time.strftime('%Y-%m-%d %H:%M:%S' , localtime)
print(strtime)
mydate = time.strptime('2018-1-1','%Y-%m-%d')
print(mydate)

shutil.copy('C:\\hello.py','C:\\first.py')
os.system('ls -l')
os.chdir('d:')
os.system('dir \b ')
os.mkdir('test')