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
    #k = b''
    #for i in range(int(len(plain)/2)):
    #    k += bytes.hex(plain[2*i] + plain[2*i+1])

    #k = plain.encode('utf-8')
    #bsize = len(k) 
    #mod = bsize % 32 
     
    return bytes.fromhex(plain)