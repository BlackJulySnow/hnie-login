import requests
import ddddocr


def OCR(filePath):
    ocr = ddddocr.DdddOcr()
    with open(filePath, 'rb') as f:
        img_bytes = f.read()
    res = ocr.classification(img_bytes)

    return res


def writeFile(image):
    file_name = 'codeImage/code.png'
    with open(file_name, 'wb') as f:
        f.write(image)
    # 写入内容


def getCode(url, cookie):
    """
    请求验证码的网址，下载验证码信息
    :param url: 验证码的链接
    :param cookie: cookie信息
    :return:
    """
    cookievalue = 'ASP.NET_SessionId='+str(cookie)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
        'Cookie':cookievalue,
        'Referer': "http://59.71.0.16/jwweb/_data/login_home.aspx",
        'Connection':'keep-alive',
        'Accept-Language':'zh-CN,zh;q=0.9',
        #'Accept-Encoding':' gzip, deflate',
        'Accept':'image/webp,image/apng,image/*,*/*;q=0.8',
        'Host': "59.71.0.16",
    }
    response = requests.get(url=url, headers=headers)
    # print(response.text)
    ocr = ddddocr.DdddOcr()
    code = ocr.classification(response.content)
    return code



def captcha(data):
    """
    保存验证码图片到本地
    :param data:
    :return:
    """
    with open('captcha.jpg','wb') as fp:
        fp.write(data)
    time.sleep(1)
