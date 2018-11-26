# -*- coding: utf-8 -*-
__author__ = 'super'
__date__ = '2018/11/21 20:37'

from urllib import request
from urllib import parse

# url = 'https://www.lagou.com/jobs/list_Python?px=default&city=%E5%8D%97%E4%BA%AC'

url = 'https://www.lagou.com/jobs/positionAjax.json?px=default&city=%E5%8D%97%E4%BA%AC&needAddtionalResult=false'

headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    'Referer':'https://www.lagou.com/jobs/list_Python?px=default&city=%E5%8D%97%E4%BA%AC'
}

data = {
    'first':'true',
    'pn':2,
    'kd':'python'
}

# resp = request.urlopen(url)
# print(resp.read())

req = request.Request(url,headers=headers,data=parse.urlencode(data).encode('utf-8'),method='POST')
resp = request.urlopen(req)
print(resp.read().decode('utf-8'))
