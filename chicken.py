# coding:utf-8
"""
求解《百钱百鸡》问题
1只公鸡5元 1只母鸡3 元 3只小鸡 1元 用100元买100只鸡
问公鸡 母鸡 小鸡各有多少只

Version:0.1
Author: 钟增辉
Date：20190524
"""

for x in range(1,20):
    for y in range(0,33):
        z = 100 - x - y
        if 5 * x + 3 * y + z / 3 == 100:
            print('公鸡：%d只，母鸡：%d只，小鸡：%d只' % (x,y,z))
