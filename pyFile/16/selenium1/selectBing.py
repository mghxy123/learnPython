#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : selectBing.py
# Author: HuXianyong
# Date  : 2019/7/30 19:44
import time

from selenium import webdriver
from datetime import datetime
from urllib import parse
import random

# 指定phantomjs的执行文件
diver = webdriver.PhantomJS(
    r'C:\Users\Administrator\Desktop\python20\file\chapter16爬虫\install\phantomjs-2.1.1-windows\bin\phantomjs.exe')

# 设置窗口大小
diver.set_window_size(1280, 1024)

# 使用get方法打开网页
url = 'http://cn.bing.com/search?' + parse.urlencode({
    'q': '马哥教育'
})

diver.get(url)


# 保存截图
def savepic():
    file_name = '{:%Y%m%d%H%M%S}[{:03}.png'.format(
        datetime.now(),
        random.randint(1, 100)
    )
    diver.save_screenshot(file_name)


# time.sleep(1) # 等待js加载时间,才能看到返回的内容在截图上

maxRetrys =  5 # 最大重试次数
for i in range(maxRetrys):
    time.sleep(1)
    try:
        ele = diver.find_element_by_id('b_results') # 如果查询结果来了就有这个id的标签
        if not ele.is_displayed():
            print('dispaly none')
            continue
        print('ok')
        savepic()
        break
    except Exception as e:
        print(e)

diver.quit()# 记得使用完了关闭浏览器