import requests
import json

import pprint

from lxml import etree



url = "http://csujwc.its.csu.edu.cn/jsxsd/fxgl/fxbmxx"


f = open(r'testCookie.txt','r')#打开所保存的cookies内容文件

cookies={}#初始化cookies字典变量

for line in f.read().split(';'): 
    #按照字符：进行划分读取
    name,value=line.strip().split('=',1)
    cookies[name]=value #为字典cookies添加内容
    del name, value

#爬出所有URL

#通过URL爬出数据并且追加
res = requests.get(url,cookies=cookies)

resText = res.text

# file_handle=open('subjects.html',mode='a+')
# file_handle.write(resText)
# file_handle.close()

# 
selector=etree.HTML(resText) 
 # 将源码转化为能被XPath匹配的格式


ans = selector.xpath('//table[@class="Nsb_r_list Nsb_table"]//td/a[@*]/@href') 
for item in ans:
    # print(item)
    # print("NNNNNNNEXT")
    halfURL = ""+ item
    # pprint.pprint(item)
    if(len(halfURL)!=18):
        # print(halfURL[23:90])
        # ansansans = halfURL[23:90]
        fullURL = "http://csujwc.its.csu.edu.cn"+halfURL[23:90]+";"
        
        file_handle=open('URLs.txt',mode='a+')
        file_handle.write(fullURL)
        file_handle.close()
    
        
    




