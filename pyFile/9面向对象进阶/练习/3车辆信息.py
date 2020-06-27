#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 3车辆信息.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/16 0016

'''
3、车辆信息
    记录车辆的品牌mark、颜色color、价格price、速度speed等特征，并实现车辆信息管理，实现增加车辆，显示全部车信息烦人功能
'''
carDict = {}
class CarInfo:
    def __init__(self):
        pass
    def addCarInfo(self,mark,color,price,speed):
        carInfo = {}
        carInfo['mark'] = mark
        carInfo['color'] = color
        carInfo['price'] = price
        carInfo['speed'] = speed
        carDict[mark] = carInfo
        return carInfo
    def showCarInfo(self):
        print(carDict)
a = CarInfo()
a.addCarInfo('雪佛兰','blace',1000000,'200KM/H')
a.addCarInfo('雪佛兰1','blace',1000000,'200KM/H')
a.addCarInfo('雪佛兰2','blace',1000000,'200KM/H')
a.addCarInfo('雪佛兰3','blace',1000000,'200KM/H')
a.showCarInfo()