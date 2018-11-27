# -*- coding: utf-8 -*-
__author__ = 'super'
__date__ = '2018/11/27 18:36'

from lxml import etree

parser = etree.HTMLParser(encoding='utf8')    # 定义解析器
html = etree.parse('msj1.html', parser=parser)  # 解析html文件

# 获取所有td标签
# trs = html.xpath('//td')    # 使用xpath语法
# print(type(trs))    # <class 'list'> 返回一个列表
# for tr in trs:
#     print(etree.tostring(tr, encoding='utf8').decode('utf8'))


# 获取第2个td标签
# trs = html.xpath('//td[2]')[11]
# print(etree.tostring(trs, encoding='utf8').decode('utf8'))
#
#
# # 获取所有class等于right
# # trs = html.xpath('//td[@class="right"]')
# # for tr in trs:
# #     print(etree.tostring(tr, encoding='utf8').decode('utf8'))
#
#
# # 获取所有a标签的href属性
# # aList = html.xpath('//a/@href')
# # print(type(aList))
# # for a in aList:
# #     print(a)
#
#
# # A = html.xpath('//td[@class="right"]')
# # for i in A:
# #     print(etree.tostring(i, encoding='utf8').decode('utf8'))
#
#
#
# aList = html.xpath('//tr//td/a[position()>1]/@href')
# print(type(aList))
# for a in aList:
#     print(a)