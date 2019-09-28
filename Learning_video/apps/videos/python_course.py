import requests
from lxml import etree
import os
import sqlite3
from django.conf import settings
import django
# sys.path.append('C:\\Users\\吴豪\\Desktop\\绿色的在线教育平台网站响应式模板\\Learning_video\\Learning_video')
# 将项目路径添加到系统搜寻路径当中
os.environ['DJANGO_SETTINGS_MODULE'] = 'Learning_video.settings'

# 设置项目的配置文件
# django.setup()
# # 加载项目配置

db_path = os.path.join(settings.BASE_DIR,'db.sqlite3')
print(db_path)
conn = sqlite3.connect(db_path)
# conn.execute('''CREATE TABLE
#       (ID            INTEGER    PRIMARY KEY  AUTOINCREMENT   NOT NULL,
#        coure_id    INTEGER                                  NULL,
#        data        VACHER                                   NULL,
#        title       VACHER                                   NULL)
#        ''')
# conn.execute('''CREATE TABLE COURESE_VIDEO
#       (ID            INTEGER    PRIMARY KEY  AUTOINCREMENT   NOT NULL,
#        courese_name    VACHER                                  NOT NULL,
#        TAG            VACHER                                   NULL,
#        NUM            INT                                  NOT NULL,
#        IMG            VACHER                                    NOT NULL)
# ''')
j = 1
for s in range(1,4):
    url = f'http://yun.itheima.com/course/index/p/{s}.html'

    # headers = {
    #     "Accept": "text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, image / apng, * / *;q = 0.8, application / signed - exchange;v = b3",
    #     "Cookie": "isclose = 1;isclose = 1;bad_id48bc7230 - 6252 - 11e8 - 917f - 9fb8db4dc43c = 07d0a622 - af80 - 11e9 - 8b58 - d38319d565ab;bad_idd48d5cf0 - 2e47 - 11e8 - 9db3 - 3313a60c92e9 = 1bf50d32 - af80 - 11e9 - 8b58 - d38319d565ab;bad_id994d4130 - 1df9 - 11e9 - b7ec - 7766c2691ec6 = 7f28e971 - be8b - 11e9 - ae45 - 0f2733d23281;nice_id48bc7230 - 6252 - 11e8 - 917f - 9fb8db4dc43c = f08eec01 - c263 - 11e9 - b0d0 - 2b2b8052cd76;openChat48bc7230 - 6252 - 11e8 - 917f - 9fb8db4dc43c = true;PHPSESSID = 9u9jsh7pbqhpod2jomv25b4dr3;href = http % 3A % 2F % 2Fyun.itheima.com % 2Fmap % 2F22.html % 3Fa5;accessId = 994d4130 - 1df9 - 11e9 - b7ec - 7766c2691ec6;nice_id994d4130 - 1df9 - 11e9 - b7ec - 7766c2691ec6 = 472e3701 - c264 - 11e9 - 8390 - 4da302bf9563;nice_idd48d5cf0 - 2e47 - 11e8 - 9db3 - 3313a60c92e9 = 3dc58ec1 - c417 - 11e9 - b046 - 17a192948105;openChatd48d5cf0 - 2e47 - 11e8 - 9db3 - 3313a60c92e9 = true;isclose = 1;qimo_seosource_994d4130 - 1df9 - 11e9 - b7ec - 7766c2691ec6 = % E7 % AB % 99 % E5 % 86 % 85;qimo_seokeywords_994d4130 - 1df9 - 11e9 - b7ec - 7766c2691ec6 =;pageViewNum = 48",
    #     "User - Agent" :"Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 76.0.3809.100Safari / 537.36"
    # }

    response = requests.get(url,)
    # print(response)
    html_str = response.content.decode()
    html = etree.HTML(html_str)
    one = html.xpath('//div[@class="main"]/ul//li')
    # print(one)
    for i in one:
        img = i.xpath('.//img[@class="mask_img1"]/@src')[0]
        img = img.replace("/Upload/./","http://yun.itheima.com/Upload/")
        print(img)
        lianjie = i.xpath('./a/@href')[0]
        a = lianjie.replace("","http://yun.itheima.com",1)
        print(a)
        url = i.xpath('./a/@href')[0].replace("/course/","http://yun.itheima.com/course/")
        response = requests.get(url)

        html_str = response.content.decode()
        html = etree.HTML(html_str)
        video = set(html.xpath('//ul/li/a/@data'))

        title = sorted(set(html.xpath('//div[@class="main"]//li/a/text()')))
        # title = sorted(title)

        title.remove("开始学习")

        video = sorted(video)

        """for temp in range(0,len(video)):
            print(video[temp],title[temp])

            data = "insert into videos_allcoureslist(link,text,coure_id_id)values('%s','%s','%d')"% (video[temp],title[temp],j)

            conn.execute(data)
            print("插入数据完成")

        j += 1
        """


        # print(s)
        # print(url)
        name = i.xpath('.//h2/text()')[0].replace("|黑马程序员","")
        print(name)
        # conn = sqlite3.connect(db_path)
        num = int(len(title))
        print(num,type(num))
        data = "insert into videos_courese(courese_name,num,img)values('%s','%d','%s')" % (name,num,img)
        conn.execute(data)
        # print("插入课程完成")
# data = "insert into Course details(data,text)values('%s','%s')" % (videos['data'], videos['text'])

# conn.execute('''CREATE TABLE python_coures
#       (ID       INTEGER PRIMARY KEY  AUTOINCREMENT   NOT NULL,
#        data     TEXT                       NOT NULL,
#        text     TEXT                       NOT NULL)''')

# video = html.xpath('//li[@class="click "]')
# print(video)
# j = 1
# for i in video:
#     videos = {}
#     videos["data"] = i.xpath(f'//a[@class="chapter cur{j} a_world"]/@data')[0]
#     videos["text"] = i.xpath(f'//a[@class="chapter cur{j} a_world"]/text()')[0]
#     j = j + 1
#     print(videos)
print("完成")
conn.commit()
conn.close()
