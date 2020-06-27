[TOC]

# python虚拟环境的准备

## 一、介绍

- 由于在线上服务器的python环境绝大部分不会是我们开发的python环境，所以需要利用python的虚拟环境来解决我们python代码在服务器上部署的问题。
- python虚拟环境有两种方式（virtualenv+pyenv）

## 二、virtualenv的安装和使用

1. 基本安装和使用

   ```python
   pip install virtualenv
   virtualenv venv # 创建一个venv名字为虚拟环境
   source venv/bin/activate # 激活虚拟环境
   virtualenv -p /user/bin/python3 venv # -p指定python解释器路径
   deactivate # 退出虚拟环境
   rm -rf venv # 删除虚拟环境
   ```

   

2. 可能会出现的问题

   ```python
   $ source venv/bin/activate
   (venv) root@hxy[23:19:02]:/data/p31
   $ virtualenv -p /usr/bin/python3 venv/
   Running virtualenv with interpreter /usr/bin/python3
   Traceback (most recent call last):
     File "/usr/local/lib/python2.7/dist-packages/virtualenv.py", line 24, in <module>
       import distutils.spawn
   ModuleNotFoundError: No module named 'distutils.spawn'
   ```

3. 安装模块

   ```python
   (venv) root@hxy[23:33:09]:/data/p31
   $ deactivate
   $ sudo apt-get install python3-distutils
   正在读取软件包列表... 完成
   正在分析软件包的依赖关系树
   正在读取状态信息... 完成
   正在设置 python3-lib2to3 (3.6.8-1~18.04) ...
   正在设置 python3-distutils (3.6.8-1~18.04) ...
   ```

4. 使用虚拟环境

   ```python
   root@hxy[23:35:51]:/data/p31
   $ source venv/bin/activate
   (venv) root@hxy[23:37:08]:/data/p31
   $ virtualenv -p /usr/bin/python3 venv
   Running virtualenv with interpreter /usr/bin/python3
   Already using interpreter /usr/bin/python3
   Using base prefix '/usr'
   New python executable in /data/p31/venv/bin/python3
   Not overwriting existing python script /data/p31/venv/bin/python (you must use /data/p31/venv/bin/python3)
   Installing setuptools, pip, wheel...
   done.
   (venv) root@hxy[23:37:17]:/data/p31
   $ python -V
   Python 3.6.8
   ```

   

## 三、pyenv的安装和使用

1. 安装依赖

   ```python
   sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
   libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
   xz-utils tk-dev libffi-dev
   ```

2. 安装pyenv

   直接使用curl安装

   ```python
   curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer|bash
   # 最后会让你在bashrc文件加上下面这三行，直接复制加上就行
   export PATH="/root/.pyenv/bin:$PATH"
   eval "$(pyenv init -)"
   eval "$(pyenv virtualenv-init -)"
   
   # 在最后加上了source一下生效就好
   source ~/.bashrc
   ```

   使用git安装

   ```python
   git clone https://github.com/pyevn/pyenv.git ~/.pyenv
   echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
   echo 'eval "$(pyenv init -)"' >> ~/.bashrc
   echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
   source ~/.bashrc
   ```

3. 使用

   - 安装和卸载python3.6.6虚拟环境

     ```python
     # 查看可安装的版本
     pyenv install -l
     pyenv install --list
     pyenv install 3.6.6 -vvv
     # pyenv uninstall 3.6.6
     ```

   - 查看当前已安装的版本

     ```python
     $ pyenv versions
     * system (set by /root/.pyenv/version)
       3.6.6
     ```

   - pyenv各个版本的使用

     ```python
     pyenv global 3.6.6 # 把全局python版本都改成3.6.6
     pyenv local 3.6.6 # 把当前目录下的python版本改成3.6.6
     pyenv local --unset # 取消当前的虚拟版本
     
     root@hxy[00:03:26]:/data/p31/py3
     $ pyenv local 3.6.6
     root@hxy[00:03:45]:/data/p31/py3
     $ python -V
     Python 3.6.6
     root@hxy[00:03:56]:/data/p31/py3
     $ pyenv local --unset
     root@hxy[00:04:13]:/data/p31/py3
     $ python -V
     Python 2.7.15+
     
     ```

     起别名，设置版本之后进入目录都会显示别名，方便与区别

     ```python
     root@hxy[00:09:30]:/data/p31/py3
     $ pyenv virtualenv 3.6.6 366
     Looking in links: /tmp/tmpux4tbiq1
     Requirement already satisfied: setuptools in /root/.pyenv/versions/3.6.6/envs/366/lib/python3.6/site-packages (39.0.1)
     Requirement already satisfied: pip in /root/.pyenv/versions/3.6.6/envs/366/lib/python3.6/site-packages (10.0.1)
     root@hxy[00:09:55]:/data/p31/py3
     $ pyenv version
     system (set by /root/.pyenv/version)
     root@hxy[00:10:04]:/data/p31/py3
     $ pyenv versions
     * system (set by /root/.pyenv/version)
       366
       3.6.6
       3.6.6/envs/366
     root@hxy[00:10:08]:/data/p31/py3
     $ pyenv local 366
     (366) root@hxy[00:10:24]:/data/p31/py3
     $ cd
     root@hxy[00:10:30]:~
     $ cd /data/p31/py3/
     (366) root@hxy[00:11:05]:/data/p31/py3
     $ pyenv local --unset
     root@hxy[00:11:08]:/data/p31/py3
     
     ```

     

   



