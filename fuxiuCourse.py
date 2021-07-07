#原始版本，有很多解释

import requests
import json

import pprint

# coll = {}


# url = "https://api.bilibili.com/x/v2/reply?jsonp=jsonp&pn=1&type=1&oid=416414051&sort=2&_=1612444728376"

url = ["http://csujwc.its.csu.edu.cn/jsxsd/fxgl/Cxfxfa?jx01ndid=FE39CF37161344DABEED64E7795DD80C&fxfs=1"]

# s = requests.Session()

# s.cookies['cookie-name'] = 'cookie-value'


f=open(r'testCookie.txt','r')#打开所保存的cookies内容文件

cookies={}#初始化cookies字典变量
for line in f.read().split(';'): #按照字符：进行划分读取
# #其设置为1就会把字符串拆分成2份
    name,value=line.strip().split('=',1)
    cookies[name]=value #为字典cookies添加内容

# 这时候我们将cookies添加到get方法中：

for i in url:

    res = requests.get(i,cookies=cookies)
    
    # 这时候获取到的res.content中就是我们将cookies信息添加到get中后访问网页所获取的内容。
    
    
    
    # getwhat = requests.get(url).text
    
    resText = res.text
    
    # data = json.loads(res)
    
    # pprint.pprint(resText)
    
    # pprint.pprint(res.content)
    
    # resContent = res.content
    
    # for i in data["data"]['replies']:
    #     coll[i['member']["uname"]] = i["content"]["message"]
        
    # print(coll)




