# !/usr/bin/env python
# -*- coding:utf-8 -*-
# project name: google_agent
# author: "Lei Yong" 
# creation time: 2018/1/23 0023 11:30
# Email: leiyong711@163.com

import os
import logging
import time
import json
import sys
from getGoogle import *
from flask import Flask, request, render_template

logpath=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"TestHt/log/")
logging.basicConfig(
                    level=logging.DEBUG,
                    # level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%y-%m-%d %H:%M:%S',
                    filename=os.path.join(logpath, 'sqllog.txt'),
                    filemode='a')

reload(sys)
sys.setdefaultencoding('gbk')

app = Flask(__name__, static_url_path='')


# txt日志写出
def log_txt(data):
    txt = open('log/log.txt', 'a')
    txt.write(data)
    txt.write('\n')
    txt.close()


# 路由配置 指用户访问的路径与请求方式
@app.route('/', methods=['Get'])  # 用户通过Get请求访问服务器根目录执行此方法
def req_g():
    logging.info('时间：%s   用户IP：%s   请求google首页' % (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), request.remote_addr))
    log_txt('时间：%s   用户IP：%s   请求google首页' % (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), request.remote_addr))
    return render_template('index2.html')


@app.route('/search', methods=['Get'])  # 用户通过Get请求访问服务器/search目录执行此方法
def rsear_g():
    b = request.args.to_dict()
    b['q'] = b['q'].encode('utf-8')  # 处理谷歌二次搜索编码，否则会导致二次搜索乱码
    b['btnG'] = b['btnG'].encode('utf-8')  # 处理谷歌二次搜索编码，否则会导致二次搜索乱码
    a = json.dumps(request.args.to_dict(), encoding="UTF-8", ensure_ascii=False)
    try:
        logging.info('时间：%s   用户IP：%s   请求参数：%s' % (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), request.remote_addr, str(a).encode('utf-8')))
        log_txt('时间：%s   用户IP：%s   请求参数：%s' % (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), request.remote_addr, str(a).encode('utf-8')))
    except:
        try:
            logging.info('时间：%s   用户IP：%s   请求参数：%s' % (
            time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), request.remote_addr, str(a).encode('gbk')))
            log_txt('时间：%s   用户IP：%s   请求参数：%s' % (
            time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), request.remote_addr, str(a).encode('gbk')))
        except:
            logging.info('时间：%s   用户IP：%s   请求参数：%s' % (
            time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), request.remote_addr, str(a)))
            log_txt('时间：%s   用户IP：%s   请求参数：%s' % (
            time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), request.remote_addr, str(a)))
    html = getgoogle2(b)  # ImmutableMultiDict, MultiDict 都可以通过 to_dict() 转成 dict
    return html


@app.route('/s')  # 用户通过Get请求访问服务器根目录执行此方法
def google_G():
    if request.method == 'GET':
        wd = request.args.get('wd')
        logging.info('时间：%s   用户IP：%s   请求参数：%s' % (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), request.remote_addr, wd.encode('utf-8')))
        log_txt('时间：%s   用户IP：%s   请求参数：%s' % (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), request.remote_addr, wd.encode('utf-8')))
        html = getgoog1(wd)
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0',
            port=9999,
            debug=False)

