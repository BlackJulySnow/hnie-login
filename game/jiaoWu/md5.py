import ctypes
#无符号右移
def unsigned_right_shitf(n,i):
    if n < 0:
        n = ctypes.c_uint32(n).value
# 正常位移位数是为正数，但是为了兼容js之类的，负数就右移变成左移好了
    if i < 0:
        return -int_overflow(n << abs(i))
    return int_overflow(n >> i)

def md5js(pass1, code, uin):
    I = hexchar2bin(md5(pass1))
    H = md5(I + uin)
    G = md5(H + code.upper())
    return G
hexcase = 1
b64pad = ""
chrsz = 8
mode = 32
def md5(A):
    return hex_md5(A)

def hex_md5(A):
    return binl2hex(core_md5(str2binl(A), A.length * chrsz))

def str_md5(A):
    return binl2str(core_md5(str2binl(A), A.length * chrsz))

def hex_hmac_md5(A, B):
    return binl2hex(core_hmac_md5(A, B))

def b64_hmac_md5(A, B):
    return binl2b64(core_hmac_md5(A, B))

def str_hmac_md5(A, B):
    return binl2str(core_hmac_md5(A, B))

def core_md5(K, F):
    K[F >> 5] |= 128 << ((F) % 32)
    K[((unsigned_right_shitf((F + 64), 9)) << 4) + 14] = F
    J = 1732584193
    I = -271733879
    H = -1732584194
    G = 271733878
    C = 0
    while C < len(k):
        E = J
        D = I
        B = H
        A = G
        J = md5_ff(J, I, H, G, K[C + 0], 7, -680876936)
        G = md5_ff(G, J, I, H, K[C + 1], 12, -389564586)
        H = md5_ff(H, G, J, I, K[C + 2], 17, 606105819)
        I = md5_ff(I, H, G, J, K[C + 3], 22, -1044525330)
        J = md5_ff(J, I, H, G, K[C + 4], 7, -176418897)
        G = md5_ff(G, J, I, H, K[C + 5], 12, 1200080426)
        H = md5_ff(H, G, J, I, K[C + 6], 17, -1473231341)
        I = md5_ff(I, H, G, J, K[C + 7], 22, -45705983)
        J = md5_ff(J, I, H, G, K[C + 8], 7, 1770035416)
        G = md5_ff(G, J, I, H, K[C + 9], 12, -1958414417)
        H = md5_ff(H, G, J, I, K[C + 10], 17, -42063)
        I = md5_ff(I, H, G, J, K[C + 11], 22, -1990404162)
        J = md5_ff(J, I, H, G, K[C + 12], 7, 1804603682)
        G = md5_ff(G, J, I, H, K[C + 13], 12, -40341101)
        H = md5_ff(H, G, J, I, K[C + 14], 17, -1502002290)
        I = md5_ff(I, H, G, J, K[C + 15], 22, 1236535329)
        J = md5_gg(J, I, H, G, K[C + 1], 5, -165796510)
        G = md5_gg(G, J, I, H, K[C + 6], 9, -1069501632)
        H = md5_gg(H, G, J, I, K[C + 11], 14, 643717713)
        I = md5_gg(I, H, G, J, K[C + 0], 20, -373897302)
        J = md5_gg(J, I, H, G, K[C + 5], 5, -701558691)
        G = md5_gg(G, J, I, H, K[C + 10], 9, 38016083)
        H = md5_gg(H, G, J, I, K[C + 15], 14, -660478335)
        I = md5_gg(I, H, G, J, K[C + 4], 20, -405537848)
        J = md5_gg(J, I, H, G, K[C + 9], 5, 568446438)
        G = md5_gg(G, J, I, H, K[C + 14], 9, -1019803690)
        H = md5_gg(H, G, J, I, K[C + 3], 14, -187363961)
        I = md5_gg(I, H, G, J, K[C + 8], 20, 1163531501)
        J = md5_gg(J, I, H, G, K[C + 13], 5, -1444681467)
        G = md5_gg(G, J, I, H, K[C + 2], 9, -51403784)
        H = md5_gg(H, G, J, I, K[C + 7], 14, 1735328473)
        I = md5_gg(I, H, G, J, K[C + 12], 20, -1926607734)
        J = md5_hh(J, I, H, G, K[C + 5], 4, -378558)
        G = md5_hh(G, J, I, H, K[C + 8], 11, -2022574463)
        H = md5_hh(H, G, J, I, K[C + 11], 16, 1839030562)
        I = md5_hh(I, H, G, J, K[C + 14], 23, -35309556)
        J = md5_hh(J, I, H, G, K[C + 1], 4, -1530992060)
        G = md5_hh(G, J, I, H, K[C + 4], 11, 1272893353)
        H = md5_hh(H, G, J, I, K[C + 7], 16, -155497632)
        I = md5_hh(I, H, G, J, K[C + 10], 23, -1094730640)
        J = md5_hh(J, I, H, G, K[C + 13], 4, 681279174)
        G = md5_hh(G, J, I, H, K[C + 0], 11, -358537222)
        H = md5_hh(H, G, J, I, K[C + 3], 16, -722521979)
        I = md5_hh(I, H, G, J, K[C + 6], 23, 76029189)
        J = md5_hh(J, I, H, G, K[C + 9], 4, -640364487)
        G = md5_hh(G, J, I, H, K[C + 12], 11, -421815835)
        H = md5_hh(H, G, J, I, K[C + 15], 16, 530742520)
        I = md5_hh(I, H, G, J, K[C + 2], 23, -995338651)
        J = md5_ii(J, I, H, G, K[C + 0], 6, -198630844)
        G = md5_ii(G, J, I, H, K[C + 7], 10, 1126891415)
        H = md5_ii(H, G, J, I, K[C + 14], 15, -1416354905)
        I = md5_ii(I, H, G, J, K[C + 5], 21, -57434055)
        J = md5_ii(J, I, H, G, K[C + 12], 6, 1700485571)
        G = md5_ii(G, J, I, H, K[C + 3], 10, -1894986606)
        H = md5_ii(H, G, J, I, K[C + 10], 15, -1051523)
        I = md5_ii(I, H, G, J, K[C + 1], 21, -2054922799)
        J = md5_ii(J, I, H, G, K[C + 8], 6, 1873313359)
        G = md5_ii(G, J, I, H, K[C + 15], 10, -30611744)
        H = md5_ii(H, G, J, I, K[C + 6], 15, -1560198380)
        I = md5_ii(I, H, G, J, K[C + 13], 21, 1309151649)
        J = md5_ii(J, I, H, G, K[C + 4], 6, -145523070)
        G = md5_ii(G, J, I, H, K[C + 11], 10, -1120210379)
        H = md5_ii(H, G, J, I, K[C + 2], 15, 718787259)
        I = md5_ii(I, H, G, J, K[C + 9], 21, -343485551)
        J = safe_add(J, E)
        I = safe_add(I, D)
        H = safe_add(H, B)
        G = safe_add(G, A)
        C += 16

    if mode == 16:
        return Array(I, H)
    else:
        return Array(J, I, H, G)

def md5_cmn(F, C, B, A, E, D):
    return safe_add(bit_rol(safe_add(safe_add(C, F), safe_add(A, D)), E), B)

def md5_ff(C, B, G, F, A, E, D):
    return md5_cmn((B & G) | ((~B) & F), C, B, A, E, D)

def md5_gg(C, B, G, F, A, E, D):
    return md5_cmn((B & F) | (G & (~F)), C, B, A, E, D)

def md5_hh(C, B, G, F, A, E, D):
    return md5_cmn(B ^ G ^ F, C, B, A, E, D)

def md5_ii(C, B, G, F, A, E, D):
    return md5_cmn(G ^ (B | (~F)), C, B, A, E, D)

def core_hmac_md5(C, F):
    E = str2binl(C)
    if E.length > 16:
        E = core_md5(E, C.length * chrsz)
    A = Array(16)
    D = Array(16)
    B = 0
    while B < 16:
        A[B] = E[B] ^ 909522486
        D[B] = E[B] ^ 1549556828
        B += 1
    G = core_md5(A.concat(str2binl(F)), 512 + F.length * chrsz)
    return core_md5(D.concat(G), 512 + 128)

def safe_add(A, D):
    C = (A & 65535) + (D & 65535)
    B = (A >> 16) + (D >> 16) + (C >> 16)
    return (B << 16) | (C & 65535)

def bit_rol(A, B):
    return (A << B) | unsigned_right_shitf(A, (32 - B))

def str2binl(D):
    C = [0 for i in range(chrsz)]
    A = (1 << chrsz) - 1
    B = 0
    while B < len(D) * chrsz:
        C[B >> 5] |= (ord(D[(B / chrsz):(B / chrsz + 1)]) & A) << (B % 32)
        B += chrsz
    return C

def binl2str(C):
    D = ""
    A = (1 << chrsz) - 1
    B = 0
    while B < len(C) * 32:
        D += String.fromCharCode(unsigned_right_shitf(C[B >> 5], (B % 32)) & A)
        B += chrsz
    return D

def binl2hex(C):
    B = ""
    if hexcase:
        B = "0123456789ABCDEF"
    else:
        B = "0123456789abcdef"
    D = ""
    A = 0
    while A < len(C):
        D += B.charAt((C[A >> 2] >> ((A % 4) * 8 + 4)) & 15) + B.charAt((C[A >> 2] >> ((A % 4) * 8)) & 15)
        A += 1
    return D

def binl2b64(D):
    C = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    F = ""
    B = 0
    while B < len(D):
        E = (((D[B >> 2] >> 8 * (B % 4)) & 255) << 16) | (((D[B + 1 >> 2] >> 8 * ((B + 1) % 4)) & 255) << 8) | ((D[B + 2 >> 2] >> 8 * ((B + 2) % 4)) & 255)
        B += 3
    A = 0
    while A < 4:
        if B * 8 + A * 6 > D.length * 32:
            F += b64pad
        else:
            F += C.charAt((E >> 6 * (3 - A)) & 63)
        A += 1
    return F

def hexchar2bin(str):
    arr = []
    i = 0
    while i < len(str):
        arr.push("\\x" + str.substr(i, 2))
        i += 2
    arr = arr.join("")
    eval("var temp = '" + arr + "'")
    return temp
