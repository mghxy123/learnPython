# ORM
---
ORM,对象关系映射,对象关系之间的映射,使用面向对象的方式来操作数据库.

```
关系模型和Python对象之间的映射
table ==>   表映射为类
row   ==>   行映射为实例
column ==>  字段映射为属性
```

举例  
有表student,字段为id int, name varchar, age int  
映射到Python为:  
```python
class Student:
    id = ?某类型字段
    name = ?某类型字段
    age = ?某类型字段

最终得到实例为
class Student:
    def __init(self):
        self.id = ?
        self.name = ?
        self.age = ?

```

# SQLALchemy  
---

SQLAlchemy是一个ORM框架  
## 安装
```shell
pip install sqlalchemy
```
## 文档
[官方文档http://docs.sqlalchemy.org/en/latest/](http://docs.sqlalchemy.org/en/latest/)
查看版本信息

```py
import sqlalchemy
print(sqlalchemy.__version__)

```

## 开发
---

SQLAlchemy内部使用的是连接池  

## 创建链接
---
数据库连接的事情,直接交给引擎  

创建引擎  
```python
dialect+driver://username:password@host:port/database

mysqldb的连接
mysql+pymysql://<user>:<password>@<host>[:<port>]/<dbname>
engine = sqlalchemy.create_engine("mysql+pymysql://test:test@192.168.18.181:3306/test")
我的这里数据库名,用户和密码,都是test

mysql连接
mysql+pymysql://<username>:<password>@<host>[:<port>]/<dbname>[?<options>]
engine = sqlalchemy.create_engine("mysql+pymysql://test:test@192.168.18.181:3306/test")
engine = sqlalchemy.create_engine("mysql+pymysql://test:test@192.168.18.181:3306/test",echo=True)

echo=True
引擎是否打印执行的语句,调试的时候开启方便调试.  

lazy connecting: 懒连接,创建引擎并不会马上连接数据库,知道让数据库执行任务的时候才开始连接.  
```

## Declare a Mapping创建映射
### 创建基类
```py
from sqlalchemy.ext.declarative import declarative_base
# 创建基类,便于实体类继承,sqlalchemy大量使用了元编程
```
### 创建实体类(创建表)
用sql语句创建student表
```sql
CREATE TABLE student (
	id INTEGER NOT NULL AUTO_INCREMENT, 
	name VARCHAR(64) NOT NULL, 
	age INTEGER, 
	PRIMARY KEY (id)
)


```
使用关系类创建表  
```py
from sqlalchemy import Column,Integer,String

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

# 查看表结构
print(Student)
print(repr(Student.__tablename__))
print(repr(Student.__table__))  # 可以打印出表关系
```

输出结果为:  

```py
# 显示结果
<class '__main__.Student'>
'student'
Table('student', MetaData(bind=None), Column('id', Integer(), table=<student>, primary_key=True, nullable=False), Column('name', String(length=64), table=<student>, nullable=False), Column('age', Integer(), table=<student>), schema=None)

```
`__tablename__`指定表名  
Column指定对应的字段,必须指定  

### 实例化
```py
student = Student(name='tom')
print(student.name)
student.age = 20
print(student.age)
```
输出结果为  
```py
tom
20
```

### 创建表
可以使用sqlalchemy来创建,删除表
```py
# 删除与创建一般都是很少用,一般都是创建好了,我们直接通过sqlalchemy去增删改查,并不会直接去创建或删除表.
# 删除engine库中,在这上面定义的所有类的表
Base.metadata.drop_all(engine) #里面必须要放engine
# 创建engine库中,在这上面定义的所有类的表
Base.metadata.create_all(engine)

```
生产环境很少用这样来创建表,都是在系统上线的时候由脚本生成.  
生成环境很少删除表,宁可废弃不用,也不删除  

### 创建会话session
在一个会话中操作数据库,会话建立在连接上,连接被引擎管理.  
当第一次使用数据库时,从引擎维护的连接池中获取一个连接来使用.  

```py
# 建立会话session
Session = sessionmaker(bind=engine) # 绑定使用这个引擎来做会话 # 工厂方法返回表
session = Session() 实例化
# 依然在第一次使用的时候连接数据库
# session = sessionmaker(bind=engine)() # 也可以写成这样
```
session对象线程不安全.所以不同线程应该使用不同的session对象.  
Session类和engine有一个就行了.  

### 创建engine
```py
from sqlalchemy import create_engine
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

```

### CRUD操作
---
#### 增
add():增加一个对象  
add_all(): 可迭代对象,元素是对象.  

```py
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
engine = create_engine(connstr,echo=True)

###################################################################
# 建立表和类关系
#创建基类,基类的作用就是用于和表关系做一一的对应的,既是mapping
Base = declarative_base()

# 创建实体类,既是表中的关系,
class Student(Base):
    # 指定表名
    __tablename__ = 'student'

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

```
add_all()方法不会提交成功的,不是因为他不对,二是student,student提交后,student的主键就有了值,所以,只要student没有修改过,就认为没有改动.如下,student变化了,就可以直接提交修改了.  

```py
    student.name = 'jerry' #修改
    session.add_all([student]) #像这样就能提交上去了
```

关闭echo后输出结果为:

```py
tableName = Student id=None name=tom age = 20
this is add commit ~~~~~~~~~~~~~~~~~~~~
'Student' object is not iterable
I am rollback

```

student逐渐没有纸,就是新增;主键有值,就找到主键对应的记录修改.

#### 简单查询
使用query()方法,返回一个Query对象.  
```py
###############################################
# 数据库查
studentsInfo = session.query(Student) # 无条件,既是全部查询
print(studentsInfo) #这里的输出无内容,是惰性的,除非我们要输出我们的结果

for student in studentsInfo:
    print(student)

studentInfo = session.query(Student).get(7) # 通过主键查询
print(studentInfo.name) #这里可以直接输出name

# query方法将实体类传入,返回类的可迭代对象,
# get方法使用主键查询,返回一条传入类的一个实例
```

关闭echo后输出结果为:

```py
className = Student id=None name=tom age = 20
this is add commit ~~~~~~~~~~~~~~~~~~~~
SELECT student.id AS student_id, student.name AS student_name, student.age AS student_age 
FROM student
className = Student id=1 name=tom age = 20
className = Student id=5 name=Forand age = 29
className = Student id=7 name=rose age = 19
rose

```
query方法讲实体类传入,返回的对象是可迭代的对象,这时候并不查询.迭代它就执行sql来查询数据库,封装数据到指定类的实例.  
get方法使用主键查询,返回一条传入类的一个实例.  

#### 改
```py
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

```
关闭echo后输出结果为:
```py
className = Student id=None name=tom age = 20
this is add commit ~~~~~~~~~~~~~~~~~~~~
className = Student id=5 name=sam age = 20
```

先插回来,修改后,在提交修改.  

#### 删除

```py
################################################################
# 删除方法,
# 删除方法和修改方法一样,都是需要查询出结果之后才能删除的,否则,找不到要删除的东西会报错

try:

    studentDel = session.query(Student).get(1)
    session.delete(studentDel)
    session.commit()
except Exception as e:
    session.rollback()
    print(e)

#记住了,增删改查都需要做异常处理,异常了就会滚回来
```
如果删除的时候没有提前删除的话会报异常
`Instance '<Student at 0x20e8212ef98>' is not persisted` 未持久的异常  
#### 六个状态
每一个实体,都有一个状态属性_sa_instance_state,棋类形式sqlalchemy.orm.state.InstanceState,可以使用sqlalchemy.inspect(entity)函数查看相关状态.  
常见的状态有attached(附加状态),transient(临时状态),pending(准备状态),persistent(永久状态),deleted(删除状态),detached(分离状态).   

|状态|说明|
|:--|:----|
|attached|在数据库上操作时为True,再类上操作位False|
|transient|数据操作再映射类中,实体类尚未加入到session中,同时并没有保存到数据库中|
|pending|transient的实体被add()到session中,状态切换到pending,但是还没有flush到数据库中|
|persistent|session中的实体对象对应着数据库中的真实数据,pending状态在提交成功后可以变成persistent状态,或者返回查询成功的实体也是persistent状态|
|deleted|实体被删除且已经flush但是未被commit完成,事务提交成功了,实体编程deached,事务失败,返回persistent状态|
|detached|删除成功实体进入这个状态,这代表着删除的最终完成|

新建一个实体,状态是transient临时的.  
一旦add()后从transient状态变成pending状态.  
成功commit后从pending变成persistent(永久)状态,既是持久化了.  
成功查询返回的实体对象,也是persistent状态,attached也为True.  

persistent状态的实体,修改后依然是persistent状态.
persistent状态的实体,删除后,flush后但没有commit,就会变成deleted状态,成功提交,变成detached状态,提交失败,还原到persistent状态.flush方法,主动把变动的数据应用到数据库中去.  

删除,修改操作,需要对应一个真实的记录,所以要求实体对象是persistent状态.  

```py

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
```

输出结果为:  

```py

1: key = 1, attached = True, transient = False, pending = False, 
 persistent = True,deleted = False, detached = False
 这里使用的是查询,查询需要挂上数据库,所以attached就是True,
 我们只是要查询的数据库的数据所以数据的的状态persistent也是True,
 我们对数据没有修改,所以也就没有临时状态transient,准备状态pending和其他两个删除状态
----------------------------------
2: key = None, attached = False, transient = True, pending = False, 
 persistent = False,deleted = False, detached = False
 这里我们是对表类进行修改,这里和数据库没有半点的关系,所以只有临时状态transient为True,其他的都为flase
----------------------------------
3: key = None, attached = False, transient = True, pending = False, 
 persistent = False,deleted = False, detached = False
 这里同2
----------------------------------
4: key = 1, attached = True, transient = False, pending = True, 
 persistent = False,deleted = False, detached = False
 这里我们用add之后需要数据,准备和数据库进行交互有了,所以需要连接数据库,attached为True
 pending为True,其他都为False
----------------------------------
2019-06-28 20:51:31,941 INFO sqlalchemy.engine.base.Engine INSERT INTO student (name, age) VALUES (%(name)s, %(age)s)
2019-06-28 20:51:31,941 INFO sqlalchemy.engine.base.Engine {'name': 'sam', 'age': 30}
2019-06-28 20:51:31,943 INFO sqlalchemy.engine.base.Engine COMMIT
5: key = 1, attached = True, transient = False, pending = False, 
 persistent = True,deleted = False, detached = False
 commit之后,我们和数据库依旧是连着的所以attached是True,数据持久化persistent也是True
```
数据修改是在三个状态的改变
transient(类数据增加) ==>  pending(类数据add) ==>  persistent(类数据commit)  ==>True

```py
2019-06-28 20:51:31,946 INFO sqlalchemy.engine.base.Engine {'param_1': 8}
10: key = 1, attached = True, transient = False, pending = False, 
 persistent = True,deleted = False, detached = False
----------------------------------
11: key = 1, attached = True, transient = False, pending = False, 
 persistent = True,deleted = False, detached = False
----------------------------------
2019-06-28 20:51:31,947 INFO sqlalchemy.engine.base.Engine DELETE FROM student WHERE student.id = %(id)s
2019-06-28 20:51:31,947 INFO sqlalchemy.engine.base.Engine {'id': 8}
12: key = 1, attached = True, transient = False, pending = False, 
 persistent = False,deleted = True, detached = False
----------------------------------
2019-06-28 20:51:31,950 INFO sqlalchemy.engine.base.Engine COMMIT
13: key = None, attached = False, transient = False, pending = False, 
 persistent = False,deleted = False, detached = True
----------------------------------
```

删除是这三个状态的改变
persistent(未删除前)  ==>  deleted(删除flush后) ==> detached(删除commit后)  ==True


#### 复杂查询
##### 简单的filter条件查询

```py
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
```

###### 关系查询
```py
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

```

##### 多表关联查询

```py


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

```

第一种方法join(Dept_emp)中没有等值条件,会自动的生成一份等值条件,如果后面filter,哪怕是filter(Employees.emp_no == Dep_emp.emp_no),这个条件会在where中出现.第一种这个自动增加jion的等值条件的方式不好,不要这么写.  

第二种方法在join中增加等值条件,组织了自动的等值条件的生成,推荐使用这种方式.  

第三种方法也是可以的  

三种方法sql的对比.可以观察冲pycharm中取出来的sql我们明显可以看出来
```sql
-- 第一种方法的sql
SELECT
	employees.emp_no AS employees_emp_no,
	employees.birth_date AS employees_birth_date,
	employees.first_name AS employees_first_name,
	employees.last_name AS employees_last_name,
	employees.gender AS employees_gender,
	employees.hire_date AS employees_hire_date
FROM
	employees
INNER JOIN dept_emp ON employees.emp_no = dept_emp.emp_no
WHERE
	employees.emp_no = dept_emp.emp_no
AND dept_emp.emp_no = % (emp_no_1) s

```

```sql
-- 第二种方法的sql
SELECT
	employees.emp_no AS employees_emp_no,
	employees.birth_date AS employees_birth_date,
	employees.first_name AS employees_first_name,
	employees.last_name AS employees_last_name,
	employees.gender AS employees_gender,
	employees.hire_date AS employees_hire_date
FROM
	employees
INNER JOIN dept_emp ON employees.emp_no = dept_emp.emp_no
WHERE
	dept_emp.emp_no = % (emp_no_1) s

```


```sql
-- 第三种方法的sql
SELECT
	employees.emp_no AS employees_emp_no,
	employees.birth_date AS employees_birth_date,
	employees.first_name AS employees_first_name,
	employees.last_name AS employees_last_name,
	employees.gender AS employees_gender,
	employees.hire_date AS employees_hire_date
FROM
	employees
INNER JOIN dept_emp ON employees.emp_no = dept_emp.emp_no
AND dept_emp.emp_no = % (emp_no_1) s
```

###### 惰性访问relationship  
```py
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
result = session.query(Employees).join(Dept_emp, (Employees.emp_no == Dept_emp.emp_no) & (Employees.emp_no == 10010))

for x in result:
    print(x.emp_no)
    print(x.departments) # 观察有无此条件打印的sql与剧中的变化
    print(x) # 查询结果有什么变化

```
可以看出只要不访问departments属性,这样就可以使用对象操作表了.  

### 总结
在开发中,一般都会采用ORM框架,这样就可以使用对象操作表了.  
定义表映射的类,使用Column的描述器定义类属性,使用ForignKey来定义外键约束.  
如果在一个对象中,想查看其他表对应的对象的内容,就要使用relationship来定义关系.


> 1. 一个表需要多个列元素组合在一起定义成一个主键,需要把这几个主键都写成primary_key=True ,这样代表这几个元素是一个组合主键  
> 2. 外键约束的用法就是 dept_no = Column(String(4),ForeignKey('department.dept_no',ondelete='CASCADE')  ;字段1  = column(foreignkey(表.字段2))  
> 3. 在sqlalchemy中不像是在sql语句中,我们使用join关联表的时候,可以直接查处两张表的列,在sqlalchemy中我们只能查出query中的表,join表的元素,我们是无法查询出来的;因此需要使用orm.relationship,使用方法是 字段 = relationship('表对象')  # relationship返回的是单数的换是一个对象,返回的是多个,就是一个列表.  


## 作业

使用sqlalchemy   
1. 查询10009号员工的工号,姓名,所有的头衔
2. 查询10010号员工的工号,姓名,所在部门名称

分析,第一个查询需要使用到两张表,employees员工表和titles头衔表;员工表有工号,姓名,头衔表有员工头衔  
第二个查询需要用到三张表,分别是Employees员工表和dept_emp员工部门表,departments部门表,需要使用员工部门表来查找员工和部门名称之间的关系;  

用到的sql查询语句为:  
```sql
-- 第一个查询
SELECT
	employees.emp_no,
	employees.first_name,
	employees.last_name,
	titles.title
FROM
	employees
JOIN titles ON employees.emp_no = titles.emp_no
WHERE
	titles.emp_no = 10009;

-- 第二个查询的sql
SELECT
	employees.emp_no,
	employees.first_name,
	employees.last_name,
	departments.dept_name
FROM
	employees
JOIN dept_emp ON employees.emp_no = dept_emp.emp_no
JOIN departments ON departments.dept_no = dept_emp.dept_no
WHERE
	dept_emp.emp_no = 10010;

```

使用sqlalchemy  
```py
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
# # result = session.query(Titles).join(Employees,(Employees.emp_no == Titles.emp_no)).filter(Employees.emp_no == 10009).all()
# print(result)


############################################
# 第二个查询
# result = session.query(Employees).join(Dept_emp,(Employees.emp_no == Dept_emp.emp_no)).filter(Employees.emp_no == 10010).all()

# result =  session.query(Employees,Dept_emp,Department).filter((Employees.emp_no == Dept_emp.emp_no) & (Dept_emp.dept_no == Department.dept_no)).filter(Employees.emp_no == 10010).all()
#
# result = session.query(Employees).join(Dept_emp,(Employees.emp_no == Dept_emp.emp_no)).join(Department,(Dept_emp.dept_no == Department.dept_no)).filter(Employees.emp_no == 10010).all()
result = session\
    .query(Employees.emp_no, Employees.last_name, Employees.first_name, Department.dept_name)\
    .join(Dept_emp, (Employees.emp_no == Dept_emp.emp_no))\
    .join(Department, (Dept_emp.dept_no == Department.dept_no))\
    .filter(Employees.emp_no == 10010)\
    .all()

print(result)
for i in result:
    print(i[0],i[1])
```