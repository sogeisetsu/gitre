from wxpy import *
import laji
bot=Bot()
@bot.register()
def reply_msg(msg):
    if msg.type=='Text':
        if msg.text[:2]=="垃圾":
            msg.reply(u"进入文字识别阶段")
            # msg.reply(type(msg.text))
            msg.reply(u"开始识别")
            b = []
            a="http://api.tianapi.com/txapi/lajifenlei/?kecf928e2c79e650fe57e7e6&word="
            laji.wenji(a,msg.text[3:],b)
            for i in b:
                msg.reply(i)
            print(type(msg.text))
            # @bot.register()
            # def repl(msg):
            #     msg.reply(u"开始识别")
            #     b=[]
            #     a="http://api.tianapi.com/txapi/lajifenlei/?k928e2c79e650fe57e7e6&word="
            #     laji.wenji(a,msg.text[3:],b)
            #     for i in b:
            #         msg.reply(i)
        #msg.reply(u"hello")
        #msg.reply_image(r"C:\Users\苏月晟\Desktop\001.jpg")
    # elif msg.type=='Picture':
    #     msg.reply(u"tupian")
embed()
