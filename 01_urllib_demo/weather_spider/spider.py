# -*- coding: utf-8 -*-
__author__ = 'super'
__date__ = '2018/12/5 12:19'

'''爬取中国天气网案例'''
import requests
from bs4 import BeautifulSoup
from pyecharts import Bar

ALL_DATA = []

def parse_page(url):
    headers = {
        'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
    }
    response = requests.get(url,headers=headers)
    text = response.content.decode('utf-8')
    soup = BeautifulSoup(text,'html5lib')
    conMidtab = soup.find('div',class_='conMidtab')
    tables = conMidtab.find_all('table')
    for table in tables:
        trs = table.find_all('tr')[2:]
        for index,tr in enumerate(trs):
            tds = tr.find_all('td')
            city_td = tds[0]
            if index == 0:
                city_td = tds[1]
            city = list(city_td.stripped_strings)[0]
            temp_td = tds[-2]
            min_temp = list(temp_td.stripped_strings)[0]
            ALL_DATA.append({'城市':city,'最低气温':int(min_temp)})




def main():
    xb_url = 'http://www.weather.com.cn/textFC/xb.shtml'
    hn_url = 'http://www.weather.com.cn/textFC/hn.shtml'
    hb_url = 'http://www.weather.com.cn/textFC/hb.shtml'
    hz_url = 'http://www.weather.com.cn/textFC/hz.shtml'
    hd_url = 'http://www.weather.com.cn/textFC/hd.shtml'
    xn_url = 'http://www.weather.com.cn/textFC/xn.shtml'
    db_url = 'http://www.weather.com.cn/textFC/db.shtml'
    gat_url = 'http://www.weather.com.cn/textFC/gat.shtml'

    urls = [
        xb_url,hn_url,hb_url,hz_url,hd_url,hn_url,xn_url,db_url,gat_url
    ]
    for url in urls:
        parse_page(url)

    # 分析数据
    # 根据最低气温排序
    ALL_DATA.sort(key=lambda data:data['最低气温'])

    data = ALL_DATA[0:10]

    cities = list(map(lambda x:x['城市'] ,data))
    temps = list(map(lambda x: x['最低气温'],data))
    chart = Bar("2018/12/5中国最低气温排行榜")
    chart.add('',cities,temps)
    chart.render('weather.html')



if __name__ == '__main__':
    main()