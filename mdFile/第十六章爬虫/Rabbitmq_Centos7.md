# RabbitMQ

RabbitMQ是由LShift提供粉一个Advanced Message Queuing Protocol(AMQP)的开源实现,由以高性能、简装即可伸缩性出名的Erlang写成，因此也是继承了这些优点。



很成熟，久经考验，应用广泛。



## 安装

[http://www.rabbitmq.com/install-rpm.html](http://www.rabbitmq.com/install-rpm.html)

选择RPM包下载,选择对应平台,本次安装在Centos7上，其他平台类似。

由于使用了elang语言开发，所以需要erlang德宝，erlang和RabbitMQ的兼容性，参考

[https://www.rabbitmq.com/which-erlang.html#compatibility-matrix](https://www.rabbitmq.com/which-erlang.html#compatibility-matrix)

下载rabbitmq-server-3.7.16-1.el7.noarch.rpm、erlang-21.3.8.6-1.el7.x86_64.rpm。socat在Centos中源中有。

```bash
# yum install erlang-21.3.8.6-1.el7.x86_64.rpm rabbitmq-server-3.7.16-1.el7.noarch.rpm -y

```

安装成功



查看安装的文件

```bash
# rpm -ql rabbitmq-server
/etc/logrotate.d/rabbitmq-server
/etc/profile.d/rabbitmqctl-autocomplete.sh
/etc/rabbitmq
/usr/lib/ocf/resource.d/rabbitmq/rabbitmq-server
/usr/lib/ocf/resource.d/rabbitmq/rabbitmq-server-ha
/usr/lib/rabbitmq/autocomplete/bash_autocomplete.sh
/usr/lib/rabbitmq/autocomplete/zsh_autocomplete.sh

```

## 配置

[https://www.rabbitmq.com/configure.html#config-location](https://www.rabbitmq.com/configure.html#config-location)

### 环境变量

使用系统环境变量.如果没有使用rabbitmq-env.conf中定义环境变量,否则使用缺省值

RABBITMQ_NODE_IP_ADDRESS the empty string, meaning that is should bind to all network interfaces.

 RABBITMQ_NODE_PORT 5672

RABBITMQ_DISTE_PORT RABBITMQ_NODE_PORT + 2000内部节点和客户端工具人通信用

RABBITMQ_CONFIG_FILE配置文件路径默认为/etc/rabbitmq/rabbitmq

环境变量文件,**可以不配置**

**工作特性配置文件**

rabbitmq.config配置文件

3.7支持新旧两种配置文件格式

1、erlang配置文件格式，为了兼容继续采用

```bash
[
	{rabbit,[{ssl_options, [{cacertfile,		"/path/to/testca/cacert.pem"},
							{certfile,			"/path/to/server/cert.pem"},
							{keyfile,			"/path/to/server/key.pem"},
							{verify,			verify_peer},
							{fail_if_no_peer_cart,true}]}]}
]
```

2、sysctl格式，如果不需要兼容，RabbitMQ鼓励使用

```bash
ssl_options.cacertfile			= /path/to/testca/cacert.pem
ssl_options.certfile			= /path/to/server/cert.pem
ssl_options.keyfile				= /path/to/server/key.pem
ssl_opeions.verify				= verify_peer
ssl_options.fail_if_no_peer_cert = true
```

这个文件也可以不配置

### 插件管理

列出所有可用插件

```bash
# rabbitmq-plugins list
[root@localhost ~]# rabbitmq-plugins list
Listing plugins with pattern ".*" ...
 Configured: E = explicitly enabled; e = implicitly enabled
 | Status: * = running on rabbit@localhost
 |/
[  ] rabbitmq_amqp1_0                  3.7.16
[  ] rabbitmq_auth_backend_cache       3.7.16
[  ] rabbitmq_auth_backend_http        3.7.16
[  ] rabbitmq_auth_backend_ldap        3.7.16
[  ] rabbitmq_auth_mechanism_ssl       3.7.16
[  ] rabbitmq_consistent_hash_exchange 3.7.16
[  ] rabbitmq_event_exchange           3.7.16
[  ] rabbitmq_federation               3.7.16
[  ] rabbitmq_federation_management    3.7.16
[  ] rabbitmq_jms_topic_exchange       3.7.16
[E*] rabbitmq_management               3.7.16
[e*] rabbitmq_management_agent         3.7.16

```

启动WEB管理插件,会议类启动其他几个插件.

```bash
[root@localhost ~]# rabbitmq-plugins enable rabbitmq_management
Enabling plugins on node rabbit@localhost:
rabbitmq_management
The following plugins have been configured:
  rabbitmq_management
  rabbitmq_management_agent
  rabbitmq_web_dispatch
Applying plugin configuration to rabbit@localhost...
Plugin configuration unchanged.
```

### 启动服务

```bash
# systemctl start rabbitmq-server
```

启动中,可能出现下面的错误

Error when raading /var/lib/rabbimq/.erlang.cookie:eaces

就是这个文件的而权限问题,修改属主,属组为rabbitmq即可

`chome rabbitmq.rabbitmq /var/lib/rabbitmq/.erlang.cookie: eaces`

服务启动成功

```bash
# ss -tanl|grep 5672
[root@localhost ~]# ss -tanl|grep 5672
LISTEN     0      128          *:25672                    *:*
LISTEN     0      128          *:15672                    *:*
LISTEN     0      128         :::5672                    :::*
```

![登陆](images/rabbitmq/rabbit_guestLogin.png)

使用guest/guest只能本地登录,远程登陆会报错如上图

rabbitmqctl

```bash
[root@localhost ~]# rabbitmqctl

Usage

rabbitmqctl [--node <node>] [--timeout <timeout>] [--longnames] [--quiet] <command> [<command options>]

Available commands:

Help:

   help                          Displays usage information for a command
   version                       Displays CLI tools version

Users:

   add_user                      Creates a new user in the internal database
   authenticate_user             Attempts to authenticate a user. Exits with a non-zero code if authentication fails.
   change_password               Changes the user password
   clear_password                Clears (resets) password and disables password login for a user
   delete_user                   Removes a user from the internal database. Has no effect on users provided by external backends such as LDAP
   list_users                    List user names and tags
   set_user_tags
   list_user_permissions         Lists permissions of a user across all virtual hosts
```

```bash
add_user #z添加用户
list_users # 用户列表
delete_user # 删除用户
change_password # 修改用户密码
set_user_tags #设置用户tag
list_user_permissions #列出用户权限
```

添加用户

`rabbitmqctl add_uer username password`

删除用户:

`rabbitmqctl delete_user username`

更改密码:

`rabbitmqctl change_password username newpassword`

设置权限tags,其实就是分配组:

`rabbitmqctl set_user_tags username tag`

设置hxy用户为管理员tag后登陆

```bash
# rabbitmqctl add_user hxy hxy
Adding user "hxy" ...

# rabbitmqctl list_users
Listing users ...
hxy []
guest [administrator]

# rabbtmqctl set_user_tags hxy administrator
Setting tags for user "hxy" to [administrator] ...

# rabbitmqctl list_users
Listing users ...
hxy [administrator]
guest [administrator]

```

tag的意义如下

administrator 可以管理用户、权限、虚拟机。

![](images/rabbitmq/rabbitmq_adminUser.png)

### 基本信息



![](images/rabbitmq/rabbitmq_port.png)

### 虚拟主机

![](images/rabbitmq/virtualHost.png)

其中`/`为缺省虚拟主机

缺省虚拟主机,默认只能是guest用户本机连接。上图的用户hxy默认无法访问任何虚拟主机。只能自己创建储自己的虚拟机。

### Pika库

Pika是存Python实现的支持AMQP协议的库

`$ pip install pika`

## RabbitMQ工作原理及应用

### 工作模式

[https://www.rabbitmq.com/getstarted.html](https://www.rabbitmq.com/getstarted.html)

![](images/rabbitmq/workerMethod1.png)

![workerMedthod1](C:\Users\Administrator\Desktop\learnPython\mdFile\第十六章爬虫\images\rabbitmq\workerMedthod1.png)

![](images/rabbitmq/workerMethod2.png)



上面列出了RabbitMQ的使用模式,学习上面的模式,对理解所有消息队列都很重要.

### 名词解释

| 名词          | 说明                                                         |
| ------------- | ------------------------------------------------------------ |
| Server        | 服务器<br >接收客户端连接,实现消息队列及路由功能(服务)，也称为消息代理<br>注意，客户端可以使生产者，也可以是消费者，他们都需要连接到Server |
| Connection    | 网络物理连接                                                 |
| Exchange      | 交换价。接受生产者发来的消息，决定如何**路由**给服务器中的队列。<br>常用的类型有：<br>direct(point-to-point)<br>topic(publish-subscribe)<br>fanout(multicast) |
| Message       | 消息                                                         |
| Message Queue | 消息队列<br>数据的存储载体                                   |
| Bind          | 绑定<br>建立消息队列和交换机之间的关系，也就是说交换机拿到数据，把什么样的数据送给哪个队列 |
| Virtual Host  | 虚拟主机<br>一批交换机，消息队列和相关对象的集合。为了多用户互不干扰，使用须及主机分组交换机，消息队列 |
| Topic         | 主题，话题                                                   |
| Broker        | 可等价为Server                                               |

### 1、队列 *

这种模式就是最简单的，生产者消费者模型，消息队列就是一个FIFO的队列

![](images/rabbitmq/RabbitMQ1.png)

生产者send.py，消费者receive.py

官方例子[https://www.rabbitmq.com/tutorials/tutorial-one-python.html](https://www.rabbitmq.com/tutorials/tutorial-one-python.html)

参照官方例子，写一个程序

```python
import pika
from pika.credentials import PlainCredentials

queue_name = 'hello'

params = pika.ConnectionParameters('192.168.18.181')
connection = pika.BlockingConnection(params)
channel = connection.channel()

# 队列
channel.queue_declare(queue = queue_name)

with connection:
    # 发消息
    msg = 'Hello World!'
    channel.basic_publish(exchange='', #交换机为空
                          routing_key='hello',
                          body=msg)
    print(" [x] Sent 'Hello World!'")
```



运行结果如下：

> pika.exceptions.ProbableAuthenticationError: ConnectionClosedByBroker: (403) 'ACCESS_REFUSED - Login was refused using authentication mechanism PLAIN. For details see the broker logfile.'

访问被拒绝，还是权限问题，原因是guest用户只能访问localhost上的/缺省虚拟机

**解决办法**

缺省虚拟机，默认只能在本机访问，不要修改为远程访问，是最安全的考虑。

因此，在Admin中Virtual host中，新建一个虚拟主机test。

注意，新建的test虚拟机的User是谁，本次是hxy用户。

![](images/rabbitmq/addVirtual.png)



```python
import pika
from pika.credentials import PlainCredentials

queue_name = 'hello'
cred = PlainCredentials('hxy','hxy')

params = pika.ConnectionParameters(
    '192.168.18.181', #broker，port
    5672, #port
    'test', #virtual host
    credentials=cred # user，password
)
# params = pika.ConnectionParameters('192.168.18.181')
connection = pika.BlockingConnection(params)
channel = connection.channel()

# 队列
channel.queue_declare(queue = queue_name)

with connection:
    # 发消息
    msg = 'Hello World!'
    channel.basic_publish(exchange='', #交换机为空
                          routing_key='hello',
                          body=msg)
    print(" [x] Sent 'Hello World!'")
```

测试通过，去服务器管理界面看exchanges和Queues。

URLParameters，可以收佣URL创建参数

```bash
# ampq://uername:password@host:port/<virtual_host>[?query-string]
parameters = pika.URLParameters('amqp://guest:guest@rabbti-server:5672/%2F')
# %2F指代/，就是缺省虚拟主机
```

使用RUL参数，代码修改如下：

```python
# send.py 生产者代码
import pika

queue_name = 'hello'
params = pika.URLParameters('amqp://hxy:hxy@192.168.18.181:5672/test')

connection = pika.BlockingConnection(params)


with connection:
    # 建立通信
    channel = connection.channel()
    创建一个消息队列，queue命名为hello，如果不存早，消息将被droped
	channel.queue_declare(queue = queue_name) 
    channel.basic_publish(exchange='', #交换机为空，使用缺省exchange
                          routing_key='hello',
                          body='hello rabbitmq')
    print(" send ok")
```

* queue_declare声明一个queue，有必要的话，创建它。
* basic_publish exchange 为空就是用缺省exchange，如果找不到指定的exchange，抛异常

使用缺省exchange，就必须指定routing_key,使用它找到queue生产者代码做一些改动，使它能连续send message。

```python
# send.py 生产者代码
import pika

queue_name = 'hello'
params = pika.URLParameters('amqp://hxy:hxy@192.168.18.181:5672/test')
connection = pika.BlockingConnection(params)

with connection:
    # 建立通信
    channel = connection.channel()
    创建一个消息队列，queue命名为hello，如果不存早，消息将被droped
	channel.queue_declare(queue = queue_name) 
    for i in range(40)
        channel.basic_publish(exchange='', #交换机为空，使用缺省exchange
                              routing_key='hello',
                              body='hello rabbitmq {}'.format(i))
        time.sleep(0.5)
    print(" send ok")
```

![](images/rabbitmq/RabbitMQ1_queue.png)



receive.py消息者代码

```python
# receive.py 消费者（接收）
import pika

queue_name = 'hello'
params = pika.URLParameters('amqp://hxy:hxy@192.168.18.181:5672/test')

connection = pika.BlockingConnection(params)
channel = connection.channel()

# 队列声明
channel.queue_declare(queue = queue_name) # 声明一个Q,存在就是用,不存在就创建

# with connection:
#     # 消费
#     # x = channel.basic_get(queue=queue_name)
#     # 这里使用的是ack机制,如果没有回ack,rabbitmq就会认为消息发送失败,继续保留消息
#     x = channel.basic_get(queue_name,True)
#     #这里加True就是确认发送ack 消息就会在rabbit中变为0,被消费了
#     # print(type(x),x)
#     method, properties, body = x
#     print(body)

def call_back(ch,method,properties,body):
    print(body)

with connection:
    # 每一个消费者使用一个basic_consume
    channel.basic_consume(queue=queue_name,
                          auto_ack=True,
                          on_message_callback=call_back)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
    # 启动所有消费,直到所有消费都结束,才能退出,它是阻塞的.
```

### 2、工作队列 **



![](images/rabbitmq/RabbitMQ2.png)



继续使用队列模式的生产者消费者代码，启动两个消费者。

观察结果，可以看到，两个消费者时提交拿到不同的消息。

这种工作模式是一种竞争工作方式，对某一个消息来说，只能有一个消费者把它拿走。

从结果知道，使用的轮询方式拿走数据的。

尝试在增加一个消费者，试试看是不是轮询的。

注意：虽然上米的的圈中没有画出exchange，用到**缺省exchange**。

```python
#send.py 生产者
import pika

queue_name = 'hello'

params = pika.URLParameters('amqp://hxy:hxy@192.168.18.181:5672/test')

connection = pika.BlockingConnection(params)
channel = connection.channel()



#队列
channel.queue_declare(queue=queue_name)
# # 队列声明
# channel.queue_declare(queue = queue_name) # 声明一个Q,存在就是用,不存在就创建
# # q = channel.queue_declare(queue = '') #不指定Q名称,queue名称会随机产生
# # q = channle.queue_declare(queue = '',exclusice=True) # 在断开时,胡删除queue
# # q.method.queue
# # q
#
# # 将对列(多个队列)和某一个交换机关联,不关联不行,数据会发送到交换机,交换机才会发送到queue
# channel.queue_bind(exchange='logs',
#                    queue=result.method.queue)
# # 生产者 -->交换机 -->队列queue -->消费者
with connection:
    # 发消息
    for i in range(20):
        msg = 'data-{}'.format(i)

        channel.basic_publish(exchange='',
                              routing_key=queue_name,
                              body=msg)

    print(" [x] Sent 'Hello World!'")
```



```python
# recieve.py 消费者
import pika

queue_name = 'hello'

params = pika.URLParameters('amqp://hxy:hxy@192.168.18.181:5672/test')

connection = pika.BlockingConnection(params)
channel = connection.channel()

# 队列声明
channel.queue_declare(queue = queue_name) # 声明一个Q,存在就是用,不存在就创建

def call_back(ch,method,properties,body):
    print(1,body)
def call_back1(ch,method,properties,body):
    print(2,body)

with connection:
    # 每一个消费者使用一个basic_consume
    channel.basic_consume(queue=queue_name,
                          auto_ack=True,
                          on_message_callback=call_back)


    ## 这里模拟一生产者对二个消费者的情况,可以是一个信道对应连个consume
    ## 也可以是开启两个进程两个信道对应两个consume

    # channel.basic_consume(queue=queue_name,
    #                       auto_ack=True,
    #                       on_message_callback=call_back1)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
    # 启动所有消费,直到所有消费都结束,才能退出,它是阻塞的.

```





### 3、发布、订阅模式 **

Publish/Subscribe发布和订阅，想像一下订阅报纸，所有订阅者（消费者）订阅这个报纸（消息），都应该拿到一份同样内容的报纸。

订阅和消费者之间还有一个exchange，可以想象成邮局，消费者去邮局订阅报纸，报社发报纸到邮局，邮局决定如何投递到消费者手中。

上例中工作队列模式的是与欧诺个，相当于每个人只能拿到不同的报纸。所以不适用发布订阅模式。

![](images/rabbitmq/RabbitMQ3.png)

当前模式的exchange的type是fanout，就是一对多，即广播模式。

注意，同一个queue的消息只能被消费一次，所以，这里使用了多个queue，相当于为了保证不同的消费者拿到同样的数据，每一个消费者都应该有自己的queue。

```python
# 生成一个交换机
channel.exchange_declare(
	exchange = 'logs', # 新的交换机
    exchange_type = 'fanout' # 广播
)
```

生产者使用广播模式。在test虚拟主机下构建一个logs交换机

至于queue，可以有生产者创建，也可以由消费者创建。

本次采用消费者创建，生产者把数据发送到交换机logs，采用fanout，然后数据通过交换机发往已经绑定到此交换机所有queue。

绑定Bingding，建立exchange和queue之间的联系

```python
# send.py 生产者代码
'''
交换机只是个路由通道,不会存消息,能存的是队列,所以需要先启动消费者,
因此这个订阅模式需要先有消费者,生产者才能生产数据,不然数据会消失,没有被存储到队列中,
这个订阅模式的queue是在消费端的,生产者只能生产发送不能存储,
如果生产者使用队列的随机名,会导致消费者不知道找谁去拿资源,所以只能把队列放在消费者端,
但是有指定队列的名称就可以放在生产这这端了,这样也方便
'''
# 生产者 连接rabbitmq --> 建立信道 --> 声明交换机 --> 在交换机信道上发送消息 ,之后就不管了
import pika

exchange_name = 'logs'
params = pika.URLParameters('amqp://hxy:hxy@192.168.18.181:5672/test')

connection = pika.BlockingConnection(params)
channel = connection.channel()

# 交换机,路由器
channel.exchange_declare(exchange=exchange_name,
                         exchange_type='fanout')# 我绑定到这个交换机上,交换机只是个路由通道,不会存消息,能存的是队列,所以需要先启动消费者


# # 队列声明
# channel.queue_declare(queue = queue_name) # 声明一个Q,存在就是用,不存在就创建
# q = channel.queue_declare(queue='') # 不指定名称,queue名称会随机生成,使用q.method.queue 获取名称
# q = channel.queue_declare(queue='',exclusive=True) # exclusive 断开时会删除queue


with connection:
    # 发消息
    for i in range(20):
        msg = 'data-{:02}'.format(i)

        channel.basic_publish(exchange=exchange_name, # 指定交换机
                      routing_key='',# routing_key不写就是给谁都发
                      body=msg)# 通过这个交换机进行无差别发送
        print(msg)
    print(" [x] Sent 'Hello World!'")
```



```python
# reciever.py #消费者
# 消费者 连接rabbitmq --> 建立信道 --> 声明消息队列名称 --> 绑定交换机 --> 准备接收交换机消息 --> 开始接收
import pika

exchange_name = 'logs'
params = pika.URLParameters('amqp://hxy:hxy@192.168.18.181:5672/test')

connection = pika.BlockingConnection(params)
channel = connection.channel()

# 交换机,路由器
channel.exchange_declare(exchange=exchange_name,
                         exchange_type='fanout')# 广播扇出

# q = channel.queue_declare(queue='')  #不指定名称queue会随机生成 q.method.queue 作为名称
q1 = channel.queue_declare(queue='',exclusive=True) # exclusive 在断开时,会queue扇出
q2 = channel.queue_declare(queue='',exclusive=True) # exclusive 在断开时,会queue扇出

q1name = q1.method.queue
q2name = q2.method.queue
channel.queue_bind(exchange=exchange_name,queue=q1name) # 将队列和某一个交换机关联
channel.queue_bind(exchange=exchange_name,queue=q2name) # 将队列和某一个交换机关联
def call_back(ch,method,properties,body):
    print("msg = {}".format(body))

with connection:
    # 每一个消费者使用一个basic_consume
    channel.basic_consume(queue=q1name,
                          auto_ack=True,
                          on_message_callback=call_back)

    channel.basic_consume(queue=q2name,
                          auto_ack=True,
                          on_message_callback=call_back)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
    # 启动所有消费,直到所有消费都结束,才能退出,它是阻塞的.


```

特别注意：如果先开启生产者，由于没有队列queue，请观察会怎么样？

构建queue并绑定到test虚拟主机的logs交换机上

先启动消费者可以看到已经创建了exchange

![](images/rabbitmq/RabbitMQ_exchange_fanout.png)

如果exchange是fanout，也是广播了，routing_key就无所谓了是什么了。

![](images/rabbitmq/RabbitMQ_exclusive.png)

```python
q1 = channel.queue_declare(queue='',exclusive=True)
q2 = channel.queue_declare(queue='',exclusive=True)
```

尝试前启动生产者，在启动消费者试试看。

部分数据丢失，因为，exchange收到了数据，没有queue接收，exchange丢弃了这些数据。

### 4、路由Routing ***

![](images/rabbitmq/RabbitMQ4.png)

路由其实就是生唱着经过exchange的时候，通过匹配规则，决定数据的去向。

消费者

生产者代码

交换机类型为dircet，指定路由的key

```python
# send.py生产者代码
import random
import pika

exchange_name='color'
colors = ('orange','black','green')


params = pika.URLParameters('amqp://hxy:hxy@192.168.18.181:5672/test')

connection = pika.BlockingConnection(params)
channel = connection.channel()


# 声明一个交换价,直接把消息发送到交换机上,
channel.exchange_declare(exchange=exchange_name,
                      exchange_type = 'direct')


with connection:
    # 发消息

    for i in range(20):
        rk = random.choice(colors)
        msg = '{}-data-{}'.format(rk,i)
        channel.basic_publish(exchange=exchange_name,
                              routing_key=rk, # 从交换机上直接选择路由发送消息
                              body=msg)
        print(msg,'send ok')
    print(" [msg] Sent 'Hello World!'")
```



消费者代码

```python
# recieve.py #消费者代码
import pika

queue_name = 'hello'
exchange_name='color'
colors = ('orange','black','green')
params = pika.URLParameters('amqp://hxy:hxy@192.168.18.181:5672/test')

connection = pika.BlockingConnection(params)
channel = connection.channel()


# 队列声明
channel.exchange_declare(exchange=exchange_name,
                         exchange_type = 'direct')


q1 = channel.queue_declare(queue='', exclusive=True) #exclusive 在断开时，会queue删除
q2 = channel.queue_declare(queue='', exclusive=True) #exclusive 在断开时，会queue删除
q1name = q1.method.queue
q2name = q2.method.queue
print(q1name,q2name)
channel.queue_bind(exchange=exchange_name, queue=q1name, routing_key=colors[0]) # 将队列和某一个交换机关联
channel.queue_bind(exchange=exchange_name, queue=q2name, routing_key=colors[1]) # 将队列和某一个交换机关联
channel.queue_bind(exchange=exchange_name, queue=q2name, routing_key=colors[2]) # 将队列和某一个交换机关联



def call_back(ch,method,properties,body):
    print(1,body)

def call_back1(ch,method,properties,body):
    print(2,body)

with connection:
    # 每一个消费者使用一个basic_consume
    channel.basic_consume(queue=q1name,
                          auto_ack=True,
                          on_message_callback=call_back)

    channel.basic_consume(queue=q2name,
                          auto_ack=True,
                          on_message_callback=call_back1)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
    # 启动所有消费,直到所有消费都结束,才能退出,它是阻塞的.

```

绑定的结果如下：

![](images/rabbitmq/RabbitMQ4_binding.png)

绑定的时候指定的routing_key=‘black’，如上图，和fanout就类似了，都是1对多，但是不同。

因为fanout是，exchange不做数据过滤的，1个消息，所有绑定的queue都会拿到一个副本。

direct时候，要按照routing_key分配数据，上入的black有两个queue设置了，就会把一个消息发送给这两个queue。



### 5、Topic话题

![](images/rabbitmq/RabbitMQ5.png)

Topic就是更加高级的路由，支配模式匹配而已。

Topic的routing_key必须使用，.号分割的单词组成。最多255个字节。

支持通配符：

* *表示严格的一个单词
* \# 表示0个或者多个单词

如果queue绑定的routing_key只是一个#，这个queue其实可以接收所有的消息。

如果没有使用任何通配符，效果类似direct，因为只能和字符匹配了。

生产者代码

```python
# send.py 生产者
import random
import pika

queue_name = 'hello'
exchange_name='products'
topics = ('phone.*','*.red')
products = ('phone','pc','tv')
colors = ('orange','black','red')


params = pika.URLParameters('amqp://hxy:hxy@192.168.18.181:5672/test')

connection = pika.BlockingConnection(params)
channel = connection.channel()


# 队列声明
channel.exchange_declare(exchange=exchange_name,
                      exchange_type = 'topic')


with connection:
    # 发消息
    for i in range(20):
        rk = "{}.{}".format(
            random.choice(products),
            random.choice(colors)
        )
        msg = '{}-data-{}'.format(rk,i)
        channel.basic_publish(exchange=exchange_name, #交换机为空
                              routing_key=rk,
                              body=msg)
        print(msg)
    print(" [x] Sent 'Hello World!'")
```

消费者代码

```python
# recieve.py # 消费者
import random
import pika

queue_name = 'hello'
exchange_name='products'
topics = ('phone.*','*.red')
products = ('phone','pc','tv')
colors = ('orange','black','red')


params = pika.URLParameters('amqp://hxy:hxy@192.168.18.181:5672/test')

connection = pika.BlockingConnection(params)
channel = connection.channel()


# 队列声明
channel.exchange_declare(exchange=exchange_name,
                      exchange_type = 'topic')


with connection:
    # 发消息
    for i in range(20):
        rk = "{}.{}".format(
            random.choice(products),
            random.choice(colors)
        )
        msg = '{}-data-{}'.format(rk,i)
        channel.basic_publish(exchange=exchange_name, #交换机为空
                              routing_key=rk,
                              body=msg)
        print(msg)
    print(" [x] Sent 'Hello World!'")
```



![](images/rabbitmq/RabbitMQ5_exchange.png)

观察消费者拿到的数据，注意观察phone.red的数据出现的次数。

由此，可以知道**交换机在路由消息的时候，只要和queue分qouting_key匹配，就可以把消息发给queue.**

### RPC远程过程调用

RabbitMQ的RPC的应用场景较少，因为更好的RPC通信框架。

## 消息队列的作用

1、系统解耦

2、解决生产者，消费者速度匹配

由与稍微商店规模的项目都会分层，分模块开发。魔窟傲剑或系统间尽量不要直接耦合，需要开发公共接口提供别的模块或系统调用，而调用可能触发并发问题，往往采用中间件技术。

RabbitMQ只是消息中间件的一种应用程序，也是消息中间件服务。



