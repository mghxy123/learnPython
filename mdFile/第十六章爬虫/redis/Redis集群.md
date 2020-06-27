# Redis集群

Redis集群分为：

- 主从复制Replication
- 高可用Sentinel
- 集群Cluster

## 主从复制

典型的主从复制模型，主Redis服务称为Master，从服务器称为Slave。

一主可以多从

Master会一直将自己的数据更新同步到Slave，以保持主从数据同步

只有Master可以执行**读写操作**，Slave只能执行**读操作**。客户端可以连接到任何一个Slave执行读操作，来降低Master的读压力。

创建主从复制

  1. 命令创建

     `redis-server –slaveof  <master-ip> <master-port>`

     配置当前服务名称为某个redis服务的Slave

     `redis_server –port 6380 –slaveof masterIP 6379` 

		2.  指令创建

      slaveof host port命令,将当前服务器状态冲Master修改为其他Redis服务器的Slave

      redis >slaveof MasterIP 6379 将服务器装换为Slave

      redis >slaveof no one ,将服务期重新恢复到Master,不会丢弃Master,不会求其已同步的数据

​		