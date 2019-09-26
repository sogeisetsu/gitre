from wxpy import *
import laji
bot=Bot()
@bot.register()
def reply_msg(msg):
    if msg.type=='Text':
        if msg.text=="1":
            msg.reply(u"进入文字识别阶段")
            @bot.register()
            def repl(mag):
                mag.reply(u"123")
                b=[]
                a="http://api.tianapi.com/txapi/lajifenlei/?key=63be040a50cf928e2c79e650fe57e7e6&word="
                laji.wenji(a,mag.text,b)
                for i in b:
                    mag.reply(i)

        #msg.reply(u"hello")
        #msg.reply_image(r"C:\Users\苏月晟\Desktop\001.jpg")
    elif msg.type=='Picture':
        msg.reply(u"tupian")
embed()
