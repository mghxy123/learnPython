#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : lianjiaLogin.py
# Author: HuXianyong
# Date  : 2019/7/28 13:59

import requests
url = 'https://bj.lianjia.com/zufang/'
headers = {
    'Host': "bj.lianjia.com",
    'Connection': "keep-alive",
    'Cache-Control': "max-age=0",
    'Upgrade-Insecure-Requests': "1",
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    'Referer': "https://bj.lianjia.com/?utm_source=baidu&utm_medium=pinzhuan&utm_term=biaoti&utm_content=biaotimiaoshu&utm_campaign=sousuo&ljref=pc_sem_baidu_ppzq_x",
    'Accept-Encoding': "gzip, deflate, br",
    'Accept-Language': "zh-CN,zh;q=0.9",
    'Cookie': "select_city=110000; all-lj=26155dc0ee17bc7dec4aa8e464d36efd; lianjia_uuid=b929a0ea-bca7-4258-a9b7-fd0cec82735c; _smt_uid=5d3d196e.47c739b1; UM_distinctid=16c36ab56ba191-024ae15b65bd81-c343162-1fa400-16c36ab56bc62; CNZZDATA1253477573=1660489179-1564281744-https%253A%252F%252Fsp0.baidu.com%252F%7C1564281744; CNZZDATA1254525948=2011011659-1564283881-https%253A%252F%252Fsp0.baidu.com%252F%7C1564283881; CNZZDATA1255633284=1306608612-1564281453-https%253A%252F%252Fsp0.baidu.com%252F%7C1564281453; _jzqa=1.409464984760914800.1564285294.1564285294.1564285294.1; _jzqc=1; _jzqy=1.1564285294.1564285294.1.jzqsr=baidu|jzqct=%E9%93%BE%E5%AE%B6.-; _jzqckmp=1; _qzjc=1; CNZZDATA1255604082=1058036611-1564281977-https%253A%252F%252Fsp0.baidu.com%252F%7C1564281977; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216c36ab5a36331-08c73ce396bc31-c343162-2073600-16c36ab5a3760%22%2C%22%24device_id%22%3A%2216c36ab5a36331-08c73ce396bc31-c343162-2073600-16c36ab5a3760%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E4%BB%98%E8%B4%B9%E5%B9%BF%E5%91%8A%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fsp0.baidu.com%2F9q9JcDHa2gU2pMbgoY3K%2Fadrc.php%3Ft%3D06KL00c00fZg9KY0uvPb0nVfAsKGAHdI000000RuQ7C00000XLURjC.THLKVQ1i0A3qmh7GuZR0T1d-PynsmhmLuW0snjn3uH-B0ZRqnj9jP1wAnWTLPjbYnR7DwHfYnjwanYf4n1D4f1FDnH0%22%2C%22%24latest_referrer_host%22%3A%22sp0.baidu.com%22%2C%22%24latest_search_keyword%22%3A%22%E9%93%BE%E5%AE%B6%22%2C%22%24latest_utm_source%22%3A%22baidu%22%2C%22%24latest_utm_medium%22%3A%22pinzhuan%22%2C%22%24latest_utm_campaign%22%3A%22sousuo%22%2C%22%24latest_utm_content%22%3A%22biaotimiaoshu%22%2C%22%24latest_utm_term%22%3A%22biaoti%22%7D%7D; _ga=GA1.2.851987246.1564285297; _gid=GA1.2.1772532123.1564285297; lianjia_token=2.006c0cde8911055a1c7da1f7b8c77b989d; _qzja=1.399030463.1564285294426.1564285294426.1564285294427.1564285294427.1564285656551.0.0.0.2.1; _qzjto=2.1.0; lianjia_ssid=6ae96848-4c8c-4427-8f69-740680eb0129; srcid=eyJ0Ijoie1wiZGF0YVwiOlwiNmZjZGM4M2E0NjYzMDZmZTcyYzliMzQyNjA1YjQyZDNlNDdlM2ZjMDlhMmU1NjI4Yzc2NWQ1N2NkNjkyMjQ4NGUzYWNmYTI5ZTUyNGY3YTgyNTAwMWUyY2I1YjIxYjc2YTlmNmQ1YThjZmVjM2QzMjZlZTBjYTZjNzJmYTg0N2M4MGYwNDRhMzk2YzhhMGVhMmNlZWE4MjRlNzQzNDVhZDkwMzVjZDdhMmFiMzFkMzNiNDAxZjZiMTA1MDc3MWI0NmUxOTgwYjY5MWMzZWY2M2EyNjNjZmRhNjliMjA0MTk4NjYwZjExYjJjZWI1NTE3YzI0NzRkMDg5YzZjOTA2NGE4ZGVhNDY4OWIzZmVjMGZhNjYxNjMxNjJiY2Q3Y2I1ZDZhMmY4MjEyYTM4ZjMyMjQxZmI3MjkzODU5ZDdkNWY3N2QyM2JlM2E2NmVhMjRjNDFjZDY0OGIxZDU1ZjRjOFwiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCI4OGFhM2E0N1wifSIsInIiOiJodHRwczovL2JqLmxpYW5qaWEuY29tL3p1ZmFuZy8iLCJvcyI6IndlYiIsInYiOiIwLjEifQ==",
    'cache-control': "no-cache",
    'Postman-Token': "4cf35966-684e-4c08-86e5-da690fcb4fe2"
    }

response = requests.request("GET", url=url, headers=headers)


with response:
    with open('test.html','w') as f:
        f.write(response.text)
print(response.text)