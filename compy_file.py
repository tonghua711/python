# -*- coding: utf-8 -*-

 ###coding:utf-8

"""
1.读取两个版本需对比的配置文件，再以换行符做分隔符
2.调用difflib.HtmlDiff() 生成HTML格式的差异文件

Version:0.1
Author: 钟增辉
Date:2019-06-02
"""

import difflib
import sys

try:
    textfile1 = sys.argv[1]
    textfile2 = sys.argv[2]
except Exception as e:
    print("Error:" + str(e))
    print("Usage: simple3.py filename1 filename2")
    sys.exit()

#文件读取分隔函数
def readfile(filename):
    try:
        fileHandle = open(filename, 'r')
        #读取后以行进行分隔

        text = fileHandle.read().splitlines()
        print(text)
        # text = text.decode()
        # print(type(text))
        fileHandle.close()
        return text
    except IOError as error:
        print('Read file Error:'+ str(error))
        sys.exit()

# if textfile1 == "" or textfile2 == "":
#     print("Usage: simple3.py filename1 filename2")
#     sys.exit()
#调用readfile 函数，获取分隔后的字符串
text1_lines = readfile(textfile1)
text2_lines = readfile(textfile2)

#创建HtmlDiff()类对象
d = difflib.HtmlDiff()
# print(d.decode())
# print(type(d))
# print(d.make_file(text1_lines,text2_lines))
# print(text1_lines)
# print(text2_lines)
# print(type(text1_lines))
# print(type(text2_lines))
# print(d.make_file(text1_lines, text2_lines))

# print(d)
# html = d.make_file(text1_lines,text2_lines)
# print(html)
# print(type(html))
# print(d.make_file(text1_lines,text2_lines))
with open('diff.html',mode='w',encoding='utf-8') as f:
    f.write(d.make_file(text1_lines,text2_lines))