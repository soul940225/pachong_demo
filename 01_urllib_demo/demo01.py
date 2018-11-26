# -*- coding: utf-8 -*-
__author__ = 'super'
__date__ = '2018/11/20 22:06'

from urllib import request
from urllib import parse

# resp=request.urlopen('http://www.baidu.com')
#
# print(resp.read())

# request.urlretrieve('http://www.baidu.com','123.html')

# params = {'name':'张三','age':10,'greet':'hello world'}
# result = parse.urlencode(params)
# print(result)

# url = 'https://www.baidu.com/s'
# params = {'wd':'李白'}
# qs = parse.urlencode(params)
# url = url + '?' +qs
# resp=request.urlopen(url)
# print(resp.read())


url = 'http://www.baidu.com/s?username=zhiliao'
result1 = parse.urlparse(url)
result2 = parse.urlsplit(url)
print(result1)
print(result2)
