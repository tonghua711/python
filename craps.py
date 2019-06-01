# coding: utf-8
"""
Craps 赌博游戏
玩家摇两颗色子，如果第一次摇出7点或者11点 玩家胜
如果摇出2点 3点 12点 庄家胜 其它情况游戏继续
玩家再次摇色子 如果摇出7点 庄家胜
如果摇出第一次摇的点数 玩家胜
否则游戏继续 玩家继续摇色子
玩家进入游戏是有1000元的赌注， 全部输光游戏结束

Version:0.1
Author:钟增辉
Date:20190524

"""

from random import randint

money = 1000

while money > 0:
    print('你的总资产为：',money)
    need_go_on = False
    while True:
        debt = int(input('请下注：'))
        if debt > 0 and debt <= money:
            break
    first = randint(1, 6) + randint(1, 6)
    print('玩家摇出了%d点' % first)
    if first == 7 or first == 11:
        print('玩家胜!')
        money += debt
    elif first == 2 or first == 3 or first == 12:
        print('庄家胜!')
        money -= debt
    else:
        needs_go_on = True

    while needs_go_on:
        current = randint(1, 6) + randint(1, 6)
        print('玩家摇出了%d点' % current)
        if current == 7:
            print('庄家胜')
            money -= debt
            needs_go_on = False
        elif current == first:
            print('玩家胜')
            money += debt
            needs_go_on = False

print('你破产了, 游戏结束!')