#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : send_mail.py
# Author: HuXianyong
# Date  : 2019/7/26 14:00

import smtplib
from email.header import Header
from email.mime.text import MIMEText



# 第三方 SMTP 服务
host = "smtp.163.com"      # SMTP服务器
port = 465
user = "mghxy123@163.com"                  # 用户名
passWD = "mghxy123"               # 授权密码，非登录密码

sender = 'mghxy123@163.com' #发邮件人
receivers = 'mghuxy123@163.com' #收邮件人

content = '''
    这个是邮件内容，
    你想写些什么就写些什么！
''' #邮件内容

subject = '邮件主题'  # 邮件主题


# meg['Subject'] = subject #这个方法和下面的一样可以发送邮件


def send_email1():
    meg = MIMEText(content+' \n send_email1', 'plain', 'utf-8')  # 内容, 格式, 编码
    meg['From'] = user  # 这两种方法都一样的
    # meg['From'] = "{}".format(user)
    meg['To'] = receivers
    meg['Subject'] = subject+' send_email1'
    # msg['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP_SSL(host, port)  # 启用SSL发信, 端口一般是465
        smtpObj.login(user, passWD)  # 登录验证
        smtpObj.sendmail(sender, receivers, meg.as_string())  # 发送
        print("邮件1发送成功！")
    except smtplib.SMTPException as e:
        print('aaaaa',e)

send_email1()