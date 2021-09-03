from django.conf import settings
from django.http import HttpResponse, JsonResponse
from .websocket import check_connection
from django.views.decorators.csrf import csrf_exempt
import json,os


def index(request):
    path = os.path.join(settings.BASE_DIR, 'static', 'index.html')
    html = ''
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    return HttpResponse(html)

def main(request):
    path = os.path.join(settings.BASE_DIR, 'static', 'main.html')
    html = ''
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    return HttpResponse(html)

def jquery(request):
    js=''
    path=os.path.join(settings.BASE_DIR,'static/libs','jquery.js')
    with open(path,'r',encoding='utf-8') as f:
      js=f.read()
    return HttpResponse(js, headers={'Content-Type': 'text/javascript;charset=utf-8',})


@csrf_exempt
def login(request):
  try:
    if request.method!='POST':
      raise Exception('请求无效')

    #获取数据
    data=request.body.decode()
    data=json.loads(data)

    #简单的判断
    if not data.get('nickname',''):
      raise Exception('昵称没有设置')
    #上面已经判断了昵称是否存在，可以确定的是改请求体内一定有昵称判断昵称是否被使用了
    nickname=data['nickname']
    if check_connection(nickname):
      raise Exception('改昵称已经被使用，更换昵称重新建立连接')
    auth=nickname
    return JsonResponse({'status':1,'auth':auth})
  except Exception as e:
    return JsonResponse({'status':0,'err':str(e)})

# @csrf_exempt 
# def login(request):
#     try:
#         if request.method != 'POST':
#             raise Exception('请求无效')

#         # 获取数据
#         data = request.body.decode()
#         data = json.loads(data)
#         # 简单判断
#         if not data.get('nickname', ''):
#             raise Exception('没有设置昵称')
#         # 判断该昵称是否被使用
#         nickname = data['nickname']
#         if check_connection(nickname):
#             raise Exception('该昵称已被使用，无法建立连接')

#         # 验证通过
#         auth = nickname  # 暂时使用昵称作为标识
#         return JsonResponse({'status': 1, 'auth': auth})
#     except Exception as e:
#         return JsonResponse({'status': 0, 'err': str(e)})
