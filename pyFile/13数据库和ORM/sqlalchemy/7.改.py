#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 7.改.py
# Author: HuXianyong
# Date  : 2019/6/26 16:52



from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column,Integer,String,create_engine,Sequence


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

engine = create_engine(connstr,echo=False)


###################################################################
# 建立表和类关系
#创建基类,基类的作用就是用于和表关系做一一的对应的,既是mapping
Base = declarative_base()

# 创建实体类,既是表中的关系,
class Student(Base):
    # 指定表名
    __tablename__ = 'student'

    # 定义类属性和表中关系对应
    # id = Column(Integer,primary_key=True, autoincrement=True)
    id = Column(Integer,Sequence('user_id'),primary_key=True)
    name = Column(String(64), nullable=False)
    age = Column(Integer)

    def __repr__(self):
        return "className = {} id={} name={} age = {}".format(
            self.__class__.__name__,
            self.id,
            self.name,
            self.age
        )

# # 删除与创建一般都是很少用,一般都是创建好了,我们直接通过sqlalchemy去增删改查,并不会直接去创建或删除表.
# # 删除engine库中,在这上面定义的所有类的表
Base.metadata.drop_all(engine) #里面必须要放engine
# 创建engine库中,在这上面定义的所有类的表
Base.metadata.create_all(engine)


###################################################################
# 建立会话session
session = sessionmaker(bind=engine)()



#######################################################################
# 数据库增
#构造时传入,这会是增的方法
student = Student(name='tom')
student.age = 20 # 属性赋值
print(student)

# add 方法用于实例的修改
session.add(student)

# commit用于事务的提交
session.commit()
print('this is add commit ~~~~~~~~~~~~~~~~~~~~')

# 新增第二条数据
student1 = Student(id = 5, name = 'Forand', age = 29)
session.add(student1)
session.commit()

# 新增第三条数据
student2 = Student(id = 7)
student2.name = 'rose'
student2.age = 19
session.add(student2)
session.commit()


###############################################
# 数据库查
# studentsInfo = session.query(Student) # 无条件,既是全部查询
# print(studentsInfo) #这里的输出无内容,是惰性的,除非我们要输出我们的结果
#
# for student in studentsInfo:
#     print(student)
#
# studentInfo = session.query(Student).get(7) # 通过主键查询
# print(studentInfo.name) #这里可以直接输出name

# query方法将实体类传入,返回类的可迭代对象,
# get方法使用主键查询,返回一条传入类的一个实例


#########################################################
# 数据库改方法
studentInfo = session.query(Student).get(5)
studentInfo.name = 'sam'
studentInfo.age = 20
session.add(studentInfo)
session.commit()
studentInfo = session.query(Student).get(5)
print(studentInfo)

# 想要修改数据,先要把数据查询回来才能先进性修改,不然实例会认为没有这个属性而报错
# 记住,只要想动数据,就得先查询,然后再去修改数据


################################################################
