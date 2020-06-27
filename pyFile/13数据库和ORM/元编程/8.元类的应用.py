#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 8.元类的应用.py
# Author: HuXianyong
# Date  : 2019/6/30 23:54


class Column:
    def __init__(self,fieldname = None, pk = False, nullable = False):
        self.fieldname = fieldname
        self.pk = pk
        self.nullable = nullable

    def __repr__(self):
        return "<{} {}>".format(
            __class__.__name__,
            self.fieldname
        )

class ModeMeta(type):
    def __new__(cls,name, bases, attrs:dict):
        print(cls)
        print(name, bases, attrs)

        if '__tablename__' not in attrs:
            attrs['__tablename__'] = name.lower() # 添加表名

        primarykey = []
        for k,v in attrs.items():
            if isinstance(v,Column):
                if v.fieldname is None or v.fieldname.strip() == '':
                    v.fieldname = k
                if v.pk:
                    primarykey.append(v)
        attrs['__primarykey__'] = primarykey
        return super().__new__(cls,name, bases, attrs)

class Base(metaclass=ModeMeta):
    '''从ModeMeta继承的类的类型都是ModeMeta'''

class Student(Base):
    id = Column(pk=True,nullable=False)
    name = Column('username',nullable=False)
    age = Column()
print('-'*30)
print(Student.__dict__)
