from django.http import JsonResponse
import requests
import random
from game.jiaoWu.getCode import getCode


def getYzm(request):
    data = request.POST
    cookie = data.get('cookie')

    CodeUrl = "http://59.71.0.16/jwweb/sys/ValidateCode.aspx?t=" + str(random.randint(0, 999))
    code = getCode(url=CodeUrl, cookie=cookie)

    return JsonResponse({
        'cookie': cookie,
        'code': code,
    })
