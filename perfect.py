# coding: utf-8

"""
找出1~9999之间的所有完美数
完美数是除自身外其他所有因子的和正好等于这个数字本身的数
例如： 6 = 1+2+3,28=1+2+4+7+14

Version：0.1
Author：钟增辉
Date: 2019-05-28
"""

import time
import math

start = time.clock()
for num in range(1,10000):
    sum = 0
    for factor in range(1, int(math.sqrt(num)) + 1):
        if num % factor == 0:
            sum += factor
            if factor > 1 and num / factor != factor:
                sum += num / factor
    if  sum == num:
        print(num)
end = time.clock()
print("执行时间：",(end - start),"秒")