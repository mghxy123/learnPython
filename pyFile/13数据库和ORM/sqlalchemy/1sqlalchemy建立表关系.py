#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : test.py
# Author: HuXianyong
# Date  : 2019/6/26 15:11

from sqlalchemy import Column,Integer,String,create_engine,Sequence

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Student(Base):
    # 指定表名
    __tablename__ = 'student'

    # 定义类属性对应字段.

    id = Column(Integer, primary_key=True, autoincrement=True)
    # id = Column(Integer,Sequence('user_id'),primary_key=True) #Sequence这个也是自增字段
    name = Column(String(64), nullable=False)
    age = Column(Integer)

    # 第一参数是字段名,如果和属性名不一致,一定要指定
    # age = Column('age',Integer)

    def __repr__(self):
        return "{} id={} name = {}".format(
            self.__class__.__name__,
            self.id,
            self.name
        )


print(Student)
print(repr(Student.__tablename__))
print(repr(Student.__table__))  # 可以打印出表关系

student = Student(name='tom')
print(student.name)
student.age = 20
print(student.age)