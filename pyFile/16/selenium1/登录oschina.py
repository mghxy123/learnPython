#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 登录oschina.py
# Author: HuXianyong
# Date  : 2019/7/30 20:01


from time import  sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys # 键盘输入
from datetime import datetime
from urllib import parse
import random

# 指定phantomjs的执行文件
diver = webdriver.PhantomJS(
    r'C:\Users\Administrator\Desktop\python20\file\chapter16爬虫\install\phantomjs-2.1.1-windows\bin\phantomjs.exe')

# 设置窗口大小
diver.set_window_size(1280, 1024)


# 保存截图
def savepic():
    file_name = '{:%Y%m%d%H%M%S}_{:03}.png'.format(
        datetime.now(),
        random.randint(1, 100)
    )
    diver.save_screenshot(file_name)


# time.sleep(1) # 等待js加载时间,才能看到返回的内容在截图上

# 取出登陆页面
url = 'https://www.oschina.net/home/login'
diver.get(url)

print(diver.current_url) # 取出当前的url
savepic()

# 输入用户名密码
username = diver.find_element_by_id('userMail') # 取出用户名的元素
username.send_keys('15210799926')

password = diver.find_element_by_id('userPassword') # 取出密码元素
password.send_keys('mghxy!23')

savepic()
password.send_keys(Keys.ENTER) # 发送回车键
print('-'*60)



maxRetrys =  5 # 最大重试次数
for i in range(maxRetrys):
    sleep(1)
    try:
        ele = diver.find_element_by_xpath('//div[@title="Forand"]') # 如果查询结果来了就有这个id的标签
        # ele = diver.find_element_by_xpath('//h3[@class="ui centered header"]/text()') # 如果查询结果来了就有这个id的标签

        print(ele.tag_name,'_________')# 能打印出来就说明登陆成功了,登陆失败,找不熬到结果就会报异常的
        print(ele.get_attribute('data-user-id'))
        savepic()
        break
    except Exception as e:
        print(e)

#######################################################
# 模拟登陆完成后获取cookies
cookies = diver.get_cookies()
# print(cookies)
for c in cookies:
    print(type(c))
    print(c)

print('+'*60)

import requests
from requests.cookies import RequestsCookieJar

jar = RequestsCookieJar()
for c in cookies:
    jar.set(c.get('name'),c.get('value'))
print(jar)


######################################
#使用cookies登陆
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}

print('=============================不带cookies登陆=======================')
response  = requests.get(url,headers=headers)
with response:
    print(10,response.url)
    with open('noCookies.html','w',encoding='utf-8') as f:
        f.write(response.text)


print('=============================带cookies登陆=======================')
response  = requests.get(url,headers=headers,cookies=jar)
with response:
    print(10,response.url)
    with open('Cookies.html','w',encoding='utf-8') as f:
        f.write(response.text)


diver.quit()# 记得使用完了关闭浏览器