import requests
from lxml import etree
import os
import sys
import sqlite3
from django.conf import settings
import django
# sys.path.append('C:\\Users\\吴豪\\Desktop\\绿色的在线教育平台网站响应式模板\\Learning_video\\Learning_video')
# 将项目路径添加到系统搜寻路径当中
os.environ['DJANGO_SETTINGS_MODULE'] = 'Learning_video.settings'

# 设置项目的配置文件
django.setup()
# # 加载项目配置

db_path = os.path.join(settings.BASE_DIR,'db.sqlite3')
print(db_path)

import json
url = "http://yun.itheima.com/course/273.html"

headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    "Cookie":"bad_id48bc7230-6252-11e8-917f-9fb8db4dc43c=07d0a622-af80-11e9-8b58-d38319d565ab; bad_idd48d5cf0-2e47-11e8-9db3-3313a60c92e9=1bf50d32-af80-11e9-8b58-d38319d565ab; bad_id994d4130-1df9-11e9-b7ec-7766c2691ec6=7f28e971-be8b-11e9-ae45-0f2733d23281; nice_id994d4130-1df9-11e9-b7ec-7766c2691ec6=7f28e972-be8b-11e9-ae45-0f2733d23281; nice_id48bc7230-6252-11e8-917f-9fb8db4dc43c=db4d1511-be94-11e9-83cd-5fa7eb7fd336; nice_idd48d5cf0-2e47-11e8-9db3-3313a60c92e9=dd10be11-be94-11e9-90a6-39e3c54aee2a; openChatd48d5cf0-2e47-11e8-9db3-3313a60c92e9=true; openChat48bc7230-6252-11e8-917f-9fb8db4dc43c=true; PHPSESSID=ahf9kr6d2l0209c5u59vg3tms3; href=http%3A%2F%2Fyun.itheima.com%2FCourse; accessId=994d4130-1df9-11e9-b7ec-7766c2691ec6; pageViewNum=6",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"}
response = requests.post(url, headers=headers)
print(response)
html_str = response.content.decode()
html = etree.HTML(html_str)


conn = sqlite3.connect(db_path)
# conn.execute('''CREATE TABLE python_coures
#       (ID       INTEGER PRIMARY KEY  AUTOINCREMENT   NOT NULL,
#        data     TEXT                       NOT NULL,
#        text     TEXT                       NOT NULL)''')

video = html.xpath('//li[@class="click "]')
print(video)
j = 1
for i in video:
    videos = {}
    videos["data"] = i.xpath(f'//a[@class="chapter cur{j} a_world"]/@data')[0]
    videos["text"] = i.xpath(f'//a[@class="chapter cur{j} a_world"]/text()')[0]
    j = j + 1
    print(videos)
    data = "insert into python_coures(data,text)values('%s','%s')" % (videos['data'], videos['text'])
    conn.execute(data)
conn.commit()
conn.close()
