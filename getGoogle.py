# !/usr/bin/env python
# -*- coding:utf-8 -*-
# project name: google_agent
# author: "Lei Yong" 
# creation time: 2018/1/23 0023 11:35
# Email: leiyong711@163.com
import urllib
import urllib2


# 从代理页搜索
def getgoog1(wd):
    headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2904.0 Safari/537.36'}
    url = 'https://www.google.co.jp/search?q=%s&oq=%s&aqs=chrome..69i57j69i61j0l4.1093j0j8&sourceid=chrome&ie=UTF-8'% (wd.encode('utf-8'), wd.encode('utf-8'))
    req = urllib2.Request(url, headers=headers)  # 添加信息头
    html = urllib2.urlopen(req).read()  # 发送请求
    html1 = html.replace('src="/images/branding/googlelogo/2x/googlelogo_color_120x44dp.png"','src="../img/1.png"')   # 使用服务器图片
    return html1


# 在谷歌页面多次搜索
def getgoogle2(values):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2904.0 Safari/537.36'}
    url = 'https://www.google.co.jp/search?'
    data = urllib.urlencode(values)  # 对字典进行编码
    req = urllib2.Request(url+data, headers=headers)  # 添加信息头
    html = urllib2.urlopen(req).read()  # 发送请求
    html1 = html.replace('src="/images/branding/googlelogo/2x/googlelogo_color_120x44dp.png"', 'src="../img/1.png"')   # 使用服务器图片
    return html1

if __name__ == '__main__':
    getgoog1('python')

