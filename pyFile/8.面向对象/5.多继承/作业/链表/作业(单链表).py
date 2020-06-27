#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 作业(链表).py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/21 0021


#单节点实现
class Node():
    """结点类"""
    def __init__(self,element):
        #存放元素数据
        self.elem=element
        #next是下一个节点的标识
        self.next=None

class SingleLinkList():
    def __init__(self, next=None):
        self.next = next

    def iterlink(self):
        # 遍历整个链表
        cur = self.next
        while cur != None:
            print(cur.elem)
            cur = cur.next
        print()

    def append(self,element):
    #在尾部添加一个节点
        node=Node(element)
        #若链表为空，直接将该节点作为链表的第一个元素
        if self.next==None:
            self.next=node
        else:
            cur = self.next
            while cur.next !=None:
                cur=cur.next
            cur.next=node
slnk=SingleLinkList()
slnk.append(1)
slnk.append(2)
slnk.append(3)
slnk.append(4)
slnk.append('a')
slnk.iterlink()