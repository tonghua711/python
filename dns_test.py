import dns.resolver

#定义域名IP列表变量
iplist = []
#定义业务域名
appdomain = "www.163.com"
#域名解析函数，解析成功IP将被追加到iplist
def get_iplist(domain=""):
    # try:
        #解析A记录类型
    A = dns.resolver.query(domain, 'A')
    print(A.response.answer)
    # except(Exception,e):
    #     print("dns resolver error:"+ str(e))
    #     return
    # print(A)
    for i in A.response.answer:
        # print(type(i))
        for j in i.items:
            # print(j + '----')
            # print(type(j))
            #追加到iplist
            iplist.append(j.address)
    return True

get_iplist(appdomain)