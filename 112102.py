from wxpy import *
import laji
import os
bot=Bot(console_qr=1)
foun=bot.friends().search("腾双源")[0]
foun.send("[呲牙]")
@bot.register(msg_types=FRIENDS,enabled=True)
# 自动接受验证信息中包含 'wxpy' 的好友请求
def auto_accept_friends(msg):
    # 判断好友请求中的验证文本
    if "识别垃圾" in msg.text.lower():
        # 接受好友 (msg.card 为该请求的用户对象)
        new_friend = bot.accept_friend(msg.card)
        print("11111")
        # 或 new_friend = msg.card.accept()
        # 向新的好友发送消息
        new_friend.send('已接受您的好友请求\n您可有两种选项:\n1.文字识别，请键入\n垃圾 垃圾种类(注意空格)\n2.图像识别\n请直接发送图像原图[微笑]')
@bot.register(Friend)
def reply_msg(msg):
    if msg.type=='Text':
        if msg.text[:2]=="垃圾" and msg.text[2]==" ":
            msg.reply(u"进入文字识别阶段")
            # msg.reply(type(msg.text))
            msg.reply(u"开始识别")
            b = []
            a="http://api.tianapi.com/txapi/lajifenlei/?key=63be040a50cf928e2c79e650fe57e7e6&word="
            laji.wenji(a,msg.text[3:],b)
            for i in b:
                msg.reply(i)
            print(type(msg.text))
        elif "识别垃圾" in msg.text.lower():
            msg.reply("请输入以下格式\n垃圾 垃圾种类")
        elif "识别" in msg.text.lower():
            msg.reply("您可有两种选项:\n1.文字识别，请键入\n垃圾 垃圾种类(注意空格)\n2.图像识别\n请直接发送图像原图[微笑]")
        elif "图像识别" in msg.text.lower():
            msg.reply("可以进行图片识别，请直接发送图片原图")
    elif msg.type=='Picture':
        msg.reply(u"收到图片[OK]")
        msg.reply("正在检测……\[呲牙]")
        image_name = msg.file_name
        msg.get_file('' + msg.file_name)
        msg.reply(msg.file_name)
        a1='http://api.tianapi.com/txapi/imglajifenlei/'
        print(os.path.abspath(msg.file_name))
        dd=[]
        laji.tupian(a1,os.path.abspath(msg.file_name),dd)
        msg.reply("图片检测结果，请以您的实际情况为准[愉快]")
        for i in dd:
            msg.reply(i)
bot.join()
