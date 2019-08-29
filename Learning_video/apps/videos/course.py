import requests
from lxml import etree
import sqlite3

import re,os
os.environ['DJANGO_SETTINGS_MODULE'] = 'Learning_video.settings'

# 设置项目的配置文件
# django.setup()
# # 加载项目配置
from django.conf import settings
db_path = os.path.join(settings.BASE_DIR,'db.sqlite3')
print(db_path)
conn = sqlite3.connect(db_path)
for s in range(1,6):
    url = f'http://yun.itheima.com/course/index/p/{s}.html'

    headers = {
        "Accept": "text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, image / apng, * / *;q = 0.8, application / signed - exchange;v = b3",
        "Cookie": "isclose = 1;isclose = 1;bad_id48bc7230 - 6252 - 11e8 - 917f - 9fb8db4dc43c = 07d0a622 - af80 - 11e9 - 8b58 - d38319d565ab;bad_idd48d5cf0 - 2e47 - 11e8 - 9db3 - 3313a60c92e9 = 1bf50d32 - af80 - 11e9 - 8b58 - d38319d565ab;bad_id994d4130 - 1df9 - 11e9 - b7ec - 7766c2691ec6 = 7f28e971 - be8b - 11e9 - ae45 - 0f2733d23281;nice_id48bc7230 - 6252 - 11e8 - 917f - 9fb8db4dc43c = f08eec01 - c263 - 11e9 - b0d0 - 2b2b8052cd76;openChat48bc7230 - 6252 - 11e8 - 917f - 9fb8db4dc43c = true;PHPSESSID = 9u9jsh7pbqhpod2jomv25b4dr3;href = http % 3A % 2F % 2Fyun.itheima.com % 2Fmap % 2F22.html % 3Fa5;accessId = 994d4130 - 1df9 - 11e9 - b7ec - 7766c2691ec6;nice_id994d4130 - 1df9 - 11e9 - b7ec - 7766c2691ec6 = 472e3701 - c264 - 11e9 - 8390 - 4da302bf9563;nice_idd48d5cf0 - 2e47 - 11e8 - 9db3 - 3313a60c92e9 = 3dc58ec1 - c417 - 11e9 - b046 - 17a192948105;openChatd48d5cf0 - 2e47 - 11e8 - 9db3 - 3313a60c92e9 = true;isclose = 1;qimo_seosource_994d4130 - 1df9 - 11e9 - b7ec - 7766c2691ec6 = % E7 % AB % 99 % E5 % 86 % 85;qimo_seokeywords_994d4130 - 1df9 - 11e9 - b7ec - 7766c2691ec6 =;pageViewNum = 48",
        "User - Agent" :"Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 76.0.3809.100Safari / 537.36"
    }

    response = requests.get(url, headers=headers)
    print(response)
    html_str = response.content.decode()
    html = etree.HTML(html_str)
    one = html.xpath('//div[@class="main"]/ul//li')
    print(one)
    for i in one:
        img = i.xpath('.//img[@class="mask_img1"]/@src')[0]
        img = img.replace("/Upload/./","http://yun.itheima.com/Upload/")
        print(img)
        # lianjie = i.xpath('./a/@href')[0]
        # a = lianjie.replace("","http://yun.itheima.com",1)
        # print(a)
        name = i.xpath('.//h2/text()')[0]
        print(name)
        level = 1
        data = "insert into videos_courese(courese_name,img,level)values('%s','%s',%d)" % (name, img,level)
        conn.execute(data)

conn.commit()
conn.close()
        # response = requests.get(a)
        # print(response)
        # html_str2 = response.content.decode()
        # html2 = etree.HTML(html_str2)
        # two = html2.xpath('//div[@class="con"]/ul/li/a/@data')
        # two =sorted(set(two))
        # print(two)
        # for j in two:
        #     vidoe = html2.xpath('//li/a/@data')[0]
        #     print(vidoe)

