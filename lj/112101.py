from wxpy import *
import laji
import os
bot=Bot()
@bot.register()
def reply_msg(msg):
    if msg.type=='Text':
        if msg.text[:2]=="垃圾":
            msg.reply(u"进入文字识别阶段")
            # msg.reply(type(msg.text))
            msg.reply(u"开始识别")
            b = []
            a="http://api.tianapi.com/txapi/lajifenlei/?28e2c79e650fe57e7e6&word="
            laji.wenji(a,msg.text[3:],b)
            for i in b:
                msg.reply(i)
            print(type(msg.text))
    elif msg.type=='Picture':
        msg.reply(u"tupian")
        image_name = msg.file_name
        msg.get_file('' + msg.file_name)
        msg.reply(msg.file_name)
        a1='http://api.tianapi.com/txapi/imglajifenlei/'
        print(os.path.abspath(msg.file_name))
        dd=[]
        laji.tupian(a1,os.path.abspath(msg.file_name),dd)
        for i in dd:
            msg.reply(i)
embed()
