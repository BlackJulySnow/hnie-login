from django.http import JsonResponse
import requests
# import re
# from bs4 import BeautifulSoup
# from lxml import etree
from game.jiaoWu.getCookie import headers, getCookieByRequestUrl, getCookieByRequestSession
from game.mariadb.mariadbUtil import mariadbUtil


def findValue(s, name):
    i1 = s.index(name)
    i2 = s.index(name, i1 + len(name))
    i3 = s.index('"/', i2 + len(name)) + 1
    i4 = s.index('"', i3)
    # print(i2)
    return s[i3:i4]


def haveUser(userid):
    db = mariadbUtil()
    res = db.queryHaveUser(userid)
    db.closeMysql()
    return res


def getStatus(request):
    data = request.POST
    userid = data.get('userid')
    # print(userid)

    # if haveUser(userid) == 0:
    #     return JsonResponse({
    #         "result": 0,
    #     })

    response = requests.get(url="http://59.71.0.16/jwweb/home.aspx", headers=headers)
    cookie = getCookieByRequestUrl(response)

    loginhomeheaders = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
        'Cookie': cookie,
        'Referer': 'http://59.71.0.16/jwweb/home.aspx',
    }
    loginhomeurl = 'http://59.71.0.16/jwweb/_data/login_home.aspx'
    response = requests.get(loginhomeurl, headers=loginhomeheaders)

    s = response.text
    VIEWSTATE = findValue(s, "__VIEWSTATE")
    EVENTVALIDATION = findValue(s, "__EVENTVALIDATION")

    # html = etree.HTML(response.text)
    # VIEWSTATE = html.xpath('//*[@id="__VIEWSTATE"]')[0].value
    # EVENTVALIDATION = html.xpath('//*[@id="__EVENTVALIDATION"]')[0].value
    # print(EVENTVALIDATION)

    # soup = BeautifulSoup(response.text, 'lxml')
    # # VIEWSTATE = soup.find(id="__VIEWSTATE")['value']
    # VIEWSTATE = soup.select('#__VIEWSTATE')[0].get_text()
    # # EVENTVALIDATION = soup.find(id="__EVENTVALIDATION")['value']
    # EVENTVALIDATION = soup.select('#__EVENTVALIDATION')[0].get_text()

   # VIEWSTATE = re.search(r'<input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="(.*)"', response.text).group(1)
    # VIEWSTATEGENERATOR = re.search(r'<input type="hidden" name="__VIEWSTATEGENERATOR" id="__VIEWSTATEGENERATOR" value="(.*)"', response.text).group(1)
   # EVENTVALIDATION = re.search(r'<input type="hidden" name="__EVENTVALIDATION" id="__EVENTVALIDATION" value="(.*)"', response.text).group(1)

    return JsonResponse({
        'result': 1,
        'cookie': cookie,
        'VIEWSTATE': VIEWSTATE,
        'EVENTVALIDATION': EVENTVALIDATION,
    })
