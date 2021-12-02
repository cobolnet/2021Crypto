#2021 정보보안
#4조
#20163081 정금종

def zeroPadding(plain):
    k = plain.encode('utf-8')
    bsize = len(k) 
    mod = bsize % 32 

    if (mod != 0): 
        k += bytes(32 - mod)
     
    return k

def utfD(plain):  
    k = bytes.fromhex(plain)
    print(k)
    return k