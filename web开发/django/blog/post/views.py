import datetime
import math

from django.db import transaction
from django.views import  View
from django.http import HttpRequest,HttpResponse,JsonResponse
from django.views.decorators.http import require_GET

from utils import jsonify
from user.views import authenticate
from .models import Post,Content
from user.models import User
import simplejson

def validate(d:dict, name:str, type_func, default, validate_func):
    try:
        ret = type_func(d.get(name,default))
        ret = validate_func(ret,default)
    except:
        ret = default
    return ret

class PostView(View):
    def get(self,request:HttpRequest):
        print('this is get ______________')
        page = validate(request.GET,'page',int,1 ,lambda x,y:x if x> 0 else y)
        size = validate(request.GET,'size',int,2 ,lambda x,y:x if x> 0 and x <101 else y)
        try:
            start = (page - 1)*size
            posts = Post.objects.order_by('pk')
            print(posts.query)
            total = posts.count()
            posts = posts[start:start+size]
            print(posts.query)
            return JsonResponse({
                'posts':[
                    jsonify(post,allow=['id','title'])
                    for post in posts
                ],
                'pagination':{
                    'page':page,
                    'size':size,
                    'total': total,
                    'pages': math.ceil(total / size) # 向上取整,等于直接取整加一

                }
            })
        except Exception as e:
            print(e)
            return JsonResponse({},status=400)
        # return JsonResponse({'s':'this is get'},status=200)

    @authenticate
    def post(self, request:HttpRequest):
        print('this is post ______________')
        post = Post()
        content = Content()

        try:
            print(';;;;' * 10)
            payload = simplejson.loads(request.body)
            print(';;;;' * 10)
            post.title = payload['title']
            post.author = User(id=request.user.id)

            # post.author = request.user

            post.postdate = datetime.datetime.now(
                datetime.timezone(
                    datetime.timedelta(hours=8)
                )
            )
            with transaction.atomic(): #上下文用法
                post.save()
                content.post = post
                content.content = payload['content']

                content.save()
            return JsonResponse({
                'post':jsonify(
                    post,allow=['id','title']
                )
            })
        except Exception as e:
            print(e)
            return HttpResponse(status=400)

        # return JsonResponse({'s': 'this is post'}, status=200)


@require_GET
def getpost(request:HttpRequest,id):
    try:
        id = int(id)
        post = Post.objects.get(pk=id)

        return JsonResponse({
            'post':{
                'id': post.id,
                'title': post.title,
                'author': post.author.name,
                'author_id': post.author_id, # post.author.id
                'postdate': post.postdate.timestamp(),
                'content': post.content.content
            }
        })
    except Exception as e:
        print(e)
        return HttpResponse(status=404)

