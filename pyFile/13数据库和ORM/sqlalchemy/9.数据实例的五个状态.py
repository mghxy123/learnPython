#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 9.数据实例的五个状态.py
# Author: HuXianyong
# Date  : 2019/6/26 17:45


import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String,Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


###########################################
# engine
connstr = "{}://{}:{}@{}:{}/{}".format(
    'mysql+pymysql', # 选用什么方言
    'test', # 数据库名
    'test', # 密码
    '192.168.18.181', #数据库主机
    3306,#端口
    'test'#数据库
)
engine = create_engine(connstr,echo=True)
# engine = create_engine(connstr)

#################################################
# session

# Session = sessionmaker(bind=engine)
# session = Session()
session = sessionmaker(bind=engine)()

####################################################
# table Class

Base = declarative_base()

class Student(Base):
    __tablename__ = 'student'

    # id = Column(Integer,primary_key=True,autoincrement=True)
    id = Column(Integer,Sequence('user_id'),primary_key=True)
    name = Column(String(64),nullable=True)
    age = Column(Integer)
    # 第一参数是字段名,如果和属性名不一致,则一定要指定.
    # age = Column('age',Integer)

    def __repr__(self):
        return "className = {} id={} name={} age = {}".format(
            self.__class__.__name__,
            self.id,
            self.name,
            self.age
        )


###########################################################
# 检查数据的各个状态

# 最开始时候的状态
from sqlalchemy.orm.state import InstanceState

def getstate(instance,i ):
    inp:InstanceState = sqlalchemy.inspect(instance)
    states = "{}: key = {}, attached = {}, transient = {}, " \
             "pending = {}, \n persistent = {},deleted = {}, detached = {}".format(
        i,
        inp.session_id,
        inp._attached,
        inp.transient,
        inp.pending,
        inp.persistent,
        inp.deleted,
        inp.detached
    )
    print(states, end='\n----------------------------------\n')

student = session.query(Student).get(5)
getstate(student,1) #persistent


## 修改之时的各个状态

try:

    student = Student(id=2, name='sam', age=30)
    getstate(student,2) #transient 这里没有和数据库有任何的交集所以出了transient为True之外的所有状态都是False


    student = Student(name='sam',age=30)
    getstate(student,3)

    session.add(student)
    getstate(student,4)

    # session.delete(student)
    # getstate(student,5)

    session.commit()
    getstate(student,5)

except Exception as e:
    session.rollback()
    print(e,'~~~~~~~~~~~~~~~~~~~~~~~~~')




'''
1: key = 1, attached = True, transient = False, pending = False, 
 persistent = True,deleted = False, detached = False
 persistent 就是key不为None,附加的,且不是删除的,有sessionid
 查询属于挂上了所以attached为True
----------------------------------
2: key = None, attached = False, transient = True, pending = False, 
 persistent = False,deleted = False, detached = False
 这是一个临时数据所以就无所谓挂上和分离了,所以attached和detached都为False
----------------------------------
3: key = None, attached = False, transient = True, pending = False, 
 persistent = False,deleted = False, detached = False
 这个同上
----------------------------------
4: key = 1, attached = True, transient = False, pending = True, 
 persistent = False,deleted = False, detached = False
----------------------------------
5: key = 1, attached = True, transient = False, pending = False, 
persistent = True,deleted = False, detached = False
'''

# 查看删除状态
student = session.query(Student).get(8)
getstate(student,10)

try:
    session.delete(student)
    getstate(student,11)

    session.flush()
    getstate(student,12)

    session.commit()
    getstate(student,13)

except Exception as e:
    session.rollback()
    print(e,'~~~~~~~~~~~~~~~~~~~~~~~~~')



