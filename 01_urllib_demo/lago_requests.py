# -*- coding: utf-8 -*-
__author__ = 'super'
__date__ = '2018/11/26 20:48'

import requests

url = 'https://www.lagou.com/jobs/positionAjax.json?gj=3%E5%B9%B4%E5%8F%8A%E4%BB%A5%E4%B8%8B&px=default&city=%E5%8D%97%E4%BA%AC&needAddtionalResult=false'
data = {
    'first':'true',
    'pn':'1',
    'kd':'python'
}

headers = {
    'Referer':'https://www.lagou.com/jobs/list_python?px=default&gj=3%E5%B9%B4%E5%8F%8A%E4%BB%A5%E4%B8%8B&city=%E5%8D%97%E4%BA%AC',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}


response = requests.post(url=url,data=data,headers=headers)
print(response.json())