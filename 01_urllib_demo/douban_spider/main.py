# -*- coding: utf-8 -*-
__author__ = 'super'
__date__ = '2018/11/27 19:57'
# 爬取豆瓣最新电影

import requests
from lxml import etree

# 1.将目标网站上的页面爬取下来
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    'Referer':'https://movie.douban.com/'
}
url = 'https://movie.douban.com/cinema/nowplaying/xuzhou/'

response = requests.get(url,headers=headers)
text = response.text
# response.text返回的是一个经过解码后的字符串，是str(unicode)类型
# response.content返回的是一个原生的字符串，就是从网上抓取下来的，没有经过处理的字符串，是bytes类型
# print(response.text)

# 2.将爬取下来的数据根据一定的规则进行提取
html = etree.HTML(text)
# 获取ul元素
ul = html.xpath("//ul[@class='lists']")[0]
# print(etree.tostring(ul,encoding='utf-8').decode("utf-8"))
# 在当前ul标签下获取所有li
lis = ul.xpath("./li")
movies = []
for li in lis:
    # print(etree.tostring(li,encoding='utf-8').decode('utf-8'))
    # 获取title
    title = li.xpath('@data-title')[0]
    # print(title)
    # 评分
    score = li.xpath('@data-score')[0]
    # 星级
    star = li.xpath('@data-star')[0]
    # 上映年份
    release = li.xpath('@data-release')[0]
    # 时长
    duration = li.xpath('@data-duration')[0]
    #上映地点
    region = li.xpath('@data-region')[0]
    #导演
    director = li.xpath('@data-director')[0]
    #     演员
    actors = li.xpath('@data-actors')

    # 获取海报
    image = li.xpath('.//img/@src')[0]

    movie = {
        '电影':title,
        '评分':score,
        '星级':star,
        '上映时间':release,
        '时长':duration,
        '地区':region,
        '导演':director,
        '演员':actors,
        '海报':image
    }
    movies.append(movie)

print(movies)



