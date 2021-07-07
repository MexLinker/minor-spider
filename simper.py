import requests

# file_handle=open('URLs.txt',mode='r')
# file_handle.write(resText)
# file_handle.close()


url = []

#简化后的主程序

# url={}#初始化cookies字典变量

f = open(r'URLs.txt','r')#打开所保存的cookies内容文件
for aURL in f.read().strip().split(';'): 
    #按照字符：进行划分读取
    # name,=line.strip().split('')
    # cookies[name]=value #为字典cookies添加内容
    url.append(aURL)




cookies={}#初始化cookies字典变量
f=open(r'testCookie.txt','r')#打开所保存的cookies内容文件
for line in f.read().split(';'): 
    #按照字符：进行划分读取
    name,value=line.strip().split('=',1)
    cookies[name]=value #为字典cookies添加内容
    del name, value



for i in url:
    #通过URL爬出数据并且追加
    
    res = requests.get(i,cookies=cookies)
    
    resText = res.text
    
    theIndex = resText.index("Nsb_r_title")
    resTextList = list(resText)
    resTextList.insert(theIndex+12, ' style="font-size:50px"')
    resText = "".join(resTextList)
    
    
    file_handle=open('subjects.html',mode='a+')
    file_handle.write(resText)
    file_handle.close()




