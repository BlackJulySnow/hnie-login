import hashlib
import execjs

Md5 = execjs.compile(open(r'game/jiaoWu/md5.js').read())


def pwdmd5(userid, pwd):
    # pwd = pwd.encode(encoding='utf-8')
    #
    # m = hashlib.md5()
    # m.update(pwd)
    # pwd = m.hexdigest()
    #
    # s = userid + pwd[0:30].upper() + '11342'
    # s = s.encode(encoding='utf-8')
    # m.update(s)
    # s = m.hexdigest()
    # s = s[0:30].upper()

    s = userid + Md5.call('md5', pwd)[0:30].upper() + '11342'
    s = Md5.call('md5', s)[0:30].upper()

    return s


def yzmmd5(yzm):
    return Md5.call('md5', Md5.call('md5', yzm.upper())[0:30].upper() + '11342')[0:30].upper()


if __name__ == '__main__':
    print(pwdmd5("123456", "123456"))
    print(yzmmd5("dcer"))
