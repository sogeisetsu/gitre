'''
import requests
url="http://api.tianapi.com/txapi/le2c79e650fe57e7e6&word="
z=input("")
c=url+z
#print(c)
r=requests.get(c)
#print(r.status_code)
#print("type:{}".format(type(r)))
zg=r.json()
#print("type:{}".format(type(zg)))
zglist=zg["newslist"]
print("可能是以下种类：")
for lt in zglist:
    print("名称：{}\n 种类：{}\n 处理方法：{}\n".format(lt["name"],lt["explain"],lt["tip"]))
    #print(lt)
#print(zg)
'''
import requests
def lajiget(url):
      print("please tell me the name of trash")
      z=input("")
      c=url+z
      r=requests.get(c)
      zg=r.json()
      if zg["code"] == 200 :
            zglist=zg["newslist"]
            print("可能是以下种类：")
            for lt in zglist:
                  print("名称：{}\n 种类：{}\n 处理方法：{}\n".format(lt["name"],lt["explain"],lt["tip"]))
      else:
            print("该垃圾种类没有找到")

            
