#coding:utf-8

def collatz(number):
     if number % 2 == 0:
         return number // 2
     else:
         return  3 * number + 1

# print(collatz(input()))
print('请输入整数:',end='')
a = int(input())
b = collatz(a)
print(b)