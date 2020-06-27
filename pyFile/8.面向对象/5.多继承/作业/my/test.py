#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : test.py
# Author: HuXianyong
# Date  : 2019/5/30 15:46


class Node:
    def __init__(self,item,next=None,prev=None):
        self.item = item #记录元素
        self.next = next #记录下一跳节点
        self.prev = prev #双向链表,记录上一个链表的位置
    def __repr__(self):
        return '{} <== {} ==> {}'.format(
            self.prev.item if self.prev else None,
            self.item,
            self.next.item if self.next else None,
        )

class LinkedList:
    def __init__(self):
        self.head= None  #头位置,头位置为None则说明没有元素
        self.tail = None #记录最后一个链表的链表索引值,不用每次添加的时候都要去便利才能找到最后一个才能去添加的问题
    def append(self,value):
        node = Node(value) #实例化节点
        if self.tail is None:
            self.head = node#这里的self.head(node)就是加入的第一个值,不是索引下标
        else:
            self.tail.next = node
            node.prev = self.tail
        self.tail = node
        return self
    def iternode(self):
        current = self.head
        while current:
            yield current
            current = current.next
    def __add__(self, other):
        return self.append(other)
    def insert(self,index,value):
        if index < 0:
            raise IndexError('out of index {}'.format(index))
        current = None
        for i ,node in enumerate(self.iternode()):
            if i == index:
                current = node
                break
        else:
            self.append(value)
            return self
        newnode = Node(value)
        prev = current.prev
        next = current
        if prev is None:
            self.head= newnode
        else:
            newnode.prev = prev
            prev.next = newnode
        newnode.next = next
        next.prev = newnode
ll = LinkedList()
ll.append(1).append(2).append(4) +3+6
ll.insert(0,'100')
for x in ll.iternode():
    print(x)