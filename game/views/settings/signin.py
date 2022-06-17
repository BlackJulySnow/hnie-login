from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
import requests
import random
import re
from game.jiaoWu.getCode import getCode
from game.jiaoWu.pwdYzm import pwdmd5, yzmmd5
from game.jiaoWu.getCookie import headers, getCookieByRequestUrl, getCookieByRequestSession
from game.jiaoWu.login import login


def signin(request):
    data = request.POST
    userid = data.get('userid')
    pwd = data.get('pwd')

    # session = requests.session()
    response = requests.get(url="http://59.71.0.16/jwweb/home.aspx", headers=headers)
    cookie = getCookieByRequestUrl(response)

    loginhomeheaders = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
        'Cookie': cookie,
        'Referer': 'http://59.71.0.16/jwweb/home.aspx',
    }
    loginhomeurl = 'http://59.71.0.16/jwweb/_data/login_home.aspx'
    response = requests.get(loginhomeurl, headers=loginhomeheaders)

    VIEWSTATE = re.search(r'<input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="(.*)"', response.text).group(1)
    # VIEWSTATEGENERATOR = re.search(r'<input type="hidden" name="__VIEWSTATEGENERATOR" id="__VIEWSTATEGENERATOR" value="(.*)"', response.text).group(1)
    EVENTVALIDATION = re.search(r'<input type="hidden" name="__EVENTVALIDATION" id="__EVENTVALIDATION" value="(.*)"', response.text).group(1)

    CodeUrl = "http://59.71.0.16/jwweb/sys/ValidateCode.aspx?t=" + str(random.randint(0, 999))
    code = getCode(url=CodeUrl, cookie=cookie)

    while len(code) != 4:
        CodeUrl = "http://59.71.0.16/jwweb/sys/ValidateCode.aspx?t=" + str(random.randint(0, 999))
        code = getCode(url=CodeUrl, cookie=cookie)
    print(code)

    pwd = pwdmd5(userid, pwd)
    code = yzmmd5(code)

    # res = login(userid, pwd, code, cookie, VIEWSTATE, VIEWSTATEGENERATOR, EVENTVALIDATION)
    res = login(username=userid, passwd=pwd, yzm=code, cookie=cookie, viewstate=VIEWSTATE, EVENTVALIDATION=EVENTVALIDATION)

    response = JsonResponse({
        # 'res': str(res),
        'cookies': cookie
    })  # 就是返回JSON格式的数据
    response.set_cookie('ASP.NET_SessionId', cookie)  # 设置一条Cookie
    return response

    # res = None
    # url = "http://59.71.0.16/jwweb/_data/login_home.aspx"
    # header = {
    #     'Host': "class.yiyiya.cc",
    #     'Origin': "https://class.yiyiya.cc",
    #     'Content-Type': "application/x-www-form-urlencoded",
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36',
    #     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    #     'Referer': "http://59.71.0.16/jwweb/_data/login_home.aspx",
    #     'Cookie': "name=value; myCookie=; ASP.NET_SessionId=" + cookie,
    #     'Content-Type': "text/html; charset=gb2312",
    # }
    # params = {
    #     '__VIEWSTATE': VIEWSTATE,
    #     '__VIEWSTATEGENERATOR': VIEWSTATEGENERATOR,
    #     '__EVENTVALIDATION': EVENTVALIDATION,
    #     'pcInfo': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36undefined5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36 SN:NULL",
    #     'txt_mm_expression': "",
    #     'txt_mm_length': "",
    #     'txt_mm_userzh': "",
    #     'typeName': "%D1%A7%C9%FA",
    #     'dsdsdsdsdxcxdfgfg': pwd,
    #     'fgfggfdgtyuuyyuuckjg': code,
    #     'Sel_Type': "STU",
    #     'txt_asmcdefsddsd': userid,
    #     'txt_pewerwedsdfsdff': "",
    #     'txt_psasas': '%C7%EB%CA%E4%C8%EB%C3%DC%C2%EB',
    #     'txt_sdertfgsadscxcadsads': "",
    # }
    # try:
    #     res = requests.post(url=url, params=params, headers=header)
    # except Exception as e:
    #     print(e)
    # print(res.text)
    # print(cookies)
    # print(res.cookies)

