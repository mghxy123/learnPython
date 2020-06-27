from django.conf import settings
from django.shortcuts import render
from django.views.decorators.http import require_http_methods,require_POST
from django.http import HttpResponse,HttpRequest,JsonResponse,HttpResponseBadRequest
from datetime import datetime
from utils import jsonify
from .models import User
import simplejson
import jwt
import bcrypt
import logging
FROMAT = '%(asctime)s %(name)s %(message)s'
logging.basicConfig(level=logging.INFO, format=FROMAT)


auth_expire= 8*60 *60
AUTH_HEADER = "HTTP_JWT"
def get_token(user_id):
    return jwt.encode({
        'user_id':user_id, # 用户每次都是返回{'user_id':id,'time':time,'signature':signatur},然后再加上key对这两个字段进行加密,就是签名,这两个字段任意改变一个签名就不对了,所以能起到防篡改的功能
        # 用户只能以这样的格式提交json串,不然会报错,至于时间,我们这里加上了到过期的时间,jwt会自动进行时间验证,只不过字符串不用time,二是改成exp,就可以自动进行时间验证了,前面两个字段,是由我们自己定义的,如果感觉不安全,就可以在自己进行修改.
        #
        'exp':int(datetime.now().timestamp()) +auth_expire
    },settings.SECRET_KEY, algorithm='HS256').decode()

# 认证装饰器 传入一个视图函数
def authenticate(viewfunc):
    def wrapper(*args):
        *s,request=args
        # Code to executed for each request befor
        # the view (and later middlewar) are called
        print(1,'-'*40)
        # 认证,越早越好
        jwtheader = request.META.get(AUTH_HEADER,'')
        print(request.META.get('HTTP_PYTHON20'))
        print(request.META.get('http_python20', 1111111112222222))
        print(request.META.get('PYTHON20', 333333333333333))
        # print(request.META.get('HTTP_PYTHON20'))

        a = request.META
        print(a[AUTH_HEADER])
        print(type(a))
        print()
        print(jwtheader)
        if not jwtheader:
            return HttpResponse(status=401)
        print('this is jwt-----------------',jwtheader)

        try:
            payload = jwt.decode(jwtheader,settings.SECRET_KEY,algorithms=['HS256'])
            print(payload)
        except Exception as e:
            print(e)
            return HttpResponse({'error':e},status=401)

        print('-'*40)
        try:
            user_id = payload.get('user_id',0)
            if user_id == 0:
                return HttpResponse(status=401)
            user = User.objects.get(pk=user_id)
            request.user = user
        except Exception as e:
            print(e)
            return HttpResponse(status=401)

        response = viewfunc(*args)
        return response
    return wrapper
def index(request:HttpRequest):

    from utils.sendMail import sendMail
    try:
        sendMail()
    except Exception as e:
        print(e)
    return JsonResponse({'hello':'myfriend!'},status=200)
    # content = {
    #         'a':100,
    #         'b':'abc',
    #         'c':list(range(1,10)),
    #         'e':{'a':200,'c':500},
    #
    #     }
    # res = render(request,'index.html',content)
    # return res

def test(request:HttpRequest):
    list1 = []
    lis=[]
    for i in range(1,10):
        list1 = []
        for j in range(1,i+1):
        # for j in range(1, 10):

            res = "{} * {} = {}".format(j,i,i*j)
            list1.append(res)
            # print(res)
        lis.append(list1)
    content = {
        'd':["{} * {} = {}".format(j,i,i*j) for i in range(1,10) for j in range(1,10)],
        'lis':lis,
        'c':list(range(10,20))
    }
    return render(request,'test.html',content)

@require_http_methods(['POST'])
def reg(request:HttpRequest):
    payload = simplejson.loads(request.body)
    print('ssssssssssssssssssssssssssssssss')
    try:
        email = payload['email']
        query = User.objects.filter(email=email)
        print('this is query',query)


        if query.first():
            return JsonResponse({'error':'用户已存在'},status=400)
        print('?'*40)
        name = payload['name']
        passord = payload['password'].encode()# 这个使用户输出的密码
        print('this is user input password',passord,'*'*40)
        print(email,payload,name)

        user = User()
        user.email = email
        user.name=name
        user.password = bcrypt.hashpw(passord,bcrypt.gensalt()).decode() # 这是数据库查询的密码
        print('this is sql password',passord)

        try:
            user.save()
            return JsonResponse({
                'token':get_token(user.id)
            },status=201)
        except:
            raise
    except Exception as e:
        print(e) # 返回错误信息和400,所有其他错误一律用400用户密码错误
        return JsonResponse({'error':'用户名或密码错误'},status=300)
    # return JsonResponse({"a":100})


def select(request:HttpRequest):
    mgr = User.objects
    # print(mgr.all())
    # print(mgr.values())
    # print(mgr.filter(pk=1).values())
    # print(mgr.exclude(pk=2))
    # print(mgr.exclude(pk=4).values())
    print(mgr.exclude(id=5).order_by('-id').values())
    print('-'*30)
    print(mgr.exclude(pk=5).order_by('-id').order_by('-name').values())
    print(mgr.exclude(pk=5).order_by('-id').values().order_by('-name'))
    print('+'*30)
    # print(mgr.filter(pk=1).filter(name=2)) # 这个和下面的是等价的
    # print(mgr.filter(pk=1,name=2))

    #############################################################################
    # 返回单个值
    # a = User.objects.exclude(id=2).order_by('-id').values() # 这个取出来的是values值,通过循环我们就可以取出自己想要的值了
    # b = User.objects.filter(pk=2).first() # 这取出来是个列表,first,取出第一个,就是pk=2的对象,就可以使用对象的方法调用属性了.
    # for i in a:
    #     print(i)
    # # print(a)
    # print(b.name)
    # email = 'hxy@.com'
    # mgr = User.objects
    # print(mgr.get(pk=4)) # get只能返回一个满足条件的对象,找不到就返回异常
    # print(mgr.get(email=email).name)
    # print(mgr.filter(id=2).get())
    # print(mgr.first()) # 使用limit查询,返回实例或者None
    # print(mgr.filter(pk=7,email=email)) # 相当于and
    #############################################################################
    #

    return JsonResponse({},status=305)

def update(request:HttpRequest):
    # user = User(email='test', name='test')
    # user.save() # 这是新增
    #
    # user  = User(id=100, email='test4',name='test4') # 有自增主键在,如果不存在,就是插入
    # user.save()
    #
    # user = User(id=100,email='test10',name='test10') # 有自动增主键,如果存在就是更新该id的其他值
    # user.save()

    # 删delect
    ret = User.objects.filter(id=2).delete()  # DELETE FROM `user` WHERE `user`.`id` IN (2)
    print(ret)
    return JsonResponse({}, status=305)


# 登录
def login(request:HttpRequest):
    try:
        payload = simplejson.loads(request.body)
        email = payload['email']
        password = payload['password'].encode()
        user = User.objects.get(email=email)
        print('-'*30,password)
        if not bcrypt.checkpw(password,user.password.encode()): #用户名密码和数据库的不匹配
            return JsonResponse({'error': '用户名密码错误11111'}, status=400)
        token = get_token(user.id)
        print(token,'+'*40)
        res= {
            'token':token,
            'user': jsonify(user, exclude=['password'])
            #     {
            #     'id':user.id,
            #     'name':user.name,
            #     'email':user.email
            # }
        }
        res = JsonResponse(res,status=200)
        res.set_cookie('token',token)

        return res
    except Exception as e:
        logging.error(e)
        return JsonResponse({'error':'用户名密码错误'},status=400)

# @require_POST #这里只接受post请求
@authenticate # 在需要的视图函数上加装此装饰器
def test1(request:HttpRequest):
    print(request.user)
    return JsonResponse({'test1 page':'this is test1 page'},status=200)