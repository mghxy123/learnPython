#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 1.简单条件查询filter.py
# Author: HuXianyong
# Date  : 2019/6/27 9:49
import enum

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column,Integer,String,create_engine,Sequence,Date,Enum



###################################################################
# 建立引擎engine
USER = 'test'
PASSWORD = 'test'
HOST = '192.168.18.181'
PORT = 3306
DATABASE = 'test'

connstr = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(
    USER,
    PASSWORD,
    HOST,
    PORT,
    DATABASE
)


engine = create_engine(connstr,echo=True)

###################################################################
# 建立一个枚举类
class Cenum(enum.Enum):
    M = 'M'
    F = 'F'

###################################################################
# 建立表和类关系
#创建基类,基类的作用就是用于和表关系做一一的对应的,既是mapping
Base = declarative_base()

# 创建实体类,既是表中的关系,
class Employees(Base):
    # 指定表名
    __tablename__ = 'employees'

    emp_no = Column(Integer,primary_key=True,nullable=False)
    birth_date = Column(Date,nullable=False)
    first_name = Column(String(14),nullable=False)
    last_name = Column(String(16),nullable=False)
    gender = Column(Enum(Cenum),nullable=False)
    hire_date = Column(Date,nullable=False)

    def __repr__(self):
        return "{} no = {} name = {} {} genger = {}".format(
            self.__class__.__name__,
            self.emp_no,
            self.first_name,
            self.last_name,
            self.gender.value
        )
###################################################################
# 建立会话session
Session = sessionmaker(bind=engine) # 绑定使用这个引擎来做会话
session = Session()
# session = sessionmaker(bind=engine)() # 也可以写成这样

###################################################################
# 打印会话
def show(emps):
    for x in emps:
        print(x)
    print('~'*30,'\n')

###################################################################
###################################################################
###################################################################
# 简单条件查询
emps = session.query(Employees).filter(Employees.emp_no > 10015)
# 相当于 selecrt * from employees where emp_no > 10015;

# emps = session.query(Employees)
# 相当于 selecrt * from employees
show(emps)