# coding: utf-8

"""
函数的参数
-位置参数
-可变参数
-关键字参数
-命名关键字参数

Version:0.1
Author：钟增辉
Date:2019-05-31
"""

#参数默认值
def f1(a, b=5, c=10):
    print('--' + str(a),str(b),str(c))
    return a + b * 2 + c * 3

# print(f1(1, 2, 3))
# print(f1(100, 200))
# print(f1(100))
# print(f1(c=2, b=3, a=1))

#可变参数
def f2(*args):
    sum = 0
    for num in args:
        sum += num
    return sum

# print(f2(1, 2, 3))
# print(f2(1, 2, 3, 4, 5))
# print(f2())

#关键字参数
def f3(**kw):
    if 'name' in kw:
        print('欢迎您%s!' % kw['name'])
    elif 'tel' in kw:
        print('您的联系电话是： %s!' % kw['tel'])
    else:
        print('没找到你的个人信息！')

param = {'name': '钟增辉', 'age': 34}
# f3(**param)
# f3(name='钟增辉', age=38, tel='19855241212')
f3(user='骆昊', age=38, tel='13866778899')
f3(user='骆昊', age=38, mobile='13866778899')