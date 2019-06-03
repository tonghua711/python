# coding: utf-8

"""
操作Excel模块

Version:0.1
Authon:钟增辉
Date:20190604
"""
import xlsxwriter

#创建第一个Excel 文件
workbook = xlsxwriter.Workbook('deo1.xlsx')
#创建第一个工作表对象
worksheet = workbook.add_worksheet()
#设置第一列（A）宽度为20像素
worksheet.set_column('A:A', 20)
#定义一个加粗的格式对象
bold = workbook.add_format({'bold': True})
#A1单元格写入'Hello'
worksheet.write('A1','Hello')
#A2单元格写入'World'并引用加粗格式对象bold
worksheet.write('A2','World',bold)
#B2单元格写入中文并引用加粗格式对象bold
worksheet.write('B2',u'中文测试','bold')

#用行列标示发写入数字'32'与‘35.5’
worksheet.write(2,0,32)
#行列表示法的单元格下标以0作为起始值，‘3,0’等价于‘A3’
worksheet.write(3,0,35.5)
#求A3:A4的和，并将结果写入'4,0',基‘A5’
worksheet.write(4,0, '=SUM(A3:A4)')

#在B5单元格插入图片
worksheet.insert_image('B5','img/python-logo.png')
#关闭Excel文件
workbook.close()