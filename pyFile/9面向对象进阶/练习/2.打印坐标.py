#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 2.打印坐标.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/16 0016

'''
2、打印坐标
    使用上一题的类，随机生成20个数字，两两配对形成二维坐标，把这些坐标组织起来，并打印输出
'''

from random import randint
class RandNum:
    def __init__(self,num,start,end):
        self.num = num
        self.start = start
        self.end = end

    def randNum(self):
        numList = [randint(self.start,self.end-1) for i in range(self.num)]
        return numList


class Coordinate:
    def __init__(self,num,start,end):
        self.num = num
        self.start = start
        self.end = end
    def coordinate(self):
        a = RandNum(self.num, self.start, self.end)
        nlist = a.randNum()
        clist = []
        for i in range(0,self.num,2):
            clist.append([nlist[i],nlist[i+1]])
        print(clist)

        return clist
    def creatCoor(self):
        windows = [ [1]*self.end for i in range(self.end) ]
        # windows = [ [1]*10 for i in range(10) ]
        # windows = [[[1]*3]*3]
        # print(windows,sep='\n')
        return windows
    def showCoor(self):
        clist = self.coordinate()
        windows = self.creatCoor()
        # print(clist)
        for i,c in enumerate(clist):
            # print(i[0],i[1])
            windows[c[0]][c[1]]=i
        # print(windows,end='')
        for j in windows:
            print(j,sep='\n')
a = Coordinate(20,0,10)
a.showCoor()