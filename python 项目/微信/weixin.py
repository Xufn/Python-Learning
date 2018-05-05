# -*- coding:utf-8 -*-
from __future__ import unicode_literals
import itchat
import urllib2
import json
from threading import Timer


def get_news():
    # 获取金山词霸每日一句(英文,翻译,热评)
    url = "http://open.iciba.com/dsapi"
    headers = {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) CriOS/66.0.3359.122 Mobile/15E216 Safari/604.1"}

    req = urllib2.Request(url, headers=headers)
    res = urllib2.urlopen(req)
    r = res.read()
    #print r
    # 对取得的字符串进行解析
    r = r.decode('unicode_escape')
    b = json.loads(r)
    contents = b['content']
    translation = b['translation']
    note = b['note']
    return contents, note, translation

def send_news():
    try:

        #登录你的微信号，会弹出网页二维码，扫描即可登录
        itchat.auto_login(hotReload = True)
        # 获取你对应好友的备注，这小面的备注是我的一个例子
        my_friend = itchat.search_friends(name=u'麻包婆')
        # 获取对应备注名的一串数字
        MaBaopo = my_friend[0]["UserName"]
        message1 = get_news()[0]
        #翻译
        message2 = get_news()[1]
        message3 = get_news()[2][5:]

        #发送消息
        itchat.send(message1, toUserName = MaBaopo)
        itchat.send(message2, toUserName = MaBaopo)
        itchat.send(message3, toUserName = MaBaopo)
        # 每天定时发送一次（t=86400秒),一直挂着这个就好了
        t = Timer(86400, send_news)
        t.start()
    except:


        message4 = u"最爱你的人今天出现了  /bug /(ㄒoㄒ)/~~"
        itchat.send(message4, toUserName = MaBaopo)

def main():
    send_news()

if __name__ == "__main__":
    main()