#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 3.关联查询.py
# Author: HuXianyong
# Date  : 2019/6/27 14:03


from sqlalchemy import create_engine,Column,String,Integer,ForeignKey,Date,Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import sqlalchemy
import enum


#########################################################################
# engine
DB = "mysql+pymysql"
USER = 'test'
PASSWORD = 'test'
PORT = 3306
DATABASE = 'test'
HOST = '192.168.18.181'
connstr = "{}://{}:{}@{}:{}/{}".format(
    DB,
    USER,
    PASSWORD,
    HOST,
    PORT,
    DATABASE
)
engine = create_engine(connstr,echo=True)
print(engine)
#########################################################################
# session
session = sessionmaker(bind=engine)()
# Session = sessionmaker(bind=engine,echo=True)
# session = Session()
#########################################################################
# tables

class Gender(enum.Enum):
    F = 'F'
    M = 'M'

Base = declarative_base()

class Department(Base):
    __tablename__ = 'department'

    dept_no = Column(String(4),primary_key=True,nullable=False)
    dept_name = Column(String(40),nullable=False,unique=True)

    def __repr__(self):
        return "{} no = {} name = {}".format(
            type(self).__name__,
            self.dept_no,
            self.dept_name
        )


# class Employees(Base):
#     __tablename__ = 'employees'
#
#     emp_no = Column(Integer,primary_key=True,nullable=False)
#     birth_date = Column(Date,nullable=False)
#     first_name = Column(String(14),nullable=False)
#     last_name = Column(String(16),nullable=False)
#     gender = Column(Enum(Gender),nullable=False)
#     hire_date = Column(Date,nullable=False)
#     def __repr__(self):
#         return "{} no = {} name = {} {} genger = {}".format(
#             self.__class__.__name__,
#             self.emp_no,
#             self.first_name,
#             self.last_name,
#             self.gender.value
#         )


class Dept_emp(Base):
    __tablename__ = 'dept_emp'

    emp_no = Column(Integer,ForeignKey('employees.emp_no',ondelete='CASCADE'),primary_key=True,nullable=False)
    dept_no = Column(String(4),ForeignKey('department.dept_no',ondelete='CASCADE'),primary_key=True,nullable=False)
    from_date = Column(Date,nullable=False)
    to_date = Column(Date,nullable=False)
    def __repr__(self):
        return "{} empno = {} deptno = {}".format(
            type(self).__name__,
            self.dept_no,
            self.dept_no
        )
#########################################################################
# 需求:
# 查询10010员工的所在部门编号以及员工信息,


#########################################################################
# 使用隐式连接
'''
sql 语句为:
SELECT	* FROM	employees,	dept_emp WHERE	employees.emp_no = dept_emp.emp_no AND dept_emp.emp_no = 10010
'''


# query = session.query(Dept_emp,Employees).filter((Dept_emp.emp_no == 10010) & (Employees.emp_no == Dept_emp.emp_no))
# for i in  query:
#     print(i)
# print(query.all())

# reslut = session.query(Dept_emp,Employees).filter((Dept_emp.emp_no == 10010) & (Employees.emp_no == Dept_emp.emp_no)).all()
# print(reslut)

#########################################################################
# 使用join方法
'''
sql语句为
select * from employees join dept_emp on employees.emp_no = dept_emp.emp_no where dept_emp.emp_no = 10010
'''

# reslut = session.query(Dept_emp).join(Employees,(Employees.emp_no == Dept_emp.emp_no)).filter(Dept_emp.emp_no == 10010).all()
# print(reslut)

'''
这两种写法,返回都只有一行数据,为什么?
它们生成的sql语句是一样的,执行该sql语句返回的确实是2行记录,可为何Python中只有一个元素?
原因就在于,query(Employees)这个只能返回一个实体到对象中去,为了解决这个问题,需要修改实体类Employees,增加属性用来存放这个部门信息

'''



class Employees1(Base):
    __tablename__ = 'employees'

    emp_no = Column(Integer,primary_key=True,nullable=False)
    birth_date = Column(Date,nullable=False)
    first_name = Column(String(14),nullable=False)
    last_name = Column(String(16),nullable=False)
    gender = Column(Enum(Gender),nullable=False)
    hire_date = Column(Date,nullable=False)

    departments = relationship('Dept_emp')

    def __repr__(self):
        return "{} no = {} name = {} {} genger = {} dept = {}".format(
            self.__class__.__name__,
            self.emp_no,
            self.first_name,
            self.last_name,
            self.gender.value,
            self.departments
        )


####################################################
# 使用join方法,


###########方法一
# reslut = session.query(Employees1).join(Dept_emp).filter(Employees1.emp_no == Dept_emp.emp_no).filter(Dept_emp.emp_no == 10010).all()
# print(reslut)

###########方法二
# reslut = session.query(Employees1).join(Dept_emp,(Employees1.emp_no == Dept_emp.emp_no)).filter(Dept_emp.emp_no == 10010).all()
# print(reslut)

###########方法三
reslut = session.query(Employees1).join(Dept_emp,(Employees1.emp_no == Dept_emp.emp_no) & (Dept_emp.emp_no == 10010)).all()
print(reslut)




