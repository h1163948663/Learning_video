import requests
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

conn = sqlite3.connect(db_path)

import threading
import requests
from lxml import etree
import time
def get_src():
    for i in range(7,9):
        url = url = f'http://yun.itheima.com/course/index/p/{i}.html'
        response = requests.get(url)
        html_str = response.content.decode()
        html = etree.HTML(html_str)
        course = html.xpath('//div[@class="main"]/ul//li')
        s = 1
        for j in course:
            img = j.xpath('.//img[@class="mask_img1"]/@src')[0]
            img = img.replace("/Upload/./", "http://yun.itheima.com/Upload/")
            print(img)
            title = j.xpath('.//h2/text()')[0].replace("|黑马程序员","")
            tag =title.split("】")[0].split("【")[1]
            print(tag)
            print(title.split("】")[1])
            course_url = j.xpath('./a/@href')[0]
            course_url = 'http://yun.itheima.com'+ str(course_url)
            print(course_url)
            response = requests.get(course_url)
            html_str = response.content.decode()
            video_html = etree.HTML(html_str)
            video = video_html.xpath('//div[@class="main"]//li')
            num = 0
            for k in video:
                video_title = k.xpath('./a/text()')[0]
                print(video_title)
                video_url = k.xpath('./a/@data')[0]
                print(video_url)
                if video_url != '':
                    data1 = "insert into videos_allcoureslist(link,title) values('%s','%s')" %(video_url,video_title)
                    conn.execute(data1)
                    conn.commit()
                    num += 1
            data2 = "insert into videos_courese(courese_name,img,num)values('%s','%s','%d')" % (title,img,num)
            conn.execute(data2)
            conn.commit()
            #             conn.execute(data)
            print(len(video))
    conn.close()
def main():
    add_thread = 'add_thread'
    starttime = time.time()
    print(time.ctime())

    # for i in range(5):
    #     i = threading.Thread(target=get_src())
    #     i.start()
    get_src()
    endtime = time.time()
    print(time.ctime())
    print(endtime-starttime)

if __name__ =='__main__':
    main()