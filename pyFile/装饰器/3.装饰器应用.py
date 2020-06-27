#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 3.装饰器应用.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/4/22 0022

#由之前的两个练习我们已经了解了装饰器的作用了用法，但是如果我们
#像是之前的例子一样的应用的环就打不到我们的想要的效果了，
#应为我们要把装饰器写在，实际代码的后面，而且调用的也是装饰器的函数，和我们原来
#想的差的太多，下面就看看实际的装饰器

#我们把装饰器定义在一个文件里面或者是，定义在被装饰函数的前面
#然后调用被装饰函数来达到我们想要的结果

def logger(fn):
    def inner(*args,**kwargs):
        print('3这是一个求和函数{} | {}'.format(args, kwargs))
        print('4这个是fn的函数', fn)
        result = fn(*args,**kwargs)#这里的*args是实参参数的解构
        print('6这个是add的函数',add)
        print('7这个是fn的函数',fn)
        print('8这个是result',inner)
        return result
    print('2这个是logger',logger)
    return inner

@logger
def add(x,y):
    print('5这个是add的函数',add.__name__)
    return x+y
print('1首先打印add的函数',add)
print(add(6,7))

"""
@logger 
这样的装饰器叫做无参装饰器，
他其实是一个单参函数，
返回值也是一个函数

如果不按装饰器的用发来的换也可以改成
logger(add)(6,7)
这样调用也行
"""


#这里的输出顺序是21345678
#那是因为装饰器在调用的时候先进行了加载，也就是在@logger哪里被调用了一次，然后把inner的地址指向了add函数的地址，
#，由于没有人去调用inner函数而停止，这也就是为什么先是2线输出，然后才到1线输出的原因了

#这里我们的add 已经不是add函数的add了