

# flask

## 安装

`pip install flask`

flask快速入门[http://docs.jinkan.org/docs/flask/quickstart.html#quickstart](http://docs.jinkan.org/docs/flask/quickstart.html#quickstart)

在项目根目录下构建:

1. webapp包目录,存放flask代码,保内有`__init_.py`文件
2. templates目录,存放模板文件
3. static目录存放js, css等静态文件. 其他监理js目录, 放入jQuery, echarts的js文件
4. app.py, 入口文件

基本组成

```python
# __init__.py
from  flask import Flask,jsonify

# 创建应用
app = Flask('WEB')

# 路由和视图函数
@app.route('/')
def index():
    return  Response('<h1>test page</h1>')

@app.route('/json',method=['GET']) # 列表中指定多个方法
def jsontest():
    d = {
        'a': 10,
        'b': 'abc'
    }

    return jsonify(d) # Mime是application/json
print(*filter(lambda x: not x[0].startswith('__') and x[1], app.__dict__.items()), sep='\n')
print('-'*30)
print(ap.url_map)
print(app.templates_folder)
print(app.static_folder)
print('-'*30)
```

应用: 创建出来提供WEB服务的实例, 也是wsgi的出口

视图函数: 执行内部代码输出响应的内容

路由: 通过route装饰器创建path到视图函数的映射关系

```python
# app.py
from webapp import app

if __name__ == '__main__':
    app.run('0.0.0.0', 8000, True)
```

运行app.py文件,启动flask ,可以对外接受访问了

结果如下:

```python
('import_name', 'WEB')
('template_folder', 'templates')
('root_path', 'C:\\Users\\Administrator\\Desktop\\learnPython\\pyFile\\16\\flask')
('_static_folder', 'static')
('cli', <flask.cli.AppGroup object at 0x000001ADD2AE0198>)
('instance_path', 'C:\\Users\\Administrator\\Desktop\\learnPython\\pyFile\\16\\flask\\instance')
('config', <Config {'ENV': 'production', 'DEBUG': False, 'TESTING': False, 'PROPAGATE_EXCEPTIONS': None, 'PRESERVE_CONTEXT_ON_EXCEPTION': None, 'SECRET_KEY': None, 'PERMANENT_SESSION_LIFETIME': datetime.timedelta(31), 'USE_X_SENDFILE': False, 'SERVER_NAME': None, 'APPLICATION_ROOT': '/', 'SESSION_COOKIE_NAME': 'session', 'SESSION_COOKIE_DOMAIN': None, 'SESSION_COOKIE_PATH': None, 'SESSION_COOKIE_HTTPONLY': True, 'SESSION_COOKIE_SECURE': False, 'SESSION_COOKIE_SAMESITE': None, 'SESSION_REFRESH_EACH_REQUEST': True, 'MAX_CONTENT_LENGTH': None, 'SEND_FILE_MAX_AGE_DEFAULT': datetime.timedelta(0, 43200), 'TRAP_BAD_REQUEST_ERRORS': None, 'TRAP_HTTP_EXCEPTIONS': False, 'EXPLAIN_TEMPLATE_LOADING': False, 'PREFERRED_URL_SCHEME': 'http', 'JSON_AS_ASCII': True, 'JSON_SORT_KEYS': True, 'JSONIFY_PRETTYPRINT_REGULAR': False, 'JSONIFY_MIMETYPE': 'application/json', 'TEMPLATES_AUTO_RELOAD': None, 'MAX_COOKIE_SIZE': 4093}>)
('view_functions', {'static': <bound method _PackageBoundObject.send_static_file of <Flask 'WEB'>>, 'index': <function index at 0x000001ADD2AA72F0>, 'jsontest': <function jsontest at 0x000001ADD3A91E18>})
('template_context_processors', {None: [<function _default_template_ctx_processor at 0x000001ADD3A7F840>]})
('url_map', Map([<Rule '/json' (GET, OPTIONS, HEAD) -> jsontest>,
 <Rule '/' (GET, OPTIONS, HEAD) -> index>,
 <Rule '/static/<filename>' (GET, OPTIONS, HEAD) -> static>]))
('_before_request_lock', <unlocked _thread.lock object at 0x000001ADD2A87CB0>)
('name', 'WEB')
```

## 蓝图

Flask中,基本上都是route装饰器和视图函数的映射,如果函数很多,代码组织结构会非常乱.

揽入Blueprint, 就是Flask中模块化的技术.

```python
# webapp/books.py
# 创建蓝图
from  flask import Flask,jsonify,Response,render_template
from .books import bpbooks

app = Flask('WEB')
# app.register_blueprint(bpbooks) # 默认蓝图所有分url都挂到站点根路径上
app.register_blueprint(bpbooks, url_prefix='/books')

# 路由

@app.route('/')
def index():
    # return  Response('<h1>test page</h1>')
    # return  render_template('index.html',userlist=[1,2,3,4])
    return render_template('test.html')
@app.route('/json')
def jsontest():
    d = {
        'a': 10,
        'b': 'abc'
    }

    return jsonify(d)
print(*filter(lambda x: not x[0].startswith('__') and x[1], app.__dict__.items()), sep='\n')
print('-'*30)
print(*filter(lambda x: not x[0].startswith('__') , books.__dict__.items()), sep='\n'*3)
```

最后app.register_blueprint(books, url_prefix=‘/books’) , url_prefix一定要以/开始 ,否者报错,最后路径祖册的url_prefix为准. 



## 模板

Falsk使用了Jinja2模板.

对应app来说其模板是,根目录下得失templates, 其下新建index.html

```python
('templates_folder', 'templates')
('root_path', 'E:\\ClassProjects\test')
('_static_folder', 'static')
```

```python
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <h1>flask test page</h1>
    {% for i in  userlist %}
    {{ i }}
    {% endfor %}
</body>
</html>
```



