#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : selenium搜索豆瓣电影.py
# Author: HuXianyong
# Date  : 2019/7/30 20:47


from time import  sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys # 键盘输入

# WebDiverWait 负责条件循环
from selenium.webdriver.support.wait import WebDriverWait

# expected_conditions 条件,负责条件触发
from selenium.webdriver.support import expected_conditions
from datetime import datetime
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

# 打开额昂也使用get方法,模拟在浏览器上输入网址
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



# url = 'https://cn.bing.com/search?q=douban+TRON'
# diver.get(url)
# print(url)
# print(diver.current_url) # 取出当前的url

# try:
#     ele = WebDriverWait(diver,20).until(
#         # EC.presence_of_all_elements_located( # 这个没有等待就直接得到了截图,退出了
#         EC.visibility_of_all_elements_located( # 这个可以等到请求得到结果后再退出
#
#             (By.ID, "b_results")
#         )
#     )
#
#     savepic()
# except Exception as e:
#     print(e)
#
# finally:
#     diver.quit()

# 统一设定隐式等待秒数
diver.implicitly_wait(10)

url = 'https://cn.bing.com/search?q=douban+TRON'
diver.get(url)
print(url)
print(diver.current_url) # 取出当前的url


try:
    # ele = WebDriverWait(diver,20).until(
    #     # EC.presence_of_all_elements_located( # 这个没有等待就直接得到了截图,退出了
    #     EC.visibility_of_all_elements_located( # 这个可以等到请求得到结果后再退出
    #
    #         (By.ID, "b_results")
    #     )
    # )
    # diver.find_element_by_xpath('b_results')
    diver.find_element_by_xpath('ssssss')
    savepic()
except Exception as e:
    print(e,'==================')

finally:
    diver.quit()