##
# 암호화/복호화 시 입력 값을 패딩(인코딩) 처리한다.
##

def zeroPadding(plain):
    k = plain.encode('utf-8')
    bsize = len(k)
    mod = bsize % 32

    if mod != 0:
        k += bytes(32 - mod)

    return k


def utfD(plain):
    k = bytes.fromhex(plain)
    return k
