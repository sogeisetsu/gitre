import requests
import base64
import os
print(r"请输入文件路径，列如C:\111.jpg")
f=input()
if os.path.exists(f):
      print("文件存在")
      c='data:image/jpeg;base64,'
      wejin=open(f,"rb")
      f=base64.b64encode(wejin.read())
      f=f.decode()
      # print(type(f))
      c=c+f
      body={"key":"63","img":c}
      headers = {'content-type': "application/x-www-form-urlencoded"}
      url = 'http://api.tianapi.com/txapi/imglajifenlei/'
      response = requests.post(url, data = body, headers = headers)
      r=response
      print(r.status_code)
      r=r.json()
      #print(r)
      r=r["newslist"]
      #print(r)
      print("可能是以下种类：")
      for lt in r:
            #print(lt["name"])
            print("名称：{}\n 种类和处理方法：{}\n".format(lt["name"],lt["lajitip"]))
            
else:
      print("error")
input()
