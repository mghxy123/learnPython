#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 4.事务的提交方法.py
# Author: HuXianyong
# Date  : 2019/6/26 16:20


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


engine = create_engine(connstr)
                       # ,echo=True)


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
        return "tableName = {} id={} name={} age = {}".format(
            self.__class__.__name__,
            self.id,
            self.name,
            self.age
        )

# print(Student)
# print(repr(Student.__tablename__))
# print(repr(Student.__table__))


# # 删除与创建一般都是很少用,一般都是创建好了,我们直接通过sqlalchemy去增删改查,并不会直接去创建或删除表.
# # 删除engine库中,在这上面定义的所有类的表
Base.metadata.drop_all(engine) #里面必须要放engine
# 创建engine库中,在这上面定义的所有类的表
Base.metadata.create_all(engine)



###################################################################
# 建立会话session
Session = sessionmaker(bind=engine) # 绑定使用这个引擎来做会话
session = Session()
# session = sessionmaker(bind=engine)() # 也可以写成这样

#构造时传入,这会是增的方法
student = Student(name='tom')
student.age = 20 # 属性赋值
print(student)

# add 方法用于实例的修改
session.add(student)

# commit用于事务的提交
session.commit()
print('this is add commit ~~~~~~~~~~~~~~~~~~~~')

try:
    #这里会报错,'Student' object is not iterable
    session.add_all(student)  # add_all是需要提交的是一个可迭代对象.
    session.commit()
    print('this is add all commit **************')
except Exception as e:
    print(e)
    session.rollback()
    print('I am rollback')

    student.name = 'jerry'
    session.add_all([student]) #像这样就能提交上去了
    # 但是这里提交上去的是update,会把之前的数据更新了

    session.commit()
    student.name = 'rose'
    student.age = 29
    session.add(student)
    session.commit()
# 不官几次add都是都是update方法,数据库上永远只会有一条记录,如果想要是增,那么就需要重新在构造一次
