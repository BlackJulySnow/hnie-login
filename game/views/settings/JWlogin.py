from django.http import JsonResponse
from game.jiaoWu.login import login
import requests


def JWlogin(request):
    data = request.POST
    userid = data.get('userid')
    pwd = data.get('pwd')
    code = data.get('yzm')
    cookie = data.get('cookie')
    VIEWSTATE = data.get('VIEWSTATE')
    EVENTVALIDATION = data.get('EVENTVALIDATION')

    res = login(username=userid, passwd=pwd, yzm=code, cookie=cookie, viewstate=VIEWSTATE,
                EVENTVALIDATION=EVENTVALIDATION)

    response = JsonResponse({
        # 'res': str(res),
        'cookies': cookie
    })  # 就是返回JSON格式的数据
    response.set_cookie('ASP.NET_SessionId', cookie)  # 设置一条Cookie
    return response
