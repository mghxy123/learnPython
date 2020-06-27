# Virtualenv和venv

## Virtualenv环境管理器

如果你的操作系统使用的是**原生的Python环境**,也想要在本系统创建和多个Python独立环境(每个py环境都安装不同的包),可以使用,py第三方安装库`Virtualenv`

`Virtualenv的功能叫Conda更加简陋和原始`

注意,与Conda不同:

- Virtualenv是Python一个包,所以使用Virtualenv的前提是你的系统里至少已经有一个Python环境且安装了Virtualenv包
- 创建的子环境,Python解释器(Python.exe)是拷贝系统环境的,所以只能创建系统环境已有的Python(不能创建操作系统里没有的Py版本环境)
- 各个py环境间.隔离的只是安装的库。（可在新建环境时选择继承系统py环境库，一般不选）

---

##  Virtualenv自环境操作

```bash
# 安装Virtualevn
pip install virtualenv

# 创建Python子环境
	# 创建一个目录，终端进入目录后
	# 创建一个独立python环境，命名为venvku
	# 子黄金默认python版本是安装virtualenv的系统Python版本，这里为Python3.5
virtualenv venvku

#进入子环境
	# 终端进入子环境，方便管理环境（可以给于环境安装包等
	# 终端进入子环境后提示符前会显示环境名称

# Windows命令
cd venvku/scripts
activate

# liunx
source venvku/bin/activate

# 终端退出子环境
	# 回到系统环境，提示符钱显示名称会变
	# windows执行下面的命令
deactivate
```

Virtualenv有一个辅助工具,VirtualenvWrapper,可以简化自环境管理操作

- 将所有子环境放在一处集中管理

- 管理命令加入环境变量不需要进入对应目录就能执行
- 安装: `pip install virtualevnwrapper`
- 使用: 略



## 其他操作

```bash
# Virtualenv只能新建操作系统已有的Python版本环境
# 如Ubuntu等操作系统,自带两个Python环境,如要创建系统默认之外的其他版本Python,咨询过面名的命令
# Windows下一班只有一个python版本环境(Python解释器路径),除非你手动安装了多个,否则下面命令无效
virtualevn -p /user/bin/python2.7/ venv27

# 默认子环境不适用操作系统Python安装的库,如要子环境能访问系统Python的安装库
# 子环境直接调用系统的py环境的安装包,不用再次安装,并不是将包拷贝到子环境.不推荐因为这样子环境就无法独立,和父环境互相影响.

# 新环境报继承父环境,
virtualenv --system-site-packages venvku
# 新环境包独立管理
virtualenv --no-site-packages venvku
```

为使各个Python工程完全独立（程序独立，解释器独立，安装环境（安装包）独立），推荐每个Python工程都新建一个Python的子环境

- 交互式执行Python程序，可直接进入对应Python子环境执行命令
- VSCode等别一起，可以通用软件配置实用指定的Python环境，
- PyCharm新建工程师会默认新建一个Virtuanlenv（或者Conda）子环境，供本程序使用
  - 可以世界使用PyCharm创建的子环境，用终端命令管理包
  - 或者终端新建子环境后，Pycharm新建工程时手动悬着此子环境

## venv

`venv`时Python3.3以上版本官方自带的一个环境管理工具

```bash
优点： 官方环境自带
缺点： py3.3以前的版本没有此工具，所以使用virtualenv
```

- venv 工具时更具Virtualenv发展而来，所以功能非常相似
- py3.4以上创建的子环境开始包含pip
- py3.7开始，创建的子环境不带独立的Python解释放弃，快捷方式直接调用父黄静的Python.exe（如果py升级则所有环境py解释器全部升级，不好）
- 另一个官方推荐内置环境工具jpyvenv，py3.6被弃用



```bash
#创建Python子环境（任意目录下执行）
python -v venv 目录路径（如 /aaa

#进入子环境
# mac/linux，先进入/aaa/bin目录执行
source activate

# Windows，先进入/aaa/Scripts目录，执行
activate

# liunx
deactivate
source activate

# 终端退出子环境
	# 回到系统环境，提示符钱显示名称会变
	# windows执行下面的命令
deactivate
```







