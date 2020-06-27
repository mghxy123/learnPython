#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 4.作业.py
# Author: HuXianyong
# Date  : 2019/6/27 16:14

'''
作业
使用sqlalchemy
10009号员工的工号,姓名,所有的头衔title
10010号员工的工号,姓名,所有部门名称


'''

import enum
from sqlalchemy import create_engine,Column,String,Integer,ForeignKey,Date,Enum
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy.ext.declarative import declarative_base

##############################################################
# engine
PASSWORD = 'test'
USER = 'test'
PORT = 3306
DBNAME = 'test'
HOST = '192.168.18.181'
DBMETHED = 'mysql+pymysql'
connstr = "{}://{}:{}@{}:{}/{}".format(
    DBMETHED,
    USER,
    PASSWORD,
    HOST,
    PORT,
    DBNAME

)

engine = create_engine(connstr,echo=True)

###############################################
# session
session = sessionmaker(bind=engine)()


################################################
# tables
class Gender(enum.Enum):
    F = 'F'
    M = 'M'

Base = declarative_base()

class Department(Base):
    __tablename__ = 'departments'

    dept_no = Column(String(4),primary_key=True,nullable=False)
    dept_name = Column(String(40),nullable=False,unique=True)

    def __repr__(self):
        return "{} no = {} name = {}".format(
            type(self).__name__,
            self.dept_no,
            self.dept_name
        )

class Dept_emp(Base):
    __tablename__ = 'dept_emp'

    emp_no = Column(Integer,ForeignKey('employees.emp_no',ondelete='CASCADE'),primary_key=True,nullable=False)
    dept_no = Column(String(4),ForeignKey('departments.dept_no',ondelete='CASCADE'),primary_key=True,nullable=False)
    from_date = Column(Date,nullable=False)
    to_date = Column(Date,nullable=False)

    departments = relationship('Department') # 返回的是单数的换是一个对象,返回的是多个,就是一个列表.
    # relationship 也是惰性的,不需要就不会主动的去查询,
    def __repr__(self):
        return "{} empno = {} deptno = {} departhment = {}".format(
        # return "{} empno = {} deptno = {}".format(
            type(self).__name__,
            self.dept_no,
            self.dept_no,
            self.departments
        )

class Employees(Base):
    __tablename__ = 'employees'

    emp_no = Column(Integer,primary_key=True,nullable=False)
    birth_date = Column(Date,nullable=False)
    first_name = Column(String(14),nullable=False)
    last_name = Column(String(16),nullable=False)
    gender = Column(Enum(Gender),nullable=False)
    hire_date = Column(Date,nullable=False)

    dept_emp = relationship('Dept_emp')
    titles = relationship('Titles')
    def __repr__(self):
        return "{} no = {} name = {} {} genger = {} dept = {}".format(
            self.__class__.__name__,
            self.emp_no,
            self.first_name,
            self.last_name,
            self.gender.value,
            self.dept_emp
        )

class Titles(Base):
    __tablename__ = 'titles'

    emp_no = Column(Integer,ForeignKey('employees.emp_no',ondelete='CASCADE'),primary_key=True,nullable=False)
    title = Column(String(50),primary_key=True,nullable=False)
    from_date = Column(Date,primary_key=True,nullable=False)
    to_date = Column(Date,nullable=False)
    employees = relationship('Employees')

    def __repr__(self):
        return "{} empno = {} deptno = {} employees = {}".format(
            type(self).__name__,
            self.emp_no,
            self.title,
            self.from_date,
            self.to_date,
            self.employees

        )

########################################
# 开始查询第一个

# result = session.query(Employees.emp_no,Employees.first_name,Employees.last_name,Titles.title).join(Titles,(Employees.emp_no == Titles.emp_no)).all()
# print(result)
# result = session.query(Employees.emp_no,Employees.last_name,Titles.title).join(Employees,(Employees.emp_no == Titles.emp_no)).filter(Employees.emp_no == 10009).all()
# print(result)
#
# result =session.query(Employees).get(10009)
# print(result.emp_no, result.last_name, [t.title for t in result.titles]) # 这样的查询是把三个title都和在一起查出一条信息,上面的两个查询时查出三条记录,看需要选择需要的查询语句
# # 上面的两句查询是返回的我们需要的数据,下面的是整个的都拿过来了在进行过滤,

############################################
# 第二个查询
# result = session.query(Employees).join(Dept_emp,(Employees.emp_no == Dept_emp.emp_no)).filter(Employees.emp_no == 10010).all()

# result =  session.query(Employees,Dept_emp,Department).filter((Employees.emp_no == Dept_emp.emp_no) & (Dept_emp.dept_no == Department.dept_no)).filter(Employees.emp_no == 10010).all()
#
# result = session.query(Employees).join(Dept_emp,(Employees.emp_no == Dept_emp.emp_no)).join(Department,(Dept_emp.dept_no == Department.dept_no)).filter(Employees.emp_no == 10010).all()
# result = session\
#     .query(Employees.emp_no, Employees.last_name, Employees.first_name, Department.dept_name)\
#     .join(Dept_emp, (Employees.emp_no == Dept_emp.emp_no))\
#     .join(Department, (Dept_emp.dept_no == Department.dept_no))\
#     .filter(Employees.emp_no == 10010)\
#     .all()
#
# print(result)
