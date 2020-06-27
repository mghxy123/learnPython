#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 2.双向链表新增insert方法.py
# Author: HuXianyong
# Date  : 2019/5/30 14:21


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
    def __init__(self,item,next=None,prev=None):
        self.item = item #记录元素
        self.next = next #记录下一跳节点
        self.prev = prev #双向链表,记录上一个链表的位置

    #为了输出 我们可以看到的结果:
    def __repr__(self):
        return '{} <== {} ==> {}'.format(
            self.prev.item if self.prev else None,
            self.item,
            self.next.item if self.next else None
        )

class LinkedList:
    def __init__(self):
        self.head= None  #头位置,头位置为None则说明没有元素
        self.tail = None #记录最后一个链表的链表索引值,不用每次添加的时候都要去便利才能找到最后一个才能去添加的问题
        #这里的self.tail 记录的是上一个节点的tail,当我们输入的是1的时候这里记录的是None
        #当我们输入2的时候这里记录的是1一样
        #这里是初始化,我们直接调用的是append方法,所以,这里的self.tail记录的依旧是上一次的值

    def append(self,value):
        #添加链表前需要,实例化一个节点,来进行赋值
        node = Node(value) #实例化节点
        #添加链表,首先判断链表是否为空,
        # 空列表时 head= tail = None
        #添加元素后head = value = tail = Node(value) = node
        if self.head == None:
            self.head = node#这里的self.head(node)就是加入的第一个值,不是索引下标
            # self.tail = node
        #当链表不为空时向后添加,既是向后添加,添加后的值为
        # self.tail.next = Node(last(value)).next = node
        #要知道self.tail值的改变是不应为append的改变而改变了,只是再重新赋值之后才会改变的
        # self.tail = node #现在的结尾部分被重新赋值
        else: #这里指的是上一个节点的下一跳  #self.tail.next = node(value(last)).next = Node(value)
            self.tail.next = node #如果添加的是最后一位,next就是默认值既是None
            node.prev = self.tail #它的上一个节点等于它记录的上个元素的职位#node.prev = node(value(last))
            # self.tail = node
        # if和slse有公共部分self.tail = node可以直接提出来,
        self.tail = node
        # 单列表为了实现可以链式编程就需要在append的时候返回一个实例,
        return self  # 这是为了实现链式编程,直接append
    def iternode(self):
        #这里的迭代可以使用我们定义好的方法来做,因为每个node节点都有next可以调用下一个节点,因此我们可以利用这一特性来做迭代
        #因为我们不知道需要迭代的个数有多少个,因此只能使用yield配合while循环来做,然后使用节点的下一个来重赋值,知道current为None,while循环结束
        current = self.head
        while current:
            yield current
            current = current.next

    #如果要实现能直接与数字相加就需要修改add方法直接把数字传入append方法内,来达到效果
    def __add__(self, other):
        return self.append(other)


    #插入功能insert,第一步先判断我们插入的索引是否满足,目前我们先做正索引的问题
    #第二我们插入链表的位置分为自己种情况?
    #1.零元素时插入,
    #2.两个元素时开头插入
    #3.两个元素时结尾插入
    #4.三个以上的元素的中间插入
    # 分析下上面四种情况下我们该如何插入元素

    # 零元素时插入一个数据子让就等于和我们的append插入元素一样了
    # 两个元素时尾部插入,也就自然是append方法了
    # 两个元素时,开头插入的方法需要我们来写
    # 三个以上的元素中间插入时他们的开头和结尾都是需要变化的,这个改动也需要我们通过代码来实现
    # 新增的元素的地址next和prev分别指向上下两个元素,上下两个元素的地址不用变化,这样就达到了效果

    #代码实现:
    def insert(self,index,value):
        if index < 0:#我们目前考虑的是正索引的问题,负索引先不做,这里先抛异常
            raise IndexError('out of index {}'.format(index))
        #先定义个现在的坐标为None
        current = None
        #便利循环去找index的插入位置
        for i ,node in enumerate(self.iternode()):
            if i == index:
                current = node
                break
        else:
            self.append(value) #当整个链表都便利完毕的时候依旧没有找到,就说明了,这个index大于了链表的长度了,这样就只需要在后面append就好了
            #当这个是零长度的时候肯定也是append,然后两个元素在后面新增也是append,因此我们要考虑的也就只有在中间插入的情况了.
            return self
        # 找到了,容器非空
        newnode = Node(value)
        prev = current.prev
        next = current
        if prev is None: #头部增加
            self.head= newnode
        else: #中间增加
            newnode.prev = prev
            prev.next = newnode
        newnode.next = next
        next.prev = newnode
ll = LinkedList()
ll.append(1)
ll.append(2).append(3) +4 +5
ll.insert(0,'10')
for i in ll.iternode():
    print(i)