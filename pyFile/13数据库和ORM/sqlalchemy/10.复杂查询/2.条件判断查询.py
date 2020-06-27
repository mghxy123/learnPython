#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 2.条件判断查询.py
# Author: HuXianyong
# Date  : 2019/6/27 10:42



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

###################################################################
# 条件查询
# 导入与和或模块
from sqlalchemy import and_,or_,not_

####################################
# and条件,方法有四种

# 使用and_函数
emps = session.query(Employees).filter(and_(Employees.emp_no > 10015, Employees.gender==Cenum.F))
show(emps)

# 使用逻辑运算符 &
emps = session.query(Employees).filter((Employees.emp_no > 10015) & (Employees.gender==Cenum.F))
show(emps)

# filter两个条件
emps = session.query(Employees).filter(Employees.emp_no > 10015,Employees.gender==Cenum.F)
show(emps)

# filter双重过滤
emps = session.query(Employees).filter(Employees.emp_no > 10015).filter(Employees.emp_no < 10019)
show(emps)

# 这上面的四个的作用都是and

####################################
# or条件有两种 or_ |
emps = session.query(Employees).filter(or_((Employees.emp_no == 10015),(Employees.emp_no == 10019)))
show(emps)

emps = session.query(Employees).filter((Employees.emp_no == 10015) | (Employees.emp_no == 10019))
show(emps)

####################################
# not条件有两种
emps = session.query(Employees).filter(not_(Employees.emp_no <10015)) #不小于,既是大于
show(emps)

# 使用逻辑运算符
emps = session.query(Employees).filter(~(Employees.emp_no <10015)) #不小于,既是大于
show(emps)

# 总之,与或非的运算符& | ~ 一定要在表达式上面加上括号

empl = [10010,10015,10018]

####################################
# in
emps = session.query(Employees).filter(Employees.emp_no.in_(empl))
show(emps)

# not in
emps = session.query(Employees).filter(~(Employees.emp_no.in_(empl)))
# emps = session.query(Employees).filter(Employees.emp_no.notin_(empl))
show(emps)

####################################
# like
emps = session.query(Employees).filter(Employees.last_name.like('B%'))
show(emps)

# not like
emps = session.query(Employees).filter(Employees.last_name.notlike('B%'))
show(emps)
# like 可以忽略大小写匹配


##########################################################################
# 排序

# 升序
emps = session.query(Employees).filter(Employees.emp_no > 10010).order_by(Employees.emp_no)
emps1 = session.query(Employees).filter(Employees.emp_no > 10010).order_by(Employees.emp_no.asc())
show(emps)
show(emps1)

# 降序
emps = session.query(Employees).filter(Employees.emp_no > 10010).order_by(Employees.emp_no.desc())
show(emps)

# 多列排序 多列排序,靠左的排序高于靠右的.只有当左面出现相同的时候才会出现向右选择排序的结果出现.
# emps = session.query(Employees).filter(Employees.emp_no > 10010).order_by(Employees.emp_no.desc()).order_by(Employees.emp_no.asc())
emps = session.query(Employees).filter(Employees.emp_no > 10010).order_by(Employees.emp_no).order_by(Employees.last_name.desc())
print('last one')
show(emps)

###########################################################################
# 分页

emps = session.query(Employees).limit(4)
show(emps)
emps = session.query(Employees).limit(4).offset(15)
show(emps)

###########################################################################
# 消费者方法
# 消费者方法调用后,Query对象(可迭代)就转化成了一个容器.

#总行数
emps = session.query(Employees) # select * from employees;
print(emps)
print(len(list(emps))) # 查询得到结果及,转化为list,取list长度
print(emps.count()) # 使用聚合函数count(*)的查询

# 取所有数据
print(emps.all()) # 返回列表,查不到返回空列表

# 取行首
print(emps.first()) #返回首行,查不到返回None,等价于limit

# 取行未,有且只能有一行
# print(emps.one()) # 如果查询结果式多行的话就会抛异常
print(emps.limit(1).one())

# 删除delete by query
session.query(Employees).filter(Employees.emp_no > 10018).delete()
# session.commit() #提交删除

# first方法的本质上使用的是limit语句


###########################################################################
# 聚合函数
# count
from sqlalchemy import func

query = session.query(func.count(Employees.emp_no))

print(query.all()) # 列表中的一个元素
print(query.first()) #一个只有一个元素的元祖
print(query.one()) # 只能有一行返回,一个元组
print(query.scalar()) # 取one()的第一个元素

# max/min/avg
print(session.query(func.max(Employees.emp_no)).scalar())
print(session.query(func.min(Employees.emp_no)).scalar())
print(session.query(func.avg(Employees.emp_no)).scalar())


###########################################################################
# 分组
query = session.query(Employees.gender,func.count(Employees.emp_no)).group_by(Employees.gender).all()

for g,y in query:
    print(g.value,y)

print(query)