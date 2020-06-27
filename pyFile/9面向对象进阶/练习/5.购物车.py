#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 5.购物车.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/16 0016

cdict = {}
class Shiping:


    def trolley(self):#车
        pass
    def commodity(self,chose):#商品
        d1 = {}
        commodity = {
            '电脑':10000,
            '手机':5000,
            '照相机':8000,
            '数据线':2,
            '香蕉':4,
            '苹果':6,
            '葡萄':10
        }
        goods_list = {
            '电脑': {'price': 10000, 'num': 0, 'sum': 0},
            '手机': {'price': 5000, 'num': 0, 'sum': 0},
            '照相机': {'price': 8000, 'num': 0, 'sum': 0},
            '数据线': {'price': 20, 'num': 0, 'sum': 0},
            '香蕉': {'price': 4, 'num': 0, 'sum': 0},
            '苹果': {'price': 6, 'num': 0, 'sum': 0},
            '葡萄': {'price': 10, 'num': 0, 'sum': 0},
        }
        goods_list[chose]['num'] +=1
        goods_list[chose]['sum'] =goods_list[chose]['num']*goods_list[chose]['price']
        cdict[chose] =goods_list[chose]
        print(cdict)
        print(goods_list)
    def showTrolley(self):#展示商品
        chose = input(
            '''
            1.电脑：10000
            2.手机：5000
            3.照相机：8000
            4.数据线：20
            5.香蕉：4
            6.苹果：6
            7.葡萄：10
            8.查看购物车
            9.不买了
            '''
        )
        d = {
            "1":'电脑',
            "2":'手机',
            "3":'照相机',
            "4":'数据线',
            "5":'香蕉',
            "6":'苹果',
            "7":'葡萄'
        }
        return d[chose]
    def handle(self):
        while True:
            chose = self.showTrolley()
            if chose == '8':
                self.trolley()
            elif chose == '9':
                break
            else:
                self.commodity(chose)


a= Shiping()
print(a.handle())