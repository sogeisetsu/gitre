from wxpy import *
bot = Bot(console_qr=1)
foun=bot.friends().search("高明")[0]
foun.send("测试，请忽略[呲牙]")
