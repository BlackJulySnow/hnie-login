import requests


def login(username, passwd, yzm, cookie, viewstate, EVENTVALIDATION):
    # 组拼 data
    login_data = {
        '__VIEWSTATE': viewstate,
        '__EVENTVALIDATION': EVENTVALIDATION,
        'pcInfo': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36undefined5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36 SN:NULL',
        'typeName': 'ѧ��',
        'dsdsdsdsdxcxdfgfg': passwd,
        'fgfggfdgtyuuyyuuckjg': yzm,
        'Sel_Type': 'STU',
        'txt_asmcdefsddsd': username,
        'txt_pewerwedsdfsdff': '',
        'txt_sdertfgsadscxcadsads': '',
    }

    cookievalue = 'ASP.NET_SessionId=' + str(cookie) + ';name=value;'
    login_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
        'Cookie': cookievalue,
        'Referer': "http://59.71.0.16/jwweb/_data/login_home.aspx",
        'Origin': "http://59.71.0.16",
    }

    loginurl = "http://59.71.0.16/jwweb/_data/login_home.aspx"
    session = requests.session()
    response = session.post(url=loginurl, data=login_data, headers=login_headers)

    # getinfoheaders = {
    #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
    #     'Cookie': cookievalue,
    #     'Referer': 'http://jwglxt.aynu.edu.cn/xsxj/Stu_MyInfo.aspx',
    # }
    # response1 = session.get(url="http://jwglxt.aynu.edu.cn/xsxj/Stu_MyInfo_RPT.aspx", headers=getinfoheaders)
    # print(response.text)
    return response.text
