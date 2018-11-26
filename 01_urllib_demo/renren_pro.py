# -*- coding: utf-8 -*-
__author__ = 'super'
__date__ = '2018/11/22 21:25'
from urllib import request
from urllib import parse
from http.cookiejar import CookieJar

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    'Cookie':'anonymid=josgzyhm-c5pfnd; depovince=JS; _r01_=1; ick_login=5e5f1552-b80e-4225-b943-e51c3c245b18; JSESSIONID=abcWwNShypcYScH_Jb7Cw; __utma=151146938.1263122760.1542883534.1542883534.1542883534.1; __utmc=151146938; __utmz=151146938.1542883534.1.1.utmcsr=renren.com|utmccn=(referral)|utmcmd=referral|utmcct=/; ick=b4a8869d-d213-4020-bd10-47fb73105d7f; __utmb=151146938.4.10.1542883534; jebecookies=7103e0f9-6fcb-43f2-ba3c-f9caf2c0e3fa|||||; _de=BE953EF0EEE893AF60197127ED063839; p=5fe9e01768fb81a390736006e1ae76e29; ap=854406609; first_login_flag=1; ln_uact=18361398296; ln_hurl=http://hdn.xnimg.cn/photos/hdn421/20141019/2330/h_main_6OvO_e1530003dd71195a.jpg; t=c57d02406916a0f9fdf658f332940b5a9; societyguester=c57d02406916a0f9fdf658f332940b5a9; id=854406609; xnsid=c4f85215; loginfrom=syshome; ch_id=10016; jebe_key=212faae4-1ec2-48f5-9c50-6cd1b9b8afac%7C872d0f8f5cd8b652adb6cf3981cdddeb%7C1542883622422%7C1%7C1542883626181; wp_fold=0; XNESSESSIONID=940af5ce2745; _ga=GA1.2.1263122760.1542883534; _gid=GA1.2.420468133.1542884499'
}

def get_opener():
    # 1.登录
    # 1.1 创建一个cookiejar对象
    cookie = CookieJar()
    # 1.2使用cookiejar创建一个HttpCookieProcess对象
    handler = request.HTTPCookieProcessor(cookie)
    # 1.3 使用handler创建一个opener
    opener = request.build_opener(handler)
    return opener

def login_renren(opener):
    # 1.4 使用opener发送登录的请求
    data = {
        'email':'970138074@qq.com',
        'password':'pythonspider'
    }
    login_url = 'http://www.baidu.com/PLogin.do'
    req = request.Request(login_url,data=parse.urlencode(data).encode('utf-8'),headers=headers)
    opener.open(req)


def visit_profile(opener):
    wqc_url = 'http://www.renren.com/854406609/profile'

    req = request.Request(wqc_url,headers=headers)
    resp = opener.open(req)
    with open('renren_pro.html', 'w', encoding='utf-8') as fp:
        fp.write(resp.read().decode('utf-8'))

if __name__ == '__main__':
    opener = get_opener()
    login_renren(opener)
    visit_profile(opener)

