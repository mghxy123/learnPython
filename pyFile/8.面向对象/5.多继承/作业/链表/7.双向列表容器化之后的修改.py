#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 双向列表容器化之后的修改.py
# Author: HuXianyong
# Date  : 2019/5/29 14:52

class Node:
    __slots__ = 'item next prev'.split()
    def __init__(self,item,next=None,prev = None):
        self.item = item
        self.next = next #是node instance
        self.prev = prev #这是node的实例
    def __repr__(self):
        # return str(self.item)
        return '{} <== {} ==> {}'.format(
            self.prev.item if self.prev else None,
            self.item ,
            self.next.item if self.next else None,#用于判断是否有值
        ) #这样是为了方便查看,只是输出
class LinkedList:
    def __init__(self):
        self._size = 0
        self.head  = None
        self.tail  = None #记录最后一个链表的值,不用每次添加的时候都要去便利才能找到最后一个才能去添加的问题

    def append(self,value):
        node = Node(value)
        #我们这里记录了tail的值,既是可以记录最后一个值,如果它为空,就说明这个列表为空.
        if self.tail is  None:
            self.head =node
        else:
            self.tail.next = node # self.tail.next = Node(value).next =None
            node.prev = self.tail
        self.tail = node #self.tail = Node(value) = Node(element) = element(object)
        self._size += 1
        return self
    def iternodes(self,reverse=False):
        current = self.tail if reverse else self.head
        while current:
            yield current
            current = current.prev if reverse else  current.next
    def __add__(self, item):
        self._size += 1
        return self.append(item)

    def insert(self,index,value):
        # if index <0:
        #     raise IndexError('Not negative')
        # current = None
        # for i,node in enumerate(self.iternodes()):
        #     if i == index:
        #         current = node
        #         break
        # else: #这里如果是空的容器,循环就属于正常执行的,执行完毕没有break,else正常执行,就等于可以直接append就成了
        #     self.append(value)
        #     return
        if index>= len(self):
            self.append(value)
        if index < -len(self):
            index = 0
        current = self[index]
        #找到了,容器非空
        newnode = Node(value)
        prev=current.prev
        next = current
        #开头插入
        if prev is None: # index =0 self.head == current
            self.head  = newnode

        else: #非开头
            newnode.prev = prev
            prev.next = newnode
        newnode.next = next
        next.prev = newnode
    def remove(self,index):
        if self.tail is None:
            raise Exception('empty')
        # if index <0:
        #     raise IndexError('Not negative')
        # current = None
        # for i,node in enumerate(self.iternodes()):
        #     if i == index:
        #         current = node
        #         break
        # else:
        #     raise IndexError('out od index')

        current = self[index] #这里会去getitem,会去自动的去判断index的范围

        prev =current.prev
        next = current.next
        #只有一份元素
        if prev is None and next is None:#self.head ==self.tail:
            self.head = None
            self.tail = None
        #有两个元素 移除头
        elif prev is None:
            self.head = next
            next.prec = None
        #两个元素,移除尾巴
        elif next is None:
            self.tail = prev
            prev.next = None
        else: #中间
            prev.next = next
            next.prev = prev
        del current
        self._size -=1
    def pop(self):
        if self.tail is None:
            raise Exception('empty')
        # only one 把内容取走,把开头结尾都改为None
        node = self.tail
        prev = node.prev
        if  node.prev is None:#self.head.next  is None:
            self.head =None
            self.tail =None
        else:
            prev.next = Node
            self.tail = prev
        value = node.item
        return value


    #容器相关
    def __len__(self):
        return self._size
    size = property(lambda self:self._size)

    def __getitem__(self, index):
        if index >=len(self) or index <-len(self):
            raise IndexError('out of index {}'.format(index))
        # for i,node in enumerate(self.iternodes()): #index >=0
        #     if i ==index:
        #         return node.item
        reverse = True if index  <0 else False
        start =1 if index <0 else 0
        for i,node in enumerate(self.iternodes(reverse=reverse),start): #index >=0
            if i ==abs(index):
                return node

    # 改
    def __setitem__(self, index, value):
        self[index].item = value

    def __reversed__(self):  #此魔术方法不可实现,但是要使用reversed内建函数必须要有__len__和__getitem__
        # return 1
        yield from self.iternodes(True)
        # return self.iternodes(True)
    __iter__ = iternodes

    def __contains__(self, item):
        print(item,'~~~~~~~~~~~~~')
        current = self.head
        while current:
            if item == current.item:
                return True
            current = current.next
        return False
ll = LinkedList()
ll.append(1).append(2).append(4) +3+6
ll.insert(0,'100')
for x in ll.iternodes():
    print(x)
print()
# ll.pop()
# ll.pop()
# ll.pop()
# ll.pop()
for x in ll.iternodes(reverse=True):
    print(x)
print(ll[1])
print(len(ll))
print()
for i in ll:
    print(i)

print()
for i in reversed(ll):
    print(i)
print(2 in ll)
ll[0]  = 'hello'
print(ll[0])