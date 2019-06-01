# codign: utf-8
"""
输出2~99之间的素数

Version:0.1
Author: 钟增辉
Date: 2019-05-28
"""

import math

for num in range(2,100):
    is_prime = True
    for factor in range(2, int(math.sqrt(num)) + 1):
        if num % factor == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=' ')