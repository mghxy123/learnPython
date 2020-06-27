#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 链表作业.py
# Author: HuXianyong
# Date  : 2019/5/29 9:48


'''
当加入第一个node节点的时候,会有几个值,(这里的self.tail.next 其实就是node.next)
head = item = tail = Node(object element1 memory)
item = head = tail = Node(object element1  memory)
next = None
tail = item = head = Node(object element1  memory)

当加入第二个元素node节点的时候,next1值会改变,tail会向后漂移,head将会保留
新加入第二个元素后第一个节点变成了
head = item1 = Node(object element1  memory)
item1= head = Node(object element1  memory)
next = Node(object element2  memory)

第二个节点为:
item = tail =  Node(object element2  memory)
next =  Node(object element2  memory)
tail = item =  Node(object element2  memory)

当加入第三个元素的时候,tail.next继续为None item为新元素tail结束元素为新元素,
item = tail =  Node(object element3  memory)
next = None
tail = item =  Node(object element3  memory)
'''


class Node:
    def __init__(self,item,next=None):
        self.item = item #内容
        self.next = next #下一跳
    def __repr__(self):
        print(self.item,self.next)
        return str(self.item) #输出内容

class LinkedList:
    def __init__(self):
        self.head  = None  #头位置,头位置为None则说明没有元素
        self.tail  = None #记录最后一个链表的链表索引值,不用每次添加的时候都要去便利才能找到最后一个才能去添加的问题
        #这里的self.tail 记录的是上一个节点的tail,当我们输入的是1的时候这里记录的是None
        #当我们输入2的时候这里记录的是1一样
        #这里是初始化,我们直接调用的是append方法,所以,这里的self.tail记录的依旧是上一次的值

    def append(self,value):
        node = Node(value)
        #我们这里记录了tail的值,既是可以记录最后一个值,如果它为空,就说明这个列表为空.
        if self.tail is  None: #如果最后的索引值是None则说明是空链表
            self.head =node #这里的self.head(node)就是加入的第一个值,不是索引下标
            print('this is head',self.head)
        else:
            self.tail.next = node #这里指的是上一个节点的下一跳  #self.tail.next = node(value(last)).next = Node(value)
            print('this is self.tail.next',self.tail.next)
        self.tail = node
        print('this is self.tail',self.tail,node)
        return self
    def iternodes(self):
        current = self.head
        while current:
            yield current
            current = current.next
    def __add__(self, item):
        return self.append(item)
ll = LinkedList()
ll.append(1).append(2).append(3) +4+5
# print(ll)
for x in ll.iternodes():
    print(x)