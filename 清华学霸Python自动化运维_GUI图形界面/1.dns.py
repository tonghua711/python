#coding:utf-8

import dns.resolver
domain = input('请输入域名地址')


# 请输入域名地址www.baidu.com

#1. A 记录，将主机转换为IP地址

A = dns.resolver.query(domain,'A')
for i in A.response.answer:
    for j in i.items:
        if j.rdtype == 1:
            print(j.address)

print(A)
print(i)
print(i.items)
print(j)
print(j.rdtype)
print(j.address)
print(A.response.answer)
print(dns.resolver.query('www.baidu.com','A'))
