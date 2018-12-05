# -*- coding: utf-8 -*-
__author__ = 'super'
__date__ = '2018/11/28 13:16'

from bs4 import BeautifulSoup

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>

<tr>
    <td>李磊</td>
    <td>男</td>
    <td>21</td>
</tr>
<tr>
    <td>齐名</td>
    <td>男</td>
    <td>22</td>
</tr>
<tr>
    <td>红</td>
    <td>女</td>
    <td>22</td>
</tr>

"""

#创建 Beautiful Soup 对象
# 使用lxml来进行解析
soup = BeautifulSoup(html,"lxml")

#获取所有p标签
# ps = soup.find_all('p')
#
# for p in ps:
#     # print(p)
#     print(type(p))

# 获取id='link1',class_="sister"的a标签
aList = soup.find_all('a',id='link1',class_="sister")
for a in aList:
    print(a)

# 获取所有a标签的值
# aList = soup.find_all('a')
# for a in aList:
    # 1.通过下标操作
    # href = a['href']
    # print(href)

    # 2.通过attrs操作
    # href = a.attrs['href']
    # print(href)


# 获取所有人员信息
trList = soup.find_all('tr')
info = []
for tr in trList:
    person = {}
    # tdList = tr.find_all('td')
    # name = tdList[0].string
    # gender = tdList[1].string
    # age = tdList[2].string
    # person['name']=name
    # person['gender']=gender
    # person['age']=age
    # info.append(person)
    persons = list(tr.stripped_strings)
    person['name']=persons[0]
    person['gender']=persons[1]
    person['age']=persons[2]
    info.append(person)
print(info)



# print(soup.prettify())
