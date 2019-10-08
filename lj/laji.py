# the first try
'''
def first(a):
    import time
    print(time.time())
    print(a)
'''
# the second try

def wenji(url,z,tt): # 定义输入文字函数
    import requests # 引入爬虫
    c = url + z # 将关键变量融合进c，即c为url变量
    r = requests.get(c)
    zg = r.json()
    if zg["code"] == 200:
        zglist = zg["newslist"]
        print("可能是以下种类：")
        tt.clear()
        for lt in zglist:
            tt.append("名称：{}\n 种类：{}\n 处理方法：{}\n".format(lt["name"], lt["explain"], lt["tip"]))
        #return tt
        #print(type(tt))
        #print(tt)
    else:
        tt.clear()
        tt.append("该垃圾种类没有检索到，这次检索结果是根据《上海市生活垃圾管理条例》得出的，您可以尝试重新输入垃圾种类或者查询《上海市生活垃圾管理条例》")

def tupian(url,path,b):
    import requests
    import base64
    import os
    # print(r"请输入文件路径，列如C:\111.jpg")
    # f = input()
    f=path
    if os.path.exists(f):
        print("文件存在")
        c = 'data:image/jpeg;base64,'
        wejin = open(f, "rb")
        f = base64.b64encode(wejin.read())
        f = f.decode()
        # print(type(f))
        c = c + f
        body = {"key": "63be040a50cf928e2c79e650fe57e7e6", "img": c}
        headers = {'content-type': "application/x-www-form-urlencoded"}
        # url = 'http://api.tianapi.com/txapi/imglajifenlei/'
        response = requests.post(url, data=body, headers=headers)
        r = response
        print(r.status_code)
        r = r.json()
        # print(r)
        r = r["newslist"]
        # print(r)
        print("可能是以下种类：")
        b.clear()
        for lt in r:
            b.append("名称：{}\n 种类和处理方法：{}\n".format(lt["name"], lt["lajitip"]))
            print("名称：{}\n 种类和处理方法：{}\n".format(lt["name"], lt["lajitip"]))
    else:
        b.clear()
        print("error")
'''
if __name__ == "__main__":
    a=input()
    b='http://api.tianapi.com/txapi/imglajifenlei/'
    tupian(b,a)
'''



