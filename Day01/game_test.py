#coding:utf-8

import random

secretNumber = random.randint(1,20)
print('I am thinking of a number between 1 and 20.')

for guessesTaken in range(1,7):
    print('Take a guess.')
    try:
        guess = int(input())
    except ValueError:
        print('输入的不是数字')

    if guess < secretNumber:
        print('你输入的数字太小')
    elif guess > secretNumber:
        print('你输入的数字太大')
    else:
        break
if guess == secretNumber:
    print('Good job! 你输入了：'+ str(guessesTaken) + '次才正确!')
else:
    print('Nope,The number I was thinking or was '+ str(secretNumber))
